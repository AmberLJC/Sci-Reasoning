#!/usr/bin/env python3
"""
Batch Prior Work Extraction Pipeline
=====================================
Processes multiple papers from ML conference datasets with:
- Checkpointing for resume capability
- Parallel processing (2 conferences at a time)
- Rate limiting to avoid API limits
- Progress tracking and logging

Usage:
    python batch_processor.py --api-key "KEY" --output-dir results/batch
    python batch_processor.py --api-key "KEY" --output-dir results/batch --resume  # Resume from checkpoint
"""

import os
import sys
import json
import time
import argparse
import threading
import re
import requests
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

# ============================================================================
# CONFIGURATION
# ============================================================================

# Rate limiting: GPT-5 tier limits
# Conservative: ~40 requests/min to stay safe
REQUESTS_PER_MINUTE = 40
REQUEST_DELAY = 60.0 / REQUESTS_PER_MINUTE  # ~1.5 seconds between requests

# Parallel processing
MAX_PARALLEL_CONFERENCES = 2  # Process 2 conferences simultaneously

# Checkpointing
CHECKPOINT_INTERVAL = 10  # Save checkpoint every N papers

# Data paths (absolute paths)
WORKSPACE_ROOT = Path(__file__).parent.parent.parent.parent  # Go up to workspace root
DATA_DIR_2324 = WORKSPACE_ROOT / "projects/ml_paper_acquisition/results/data/2023-2024"
DATA_DIR_2025 = WORKSPACE_ROOT / "projects/ml_paper_acquisition/results/data/2025"

# OpenAI API
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

# ============================================================================
# PROMPTS
# ============================================================================

SYSTEM_PROMPT = """You are an expert AI research analyst. Your task is to identify the KEY PRIOR WORKS that DIRECTLY led to a research paper's core innovation.

## CRITICAL: Focus on DIRECT Intellectual Lineage

You must identify papers that are **directly responsible** for the current paper's main contributions. Ask yourself:
- "Without this prior work, would the current paper's core idea exist?"
- "Did this prior work directly inspire, enable, or motivate the KEY INNOVATION?"
- "Is this paper cited in the Introduction or Related Work as a PRIMARY influence?"

### ❌ DO NOT INCLUDE:
- Generic infrastructure/tools (e.g., PyTorch, CUDA, standard attention mechanisms)
- Complementary optimizations that are orthogonal to the main contribution
- Papers that share the same domain but don't directly influence the core idea
- Standard baselines that are just compared against without deeper connection
- Well-known foundational works that everyone cites but aren't specific to this innovation

### ✅ DO INCLUDE:
- Papers whose specific IDEAS, METHODS, or FINDINGS directly shaped the current work
- Papers whose LIMITATIONS or GAPS the current paper explicitly addresses
- Papers that introduced the PROBLEM FORMULATION the current paper builds on
- Papers whose TECHNIQUES are directly extended or modified
- Papers that provide the KEY INSIGHT that the current paper leverages

## Role Classifications (assign ONE per paper):

1. **Baseline**: The primary system/method this paper improves upon or compares against as its main competitor
2. **Inspiration**: Paper whose specific idea/approach directly sparked the current paper's key innovation  
3. **Gap Identification**: Paper whose explicit limitations/failures motivated this research direction
4. **Foundation**: Paper that introduced the core problem formulation, dataset, or theoretical framework used
5. **Extension**: Paper whose specific method is directly extended, modified, or generalized
6. **Related Problem**: Paper solving a closely related problem whose solution approach informed this work

## Output Requirements:

For each prior work (identify 5-7 papers, quality over quantity):
1. **Role**: One of the six classifications above
2. **Relationship Sentence**: ONE specific sentence explaining the DIRECT connection to the current paper's innovation. Be concrete about WHAT was borrowed/extended/addressed.

## Synthesis Narrative (200-300 words):
Write a cohesive narrative that flows naturally (NO explicit "Part 1" / "Part 2" labels):

**First ~150 words - Prior Work with Relevant Details:**
Describe each prior work, but FOCUS ONLY on the specific aspects/details that relate to the current paper's innovation. For each prior work, highlight:
- The specific technique, insight, or finding that is relevant (not a general summary)
- How this specific detail connects to what the current paper does
- Do NOT mention the current paper yet - just establish what relevant knowledge existed

**Remaining ~100 words - How They Collectively Inspired Current Work:**
Transition naturally to explain:
- What gap or opportunity emerged from the combination of these prior works
- How the current paper synthesizes or builds upon these specific relevant details
- Why this was a natural next step given the prior work landscape

The narrative should read as one flowing paragraph, not two separate sections.

## Output Format (JSON):
```json
{
  "prior_works": [
    {
      "title": "Exact paper title",
      "authors": "First author et al.",
      "year": 2023,
      "arxiv_id": "if known",
      "role": "One of six roles",
      "relationship_sentence": "Specific sentence about DIRECT connection to core innovation"
    }
  ],
  "synthesis_narrative": "200-300 word flowing narrative: describe prior works focusing on details relevant to current paper, then show how they collectively inspired this work"
}
```

Remember: Every paper you include should pass the test: "This paper DIRECTLY influenced the core innovation, not just the general research area."
"""

# ============================================================================
# RATE LIMITER
# ============================================================================

class RateLimiter:
    """Thread-safe rate limiter for API calls."""
    
    def __init__(self, requests_per_minute):
        self.min_interval = 60.0 / requests_per_minute
        self.last_request_time = 0
        self.lock = threading.Lock()
    
    def wait(self):
        """Wait if necessary to respect rate limit."""
        with self.lock:
            now = time.time()
            elapsed = now - self.last_request_time
            if elapsed < self.min_interval:
                sleep_time = self.min_interval - elapsed
                time.sleep(sleep_time)
            self.last_request_time = time.time()

# Global rate limiter
rate_limiter = RateLimiter(REQUESTS_PER_MINUTE)

# ============================================================================
# CHECKPOINT MANAGER
# ============================================================================

class CheckpointManager:
    """Manages checkpoints for resumable processing."""
    
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoint_file = self.checkpoint_dir / "checkpoint.json"
        self.lock = threading.Lock()
        
        # Load existing checkpoint or create new
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file) as f:
                self.state = json.load(f)
        else:
            self.state = {
                "processed_papers": {},  # paper_id -> status
                "conference_progress": {},  # conference -> {total, completed, failed}
                "started_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "total_processed": 0,
                "total_failed": 0
            }
    
    def is_processed(self, paper_id):
        """Check if paper has already been processed."""
        return paper_id in self.state["processed_papers"]
    
    def mark_processed(self, paper_id, status="success", error=None):
        """Mark a paper as processed."""
        with self.lock:
            self.state["processed_papers"][paper_id] = {
                "status": status,
                "timestamp": datetime.now().isoformat(),
                "error": error
            }
            if status == "success":
                self.state["total_processed"] += 1
            else:
                self.state["total_failed"] += 1
            self.state["last_updated"] = datetime.now().isoformat()
    
    def update_conference_progress(self, conference, total=None, completed=None, failed=None):
        """Update progress for a conference."""
        with self.lock:
            if conference not in self.state["conference_progress"]:
                self.state["conference_progress"][conference] = {
                    "total": 0, "completed": 0, "failed": 0
                }
            
            if total is not None:
                self.state["conference_progress"][conference]["total"] = total
            if completed is not None:
                self.state["conference_progress"][conference]["completed"] = completed
            if failed is not None:
                self.state["conference_progress"][conference]["failed"] = failed
    
    def save(self):
        """Save checkpoint to disk."""
        with self.lock:
            self.state["last_updated"] = datetime.now().isoformat()
            with open(self.checkpoint_file, 'w') as f:
                json.dump(self.state, f, indent=2)
    
    def get_stats(self):
        """Get current processing statistics."""
        return {
            "total_processed": self.state["total_processed"],
            "total_failed": self.state["total_failed"],
            "conferences": self.state["conference_progress"]
        }

# ============================================================================
# GPT-5 API
# ============================================================================

def call_gpt5(messages, api_key):
    """Call GPT-5 API with the given messages."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-5",
        "messages": messages
    }
    
    response = requests.post(
        OPENAI_API_URL,
        headers=headers,
        json=payload,
        timeout=300
    )
    
    if response.status_code != 200:
        raise Exception(f"GPT-5 API error: {response.status_code} - {response.text}")
    
    result = response.json()
    return result['choices'][0]['message']['content']

# ============================================================================
# MARKDOWN GENERATOR
# ============================================================================

def generate_markdown_report(analysis):
    """Generate a markdown report from analysis results."""
    
    target = analysis.get("target_paper", {})
    prior_works = analysis.get("prior_works", [])
    synthesis = analysis.get("synthesis_narrative", "")
    
    # Group prior works by role
    works_by_role = defaultdict(list)
    for pw in prior_works:
        role = pw.get("role", "Unknown")
        works_by_role[role].append(pw)
    
    # Build markdown
    md = f"""# Prior Work Analysis Report

## Target Paper

**Title:** {target.get('title', 'Unknown')}

**Conference:** {target.get('conference', 'Unknown')} {target.get('year', '')} ({target.get('presentation_type', 'Unknown')})

**Authors:** {target.get('authors', 'Unknown')}

**Keywords:** {target.get('keywords', 'N/A')}

**Abstract:** 
> {target.get('abstract', 'No abstract available')[:500]}...

---

## Key Prior Works ({len(prior_works)} papers with direct influence)

"""
    
    # Add prior works grouped by role
    role_emojis = {
        "Baseline": "📊",
        "Inspiration": "💡",
        "Gap Identification": "🔍",
        "Foundation": "🏗️",
        "Extension": "🔧",
        "Related Problem": "🔗"
    }
    
    for role in ["Foundation", "Inspiration", "Gap Identification", "Baseline", "Extension", "Related Problem"]:
        if role in works_by_role:
            emoji = role_emojis.get(role, "📄")
            md += f"### {emoji} {role}\n\n"
            
            for pw in works_by_role[role]:
                title = pw.get("title", "Unknown")
                authors = pw.get("authors", "Unknown")
                year = pw.get("year", "")
                relationship = pw.get("relationship_sentence", "")
                
                md += f"**{title}** ({year})\n"
                md += f"- *Authors:* {authors}\n"
                md += f"- *Direct Connection:* {relationship}\n\n"
    
    # Add synthesis
    md += f"""---

## Synthesis: How Prior Work Led to This Paper

{synthesis}

---

*Analysis generated on: {analysis.get('analysis_timestamp', datetime.now().isoformat())}*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
"""
    
    return md

# ============================================================================
# PAPER PROCESSOR
# ============================================================================

def analyze_paper_from_metadata(paper, api_key):
    """
    Analyze a paper using only its metadata (no PDF).
    
    Args:
        paper: Dict with title, authors, abstract, keywords, conference, year
        api_key: OpenAI API key
    
    Returns:
        Dict with analysis results or None if failed
    """
    # Rate limit
    rate_limiter.wait()
    
    # Build paper context
    paper_context = f"""## Paper Title:
{paper.get('title', 'Unknown')}

## Authors:
{paper.get('authors', 'Unknown')}

## Conference:
{paper.get('conference', 'Unknown')} {paper.get('year', '')} ({paper.get('presentation_type', 'Unknown')})

## Keywords:
{paper.get('keywords', 'N/A')}

## Abstract:
{paper.get('abstract', 'No abstract available')}
"""
    
    user_prompt = f"""Analyze this research paper and identify the prior works that DIRECTLY led to its core innovation.

{paper_context}

---

TASK: Identify 5-7 prior works that DIRECTLY influenced this paper's KEY CONTRIBUTION. 

Focus on papers that:
1. Introduced ideas/methods this paper directly builds on
2. Had limitations this paper explicitly addresses  
3. Defined the problem formulation used here
4. Are the primary baselines being improved upon

DO NOT include generic tools, orthogonal optimizations, or tangentially related work.

Return your analysis as valid JSON."""
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = call_gpt5(messages, api_key)
        
        # Parse JSON response
        response_text = response.strip()
        
        # Handle markdown code blocks
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            parts = response_text.split("```")
            if len(parts) >= 2:
                response_text = parts[1].strip()
        
        # Try to find JSON object
        json_match = re.search(r'\{[\s\S]*\}', response_text)
        if json_match:
            response_text = json_match.group()
        
        analysis = json.loads(response_text)
        
        # Add paper metadata to analysis
        analysis["target_paper"] = {
            "title": paper.get('title'),
            "authors": paper.get('authors'),
            "conference": paper.get('conference'),
            "year": paper.get('year'),
            "presentation_type": paper.get('presentation_type'),
            "keywords": paper.get('keywords'),
            "abstract": paper.get('abstract'),
            "openreview_id": paper.get('openreview_id'),
            "forum_id": paper.get('forum_id')
        }
        analysis["analysis_timestamp"] = datetime.now().isoformat()
        
        return analysis
        
    except json.JSONDecodeError as e:
        print(f"    [ERROR] Failed to parse JSON response: {e}")
        return None
    except Exception as e:
        print(f"    [ERROR] API call failed: {e}")
        return None

def process_single_paper(paper, api_key, output_dir, checkpoint_mgr):
    """
    Process a single paper and save results.
    
    Returns:
        Tuple of (paper_id, success_bool, error_message)
    """
    paper_id = paper.get('openreview_id') or paper.get('forum_id') or paper.get('title', 'unknown')[:50]
    safe_id = paper_id.replace('/', '_').replace('\\', '_')
    
    # Skip if already processed
    if checkpoint_mgr.is_processed(safe_id):
        return (safe_id, True, "skipped - already processed")
    
    try:
        # Analyze paper
        analysis = analyze_paper_from_metadata(paper, api_key)
        
        if analysis is None:
            checkpoint_mgr.mark_processed(safe_id, status="failed", error="Analysis returned None")
            return (safe_id, False, "Analysis returned None")
        
        # Save JSON
        json_path = output_dir / f"{safe_id}.json"
        with open(json_path, 'w') as f:
            json.dump(analysis, f, indent=2)
        
        # Save Markdown
        md_content = generate_markdown_report(analysis)
        md_path = output_dir / f"{safe_id}.md"
        with open(md_path, 'w') as f:
            f.write(md_content)
        
        checkpoint_mgr.mark_processed(safe_id, status="success")
        return (safe_id, True, None)
        
    except Exception as e:
        error_msg = str(e)
        checkpoint_mgr.mark_processed(safe_id, status="failed", error=error_msg)
        return (safe_id, False, error_msg)

# ============================================================================
# CONFERENCE PROCESSOR
# ============================================================================

def process_conference(conference_name, papers, api_key, output_dir, checkpoint_mgr):
    """
    Process all papers from a single conference.
    
    Args:
        conference_name: e.g., "ICLR_2024"
        papers: List of paper dicts
        api_key: OpenAI API key
        output_dir: Base output directory
        checkpoint_mgr: CheckpointManager instance
    
    Returns:
        Dict with processing statistics
    """
    conf_output_dir = output_dir / conference_name
    conf_output_dir.mkdir(parents=True, exist_ok=True)
    
    total = len(papers)
    completed = 0
    failed = 0
    skipped = 0
    
    checkpoint_mgr.update_conference_progress(conference_name, total=total)
    
    print(f"\n{'='*60}")
    print(f"Processing {conference_name}: {total} papers")
    print(f"{'='*60}")
    
    for i, paper in enumerate(papers):
        paper_id = paper.get('openreview_id') or paper.get('forum_id') or f"paper_{i}"
        safe_id = paper_id.replace('/', '_').replace('\\', '_')
        
        # Progress indicator
        progress_pct = (i + 1) / total * 100
        title_preview = paper.get('title', 'Unknown')[:55]
        print(f"  [{i+1}/{total}] ({progress_pct:.1f}%) {title_preview}...")
        
        # Process paper
        pid, success, error = process_single_paper(paper, api_key, conf_output_dir, checkpoint_mgr)
        
        if error == "skipped - already processed":
            skipped += 1
            print(f"    [SKIP] Already processed")
        elif success:
            completed += 1
            print(f"    [OK] Saved to {safe_id}.json")
        else:
            failed += 1
            print(f"    [FAIL] {error}")
        
        # Save checkpoint periodically
        if (i + 1) % CHECKPOINT_INTERVAL == 0:
            checkpoint_mgr.update_conference_progress(
                conference_name, 
                completed=completed + skipped, 
                failed=failed
            )
            checkpoint_mgr.save()
            print(f"    [CHECKPOINT] Saved progress ({completed + skipped}/{total})")
    
    # Final checkpoint for this conference
    checkpoint_mgr.update_conference_progress(
        conference_name, 
        completed=completed + skipped, 
        failed=failed
    )
    checkpoint_mgr.save()
    
    return {
        "conference": conference_name,
        "total": total,
        "completed": completed,
        "failed": failed,
        "skipped": skipped
    }

# ============================================================================
# MAIN BATCH PROCESSOR
# ============================================================================

def load_all_papers():
    """Load all oral/spotlight papers from both datasets."""
    papers_by_conference = {}
    
    # Load 2023-2024 papers
    path_2324 = DATA_DIR_2324 / "oral_spotlight_papers_fast.json"
    if path_2324.exists():
        with open(path_2324) as f:
            data = json.load(f)
        
        for paper in data:
            conf_key = f"{paper['conference']}_{paper['year']}"
            if conf_key not in papers_by_conference:
                papers_by_conference[conf_key] = []
            papers_by_conference[conf_key].append(paper)
    
    # Load 2025 papers
    path_2025 = DATA_DIR_2025 / "oral_spotlight_papers_2025.json"
    if path_2025.exists():
        with open(path_2025) as f:
            data = json.load(f)
        
        for paper in data:
            conf_key = f"{paper['conference']}_{paper['year']}"
            if conf_key not in papers_by_conference:
                papers_by_conference[conf_key] = []
            papers_by_conference[conf_key].append(paper)
    
    return papers_by_conference

def run_batch_processing(api_key, output_dir, max_parallel=2):
    """
    Run batch processing on all papers.
    
    Args:
        api_key: OpenAI API key
        output_dir: Output directory path
        max_parallel: Max conferences to process in parallel
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Initialize checkpoint manager
    checkpoint_mgr = CheckpointManager(output_path)
    
    # Load all papers
    print("Loading papers from datasets...")
    papers_by_conference = load_all_papers()
    
    # Print summary
    print("\n" + "="*60)
    print("BATCH PROCESSING SUMMARY")
    print("="*60)
    total_papers = 0
    conferences = sorted(papers_by_conference.keys())
    for conf in conferences:
        count = len(papers_by_conference[conf])
        total_papers += count
        print(f"  {conf}: {count} papers")
    print(f"\n  TOTAL: {total_papers} papers across {len(conferences)} conferences")
    print("="*60)
    
    # Check existing progress
    stats = checkpoint_mgr.get_stats()
    if stats["total_processed"] > 0:
        print(f"\n[RESUME] Found existing checkpoint:")
        print(f"  Already processed: {stats['total_processed']}")
        print(f"  Previously failed: {stats['total_failed']}")
    
    # Process conferences in parallel (2 at a time)
    print(f"\nProcessing {max_parallel} conferences in parallel...")
    print(f"Rate limit: {REQUESTS_PER_MINUTE} requests/minute")
    
    start_time = time.time()
    all_results = []
    
    # Use ThreadPoolExecutor for parallel conference processing
    with ThreadPoolExecutor(max_workers=max_parallel) as executor:
        futures = {}
        
        for conf in conferences:
            papers = papers_by_conference[conf]
            future = executor.submit(
                process_conference,
                conf,
                papers,
                api_key,
                output_path,
                checkpoint_mgr
            )
            futures[future] = conf
        
        # Collect results as they complete
        for future in as_completed(futures):
            conf = futures[future]
            try:
                result = future.result()
                all_results.append(result)
                print(f"\n[COMPLETE] {conf}: {result['completed']}/{result['total']} successful")
            except Exception as e:
                print(f"\n[ERROR] {conf} failed: {e}")
    
    # Final summary
    elapsed = time.time() - start_time
    final_stats = checkpoint_mgr.get_stats()
    
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    print(f"Total processed: {final_stats['total_processed']}")
    print(f"Total failed: {final_stats['total_failed']}")
    print(f"Time elapsed: {elapsed/3600:.2f} hours")
    if elapsed > 0:
        print(f"Average: {final_stats['total_processed'] / (elapsed/60):.1f} papers/minute")
    print("="*60)
    
    # Save final summary
    summary = {
        "completed_at": datetime.now().isoformat(),
        "total_processed": final_stats['total_processed'],
        "total_failed": final_stats['total_failed'],
        "elapsed_seconds": elapsed,
        "conferences": all_results
    }
    
    with open(output_path / "batch_summary.json", 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nResults saved to: {output_path}")
    print(f"Checkpoint file: {output_path}/checkpoint.json")

# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Batch Prior Work Extraction Pipeline")
    parser.add_argument("--api-key", required=True, help="OpenAI API key")
    parser.add_argument("--output-dir", default="results/batch", help="Output directory")
    parser.add_argument("--max-parallel", type=int, default=2, help="Max parallel conferences")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    
    args = parser.parse_args()
    
    # Run batch processing
    run_batch_processing(
        api_key=args.api_key,
        output_dir=args.output_dir,
        max_parallel=args.max_parallel
    )

if __name__ == "__main__":
    main()

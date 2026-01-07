#!/usr/bin/env python3
"""
Batch Prior Work Extraction Pipeline v2
========================================
With retry mechanism and exponential backoff for rate limits.

Features:
- Exponential backoff retry (up to 5 retries)
- Lower rate limit (20 req/min) to avoid quota issues
- Retry-only mode for failed papers
- Better error handling

Usage:
    # Normal run (skips already successful papers)
    python batch_processor_v2.py --api-key "KEY" --output-dir results/batch
    
    # Retry only failed papers
    python batch_processor_v2.py --api-key "KEY" --output-dir results/batch --retry-failed
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
import random

# ============================================================================
# CONFIGURATION
# ============================================================================

# Rate limiting - VERY CONSERVATIVE to avoid quota issues
REQUESTS_PER_MINUTE = 10  # Very conservative - 1 request per 6 seconds
REQUEST_DELAY = 60.0 / REQUESTS_PER_MINUTE  # 6 seconds between requests

# Retry configuration
MAX_RETRIES = 8  # More retries
INITIAL_BACKOFF = 30  # Start with 30 seconds
MAX_BACKOFF = 300  # Up to 5 minutes

# Parallel processing - reduced to 1 to avoid rate limits
MAX_PARALLEL_CONFERENCES = 1  # Process 1 conference at a time

# Checkpointing
CHECKPOINT_INTERVAL = 10

# Data paths
WORKSPACE_ROOT = Path(__file__).parent.parent.parent.parent
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
# RATE LIMITER WITH BACKOFF
# ============================================================================

class RateLimiter:
    """Thread-safe rate limiter with adaptive backoff."""
    
    def __init__(self, requests_per_minute):
        self.min_interval = 60.0 / requests_per_minute
        self.last_request_time = 0
        self.lock = threading.Lock()
        self.backoff_until = 0  # Timestamp until which we should wait
    
    def wait(self):
        """Wait if necessary to respect rate limit."""
        with self.lock:
            now = time.time()
            
            # Check if we're in backoff period
            if now < self.backoff_until:
                sleep_time = self.backoff_until - now
                print(f"    [RATE LIMIT] Backing off for {sleep_time:.1f}s...")
                time.sleep(sleep_time)
                now = time.time()
            
            # Normal rate limiting
            elapsed = now - self.last_request_time
            if elapsed < self.min_interval:
                sleep_time = self.min_interval - elapsed
                time.sleep(sleep_time)
            
            self.last_request_time = time.time()
    
    def trigger_backoff(self, seconds):
        """Trigger a backoff period after rate limit error."""
        with self.lock:
            self.backoff_until = time.time() + seconds

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
        
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file) as f:
                self.state = json.load(f)
        else:
            self.state = {
                "processed_papers": {},
                "conference_progress": {},
                "started_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "total_processed": 0,
                "total_failed": 0
            }
    
    def is_processed_successfully(self, paper_id):
        """Check if paper has been successfully processed."""
        if paper_id not in self.state["processed_papers"]:
            return False
        return self.state["processed_papers"][paper_id].get("status") == "success"
    
    def is_failed(self, paper_id):
        """Check if paper has failed processing."""
        if paper_id not in self.state["processed_papers"]:
            return False
        return self.state["processed_papers"][paper_id].get("status") == "failed"
    
    def get_failed_papers(self):
        """Get list of failed paper IDs."""
        return [
            paper_id for paper_id, info in self.state["processed_papers"].items()
            if info.get("status") == "failed"
        ]
    
    def mark_processed(self, paper_id, status="success", error=None):
        """Mark a paper as processed."""
        with self.lock:
            was_failed = self.state["processed_papers"].get(paper_id, {}).get("status") == "failed"
            
            self.state["processed_papers"][paper_id] = {
                "status": status,
                "timestamp": datetime.now().isoformat(),
                "error": error
            }
            
            # Update counts
            if status == "success":
                if was_failed:
                    # Converting from failed to success
                    self.state["total_failed"] = max(0, self.state["total_failed"] - 1)
                self.state["total_processed"] += 1
            elif status == "failed" and not was_failed:
                self.state["total_failed"] += 1
            
            self.state["last_updated"] = datetime.now().isoformat()
    
    def clear_failed_status(self, paper_id):
        """Clear failed status to allow retry."""
        with self.lock:
            if paper_id in self.state["processed_papers"]:
                if self.state["processed_papers"][paper_id].get("status") == "failed":
                    del self.state["processed_papers"][paper_id]
                    self.state["total_failed"] = max(0, self.state["total_failed"] - 1)
    
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
# GPT-5 API WITH RETRY
# ============================================================================

def call_gpt5_with_retry(messages, api_key, max_retries=MAX_RETRIES):
    """Call GPT-5 API with exponential backoff retry."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-5",
        "messages": messages
    }
    
    last_error = None
    
    for attempt in range(max_retries):
        try:
            # Wait for rate limiter
            rate_limiter.wait()
            
            response = requests.post(
                OPENAI_API_URL,
                headers=headers,
                json=payload,
                timeout=300
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            
            elif response.status_code == 429:
                # Rate limit - exponential backoff
                backoff = min(INITIAL_BACKOFF * (2 ** attempt) + random.uniform(0, 1), MAX_BACKOFF)
                print(f"    [RETRY {attempt+1}/{max_retries}] Rate limited (429). Backing off {backoff:.1f}s...")
                rate_limiter.trigger_backoff(backoff)
                time.sleep(backoff)
                last_error = f"Rate limited (429)"
                
            elif response.status_code >= 500:
                # Server error - retry with backoff
                backoff = min(INITIAL_BACKOFF * (2 ** attempt), MAX_BACKOFF)
                print(f"    [RETRY {attempt+1}/{max_retries}] Server error ({response.status_code}). Backing off {backoff:.1f}s...")
                time.sleep(backoff)
                last_error = f"Server error ({response.status_code})"
                
            else:
                # Other error - don't retry
                raise Exception(f"GPT-5 API error: {response.status_code} - {response.text[:200]}")
                
        except requests.exceptions.Timeout:
            backoff = min(INITIAL_BACKOFF * (2 ** attempt), MAX_BACKOFF)
            print(f"    [RETRY {attempt+1}/{max_retries}] Timeout. Backing off {backoff:.1f}s...")
            time.sleep(backoff)
            last_error = "Timeout"
            
        except requests.exceptions.RequestException as e:
            backoff = min(INITIAL_BACKOFF * (2 ** attempt), MAX_BACKOFF)
            print(f"    [RETRY {attempt+1}/{max_retries}] Request error: {e}. Backing off {backoff:.1f}s...")
            time.sleep(backoff)
            last_error = str(e)
    
    raise Exception(f"Failed after {max_retries} retries. Last error: {last_error}")

# ============================================================================
# MARKDOWN GENERATOR
# ============================================================================

def generate_markdown_report(analysis):
    """Generate a markdown report from analysis results."""
    
    target = analysis.get("target_paper", {})
    prior_works = analysis.get("prior_works", [])
    synthesis = analysis.get("synthesis_narrative", "")
    
    works_by_role = defaultdict(list)
    for pw in prior_works:
        role = pw.get("role", "Unknown")
        works_by_role[role].append(pw)
    
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
    """Analyze a paper using only its metadata."""
    
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
        response = call_gpt5_with_retry(messages, api_key)
        
        response_text = response.strip()
        
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            parts = response_text.split("```")
            if len(parts) >= 2:
                response_text = parts[1].strip()
        
        json_match = re.search(r'\{[\s\S]*\}', response_text)
        if json_match:
            response_text = json_match.group()
        
        analysis = json.loads(response_text)
        
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

def process_single_paper(paper, api_key, output_dir, checkpoint_mgr, force_retry=False):
    """Process a single paper and save results."""
    paper_id = paper.get('openreview_id') or paper.get('forum_id') or paper.get('title', 'unknown')[:50]
    safe_id = paper_id.replace('/', '_').replace('\\', '_')
    
    # Skip if already successful (unless force_retry)
    if checkpoint_mgr.is_processed_successfully(safe_id) and not force_retry:
        return (safe_id, True, "skipped - already successful")
    
    try:
        analysis = analyze_paper_from_metadata(paper, api_key)
        
        if analysis is None:
            checkpoint_mgr.mark_processed(safe_id, status="failed", error="Analysis returned None")
            return (safe_id, False, "Analysis returned None")
        
        json_path = output_dir / f"{safe_id}.json"
        with open(json_path, 'w') as f:
            json.dump(analysis, f, indent=2)
        
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

def process_conference(conference_name, papers, api_key, output_dir, checkpoint_mgr, retry_failed_only=False):
    """Process all papers from a single conference."""
    conf_output_dir = output_dir / conference_name
    conf_output_dir.mkdir(parents=True, exist_ok=True)
    
    # Filter papers based on mode
    if retry_failed_only:
        failed_ids = set(checkpoint_mgr.get_failed_papers())
        papers_to_process = []
        for paper in papers:
            paper_id = paper.get('openreview_id') or paper.get('forum_id') or paper.get('title', 'unknown')[:50]
            safe_id = paper_id.replace('/', '_').replace('\\', '_')
            if safe_id in failed_ids:
                papers_to_process.append(paper)
        print(f"  [RETRY MODE] Found {len(papers_to_process)} failed papers to retry")
    else:
        papers_to_process = papers
    
    total = len(papers_to_process)
    if total == 0:
        return {"conference": conference_name, "total": 0, "completed": 0, "failed": 0, "skipped": 0}
    
    completed = 0
    failed = 0
    skipped = 0
    
    checkpoint_mgr.update_conference_progress(conference_name, total=len(papers))
    
    print(f"\n{'='*60}")
    print(f"Processing {conference_name}: {total} papers")
    print(f"{'='*60}")
    
    for i, paper in enumerate(papers_to_process):
        paper_id = paper.get('openreview_id') or paper.get('forum_id') or f"paper_{i}"
        safe_id = paper_id.replace('/', '_').replace('\\', '_')
        
        progress_pct = (i + 1) / total * 100
        title_preview = paper.get('title', 'Unknown')[:55]
        print(f"  [{i+1}/{total}] ({progress_pct:.1f}%) {title_preview}...")
        
        pid, success, error = process_single_paper(
            paper, api_key, conf_output_dir, checkpoint_mgr, 
            force_retry=retry_failed_only
        )
        
        if error == "skipped - already successful":
            skipped += 1
            print(f"    [SKIP] Already successful")
        elif success:
            completed += 1
            print(f"    [OK] Saved to {safe_id}.json")
        else:
            failed += 1
            print(f"    [FAIL] {error}")
        
        if (i + 1) % CHECKPOINT_INTERVAL == 0:
            checkpoint_mgr.save()
            print(f"    [CHECKPOINT] Saved progress")
    
    checkpoint_mgr.save()
    
    return {
        "conference": conference_name,
        "total": total,
        "completed": completed,
        "failed": failed,
        "skipped": skipped
    }

# ============================================================================
# MAIN
# ============================================================================

def load_all_papers():
    """Load all oral/spotlight papers from both datasets."""
    papers_by_conference = {}
    
    path_2324 = DATA_DIR_2324 / "oral_spotlight_papers_fast.json"
    if path_2324.exists():
        with open(path_2324) as f:
            data = json.load(f)
        for paper in data:
            conf_key = f"{paper['conference']}_{paper['year']}"
            if conf_key not in papers_by_conference:
                papers_by_conference[conf_key] = []
            papers_by_conference[conf_key].append(paper)
    
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

def run_batch_processing(api_key, output_dir, max_parallel=1, retry_failed_only=False):
    """Run batch processing on all papers."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    checkpoint_mgr = CheckpointManager(output_path)
    
    print("Loading papers from datasets...")
    papers_by_conference = load_all_papers()
    
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
    
    if retry_failed_only:
        failed_count = len(checkpoint_mgr.get_failed_papers())
        print(f"\n  [RETRY MODE] Will retry {failed_count} failed papers")
    
    print("="*60)
    
    stats = checkpoint_mgr.get_stats()
    if stats["total_processed"] > 0:
        print(f"\n[RESUME] Found existing checkpoint:")
        print(f"  Already processed: {stats['total_processed']}")
        print(f"  Previously failed: {stats['total_failed']}")
    
    print(f"\nProcessing {max_parallel} conference(s) at a time...")
    print(f"Rate limit: {REQUESTS_PER_MINUTE} requests/minute")
    print(f"Max retries per request: {MAX_RETRIES}")
    
    start_time = time.time()
    all_results = []
    
    # Process conferences sequentially to avoid rate limits
    for conf in conferences:
        papers = papers_by_conference[conf]
        try:
            result = process_conference(
                conf, papers, api_key, output_path, checkpoint_mgr,
                retry_failed_only=retry_failed_only
            )
            all_results.append(result)
            print(f"\n[COMPLETE] {conf}: {result['completed']}/{result['total']} successful")
        except Exception as e:
            print(f"\n[ERROR] {conf} failed: {e}")
    
    elapsed = time.time() - start_time
    final_stats = checkpoint_mgr.get_stats()
    
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    print(f"Total processed: {final_stats['total_processed']}")
    print(f"Total failed: {final_stats['total_failed']}")
    print(f"Time elapsed: {elapsed/3600:.2f} hours")
    if elapsed > 0:
        print(f"Average: {sum(r['completed'] for r in all_results) / (elapsed/60):.1f} papers/minute")
    print("="*60)
    
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

def main():
    parser = argparse.ArgumentParser(description="Batch Prior Work Extraction Pipeline v2")
    parser.add_argument("--api-key", required=True, help="OpenAI API key")
    parser.add_argument("--output-dir", default="results/batch", help="Output directory")
    parser.add_argument("--max-parallel", type=int, default=1, help="Max parallel conferences")
    parser.add_argument("--retry-failed", action="store_true", help="Only retry failed papers")
    
    args = parser.parse_args()
    
    run_batch_processing(
        api_key=args.api_key,
        output_dir=args.output_dir,
        max_parallel=args.max_parallel,
        retry_failed_only=args.retry_failed
    )

if __name__ == "__main__":
    main()

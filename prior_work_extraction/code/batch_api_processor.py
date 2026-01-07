#!/usr/bin/env python3
"""
Batch API Prior Work Extraction Pipeline
=========================================
Uses OpenAI Batch API for 50% cost savings and high throughput.

Workflow:
1. Prepare batch input file (JSONL)
2. Upload file to OpenAI
3. Create batch job
4. Poll for completion
5. Download and process results

Usage:
    # Step 1: Prepare and submit batch
    python batch_api_processor.py --api-key "KEY" --output-dir results/batch --prepare-batch
    
    # Step 2: Check batch status
    python batch_api_processor.py --api-key "KEY" --output-dir results/batch --check-batch
    
    # Step 3: Process completed batch results
    python batch_api_processor.py --api-key "KEY" --output-dir results/batch --process-results
"""

import os
import sys
import json
import time
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict
from openai import OpenAI

# ============================================================================
# CONFIGURATION
# ============================================================================

WORKSPACE_ROOT = Path(__file__).parent.parent.parent.parent
DATA_DIR_2324 = WORKSPACE_ROOT / "projects/ml_paper_acquisition/results/data/2023-2024"
DATA_DIR_2025 = WORKSPACE_ROOT / "projects/ml_paper_acquisition/results/data/2025"

# Batch settings
BATCH_SIZE = 500  # Papers per batch file (OpenAI limit considerations)
COMPLETION_WINDOW = "24h"  # Can be "24h" for cheaper processing

# ============================================================================
# PROMPTS
# ============================================================================

SYSTEM_PROMPT = """You are an expert AI research analyst. Your task is to identify the KEY PRIOR WORKS that DIRECTLY led to a research paper's core innovation.

## CRITICAL: Focus on DIRECT Intellectual Lineage

You must identify papers that are **directly responsible** for the current paper's main contributions. Ask yourself:
- "Without this prior work, would the current paper's core idea exist?"
- "Did this prior work directly inspire, enable, or motivate the KEY INNOVATION?"

### ❌ DO NOT INCLUDE:
- Generic infrastructure/tools (e.g., PyTorch, CUDA, standard attention mechanisms)
- Complementary optimizations that are orthogonal to the main contribution
- Papers that share the same domain but don't directly influence the core idea

### ✅ DO INCLUDE:
- Papers whose specific IDEAS, METHODS, or FINDINGS directly shaped the current work
- Papers whose LIMITATIONS or GAPS the current paper explicitly addresses
- Papers that introduced the PROBLEM FORMULATION the current paper builds on
- Papers whose TECHNIQUES are directly extended or modified

## Role Classifications (assign ONE per paper):

1. **Baseline**: The primary system/method this paper improves upon
2. **Inspiration**: Paper whose specific idea directly sparked the current paper's key innovation  
3. **Gap Identification**: Paper whose explicit limitations motivated this research
4. **Foundation**: Paper that introduced the core problem formulation or theoretical framework
5. **Extension**: Paper whose specific method is directly extended or modified
6. **Related Problem**: Paper solving a related problem whose approach informed this work

## Output Format (JSON):
```json
{
  "prior_works": [
    {
      "title": "Exact paper title",
      "authors": "First author et al.",
      "year": 2023,
      "role": "One of six roles",
      "relationship_sentence": "Specific sentence about DIRECT connection"
    }
  ],
  "synthesis_narrative": "200-300 word flowing narrative"
}
```"""

# ============================================================================
# CHECKPOINT MANAGER
# ============================================================================

class CheckpointManager:
    """Manages checkpoints for resumable processing."""
    
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoint_file = self.checkpoint_dir / "checkpoint.json"
        
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
                "total_failed": 0,
                "batch_jobs": {}  # Track batch job IDs
            }
    
    def is_processed_successfully(self, paper_id):
        """Check if paper has been successfully processed."""
        if paper_id not in self.state["processed_papers"]:
            return False
        return self.state["processed_papers"][paper_id].get("status") == "success"
    
    def get_failed_papers(self):
        """Get list of failed paper IDs."""
        return [
            paper_id for paper_id, info in self.state["processed_papers"].items()
            if info.get("status") == "failed"
        ]
    
    def mark_processed(self, paper_id, status="success", error=None):
        """Mark a paper as processed."""
        was_failed = self.state["processed_papers"].get(paper_id, {}).get("status") == "failed"
        
        self.state["processed_papers"][paper_id] = {
            "status": status,
            "timestamp": datetime.now().isoformat(),
            "error": error
        }
        
        if status == "success":
            if was_failed:
                self.state["total_failed"] = max(0, self.state["total_failed"] - 1)
            self.state["total_processed"] += 1
        elif status == "failed" and not was_failed:
            self.state["total_failed"] += 1
        
        self.state["last_updated"] = datetime.now().isoformat()
    
    def add_batch_job(self, batch_id, file_id, paper_ids):
        """Track a batch job."""
        self.state["batch_jobs"][batch_id] = {
            "file_id": file_id,
            "paper_ids": paper_ids,
            "status": "submitted",
            "submitted_at": datetime.now().isoformat()
        }
        self.save()
    
    def update_batch_status(self, batch_id, status):
        """Update batch job status."""
        if batch_id in self.state["batch_jobs"]:
            self.state["batch_jobs"][batch_id]["status"] = status
            self.state["batch_jobs"][batch_id]["updated_at"] = datetime.now().isoformat()
            self.save()
    
    def get_pending_batches(self):
        """Get batch jobs that are still pending."""
        return {
            bid: info for bid, info in self.state.get("batch_jobs", {}).items()
            if info.get("status") not in ["completed", "failed", "processed"]
        }
    
    def save(self):
        """Save checkpoint to disk."""
        self.state["last_updated"] = datetime.now().isoformat()
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def get_stats(self):
        """Get current processing statistics."""
        return {
            "total_processed": self.state["total_processed"],
            "total_failed": self.state["total_failed"],
            "batch_jobs": len(self.state.get("batch_jobs", {}))
        }

# ============================================================================
# DATA LOADING
# ============================================================================

def load_all_papers():
    """Load all oral/spotlight papers from both datasets."""
    papers_by_conference = {}
    all_papers = []
    
    path_2324 = DATA_DIR_2324 / "oral_spotlight_papers_fast.json"
    if path_2324.exists():
        with open(path_2324) as f:
            data = json.load(f)
        for paper in data:
            conf_key = f"{paper['conference']}_{paper['year']}"
            if conf_key not in papers_by_conference:
                papers_by_conference[conf_key] = []
            papers_by_conference[conf_key].append(paper)
            all_papers.append(paper)
    
    path_2025 = DATA_DIR_2025 / "oral_spotlight_papers_2025.json"
    if path_2025.exists():
        with open(path_2025) as f:
            data = json.load(f)
        for paper in data:
            conf_key = f"{paper['conference']}_{paper['year']}"
            if conf_key not in papers_by_conference:
                papers_by_conference[conf_key] = []
            papers_by_conference[conf_key].append(paper)
            all_papers.append(paper)
    
    return papers_by_conference, all_papers

def get_paper_id(paper):
    """Get unique ID for a paper."""
    paper_id = paper.get('openreview_id') or paper.get('forum_id') or paper.get('title', 'unknown')[:50]
    return paper_id.replace('/', '_').replace('\\', '_')

# ============================================================================
# BATCH PREPARATION
# ============================================================================

def create_batch_request(paper, custom_id):
    """Create a single batch request for a paper."""
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

Return your analysis as valid JSON."""
    
    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]
        }
    }

def prepare_batch_files(papers, checkpoint_mgr, output_dir, retry_failed=True):
    """Prepare JSONL batch files for papers that need processing."""
    
    # Filter papers that need processing
    papers_to_process = []
    for paper in papers:
        paper_id = get_paper_id(paper)
        
        # Skip already successful
        if checkpoint_mgr.is_processed_successfully(paper_id):
            continue
        
        # If retry_failed, include failed papers
        if retry_failed or paper_id not in checkpoint_mgr.state["processed_papers"]:
            papers_to_process.append((paper_id, paper))
    
    print(f"Papers to process: {len(papers_to_process)}")
    
    if not papers_to_process:
        print("No papers to process!")
        return []
    
    # Create batch files
    batch_files = []
    batch_dir = output_dir / "batch_files"
    batch_dir.mkdir(parents=True, exist_ok=True)
    
    for i in range(0, len(papers_to_process), BATCH_SIZE):
        batch_papers = papers_to_process[i:i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        
        batch_file = batch_dir / f"batch_{batch_num}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
        
        with open(batch_file, 'w') as f:
            for paper_id, paper in batch_papers:
                request = create_batch_request(paper, paper_id)
                f.write(json.dumps(request) + '\n')
        
        batch_files.append({
            "file": batch_file,
            "paper_ids": [p[0] for p in batch_papers],
            "count": len(batch_papers)
        })
        
        print(f"Created batch file {batch_num}: {batch_file.name} ({len(batch_papers)} papers)")
    
    return batch_files

# ============================================================================
# BATCH API OPERATIONS
# ============================================================================

def submit_batch(client, batch_file_info, checkpoint_mgr):
    """Submit a batch file to OpenAI Batch API."""
    batch_file = batch_file_info["file"]
    paper_ids = batch_file_info["paper_ids"]
    
    print(f"\nUploading {batch_file.name}...")
    
    # Upload file
    with open(batch_file, 'rb') as f:
        file_response = client.files.create(
            file=f,
            purpose="batch"
        )
    
    file_id = file_response.id
    print(f"  File uploaded: {file_id}")
    
    # Create batch
    batch_response = client.batches.create(
        input_file_id=file_id,
        endpoint="/v1/chat/completions",
        completion_window=COMPLETION_WINDOW
    )
    
    batch_id = batch_response.id
    print(f"  Batch created: {batch_id}")
    
    # Track in checkpoint
    checkpoint_mgr.add_batch_job(batch_id, file_id, paper_ids)
    
    return batch_id

def check_batch_status(client, checkpoint_mgr):
    """Check status of all pending batches."""
    pending = checkpoint_mgr.get_pending_batches()
    
    if not pending:
        print("No pending batches.")
        return {}
    
    print(f"\nChecking {len(pending)} pending batches...")
    
    statuses = {}
    for batch_id, info in pending.items():
        try:
            batch = client.batches.retrieve(batch_id)
            status = batch.status
            
            statuses[batch_id] = {
                "status": status,
                "request_counts": {
                    "total": batch.request_counts.total,
                    "completed": batch.request_counts.completed,
                    "failed": batch.request_counts.failed
                },
                "output_file_id": batch.output_file_id,
                "error_file_id": batch.error_file_id
            }
            
            checkpoint_mgr.update_batch_status(batch_id, status)
            
            print(f"  {batch_id}: {status} ({batch.request_counts.completed}/{batch.request_counts.total} completed)")
            
        except Exception as e:
            print(f"  {batch_id}: Error checking status - {e}")
            statuses[batch_id] = {"status": "error", "error": str(e)}
    
    return statuses

def download_and_process_results(client, checkpoint_mgr, output_dir):
    """Download and process completed batch results."""
    
    # Check for completed batches
    statuses = check_batch_status(client, checkpoint_mgr)
    
    completed_batches = [
        (bid, info) for bid, info in statuses.items()
        if info.get("status") == "completed" and info.get("output_file_id")
    ]
    
    if not completed_batches:
        print("No completed batches to process.")
        return
    
    print(f"\nProcessing {len(completed_batches)} completed batches...")
    
    for batch_id, info in completed_batches:
        output_file_id = info["output_file_id"]
        
        print(f"\nDownloading results for batch {batch_id}...")
        
        try:
            # Download output file
            content = client.files.content(output_file_id)
            results_text = content.text
            
            # Process each result
            success_count = 0
            fail_count = 0
            
            for line in results_text.strip().split('\n'):
                if not line:
                    continue
                
                result = json.loads(line)
                paper_id = result.get("custom_id")
                
                if result.get("error"):
                    checkpoint_mgr.mark_processed(paper_id, status="failed", error=str(result["error"]))
                    fail_count += 1
                    continue
                
                try:
                    # Extract response
                    response_body = result.get("response", {}).get("body", {})
                    content = response_body.get("choices", [{}])[0].get("message", {}).get("content", "")
                    
                    # Parse JSON from response
                    response_text = content.strip()
                    if "```json" in response_text:
                        response_text = response_text.split("```json")[1].split("```")[0].strip()
                    elif "```" in response_text:
                        parts = response_text.split("```")
                        if len(parts) >= 2:
                            response_text = parts[1].strip()
                    
                    import re
                    json_match = re.search(r'\{[\s\S]*\}', response_text)
                    if json_match:
                        response_text = json_match.group()
                    
                    analysis = json.loads(response_text)
                    
                    # Get paper info from checkpoint batch job
                    batch_info = checkpoint_mgr.state["batch_jobs"].get(batch_id, {})
                    
                    # Add metadata
                    analysis["analysis_timestamp"] = datetime.now().isoformat()
                    analysis["batch_id"] = batch_id
                    
                    # Determine conference from paper_id pattern or save to general folder
                    conf_output_dir = output_dir / "batch_results"
                    conf_output_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Save JSON
                    json_path = conf_output_dir / f"{paper_id}.json"
                    with open(json_path, 'w') as f:
                        json.dump(analysis, f, indent=2)
                    
                    # Save Markdown
                    md_content = generate_markdown_report(analysis, paper_id)
                    md_path = conf_output_dir / f"{paper_id}.md"
                    with open(md_path, 'w') as f:
                        f.write(md_content)
                    
                    checkpoint_mgr.mark_processed(paper_id, status="success")
                    success_count += 1
                    
                except Exception as e:
                    checkpoint_mgr.mark_processed(paper_id, status="failed", error=str(e))
                    fail_count += 1
            
            # Mark batch as processed
            checkpoint_mgr.update_batch_status(batch_id, "processed")
            checkpoint_mgr.save()
            
            print(f"  Batch {batch_id}: {success_count} success, {fail_count} failed")
            
        except Exception as e:
            print(f"  Error processing batch {batch_id}: {e}")

# ============================================================================
# MARKDOWN GENERATOR
# ============================================================================

def generate_markdown_report(analysis, paper_id):
    """Generate a markdown report from analysis results."""
    
    prior_works = analysis.get("prior_works", [])
    synthesis = analysis.get("synthesis_narrative", "")
    
    works_by_role = defaultdict(list)
    for pw in prior_works:
        role = pw.get("role", "Unknown")
        works_by_role[role].append(pw)
    
    md = f"""# Prior Work Analysis Report

## Paper ID: {paper_id}

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

*Pipeline: Prior Work Extraction - Batch API*
"""
    
    return md

# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Batch API Prior Work Extraction")
    parser.add_argument("--api-key", required=True, help="OpenAI API key")
    parser.add_argument("--output-dir", default="results/batch", help="Output directory")
    parser.add_argument("--prepare-batch", action="store_true", help="Prepare and submit batch jobs")
    parser.add_argument("--check-batch", action="store_true", help="Check batch job status")
    parser.add_argument("--process-results", action="store_true", help="Process completed batch results")
    parser.add_argument("--retry-failed", action="store_true", default=True, help="Include failed papers")
    parser.add_argument("--max-batches", type=int, default=10, help="Max batches to submit at once")
    
    args = parser.parse_args()
    
    # Initialize client
    client = OpenAI(api_key=args.api_key)
    
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    checkpoint_mgr = CheckpointManager(output_path)
    
    # Load papers
    print("Loading papers...")
    papers_by_conf, all_papers = load_all_papers()
    print(f"Total papers: {len(all_papers)}")
    
    stats = checkpoint_mgr.get_stats()
    print(f"Already processed: {stats['total_processed']}")
    print(f"Failed: {stats['total_failed']}")
    
    if args.prepare_batch:
        print("\n" + "="*60)
        print("PREPARING AND SUBMITTING BATCHES")
        print("="*60)
        
        # Prepare batch files
        batch_files = prepare_batch_files(
            all_papers, checkpoint_mgr, output_path, 
            retry_failed=args.retry_failed
        )
        
        if not batch_files:
            return
        
        # Submit batches (limit to max_batches)
        batches_to_submit = batch_files[:args.max_batches]
        print(f"\nSubmitting {len(batches_to_submit)} batches...")
        
        for batch_info in batches_to_submit:
            try:
                batch_id = submit_batch(client, batch_info, checkpoint_mgr)
                print(f"  Submitted: {batch_id}")
            except Exception as e:
                print(f"  Error submitting batch: {e}")
        
        print("\nBatches submitted! Use --check-batch to monitor progress.")
    
    if args.check_batch:
        print("\n" + "="*60)
        print("CHECKING BATCH STATUS")
        print("="*60)
        
        check_batch_status(client, checkpoint_mgr)
    
    if args.process_results:
        print("\n" + "="*60)
        print("PROCESSING COMPLETED RESULTS")
        print("="*60)
        
        download_and_process_results(client, checkpoint_mgr, output_path)
        
        # Print final stats
        stats = checkpoint_mgr.get_stats()
        print(f"\nFinal stats:")
        print(f"  Processed: {stats['total_processed']}")
        print(f"  Failed: {stats['total_failed']}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Batch Monitor - Continuously monitors batches and resubmits when capacity available.
"""

import sys
import json
import time
import re
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from collections import defaultdict

API_KEY = "YOUR_OPENAI_API_KEY"
OUTPUT_DIR = Path(__file__).parent.parent / "results" / "batch"
CHECKPOINT_FILE = OUTPUT_DIR / "checkpoint.json"
BATCH_FILES_DIR = OUTPUT_DIR / "batch_files"

# Batch settings
BATCH_SIZE = 500
MAX_CONCURRENT_BATCHES = 3  # Stay under token limit

def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            return json.load(f)
    return {"processed_papers": {}, "total_processed": 0, "total_failed": 0, "batch_jobs": {}}

def save_checkpoint(checkpoint):
    checkpoint["last_updated"] = datetime.now().isoformat()
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(checkpoint, f, indent=2)

def generate_markdown_report(analysis, paper_id):
    """Generate markdown report."""
    prior_works = analysis.get("prior_works", [])
    synthesis = analysis.get("synthesis_narrative", "")
    target = analysis.get("target_paper", {})
    
    works_by_role = defaultdict(list)
    for pw in prior_works:
        works_by_role[pw.get("role", "Unknown")].append(pw)
    
    md = f"""# Prior Work Analysis Report

## Target Paper
**Title:** {target.get('title', paper_id)}
**Conference:** {target.get('conference', 'Unknown')} {target.get('year', '')}
**Authors:** {target.get('authors', 'Unknown')}

---

## Key Prior Works ({len(prior_works)} papers)

"""
    
    role_emojis = {"Baseline": "📊", "Inspiration": "💡", "Gap Identification": "🔍",
                   "Foundation": "🏗️", "Extension": "🔧", "Related Problem": "🔗"}
    
    for role in ["Foundation", "Inspiration", "Gap Identification", "Baseline", "Extension", "Related Problem"]:
        if role in works_by_role:
            md += f"### {role_emojis.get(role, '📄')} {role}\n\n"
            for pw in works_by_role[role]:
                md += f"**{pw.get('title', 'Unknown')}** ({pw.get('year', '')})\n"
                md += f"- *Authors:* {pw.get('authors', 'Unknown')}\n"
                md += f"- *Connection:* {pw.get('relationship_sentence', '')}\n\n"
    
    md += f"---\n\n## Synthesis\n\n{synthesis}\n\n---\n*Generated: {datetime.now().isoformat()}*\n"
    return md

def check_and_process(client, checkpoint):
    """Check batch status and process completed ones."""
    batches = client.batches.list(limit=20)
    
    in_progress_count = 0
    completed_batches = []
    
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Checking batches...")
    
    for batch in batches.data:
        if batch.status in ["in_progress", "validating", "finalizing"]:
            in_progress_count += 1
            print(f"  🔄 {batch.id[:20]}... {batch.status} ({batch.request_counts.completed}/{batch.request_counts.total})")
        elif batch.status == "completed":
            # Check if already processed
            if checkpoint.get("batch_jobs", {}).get(batch.id, {}).get("status") != "processed":
                completed_batches.append(batch)
                print(f"  ✅ {batch.id[:20]}... COMPLETED - ready to process")
            else:
                print(f"  ✅ {batch.id[:20]}... already processed")
    
    # Process completed batches
    results_dir = OUTPUT_DIR / "batch_results"
    results_dir.mkdir(parents=True, exist_ok=True)
    
    for batch in completed_batches:
        if not batch.output_file_id:
            continue
            
        print(f"\n  Processing {batch.id[:20]}...")
        
        try:
            content = client.files.content(batch.output_file_id)
            results_text = content.text
            
            success = 0
            fail = 0
            
            for line in results_text.strip().split('\n'):
                if not line:
                    continue
                
                result = json.loads(line)
                paper_id = result.get("custom_id")
                
                # Skip if already processed
                if checkpoint["processed_papers"].get(paper_id, {}).get("status") == "success":
                    continue
                
                if result.get("error"):
                    if checkpoint["processed_papers"].get(paper_id, {}).get("status") != "failed":
                        checkpoint["total_failed"] = checkpoint.get("total_failed", 0) + 1
                    checkpoint["processed_papers"][paper_id] = {"status": "failed", "error": str(result["error"])}
                    fail += 1
                    continue
                
                try:
                    response_body = result.get("response", {}).get("body", {})
                    content_text = response_body.get("choices", [{}])[0].get("message", {}).get("content", "")
                    
                    response_text = content_text.strip()
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
                    analysis["analysis_timestamp"] = datetime.now().isoformat()
                    
                    with open(results_dir / f"{paper_id}.json", 'w') as f:
                        json.dump(analysis, f, indent=2)
                    
                    md = generate_markdown_report(analysis, paper_id)
                    with open(results_dir / f"{paper_id}.md", 'w') as f:
                        f.write(md)
                    
                    # Only increment if not already successful
                    if checkpoint["processed_papers"].get(paper_id, {}).get("status") != "success":
                        checkpoint["total_processed"] = checkpoint.get("total_processed", 0) + 1
                    checkpoint["processed_papers"][paper_id] = {"status": "success"}
                    success += 1
                    
                except Exception as e:
                    if checkpoint["processed_papers"].get(paper_id, {}).get("status") != "failed":
                        checkpoint["total_failed"] = checkpoint.get("total_failed", 0) + 1
                    checkpoint["processed_papers"][paper_id] = {"status": "failed", "error": str(e)}
                    fail += 1
            
            if "batch_jobs" not in checkpoint:
                checkpoint["batch_jobs"] = {}
            checkpoint["batch_jobs"][batch.id] = {"status": "processed", "processed_at": datetime.now().isoformat()}
            save_checkpoint(checkpoint)
            
            print(f"    ✅ {success} success, ❌ {fail} failed")
            
        except Exception as e:
            print(f"    Error: {e}")
    
    return in_progress_count

def get_unprocessed_papers(checkpoint):
    """Get papers that haven't been successfully processed."""
    # Load all papers
    workspace_root = Path(__file__).parent.parent.parent.parent
    data_2324 = workspace_root / "projects/ml_paper_acquisition/results/data/2023-2024/oral_spotlight_papers_fast.json"
    data_2025 = workspace_root / "projects/ml_paper_acquisition/results/data/2025/oral_spotlight_papers_2025.json"
    
    all_papers = []
    for path in [data_2324, data_2025]:
        if path.exists():
            with open(path) as f:
                all_papers.extend(json.load(f))
    
    unprocessed = []
    for paper in all_papers:
        paper_id = paper.get('openreview_id') or paper.get('forum_id') or paper.get('title', 'unknown')[:50]
        paper_id = paper_id.replace('/', '_').replace('\\', '_')
        
        if checkpoint["processed_papers"].get(paper_id, {}).get("status") != "success":
            unprocessed.append((paper_id, paper))
    
    return unprocessed

def submit_batch(client, papers, batch_num, checkpoint):
    """Submit a batch of papers."""
    BATCH_FILES_DIR.mkdir(parents=True, exist_ok=True)
    
    batch_file = BATCH_FILES_DIR / f"batch_{batch_num}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
    
    SYSTEM_PROMPT = """You are an expert AI research analyst identifying KEY PRIOR WORKS that DIRECTLY led to a paper's core innovation. Focus on papers with direct intellectual contribution. Output JSON with prior_works array and synthesis_narrative."""
    
    with open(batch_file, 'w') as f:
        for paper_id, paper in papers:
            request = {
                "custom_id": paper_id,
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": "gpt-5",
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": f"""Analyze this paper and identify 5-7 prior works that DIRECTLY influenced its KEY CONTRIBUTION.

## Paper: {paper.get('title', 'Unknown')}
## Authors: {paper.get('authors', 'Unknown')}
## Conference: {paper.get('conference', '')} {paper.get('year', '')}
## Abstract: {paper.get('abstract', '')}

Return JSON with: prior_works (array with title, authors, year, role, relationship_sentence) and synthesis_narrative (200-300 words)."""}
                    ]
                }
            }
            f.write(json.dumps(request) + '\n')
    
    print(f"  Uploading batch {batch_num} ({len(papers)} papers)...")
    
    with open(batch_file, 'rb') as f:
        file_response = client.files.create(file=f, purpose="batch")
    
    batch_response = client.batches.create(
        input_file_id=file_response.id,
        endpoint="/v1/chat/completions",
        completion_window="24h"
    )
    
    if "batch_jobs" not in checkpoint:
        checkpoint["batch_jobs"] = {}
    checkpoint["batch_jobs"][batch_response.id] = {
        "status": "submitted",
        "paper_ids": [p[0] for p in papers],
        "submitted_at": datetime.now().isoformat()
    }
    save_checkpoint(checkpoint)
    
    print(f"  ✅ Batch submitted: {batch_response.id}")
    return batch_response.id

def main():
    client = OpenAI(api_key=API_KEY)
    checkpoint = load_checkpoint()
    
    print("="*70)
    print("BATCH MONITOR")
    print("="*70)
    print(f"Current stats: {checkpoint.get('total_processed', 0)} processed, {checkpoint.get('total_failed', 0)} failed")
    
    iteration = 0
    while True:
        iteration += 1
        
        # Check and process completed batches
        in_progress = check_and_process(client, checkpoint)
        
        # Get unprocessed papers
        unprocessed = get_unprocessed_papers(checkpoint)
        
        print(f"\n  📊 Stats: {checkpoint.get('total_processed', 0)} processed | {len(unprocessed)} remaining | {in_progress} batches running")
        
        # If we have capacity and unprocessed papers, submit more batches
        if in_progress < MAX_CONCURRENT_BATCHES and unprocessed:
            batches_to_submit = MAX_CONCURRENT_BATCHES - in_progress
            
            for i in range(batches_to_submit):
                start_idx = i * BATCH_SIZE
                end_idx = min(start_idx + BATCH_SIZE, len(unprocessed))
                
                if start_idx >= len(unprocessed):
                    break
                
                batch_papers = unprocessed[start_idx:end_idx]
                
                try:
                    submit_batch(client, batch_papers, iteration * 10 + i, checkpoint)
                except Exception as e:
                    if "token_limit_exceeded" in str(e):
                        print(f"  ⚠️ Token limit reached, waiting...")
                        break
                    else:
                        print(f"  ❌ Error submitting batch: {e}")
        
        # Check if done
        if len(unprocessed) == 0 and in_progress == 0:
            print("\n" + "="*70)
            print("🎉 ALL PAPERS PROCESSED!")
            print(f"Total: {checkpoint.get('total_processed', 0)} successful, {checkpoint.get('total_failed', 0)} failed")
            print("="*70)
            break
        
        # Wait before next check
        print(f"\n  ⏳ Waiting 60s before next check...")
        time.sleep(60)

if __name__ == "__main__":
    main()

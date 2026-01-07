#!/usr/bin/env python3
"""
Quick script to check batch status and process results.
"""

import sys
import json
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from collections import defaultdict
import re

API_KEY = "YOUR_OPENAI_API_KEY"
OUTPUT_DIR = Path("results/batch")
CHECKPOINT_FILE = OUTPUT_DIR / "checkpoint.json"

def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            return json.load(f)
    return {"processed_papers": {}, "total_processed": 0, "total_failed": 0, "batch_jobs": {}}

def save_checkpoint(checkpoint):
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(checkpoint, f, indent=2)

def generate_markdown_report(analysis, paper_id):
    """Generate a markdown report from analysis results."""
    prior_works = analysis.get("prior_works", [])
    synthesis = analysis.get("synthesis_narrative", "")
    target = analysis.get("target_paper", {})
    
    works_by_role = defaultdict(list)
    for pw in prior_works:
        role = pw.get("role", "Unknown")
        works_by_role[role].append(pw)
    
    md = f"""# Prior Work Analysis Report

## Target Paper

**Title:** {target.get('title', paper_id)}

**Conference:** {target.get('conference', 'Unknown')} {target.get('year', '')}

**Authors:** {target.get('authors', 'Unknown')}

---

## Key Prior Works ({len(prior_works)} papers)

"""
    
    role_emojis = {
        "Baseline": "📊", "Inspiration": "💡", "Gap Identification": "🔍",
        "Foundation": "🏗️", "Extension": "🔧", "Related Problem": "🔗"
    }
    
    for role in ["Foundation", "Inspiration", "Gap Identification", "Baseline", "Extension", "Related Problem"]:
        if role in works_by_role:
            emoji = role_emojis.get(role, "📄")
            md += f"### {emoji} {role}\n\n"
            for pw in works_by_role[role]:
                md += f"**{pw.get('title', 'Unknown')}** ({pw.get('year', '')})\n"
                md += f"- *Authors:* {pw.get('authors', 'Unknown')}\n"
                md += f"- *Connection:* {pw.get('relationship_sentence', '')}\n\n"
    
    md += f"""---

## Synthesis

{synthesis}

---
*Generated: {datetime.now().isoformat()}*
"""
    return md

def check_status():
    """Check status of all batches."""
    client = OpenAI(api_key=API_KEY)
    
    print("="*70)
    print("BATCH STATUS CHECK")
    print("="*70)
    
    batches = client.batches.list(limit=20)
    
    total_papers = 0
    completed_papers = 0
    in_progress = 0
    completed_batches = []
    
    for batch in batches.data:
        status = batch.status
        total = batch.request_counts.total
        done = batch.request_counts.completed
        failed = batch.request_counts.failed
        
        total_papers += total
        completed_papers += done
        
        status_emoji = {
            "completed": "✅",
            "in_progress": "🔄",
            "validating": "⏳",
            "failed": "❌",
            "finalizing": "📦"
        }.get(status, "❓")
        
        print(f"{status_emoji} {batch.id[:20]}... | {status:12} | {done:4}/{total:4} done | {failed} failed")
        
        if status == "in_progress" or status == "validating":
            in_progress += 1
        
        if status == "completed":
            completed_batches.append(batch)
    
    print("-"*70)
    print(f"Total: {completed_papers}/{total_papers} papers completed | {in_progress} batches in progress")
    print("="*70)
    
    return completed_batches

def process_completed_batches(completed_batches):
    """Download and process completed batch results."""
    if not completed_batches:
        print("No completed batches to process.")
        return
    
    client = OpenAI(api_key=API_KEY)
    checkpoint = load_checkpoint()
    
    results_dir = OUTPUT_DIR / "batch_results"
    results_dir.mkdir(parents=True, exist_ok=True)
    
    for batch in completed_batches:
        batch_id = batch.id
        
        # Skip if already processed
        if checkpoint.get("batch_jobs", {}).get(batch_id, {}).get("status") == "processed":
            print(f"Batch {batch_id[:20]}... already processed, skipping")
            continue
        
        if not batch.output_file_id:
            print(f"Batch {batch_id[:20]}... has no output file")
            continue
        
        print(f"\nProcessing batch {batch_id[:20]}...")
        
        try:
            # Download results
            content = client.files.content(batch.output_file_id)
            results_text = content.text
            
            success = 0
            fail = 0
            
            for line in results_text.strip().split('\n'):
                if not line:
                    continue
                
                result = json.loads(line)
                paper_id = result.get("custom_id")
                
                if result.get("error"):
                    checkpoint["processed_papers"][paper_id] = {"status": "failed", "error": str(result["error"])}
                    checkpoint["total_failed"] = checkpoint.get("total_failed", 0) + 1
                    fail += 1
                    continue
                
                try:
                    response_body = result.get("response", {}).get("body", {})
                    content_text = response_body.get("choices", [{}])[0].get("message", {}).get("content", "")
                    
                    # Parse JSON
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
                    
                    # Save JSON
                    with open(results_dir / f"{paper_id}.json", 'w') as f:
                        json.dump(analysis, f, indent=2)
                    
                    # Save Markdown
                    md = generate_markdown_report(analysis, paper_id)
                    with open(results_dir / f"{paper_id}.md", 'w') as f:
                        f.write(md)
                    
                    checkpoint["processed_papers"][paper_id] = {"status": "success"}
                    checkpoint["total_processed"] = checkpoint.get("total_processed", 0) + 1
                    success += 1
                    
                except Exception as e:
                    checkpoint["processed_papers"][paper_id] = {"status": "failed", "error": str(e)}
                    checkpoint["total_failed"] = checkpoint.get("total_failed", 0) + 1
                    fail += 1
            
            # Mark batch as processed
            if "batch_jobs" not in checkpoint:
                checkpoint["batch_jobs"] = {}
            checkpoint["batch_jobs"][batch_id] = {"status": "processed"}
            
            save_checkpoint(checkpoint)
            print(f"  ✅ {success} success, ❌ {fail} failed")
            
        except Exception as e:
            print(f"  Error: {e}")
    
    # Final stats
    print("\n" + "="*70)
    print("FINAL STATS")
    print("="*70)
    print(f"Total processed: {checkpoint.get('total_processed', 0)}")
    print(f"Total failed: {checkpoint.get('total_failed', 0)}")

if __name__ == "__main__":
    completed = check_status()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--process":
        process_completed_batches(completed)

#!/usr/bin/env python3
"""
Classification script - classifies all papers using discovered taxonomy.
Optimized for speed with batching and progress tracking.
"""

import os
import json
import time
from pathlib import Path
from collections import defaultdict
from typing import List, Dict
import openai

# Configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = "gpt-5-mini"
BASE_PATH = Path("/home/orchestra/projects/synthesis_graph_pipeline/results/conferences")
OUTPUT_PATH = Path("/home/orchestra/projects/thinking_patterns_llm_analysis/results")
CLASSIFICATION_BATCH_SIZE = 5

# Cost tracking
INPUT_COST_PER_M = 0.25
OUTPUT_COST_PER_M = 2.0

class CostTracker:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.calls = []
    
    def add_call(self, input_tokens: int, output_tokens: int, phase: str):
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        cost = (input_tokens / 1_000_000 * INPUT_COST_PER_M + 
                output_tokens / 1_000_000 * OUTPUT_COST_PER_M)
        self.calls.append({"phase": phase, "input_tokens": input_tokens, 
                          "output_tokens": output_tokens, "cost": cost})
        return cost
    
    def get_total_cost(self) -> float:
        return (self.total_input_tokens / 1_000_000 * INPUT_COST_PER_M + 
                self.total_output_tokens / 1_000_000 * OUTPUT_COST_PER_M)
    
    def get_summary(self) -> Dict:
        return {
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_cost_usd": round(self.get_total_cost(), 4),
            "num_calls": len(self.calls)
        }

cost_tracker = CostTracker()

def call_gpt(messages: List[Dict], phase: str) -> str:
    """Call GPT-5-mini API."""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    for attempt in range(3):
        try:
            response = client.chat.completions.create(model=MODEL, messages=messages)
            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens
            cost = cost_tracker.add_call(input_tokens, output_tokens, phase)
            return response.choices[0].message.content
        except Exception as e:
            print(f"  [Error] Attempt {attempt+1}: {e}")
            if attempt < 2:
                time.sleep(2 ** attempt)
            else:
                raise

def load_all_papers() -> List[Dict]:
    """Load all synthesis narratives."""
    papers = []
    for conf_dir in BASE_PATH.iterdir():
        if not conf_dir.is_dir():
            continue
        parts = conf_dir.name.split("-")
        if len(parts) < 3:
            continue
        conference, year, ptype = parts[0], parts[1], parts[2]
        
        for json_file in conf_dir.glob("synthesis_*.json"):
            try:
                with open(json_file) as f:
                    data = json.load(f)
                if data.get("status") != "success":
                    continue
                synthesis_graph = data.get("synthesis_graph", {})
                narrative = synthesis_graph.get("synthesis_narrative", "")
                if not narrative or len(narrative) < 100:
                    continue
                papers.append({
                    "title": data.get("title", ""),
                    "conference": conference,
                    "year": int(year),
                    "presentation_type": ptype,
                    "synthesis_narrative": narrative,
                    "file_path": str(json_file)
                })
            except Exception as e:
                pass
    return papers

def classify_batch(papers: List[Dict], taxonomy: List[Dict], batch_num: int) -> List[Dict]:
    """Classify a batch of papers."""
    taxonomy_ref = "\n".join([
        f"- {p['id']}: {p['name']} - {p['description'][:100]}..."
        for p in taxonomy
    ])
    
    papers_text = "\n\n---\n\n".join([
        f"Paper {i+1}: \"{p['title'][:60]}...\"\n{p['synthesis_narrative'][:800]}"
        for i, p in enumerate(papers)
    ])
    
    system_prompt = "You are an expert at classifying research thinking patterns. Be concise."
    user_prompt = f"""TAXONOMY:
{taxonomy_ref}

PAPERS:
{papers_text}

Classify each paper. Output JSON only:
{{"classifications": [{{"paper_index": 1, "primary_pattern": "P01", "secondary_patterns": ["P03"], "confidence": "high", "reasoning": "brief"}}]}}"""

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
    response = call_gpt(messages, f"classify_{batch_num}")
    
    try:
        if "```json" in response:
            json_str = response.split("```json")[1].split("```")[0]
        elif "```" in response:
            json_str = response.split("```")[1].split("```")[0]
        else:
            json_str = response
        result = json.loads(json_str)
        classifications = result.get("classifications", [])
        for i, paper in enumerate(papers):
            if i < len(classifications):
                paper["classification"] = classifications[i]
            else:
                paper["classification"] = {"primary_pattern": "unknown", "secondary_patterns": []}
        return papers
    except:
        for paper in papers:
            paper["classification"] = {"primary_pattern": "unknown", "secondary_patterns": []}
        return papers

def main():
    print("=" * 60)
    print("CLASSIFICATION ENGINE")
    print("=" * 60)
    
    # Load taxonomy
    with open(OUTPUT_PATH / "pattern_taxonomy.json") as f:
        taxonomy_data = json.load(f)
    taxonomy = taxonomy_data.get("taxonomy", [])
    print(f"Loaded taxonomy with {len(taxonomy)} patterns")
    
    # Load papers
    print("\nLoading papers...")
    papers = load_all_papers()
    print(f"Loaded {len(papers)} papers")
    
    # Check for existing progress
    checkpoint_file = OUTPUT_PATH / "classification_checkpoint.json"
    classified_papers = []
    start_idx = 0
    
    if checkpoint_file.exists():
        with open(checkpoint_file) as f:
            checkpoint = json.load(f)
        classified_papers = checkpoint.get("classified", [])
        start_idx = len(classified_papers)
        cost_tracker.total_input_tokens = checkpoint.get("input_tokens", 0)
        cost_tracker.total_output_tokens = checkpoint.get("output_tokens", 0)
        print(f"Resuming from checkpoint: {start_idx} papers already classified")
    
    # Classify remaining papers
    total_batches = (len(papers) - start_idx + CLASSIFICATION_BATCH_SIZE - 1) // CLASSIFICATION_BATCH_SIZE
    
    print(f"\nClassifying {len(papers) - start_idx} remaining papers in {total_batches} batches...")
    
    for i in range(start_idx, len(papers), CLASSIFICATION_BATCH_SIZE):
        batch = papers[i:i + CLASSIFICATION_BATCH_SIZE]
        batch_num = (i - start_idx) // CLASSIFICATION_BATCH_SIZE + 1
        
        classified_batch = classify_batch(batch, taxonomy, batch_num)
        classified_papers.extend(classified_batch)
        
        # Progress update every 25 batches
        if batch_num % 25 == 0 or i + CLASSIFICATION_BATCH_SIZE >= len(papers):
            pct = len(classified_papers) / len(papers) * 100
            print(f"  Progress: {len(classified_papers)}/{len(papers)} ({pct:.1f}%) | Cost: ${cost_tracker.get_total_cost():.4f}")
            
            # Save checkpoint
            with open(checkpoint_file, "w") as f:
                json.dump({
                    "classified": [{
                        "title": p["title"],
                        "conference": p["conference"],
                        "year": p["year"],
                        "presentation_type": p["presentation_type"],
                        "classification": p["classification"]
                    } for p in classified_papers],
                    "input_tokens": cost_tracker.total_input_tokens,
                    "output_tokens": cost_tracker.total_output_tokens
                }, f)
        
        time.sleep(0.15)  # Rate limiting
    
    # Save final results
    print("\nSaving final results...")
    with open(OUTPUT_PATH / "classified_papers.json", "w") as f:
        json.dump([{
            "title": p["title"],
            "conference": p["conference"],
            "year": p["year"],
            "presentation_type": p["presentation_type"],
            "classification": p["classification"]
        } for p in classified_papers], f, indent=2)
    
    # Save cost tracking
    with open(OUTPUT_PATH / "classification_cost.json", "w") as f:
        json.dump(cost_tracker.get_summary(), f, indent=2)
    
    print(f"\n✓ Classification complete!")
    print(f"  Papers classified: {len(classified_papers)}")
    print(f"  API calls: {cost_tracker.get_summary()['num_calls']}")
    print(f"  Total cost: ${cost_tracker.get_total_cost():.4f}")
    
    return classified_papers

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Research Idea Generation Evaluation Pipeline v3
Uses Exa AI for paper search and content retrieval
Evaluates GPT-5.2's ability to generate research ideas matching real papers

Author: Orchestra Agent
Date: 2026-01-04
"""

import os
import sys
import json
import time
import re
import requests
from datetime import datetime
from pathlib import Path

# Add exa_py to path
sys.path.insert(0, '/tmp/exa_lib')

from exa_py import Exa

# Configuration
EXA_API_KEY = "3cf16e91-4d99-46fe-b0cd-7db130faf61f"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Pricing for GPT-5.2
INPUT_COST_PER_1M = 2.0   # $2 per 1M input tokens
OUTPUT_COST_PER_1M = 14.0  # $14 per 1M output tokens

# Initialize Exa client
exa = Exa(api_key=EXA_API_KEY)


def clean_title_for_search(title):
    """Clean paper title for better search results"""
    # Remove (Author et al., Year) patterns
    title = re.sub(r'\s*\([^)]*et al[^)]*\)', '', title)
    title = re.sub(r'\s*\([^)]*\d{4}[^)]*\)', '', title)
    # Remove [number] citations
    title = re.sub(r'\s*\[\d+\]', '', title)
    # Take first part before / or —
    title = re.split(r'\s*/\s*|—', title)[0]
    # Clean up whitespace
    title = re.sub(r'\s+', ' ', title).strip()
    return title


def is_valid_paper_url(url):
    """Check if URL is likely a research paper source"""
    valid_domains = [
        'arxiv.org', 'openreview.net', 'papers.nips.cc', 'proceedings.mlr.press',
        'aclanthology.org', 'semanticscholar.org', 'dl.acm.org', 'ieee.org',
        'springer.com', 'nature.com', 'science.org', 'pnas.org', 'aaai.org',
        'github.com', 'huggingface.co', 'paperswithcode.com', 'biorxiv.org',
        'medrxiv.org', 'ssrn.com', 'researchgate.net', 'sciencedirect.com'
    ]
    return any(domain in url.lower() for domain in valid_domains)


def search_paper_with_exa(title, max_chars=8000):
    """Search for a paper using Exa AI and retrieve content"""
    cleaned_title = clean_title_for_search(title)
    
    try:
        # Search with research paper category
        result = exa.search_and_contents(
            cleaned_title,
            type="auto",
            num_results=3,  # Get top 3 to filter
            text={"max_characters": max_chars},
            category="research paper"
        )
        
        if result.results:
            # Prefer results from academic domains
            for paper in result.results:
                if is_valid_paper_url(paper.url):
                    return {
                        "success": True,
                        "title": paper.title,
                        "url": paper.url,
                        "content": paper.text or "",
                        "original_query": title,
                        "cleaned_query": cleaned_title
                    }
            
            # Fallback to first result if no academic domain found
            paper = result.results[0]
            return {
                "success": True,
                "title": paper.title,
                "url": paper.url,
                "content": paper.text or "",
                "original_query": title,
                "cleaned_query": cleaned_title,
                "note": "Non-academic source"
            }
        else:
            return {
                "success": False,
                "title": None,
                "url": None,
                "content": "",
                "original_query": title,
                "cleaned_query": cleaned_title,
                "error": "No results found"
            }
    except Exception as e:
        return {
            "success": False,
            "title": None,
            "url": None,
            "content": "",
            "original_query": title,
            "cleaned_query": cleaned_title,
            "error": str(e)
        }


def call_openai_api(messages, model="gpt-5.2"):
    """Call OpenAI API and track token usage"""
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": messages
    }
    
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data,
        timeout=120
    )
    
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code} - {response.text}")
    
    result = response.json()
    usage = result.get("usage", {})
    
    return {
        "content": result["choices"][0]["message"]["content"],
        "input_tokens": usage.get("prompt_tokens", 0),
        "output_tokens": usage.get("completion_tokens", 0)
    }


def generate_research_ideas(predecessor_contents, k=10):
    """Generate k research ideas based on predecessor paper contents"""
    
    # Build context from predecessors
    context_parts = []
    for i, pred in enumerate(predecessor_contents):
        if pred.get("success") and pred.get("content"):
            content = pred["content"][:6000]  # Limit each paper's content
            context_parts.append(f"=== Paper {i+1}: {pred.get('title', 'Unknown')} ===\n{content}\n")
    
    if not context_parts:
        return None, 0, 0
    
    context = "\n".join(context_parts)
    
    prompt = f"""You are a research scientist analyzing recent papers to identify promising research directions.

Based on the following papers, generate exactly {k} novel research ideas that could naturally follow from this body of work. Each idea should:
1. Build upon concepts, methods, or findings from these papers
2. Be specific and actionable (not vague)
3. Represent a meaningful contribution to the field

Papers:
{context}

Generate exactly {k} research ideas. For each idea, provide:
- A concise title (1 line)
- A brief description of the key contribution (2-3 sentences)

Format your response as a numbered list (1-{k})."""

    messages = [{"role": "user", "content": prompt}]
    
    result = call_openai_api(messages)
    return result["content"], result["input_tokens"], result["output_tokens"]


def judge_similarity(generated_idea, ground_truth_title, ground_truth_contribution):
    """Use LLM to judge if generated idea matches ground truth"""
    
    prompt = f"""You are evaluating whether a generated research idea matches a real published paper.

Generated Idea:
{generated_idea}

Real Published Paper:
Title: {ground_truth_title}
Contribution: {ground_truth_contribution}

Does the generated idea capture the same core concept, approach, or contribution as the real paper?
Consider semantic similarity, not exact wording. The idea should address the same problem with a similar approach.

Respond with ONLY one of:
- "MATCH" if the generated idea substantially aligns with the real paper's core contribution
- "NO_MATCH" if they are about different topics or approaches"""

    messages = [{"role": "user", "content": prompt}]
    
    result = call_openai_api(messages)
    response = result["content"].strip().upper()
    
    is_match = "MATCH" in response and "NO_MATCH" not in response
    
    return is_match, result["input_tokens"], result["output_tokens"]


def parse_ideas_from_response(response_text):
    """Parse individual ideas from the generated response"""
    ideas = []
    
    # Split by numbered items (1., 2., etc.)
    pattern = r'\d+\.\s*\*?\*?([^*\n]+)\*?\*?\s*\n([^0-9]+?)(?=\d+\.|$)'
    matches = re.findall(pattern, response_text, re.DOTALL)
    
    if matches:
        for title, description in matches:
            ideas.append(f"{title.strip()}\n{description.strip()}")
    else:
        # Fallback: split by double newlines or numbered patterns
        parts = re.split(r'\n\s*\d+[\.\)]\s*', response_text)
        ideas = [p.strip() for p in parts if p.strip() and len(p.strip()) > 20]
    
    return ideas[:10]  # Return at most 10


def load_synthesis_data(data_dir):
    """Load all synthesis JSON files from the data directory"""
    papers = []
    
    synthesis_files = sorted(Path(data_dir).glob("synthesis_*.json"))
    
    for filepath in synthesis_files:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Extract paper info from the new structure
            paper_title = data.get("title", "")
            sg = data.get("synthesis_graph", {})
            contribution = sg.get("target_paper_contribution", "")
            
            # Extract predecessor titles
            predecessors = []
            for pred in sg.get("intellectual_predecessors", []):
                if isinstance(pred, dict):
                    pred_title = pred.get("paper_title", "")
                    if pred_title:
                        predecessors.append(pred_title)
                elif isinstance(pred, str):
                    predecessors.append(pred)
            
            if paper_title and predecessors:
                papers.append({
                    "paper_title": paper_title,
                    "contribution": contribution,
                    "predecessors": predecessors,
                    "source_file": filepath.name
                })
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
    
    return papers


def evaluate_single_paper(paper_data, paper_idx, k=10):
    """Evaluate idea generation for a single paper"""
    print(f"\n{'='*70}")
    print(f"[{paper_idx}] Evaluating: {paper_data['paper_title'][:60]}...")
    print(f"    Predecessors: {len(paper_data['predecessors'])}")
    
    # Step 1: Crawl predecessor papers using Exa
    predecessor_contents = []
    crawl_successes = 0
    academic_sources = 0
    
    for i, pred_title in enumerate(paper_data['predecessors']):
        print(f"    Crawling [{i+1}/{len(paper_data['predecessors'])}]: {pred_title[:50]}...")
        
        result = search_paper_with_exa(pred_title)
        predecessor_contents.append(result)
        
        if result["success"]:
            crawl_successes += 1
            content_len = len(result.get("content", ""))
            is_academic = is_valid_paper_url(result.get("url", ""))
            if is_academic:
                academic_sources += 1
            print(f"        ✓ Found: {result.get('url', 'N/A')[:60]} ({content_len} chars)")
        else:
            print(f"        ✗ Not found: {result.get('error', 'Unknown error')}")
        
        # Small delay to avoid rate limiting
        time.sleep(0.3)
    
    crawl_rate = crawl_successes / len(paper_data['predecessors']) if paper_data['predecessors'] else 0
    print(f"    Crawl success: {crawl_successes}/{len(paper_data['predecessors'])} ({crawl_rate*100:.1f}%)")
    print(f"    Academic sources: {academic_sources}/{crawl_successes}")
    
    # Step 2: Generate research ideas
    print(f"    Generating {k} research ideas...")
    
    total_input_tokens = 0
    total_output_tokens = 0
    
    ideas_text, in_tokens, out_tokens = generate_research_ideas(predecessor_contents, k)
    total_input_tokens += in_tokens
    total_output_tokens += out_tokens
    
    if not ideas_text:
        print(f"    ✗ Failed to generate ideas (no content crawled)")
        return {
            "paper_idx": paper_idx,
            "paper_title": paper_data["paper_title"],
            "contribution": paper_data["contribution"],
            "num_predecessors": len(paper_data["predecessors"]),
            "predecessors_crawled": crawl_successes,
            "academic_sources": academic_sources,
            "crawl_rate": crawl_rate,
            "ideas_generated": 0,
            "hit_at_k": False,
            "matching_idea_idx": None,
            "input_tokens": total_input_tokens,
            "output_tokens": total_output_tokens,
            "predecessor_details": predecessor_contents,
            "generated_ideas": [],
            "judgments": []
        }
    
    # Parse individual ideas
    ideas = parse_ideas_from_response(ideas_text)
    print(f"    Parsed {len(ideas)} ideas")
    
    # Step 3: Judge each idea against ground truth
    print(f"    Judging similarity to ground truth...")
    
    hit = False
    matching_idx = None
    judgments = []
    
    for i, idea in enumerate(ideas):
        is_match, in_tokens, out_tokens = judge_similarity(
            idea, 
            paper_data["paper_title"],
            paper_data["contribution"]
        )
        total_input_tokens += in_tokens
        total_output_tokens += out_tokens
        
        judgments.append({
            "idea_idx": i,
            "idea_text": idea[:200],
            "is_match": is_match
        })
        
        if is_match and not hit:
            hit = True
            matching_idx = i
            print(f"        ✓ HIT at idea {i+1}!")
        
        time.sleep(0.2)  # Rate limiting
    
    if not hit:
        print(f"        ✗ No match found")
    
    return {
        "paper_idx": paper_idx,
        "paper_title": paper_data["paper_title"],
        "contribution": paper_data["contribution"],
        "num_predecessors": len(paper_data["predecessors"]),
        "predecessors_crawled": crawl_successes,
        "academic_sources": academic_sources,
        "crawl_rate": crawl_rate,
        "ideas_generated": len(ideas),
        "hit_at_k": hit,
        "matching_idea_idx": matching_idx,
        "input_tokens": total_input_tokens,
        "output_tokens": total_output_tokens,
        "predecessor_details": predecessor_contents,
        "generated_ideas": ideas,
        "generated_ideas_raw": ideas_text,
        "judgments": judgments
    }


def main():
    """Main evaluation pipeline"""
    print("="*70)
    print("Research Idea Generation Evaluation v3 (Exa AI)")
    print("="*70)
    print(f"Model: gpt-5.2")
    print(f"k: 10")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # Load data
    data_dir = "projects/synthesis_graph_pipeline/results/conferences/NeurIPS-2025-oral"
    papers = load_synthesis_data(data_dir)
    print(f"\nLoaded {len(papers)} papers from {data_dir}")
    
    # Run evaluation
    results = []
    total_input_tokens = 0
    total_output_tokens = 0
    
    start_time = time.time()
    
    for idx, paper in enumerate(papers):
        result = evaluate_single_paper(paper, idx, k=10)
        results.append(result)
        
        total_input_tokens += result["input_tokens"]
        total_output_tokens += result["output_tokens"]
        
        # Progress update
        hits_so_far = sum(1 for r in results if r["hit_at_k"])
        print(f"\n    Progress: {idx+1}/{len(papers)} | Hits: {hits_so_far}/{idx+1} ({hits_so_far/(idx+1)*100:.1f}%)")
        
        input_cost = (total_input_tokens / 1_000_000) * INPUT_COST_PER_1M
        output_cost = (total_output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
        print(f"    Tokens: {total_input_tokens:,} in / {total_output_tokens:,} out | Cost: ${input_cost + output_cost:.2f}")
        
        # Save intermediate results every 10 papers
        if (idx + 1) % 10 == 0:
            save_results(results, total_input_tokens, total_output_tokens, start_time, interim=True)
    
    # Final save
    save_results(results, total_input_tokens, total_output_tokens, start_time, interim=False)
    
    # Print summary
    elapsed = time.time() - start_time
    hits = sum(1 for r in results if r["hit_at_k"])
    avg_crawl = sum(r["crawl_rate"] for r in results) / len(results)
    avg_academic = sum(r.get("academic_sources", 0) for r in results) / len(results)
    
    input_cost = (total_input_tokens / 1_000_000) * INPUT_COST_PER_1M
    output_cost = (total_output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    total_cost = input_cost + output_cost
    
    print("\n" + "="*70)
    print("FINAL RESULTS")
    print("="*70)
    print(f"Papers evaluated: {len(results)}")
    print(f"Hit@10: {hits}/{len(results)} = {hits/len(results)*100:.2f}%")
    print(f"Average crawl rate: {avg_crawl*100:.1f}%")
    print(f"Average academic sources per paper: {avg_academic:.1f}")
    print(f"Runtime: {elapsed/60:.1f} minutes")
    print(f"\nAPI Cost:")
    print(f"  Input:  {total_input_tokens:,} tokens = ${input_cost:.2f}")
    print(f"  Output: {total_output_tokens:,} tokens = ${output_cost:.2f}")
    print(f"  Total:  ${total_cost:.2f}")
    print("="*70)


def save_results(results, total_input_tokens, total_output_tokens, start_time, interim=False):
    """Save results to JSON file"""
    elapsed = time.time() - start_time
    hits = sum(1 for r in results if r["hit_at_k"])
    avg_crawl = sum(r["crawl_rate"] for r in results) / len(results) if results else 0
    avg_academic = sum(r.get("academic_sources", 0) for r in results) / len(results) if results else 0
    
    input_cost = (total_input_tokens / 1_000_000) * INPUT_COST_PER_1M
    output_cost = (total_output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    
    output_data = {
        "summary": {
            "model": "gpt-5.2",
            "k": 10,
            "crawl_method": "exa_ai",
            "total_papers": len(results),
            "hits": hits,
            "hit_rate_percent": round(hits / len(results) * 100, 2) if results else 0,
            "average_crawl_rate": round(avg_crawl * 100, 2),
            "average_academic_sources": round(avg_academic, 2),
            "runtime_minutes": round(elapsed / 60, 2),
            "cost": {
                "input_tokens": total_input_tokens,
                "output_tokens": total_output_tokens,
                "input_cost_usd": round(input_cost, 2),
                "output_cost_usd": round(output_cost, 2),
                "total_cost_usd": round(input_cost + output_cost, 2)
            },
            "timestamp": datetime.now().isoformat()
        },
        "results": results
    }
    
    suffix = "_interim" if interim else "_final"
    output_path = f"projects/research_idea_evaluation/results/evaluation_results_gpt52_v3_exa{suffix}.json"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\n    Results saved to: {output_path}")


if __name__ == "__main__":
    main()

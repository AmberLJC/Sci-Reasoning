#!/usr/bin/env python3
"""
Research Idea Generation Evaluation - Claude Opus 4
Uses Exa AI for paper retrieval, Claude Opus 4 for idea generation and judging
"""

import os
import sys
import json
import time
import re
import requests
from datetime import datetime
from pathlib import Path

sys.path.insert(0, '/tmp/exa_lib')
from exa_py import Exa

# Configuration
EXA_API_KEY = "3cf16e91-4d99-46fe-b0cd-7db130faf61f"
ANTHROPIC_API_KEY = "YOUR_OPENAI_API_KEY"

# Pricing for Claude Opus 4
INPUT_COST_PER_1M = 15.0   # $15 per 1M input tokens
OUTPUT_COST_PER_1M = 75.0  # $75 per 1M output tokens

exa = Exa(api_key=EXA_API_KEY)


def clean_title_for_search(title):
    title = re.sub(r'\s*\([^)]*et al[^)]*\)', '', title)
    title = re.sub(r'\s*\([^)]*\d{4}[^)]*\)', '', title)
    title = re.sub(r'\s*\[\d+\]', '', title)
    title = re.split(r'\s*/\s*|—', title)[0]
    title = re.sub(r'\s+', ' ', title).strip()
    return title


def is_quality_content(content):
    if not content or len(content) < 200:
        return False
    boilerplate_indicators = [
        "Skip to main content", "Cornell University", "We gratefully acknowledge",
        "arXiv is a free distribution service", "arXiv.org e-Print archive",
    ]
    content_lower = content[:500].lower()
    boilerplate_count = sum(1 for b in boilerplate_indicators if b.lower() in content_lower)
    return boilerplate_count <= 1


def search_paper_with_exa(title, max_chars=10000):
    cleaned_title = clean_title_for_search(title)
    try:
        result = exa.search_and_contents(cleaned_title, type="auto", num_results=3,
                                         text={"max_characters": max_chars}, category="research paper")
        if result.results:
            for paper in result.results:
                content = paper.text or ""
                if is_quality_content(content):
                    return {"success": True, "title": paper.title, "url": paper.url, "content": content,
                            "content_quality": "good"}
            return {"success": True, "title": result.results[0].title, "url": result.results[0].url,
                    "content": result.results[0].text or "", "content_quality": "fallback"}
        return {"success": False, "content": "", "error": "No results found"}
    except Exception as e:
        return {"success": False, "content": "", "error": str(e)}


def call_claude_api(messages, max_retries=3):
    """Call Anthropic Claude Opus 4 API"""
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01"
    }
    
    claude_messages = []
    for msg in messages:
        if msg["role"] != "system":
            claude_messages.append({"role": msg["role"], "content": msg["content"]})
    
    data = {
        "model": "claude-opus-4-20250514",
        "max_tokens": 4096,
        "messages": claude_messages
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=data,
                timeout=180
            )
            if response.status_code == 200:
                result = response.json()
                content = result["content"][0]["text"] if result.get("content") else ""
                usage = result.get("usage", {})
                return {
                    "content": content,
                    "input_tokens": usage.get("input_tokens", 0),
                    "output_tokens": usage.get("output_tokens", 0)
                }
            elif response.status_code in [500, 502, 503, 504, 529]:
                print(f"        Server error {response.status_code}, retrying ({attempt+1}/{max_retries})...")
                time.sleep(5 * (attempt + 1))
            elif response.status_code == 429:
                print(f"        Rate limit, waiting 30s ({attempt+1}/{max_retries})...")
                time.sleep(30)
            else:
                raise Exception(f"API error: {response.status_code} - {response.text[:200]}")
        except requests.exceptions.Timeout:
            print(f"        Timeout, retrying ({attempt+1}/{max_retries})...")
            time.sleep(10)
    
    raise Exception(f"Failed after {max_retries} retries")


def generate_research_ideas(predecessor_contents, k=10):
    context_parts = []
    for i, pred in enumerate(predecessor_contents):
        if pred.get("success") and pred.get("content") and len(pred["content"]) >= 300:
            context_parts.append(f"=== Paper {i+1}: {pred.get('title', 'Unknown')} ===\n{pred['content'][:6000]}\n")
    if not context_parts:
        return None, 0, 0
    
    prompt = f"""You are a research scientist analyzing recent papers to identify promising research directions.

Based on the following papers, generate exactly {k} novel research ideas that could naturally follow from this body of work. Each idea should:
1. Build upon concepts, methods, or findings from these papers
2. Be specific and actionable (not vague)
3. Represent a meaningful contribution to the field

Papers:
{chr(10).join(context_parts)}

Generate exactly {k} research ideas. For each idea, provide:
- A concise title (1 line)
- A brief description of the key contribution (2-3 sentences)

Format your response as a numbered list (1-{k})."""
    
    result = call_claude_api([{"role": "user", "content": prompt}])
    return result["content"], result["input_tokens"], result["output_tokens"]


def judge_similarity(generated_idea, ground_truth_title, ground_truth_contribution):
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
    
    result = call_claude_api([{"role": "user", "content": prompt}])
    response = result["content"].strip().upper()
    is_match = "MATCH" in response and "NO_MATCH" not in response
    return is_match, result["input_tokens"], result["output_tokens"]


def parse_ideas_from_response(response_text):
    ideas = []
    pattern = r'\d+\.\s*\*?\*?([^*\n]+)\*?\*?\s*\n([^0-9]+?)(?=\d+\.|$)'
    matches = re.findall(pattern, response_text, re.DOTALL)
    if matches:
        for title, description in matches:
            ideas.append(f"{title.strip()}\n{description.strip()}")
    else:
        parts = re.split(r'\n\s*\d+[\.\)]\s*', response_text)
        ideas = [p.strip() for p in parts if p.strip() and len(p.strip()) > 20]
    return ideas[:10]


def load_synthesis_data(data_dir):
    papers = []
    for filepath in sorted(Path(data_dir).glob("synthesis_*.json")):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            paper_title = data.get("title", "")
            sg = data.get("synthesis_graph", {})
            contribution = sg.get("target_paper_contribution", "")
            predecessors = [pred.get("paper_title", "") if isinstance(pred, dict) else pred
                          for pred in sg.get("intellectual_predecessors", []) if pred]
            predecessors = [p for p in predecessors if p]
            if paper_title and predecessors:
                papers.append({"paper_title": paper_title, "contribution": contribution,
                              "predecessors": predecessors, "source_file": filepath.name})
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
    return papers


def evaluate_single_paper(paper_data, paper_idx, k=10):
    print(f"\n{'='*70}")
    print(f"[{paper_idx}] Evaluating: {paper_data['paper_title'][:60]}...")
    print(f"    Predecessors: {len(paper_data['predecessors'])}")
    
    predecessor_contents = []
    crawl_successes = 0
    
    for i, pred_title in enumerate(paper_data['predecessors']):
        print(f"    Crawling [{i+1}/{len(paper_data['predecessors'])}]: {pred_title[:50]}...")
        result = search_paper_with_exa(pred_title)
        predecessor_contents.append(result)
        if result["success"]:
            crawl_successes += 1
            print(f"        ✓ Found ({len(result.get('content', ''))} chars)")
        else:
            print(f"        ✗ Not found: {result.get('error', 'Unknown error')}")
        time.sleep(0.3)
    
    crawl_rate = crawl_successes / len(paper_data['predecessors']) if paper_data['predecessors'] else 0
    print(f"    Crawl: {crawl_successes}/{len(paper_data['predecessors'])} ({crawl_rate*100:.0f}%)")
    
    print(f"    Generating 10 research ideas...")
    total_input_tokens = 0
    total_output_tokens = 0
    
    ideas_text, in_tokens, out_tokens = generate_research_ideas(predecessor_contents, k)
    total_input_tokens += in_tokens
    total_output_tokens += out_tokens
    
    if not ideas_text:
        return {"paper_idx": paper_idx, "paper_title": paper_data["paper_title"],
                "contribution": paper_data["contribution"], "num_predecessors": len(paper_data["predecessors"]),
                "predecessors_crawled": crawl_successes, "crawl_rate": crawl_rate, "ideas_generated": 0,
                "hit_at_k": False, "matching_idea_idx": None, "input_tokens": total_input_tokens,
                "output_tokens": total_output_tokens, "judgments": []}
    
    ideas = parse_ideas_from_response(ideas_text)
    print(f"    Parsed {len(ideas)} ideas, judging...")
    
    hit = False
    matching_idx = None
    judgments = []
    
    for i, idea in enumerate(ideas):
        is_match, in_tokens, out_tokens = judge_similarity(idea, paper_data["paper_title"], paper_data["contribution"])
        total_input_tokens += in_tokens
        total_output_tokens += out_tokens
        judgments.append({"idea_idx": i, "idea_text": idea[:200], "is_match": is_match})
        if is_match and not hit:
            hit = True
            matching_idx = i
            print(f"        ✓ HIT at idea {i+1}!")
        time.sleep(0.3)
    
    if not hit:
        print(f"        ✗ No match")
    
    return {"paper_idx": paper_idx, "paper_title": paper_data["paper_title"],
            "contribution": paper_data["contribution"], "num_predecessors": len(paper_data["predecessors"]),
            "predecessors_crawled": crawl_successes, "crawl_rate": crawl_rate, "ideas_generated": len(ideas),
            "hit_at_k": hit, "matching_idea_idx": matching_idx, "input_tokens": total_input_tokens,
            "output_tokens": total_output_tokens, "judgments": judgments}


def save_results(results, total_input_tokens, total_output_tokens, start_time, interim=False):
    hits = sum(1 for r in results if r["hit_at_k"])
    avg_crawl = sum(r["crawl_rate"] for r in results) / len(results) if results else 0
    input_cost = (total_input_tokens / 1_000_000) * INPUT_COST_PER_1M
    output_cost = (total_output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    
    output_data = {
        "summary": {"model": "claude-opus-4", "k": 10, "crawl_method": "exa_ai",
                   "total_papers": len(results), "hits": hits,
                   "hit_rate_percent": round(hits / len(results) * 100, 2) if results else 0,
                   "average_crawl_rate": round(avg_crawl * 100, 2),
                   "runtime_minutes": round((time.time() - start_time) / 60, 2),
                   "cost": {"input_tokens": total_input_tokens, "output_tokens": total_output_tokens,
                           "input_cost_usd": round(input_cost, 2), "output_cost_usd": round(output_cost, 2),
                           "total_cost_usd": round(input_cost + output_cost, 2)},
                   "timestamp": datetime.now().isoformat()},
        "results": results
    }
    
    suffix = "_interim" if interim else "_final"
    output_path = f"projects/research_idea_evaluation/results/evaluation_results_claude_opus{suffix}.json"
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    print(f"\n    Saved: {output_path}")


def main():
    print("="*70)
    print("Research Idea Generation - Claude Opus 4")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    papers = load_synthesis_data("projects/synthesis_graph_pipeline/results/conferences/NeurIPS-2025-oral")
    print(f"Total papers: {len(papers)}")
    
    results = []
    total_input_tokens = 0
    total_output_tokens = 0
    start_time = time.time()
    
    for idx, paper in enumerate(papers):
        result = evaluate_single_paper(paper, idx, k=10)
        results.append(result)
        total_input_tokens += result["input_tokens"]
        total_output_tokens += result["output_tokens"]
        
        hits = sum(1 for r in results if r["hit_at_k"])
        input_cost = (total_input_tokens / 1_000_000) * INPUT_COST_PER_1M
        output_cost = (total_output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
        print(f"\n    Progress: {idx+1}/{len(papers)} | Hits: {hits}/{len(results)} ({hits/len(results)*100:.1f}%) | Cost: ${input_cost + output_cost:.2f}")
        
        if (idx + 1) % 10 == 0:
            save_results(results, total_input_tokens, total_output_tokens, start_time, interim=True)
    
    save_results(results, total_input_tokens, total_output_tokens, start_time, interim=False)
    
    hits = sum(1 for r in results if r["hit_at_k"])
    input_cost = (total_input_tokens / 1_000_000) * INPUT_COST_PER_1M
    output_cost = (total_output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    
    print("\n" + "="*70)
    print("FINAL RESULTS - Claude Opus 4")
    print("="*70)
    print(f"Papers: {len(results)} | Hit@10: {hits}/{len(results)} = {hits/len(results)*100:.2f}%")
    print(f"Cost: ${input_cost + output_cost:.2f} ({total_input_tokens:,} in / {total_output_tokens:,} out)")
    print("="*70)


if __name__ == "__main__":
    main()

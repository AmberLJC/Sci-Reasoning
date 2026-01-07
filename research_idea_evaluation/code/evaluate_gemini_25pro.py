#!/usr/bin/env python3
"""
Research Idea Generation Evaluation - Gemini 2.5 Pro
Fresh start with gemini-2.5-pro model
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

EXA_API_KEY = "3cf16e91-4d99-46fe-b0cd-7db130faf61f"
GEMINI_API_KEY = "AIzaSyCYhkghQSuTq-AsWQhAdZf4bHQoMFV3DhM"

# Gemini 2.5 Pro pricing
INPUT_COST_PER_1M = 1.25
OUTPUT_COST_PER_1M = 10.0

exa = Exa(api_key=EXA_API_KEY)


def clean_title_for_search(title):
    title = re.sub(r'\s*\([^)]*et al[^)]*\)', '', title)
    title = re.sub(r'\s*\([^)]*\d{4}[^)]*\)', '', title)
    title = re.sub(r'\s*\[\d+\]', '', title)
    title = re.split(r'\s*/\s*|—', title)[0]
    return re.sub(r'\s+', ' ', title).strip()


def is_quality_content(content):
    if not content or len(content) < 200:
        return False
    boilerplate = ["Skip to main content", "Cornell University", "We gratefully acknowledge"]
    return sum(1 for b in boilerplate if b.lower() in content[:500].lower()) <= 1


def search_paper_with_exa(title, max_chars=10000):
    cleaned_title = clean_title_for_search(title)
    try:
        result = exa.search_and_contents(cleaned_title, type="auto", num_results=3,
                                         text={"max_characters": max_chars}, category="research paper")
        if result.results:
            for paper in result.results:
                if is_quality_content(paper.text or ""):
                    return {"success": True, "title": paper.title, "url": paper.url, 
                            "content": paper.text or "", "content_quality": "good"}
            return {"success": True, "title": result.results[0].title, "url": result.results[0].url,
                    "content": result.results[0].text or "", "content_quality": "fallback"}
        return {"success": False, "content": "", "error": "No results"}
    except Exception as e:
        return {"success": False, "content": "", "error": str(e)}


def call_gemini_api(prompt, max_retries=5):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key={GEMINI_API_KEY}"
    data = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"maxOutputTokens": 8192}}
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers={"Content-Type": "application/json"}, json=data, timeout=180)
            if response.status_code == 200:
                result = response.json()
                content = ""
                if result.get("candidates") and result["candidates"][0].get("content", {}).get("parts"):
                    content = result["candidates"][0]["content"]["parts"][0].get("text", "")
                usage = result.get("usageMetadata", {})
                return {"content": content, 
                        "input_tokens": usage.get("promptTokenCount", 0),
                        "output_tokens": usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)}
            elif response.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"        Rate limit, waiting {wait}s ({attempt+1}/{max_retries})...")
                time.sleep(wait)
            elif response.status_code == 500:
                print(f"        Server error, waiting 10s ({attempt+1}/{max_retries})...")
                time.sleep(10)
            else:
                print(f"        API error {response.status_code}: {response.text[:100]}")
                time.sleep(5)
        except requests.exceptions.Timeout:
            print(f"        Timeout, retrying ({attempt+1}/{max_retries})...")
            time.sleep(10)
        except Exception as e:
            print(f"        Error: {e}, retrying ({attempt+1}/{max_retries})...")
            time.sleep(5)
    
    raise Exception(f"Failed after {max_retries} retries")


def generate_research_ideas(predecessor_contents, k=10):
    context_parts = [f"=== Paper {i+1}: {p.get('title', 'Unknown')} ===\n{p['content'][:6000]}\n"
                     for i, p in enumerate(predecessor_contents) if p.get("success") and len(p.get("content", "")) >= 300]
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
    
    result = call_gemini_api(prompt)
    return result["content"], result["input_tokens"], result["output_tokens"]


def judge_similarity(idea, title, contribution):
    prompt = f"""You are evaluating whether a generated research idea matches a real published paper.

Generated Idea:
{idea}

Real Published Paper:
Title: {title}
Contribution: {contribution}

Does the generated idea capture the same core concept, approach, or contribution as the real paper?
Consider semantic similarity, not exact wording. The idea should address the same problem with a similar approach.

Respond with ONLY one of:
- "MATCH" if the generated idea substantially aligns with the real paper's core contribution
- "NO_MATCH" if they are about different topics or approaches"""
    
    result = call_gemini_api(prompt)
    response = result["content"].strip().upper()
    return "MATCH" in response and "NO_MATCH" not in response, result["input_tokens"], result["output_tokens"]


def parse_ideas(text):
    if not text:
        return []
    pattern = r'\d+\.\s*\*?\*?([^*\n]+)\*?\*?\s*\n([^0-9]+?)(?=\d+\.|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return [f"{t.strip()}\n{d.strip()}" for t, d in matches][:10]
    parts = re.split(r'\n\s*\d+[\.\)]\s*', text)
    return [p.strip() for p in parts if p.strip() and len(p.strip()) > 20][:10]


def load_synthesis_data(data_dir):
    papers = []
    for fp in sorted(Path(data_dir).glob("synthesis_*.json")):
        try:
            with open(fp) as f:
                data = json.load(f)
            sg = data.get("synthesis_graph", {})
            preds = [p.get("paper_title", "") if isinstance(p, dict) else p for p in sg.get("intellectual_predecessors", [])]
            preds = [p for p in preds if p]
            if data.get("title") and preds:
                papers.append({"paper_title": data["title"], "contribution": sg.get("target_paper_contribution", ""),
                              "predecessors": preds})
        except:
            pass
    return papers


def evaluate_paper(paper, idx, k=10):
    print(f"\n{'='*70}")
    print(f"[{idx}] {paper['paper_title'][:60]}...")
    print(f"    Predecessors: {len(paper['predecessors'])}")
    
    preds = []
    for i, t in enumerate(paper['predecessors']):
        print(f"    Crawling [{i+1}/{len(paper['predecessors'])}]: {t[:50]}...")
        r = search_paper_with_exa(t)
        preds.append(r)
        if r['success']:
            print(f"        ✓ Found ({len(r.get('content', ''))} chars)")
        else:
            print(f"        ✗ Not found")
        time.sleep(0.3)
    
    crawl_rate = sum(1 for p in preds if p['success']) / len(paper['predecessors'])
    print(f"    Crawl: {crawl_rate*100:.0f}%")
    
    total_in, total_out = 0, 0
    
    print(f"    Generating ideas...")
    time.sleep(2)  # Small delay before API call
    ideas_text, in_t, out_t = generate_research_ideas(preds, k)
    total_in += in_t
    total_out += out_t
    
    if not ideas_text:
        print(f"    ✗ Failed to generate ideas")
        return {"paper_idx": idx, "paper_title": paper["paper_title"], "hit_at_k": False,
                "crawl_rate": crawl_rate, "input_tokens": total_in, "output_tokens": total_out,
                "ideas_generated": 0, "contribution": paper["contribution"]}
    
    ideas = parse_ideas(ideas_text)
    print(f"    Parsed {len(ideas)} ideas, judging...")
    
    hit, match_idx = False, None
    judgments = []
    
    for i, idea in enumerate(ideas):
        time.sleep(1)  # Delay between judge calls
        is_match, in_t, out_t = judge_similarity(idea, paper["paper_title"], paper["contribution"])
        total_in += in_t
        total_out += out_t
        judgments.append({"idea_idx": i, "is_match": is_match})
        if is_match and not hit:
            hit, match_idx = True, i
            print(f"        ✓ HIT at idea {i+1}!")
    
    if not hit:
        print(f"        ✗ No match")
    
    return {"paper_idx": idx, "paper_title": paper["paper_title"], "hit_at_k": hit,
            "matching_idea_idx": match_idx, "crawl_rate": crawl_rate,
            "input_tokens": total_in, "output_tokens": total_out,
            "ideas_generated": len(ideas), "contribution": paper["contribution"],
            "judgments": judgments}


def save_results(results, total_in, total_out, start_time, interim=False):
    hits = sum(1 for r in results if r["hit_at_k"])
    avg_crawl = sum(r["crawl_rate"] for r in results) / len(results) if results else 0
    input_cost = (total_in / 1_000_000) * INPUT_COST_PER_1M
    output_cost = (total_out / 1_000_000) * OUTPUT_COST_PER_1M
    
    data = {
        "summary": {
            "model": "gemini-2.5-pro",
            "k": 10,
            "crawl_method": "exa_ai",
            "total_papers": len(results),
            "hits": hits,
            "hit_rate_percent": round(hits / len(results) * 100, 2) if results else 0,
            "average_crawl_rate": round(avg_crawl * 100, 2),
            "runtime_minutes": round((time.time() - start_time) / 60, 2),
            "cost": {
                "input_tokens": total_in,
                "output_tokens": total_out,
                "input_cost_usd": round(input_cost, 2),
                "output_cost_usd": round(output_cost, 2),
                "total_cost_usd": round(input_cost + output_cost, 2)
            },
            "timestamp": datetime.now().isoformat()
        },
        "results": results
    }
    
    suffix = "_interim" if interim else "_final"
    path = f"projects/research_idea_evaluation/results/evaluation_results_gemini_25pro{suffix}.json"
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\n    Saved: {path}")


def main():
    print("="*70)
    print("Research Idea Generation - Gemini 2.5 Pro")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    papers = load_synthesis_data("projects/synthesis_graph_pipeline/results/conferences/NeurIPS-2025-oral")
    print(f"Total papers: {len(papers)}")
    
    results = []
    total_in = 0
    total_out = 0
    start_time = time.time()
    
    for idx, paper in enumerate(papers):
        result = evaluate_paper(paper, idx, k=10)
        results.append(result)
        total_in += result["input_tokens"]
        total_out += result["output_tokens"]
        
        hits = sum(1 for r in results if r["hit_at_k"])
        input_cost = (total_in / 1_000_000) * INPUT_COST_PER_1M
        output_cost = (total_out / 1_000_000) * OUTPUT_COST_PER_1M
        print(f"\n    Progress: {idx+1}/{len(papers)} | Hits: {hits}/{len(results)} ({hits/len(results)*100:.1f}%) | Cost: ${input_cost + output_cost:.2f}")
        
        if (idx + 1) % 10 == 0:
            save_results(results, total_in, total_out, start_time, interim=True)
        
        # Delay between papers to avoid rate limits
        time.sleep(3)
    
    save_results(results, total_in, total_out, start_time, interim=False)
    
    hits = sum(1 for r in results if r["hit_at_k"])
    input_cost = (total_in / 1_000_000) * INPUT_COST_PER_1M
    output_cost = (total_out / 1_000_000) * OUTPUT_COST_PER_1M
    
    print("\n" + "="*70)
    print("FINAL RESULTS - Gemini 2.5 Pro")
    print("="*70)
    print(f"Papers: {len(results)} | Hit@10: {hits}/{len(results)} = {hits/len(results)*100:.2f}%")
    print(f"Cost: ${input_cost + output_cost:.2f} ({total_in:,} in / {total_out:,} out)")
    print("="*70)


if __name__ == "__main__":
    main()

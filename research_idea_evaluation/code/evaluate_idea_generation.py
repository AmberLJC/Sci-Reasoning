#!/usr/bin/env python3
"""
Research Idea Generation Evaluation Pipeline

Evaluates whether GPT-5.2 can generate research ideas that align with real 
published papers, given only prior work (intellectual_predecessors) as context.

Metric: Hit@k — success if any of k=10 generated ideas matches ground truth paper g
"""

import os
import sys
import json
import time
import glob
import re
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
import requests

# OpenAI API configuration
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
MODEL = "gpt-5.2"

# Exa API for paper search and crawling (from environment or hardcoded for this task)
EXA_API_KEY = os.environ.get("EXA_API_KEY", "")

# API Pricing (per 1M tokens)
INPUT_COST_PER_1M = 2.0
OUTPUT_COST_PER_1M = 14.0

# Configuration
K_IDEAS = 10  # Number of ideas to generate
MAX_PAPERS = None  # Set to None for all papers, or a number for testing
MAX_CHARS_PER_PAPER = 15000  # ~3 pages worth of content

@dataclass
class CostTracker:
    """Track API costs"""
    input_tokens: int = 0
    output_tokens: int = 0
    
    @property
    def input_cost(self) -> float:
        return (self.input_tokens / 1_000_000) * INPUT_COST_PER_1M
    
    @property
    def output_cost(self) -> float:
        return (self.output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    
    @property
    def total_cost(self) -> float:
        return self.input_cost + self.output_cost
    
    def add(self, input_tokens: int, output_tokens: int):
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
    
    def to_dict(self) -> Dict:
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "input_cost_usd": round(self.input_cost, 4),
            "output_cost_usd": round(self.output_cost, 4),
            "total_cost_usd": round(self.total_cost, 4)
        }


@dataclass
class EvaluationResult:
    """Result for a single paper evaluation"""
    paper_idx: int
    paper_title: str
    paper_contribution: str
    num_predecessors: int
    predecessors_crawled: int
    predecessor_content_length: int
    generated_ideas: List[Dict]
    similarity_scores: List[Dict]  # Each dict has: idea_idx, is_match, reasoning
    hit_at_k: bool  # True if any idea matches
    best_match_idx: Optional[int]
    best_match_reasoning: Optional[str]
    error: Optional[str] = None


def call_openai_api(messages: List[Dict], max_retries: int = 3) -> Tuple[str, int, int]:
    """
    Call OpenAI API with gpt-5.2
    Returns: (response_text, input_tokens, output_tokens)
    """
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL,
        "messages": messages
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=180
            )
            
            if response.status_code == 200:
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {})
                input_tokens = usage.get("prompt_tokens", 0)
                output_tokens = usage.get("completion_tokens", 0)
                return content, input_tokens, output_tokens
            elif response.status_code == 429:
                # Rate limited, wait and retry
                wait_time = 2 ** attempt * 10
                print(f"    Rate limited, waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"    API error {response.status_code}: {response.text[:200]}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                    
        except Exception as e:
            print(f"    Request error: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
    
    raise Exception(f"Failed after {max_retries} attempts")


def search_paper_arxiv(title: str) -> Optional[str]:
    """Search for paper on arxiv and return PDF URL"""
    # Clean title for search
    clean_title = re.sub(r'[^\w\s]', ' ', title).strip()
    
    try:
        # Use arxiv API
        import urllib.parse
        query = urllib.parse.quote(clean_title)
        url = f"http://export.arxiv.org/api/query?search_query=ti:{query}&max_results=3"
        
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            # Parse XML to find arxiv ID
            import xml.etree.ElementTree as ET
            root = ET.fromstring(response.content)
            
            # Find entry with matching title
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                entry_title = entry.find('atom:title', ns)
                if entry_title is not None:
                    # Check if titles are similar enough
                    entry_title_clean = re.sub(r'\s+', ' ', entry_title.text.strip().lower())
                    search_title_clean = clean_title.lower()
                    
                    # Simple similarity check
                    if len(set(entry_title_clean.split()) & set(search_title_clean.split())) >= 3:
                        # Get arxiv ID from link
                        for link in entry.findall('atom:link', ns):
                            if link.get('title') == 'pdf':
                                return link.get('href')
                        # Fallback: construct PDF URL from ID
                        id_elem = entry.find('atom:id', ns)
                        if id_elem is not None:
                            arxiv_id = id_elem.text.split('/')[-1]
                            return f"https://arxiv.org/pdf/{arxiv_id}"
    except Exception as e:
        print(f"      arxiv search error: {e}")
    
    return None


def crawl_paper_content(url: str, max_chars: int = MAX_CHARS_PER_PAPER) -> Optional[str]:
    """Crawl paper content from URL using requests (for PDF URLs)"""
    try:
        # For arxiv PDFs, we can try to get the abstract page first
        if 'arxiv.org/pdf' in url:
            abs_url = url.replace('/pdf/', '/abs/').replace('.pdf', '')
            # Try to get abstract
            response = requests.get(abs_url, timeout=30)
            if response.status_code == 200:
                # Extract abstract from HTML
                text = response.text
                # Simple extraction of abstract
                abstract_match = re.search(r'<blockquote[^>]*class="abstract[^"]*"[^>]*>(.*?)</blockquote>', text, re.DOTALL)
                if abstract_match:
                    abstract = re.sub(r'<[^>]+>', '', abstract_match.group(1)).strip()
                    return abstract[:max_chars]
        
        # For other URLs, try direct fetch
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.text[:max_chars]
            
    except Exception as e:
        print(f"      crawl error: {e}")
    
    return None


def get_paper_content_from_synthesis(pred: Dict) -> str:
    """Extract paper content from synthesis data (fallback)"""
    content_parts = []
    
    title = pred.get('paper_title', 'Unknown')
    content_parts.append(f"Title: {title}")
    
    role = pred.get('assigned_role', '')
    if role:
        content_parts.append(f"Role in research: {role}")
    
    quote = pred.get('justification_quote', '')
    if quote:
        content_parts.append(f"Key finding: {quote}")
    
    explanation = pred.get('explanation', '')
    if explanation:
        content_parts.append(f"Explanation: {explanation}")
    
    what_took = pred.get('what_authors_took', '')
    if what_took:
        content_parts.append(f"Contribution used: {what_took}")
    
    return "\n".join(content_parts)


def load_synthesis_files(data_dir: str) -> List[Dict]:
    """Load all synthesis JSON files from the directory"""
    papers = []
    pattern = os.path.join(data_dir, "synthesis_*.json")
    files = sorted(glob.glob(pattern))
    
    for filepath in files:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                if data.get("status") == "success" and data.get("synthesis_graph"):
                    papers.append(data)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
    
    return papers


def extract_predecessor_info(paper: Dict) -> List[Dict]:
    """Extract predecessor information from a paper"""
    synthesis = paper.get("synthesis_graph", {})
    predecessors = synthesis.get("intellectual_predecessors", [])
    return predecessors


def build_predecessor_content(predecessors: List[Dict], use_crawling: bool = False) -> Tuple[str, int]:
    """
    Build content string from predecessors.
    Returns (content_string, num_crawled)
    """
    content_parts = []
    crawled_count = 0
    
    for i, pred in enumerate(predecessors, 1):
        title = pred.get('paper_title', 'Unknown')
        
        # Try to get actual paper content if crawling is enabled
        paper_content = None
        if use_crawling:
            print(f"      Searching for: {title[:50]}...")
            pdf_url = search_paper_arxiv(title)
            if pdf_url:
                print(f"      Found: {pdf_url}")
                paper_content = crawl_paper_content(pdf_url)
                if paper_content:
                    crawled_count += 1
                    print(f"      Crawled {len(paper_content)} chars")
        
        # Build content for this predecessor
        if paper_content:
            content = f"""
=== Prior Work {i}: "{title}" ===
{paper_content}
"""
        else:
            # Fallback to synthesis data
            content = f"""
=== Prior Work {i} ===
{get_paper_content_from_synthesis(pred)}
"""
        content_parts.append(content)
    
    return "\n".join(content_parts), crawled_count


def generate_ideas_prompt(predecessor_content: str, k: int = 10) -> str:
    """Create prompt for generating research ideas based on predecessors"""
    
    prompt = f"""You are a research scientist identifying promising research directions.

Given the following prior works (intellectual predecessors), generate exactly {k} novel research ideas that could naturally build upon and synthesize these works. Each idea should:
1. Combine insights from multiple predecessor papers
2. Address gaps or limitations in the current work
3. Propose a concrete, actionable research direction
4. Be specific enough to be a real paper contribution

PRIOR WORKS:
{predecessor_content}

Generate exactly {k} research ideas. For each idea, provide:
- A concise title (like a paper title)
- A 2-3 sentence description of the core contribution

Format your response as a JSON array with {k} objects, each having "title" and "description" fields.
Output ONLY the JSON array, no other text."""

    return prompt


def judge_similarity_prompt(generated_idea: Dict, ground_truth_title: str, 
                           ground_truth_contribution: str) -> str:
    """Create prompt for judging if a generated idea matches the ground truth"""
    
    prompt = f"""You are evaluating whether a generated research idea matches a real published paper.

GENERATED IDEA:
Title: {generated_idea.get('title', 'Unknown')}
Description: {generated_idea.get('description', 'Unknown')}

REAL PUBLISHED PAPER:
Title: {ground_truth_title}
Contribution: {ground_truth_contribution}

Determine if the generated idea is semantically similar to the real paper. Consider:
1. Do they address the same core problem or research question?
2. Do they propose similar methodological approaches?
3. Would the generated idea, if fully developed, result in a similar contribution?

A match means the ideas are substantially aligned in their core direction, not necessarily identical in every detail.

Respond with a JSON object containing:
- "is_match": true or false
- "confidence": a number from 0 to 1
- "reasoning": a brief explanation (2-3 sentences)

Output ONLY the JSON object, no other text."""

    return prompt


def parse_json_response(response: str) -> Any:
    """Parse JSON from LLM response, handling common issues"""
    response = response.strip()
    
    # Remove markdown code blocks
    if response.startswith("```json"):
        response = response[7:]
    if response.startswith("```"):
        response = response[3:]
    if response.endswith("```"):
        response = response[:-3]
    
    response = response.strip()
    
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        # Try to find JSON array or object in response
        array_match = re.search(r'\[[\s\S]*\]', response)
        if array_match:
            try:
                return json.loads(array_match.group())
            except:
                pass
        
        obj_match = re.search(r'\{[\s\S]*\}', response)
        if obj_match:
            try:
                return json.loads(obj_match.group())
            except:
                pass
        
        raise


def generate_ideas(predecessor_content: str, cost_tracker: CostTracker) -> List[Dict]:
    """Generate k research ideas using GPT-5.2"""
    
    prompt = generate_ideas_prompt(predecessor_content, K_IDEAS)
    
    messages = [
        {"role": "system", "content": "You are a helpful research assistant that generates novel research ideas based on prior work. Always respond with valid JSON."},
        {"role": "user", "content": prompt}
    ]
    
    response, input_tokens, output_tokens = call_openai_api(messages)
    cost_tracker.add(input_tokens, output_tokens)
    
    # Parse JSON response
    try:
        ideas = parse_json_response(response)
        if isinstance(ideas, list):
            return ideas
        return []
    except Exception as e:
        print(f"    JSON parse error: {e}")
        print(f"    Response preview: {response[:300]}...")
        return []


def judge_similarity(idea: Dict, ground_truth_title: str, 
                    ground_truth_contribution: str, cost_tracker: CostTracker) -> Dict:
    """Judge if a generated idea matches the ground truth using GPT-5.2"""
    
    prompt = judge_similarity_prompt(idea, ground_truth_title, ground_truth_contribution)
    
    messages = [
        {"role": "system", "content": "You are an expert at evaluating research paper similarity. Always respond with valid JSON."},
        {"role": "user", "content": prompt}
    ]
    
    response, input_tokens, output_tokens = call_openai_api(messages)
    cost_tracker.add(input_tokens, output_tokens)
    
    # Parse JSON response
    try:
        result = parse_json_response(response)
        if isinstance(result, dict):
            return result
        return {"is_match": False, "confidence": 0, "reasoning": "Invalid response format"}
    except Exception as e:
        print(f"    JSON parse error in similarity judgment: {e}")
        return {"is_match": False, "confidence": 0, "reasoning": f"Parse error: {str(e)}"}


def evaluate_single_paper(paper: Dict, cost_tracker: CostTracker, 
                         use_crawling: bool = False) -> EvaluationResult:
    """Evaluate idea generation for a single paper"""
    
    synthesis = paper.get("synthesis_graph", {})
    paper_title = synthesis.get("target_paper_title", paper.get("title", "Unknown"))
    paper_contribution = synthesis.get("target_paper_contribution", "")
    predecessors = extract_predecessor_info(paper)
    
    print(f"\n  Target: {paper_title[:60]}...")
    print(f"  Predecessors: {len(predecessors)}")
    
    # Build predecessor content
    print(f"  Building predecessor content...")
    predecessor_content, crawled_count = build_predecessor_content(predecessors, use_crawling)
    content_length = len(predecessor_content)
    print(f"  Content length: {content_length} chars, Crawled: {crawled_count}/{len(predecessors)}")
    
    # Generate ideas
    print(f"  Generating {K_IDEAS} ideas...")
    ideas = generate_ideas(predecessor_content, cost_tracker)
    print(f"  Generated {len(ideas)} ideas")
    
    if not ideas:
        return EvaluationResult(
            paper_idx=paper.get("paper_idx", -1),
            paper_title=paper_title,
            paper_contribution=paper_contribution,
            num_predecessors=len(predecessors),
            predecessors_crawled=crawled_count,
            predecessor_content_length=content_length,
            generated_ideas=[],
            similarity_scores=[],
            hit_at_k=False,
            best_match_idx=None,
            best_match_reasoning=None,
            error="Failed to generate ideas"
        )
    
    # Judge similarity for each idea
    print(f"  Judging similarity for {len(ideas)} ideas...")
    similarity_scores = []
    best_match_idx = None
    best_confidence = 0
    
    for idx, idea in enumerate(ideas):
        result = judge_similarity(idea, paper_title, paper_contribution, cost_tracker)
        result["idea_idx"] = idx
        similarity_scores.append(result)
        
        if result.get("is_match", False):
            if result.get("confidence", 0) > best_confidence:
                best_confidence = result.get("confidence", 0)
                best_match_idx = idx
    
    hit_at_k = any(s.get("is_match", False) for s in similarity_scores)
    
    return EvaluationResult(
        paper_idx=paper.get("paper_idx", -1),
        paper_title=paper_title,
        paper_contribution=paper_contribution,
        num_predecessors=len(predecessors),
        predecessors_crawled=crawled_count,
        predecessor_content_length=content_length,
        generated_ideas=[{"title": i.get("title", ""), "description": i.get("description", "")} for i in ideas],
        similarity_scores=similarity_scores,
        hit_at_k=hit_at_k,
        best_match_idx=best_match_idx,
        best_match_reasoning=similarity_scores[best_match_idx].get("reasoning") if best_match_idx is not None else None
    )


def run_evaluation(data_dir: str, output_dir: str, max_papers: Optional[int] = None,
                  use_crawling: bool = False):
    """Run the full evaluation pipeline"""
    
    print("=" * 70)
    print("Research Idea Generation Evaluation")
    print(f"Model: {MODEL}")
    print(f"k = {K_IDEAS} ideas per paper")
    print(f"Paper crawling: {'Enabled' if use_crawling else 'Disabled (using synthesis data)'}")
    print("=" * 70)
    
    # Load papers
    print("\nLoading synthesis files...")
    papers = load_synthesis_files(data_dir)
    print(f"Loaded {len(papers)} papers")
    
    if max_papers:
        papers = papers[:max_papers]
        print(f"Limiting to {max_papers} papers for testing")
    
    # Initialize tracking
    cost_tracker = CostTracker()
    results = []
    hits = 0
    
    start_time = time.time()
    
    # Evaluate each paper
    for i, paper in enumerate(papers):
        print(f"\n{'='*70}")
        print(f"[{i+1}/{len(papers)}] Evaluating paper {paper.get('paper_idx', i)}...")
        
        try:
            result = evaluate_single_paper(paper, cost_tracker, use_crawling)
            results.append(result)
            
            if result.hit_at_k:
                hits += 1
                print(f"  ✓ HIT! Best match: idea {result.best_match_idx}")
                if result.best_match_reasoning:
                    print(f"    Reasoning: {result.best_match_reasoning[:100]}...")
            else:
                print(f"  ✗ No match")
            
            # Print running stats
            hit_rate = hits / (i + 1) * 100
            elapsed = time.time() - start_time
            print(f"  Running Hit@{K_IDEAS}: {hits}/{i+1} ({hit_rate:.1f}%)")
            print(f"  API Cost so far: ${cost_tracker.total_cost:.4f}")
            print(f"  Elapsed time: {elapsed/60:.1f} min")
            
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            results.append(EvaluationResult(
                paper_idx=paper.get("paper_idx", i),
                paper_title=paper.get("title", "Unknown"),
                paper_contribution="",
                num_predecessors=0,
                predecessors_crawled=0,
                predecessor_content_length=0,
                generated_ideas=[],
                similarity_scores=[],
                hit_at_k=False,
                best_match_idx=None,
                best_match_reasoning=None,
                error=str(e)
            ))
        
        # Save intermediate results every 10 papers
        if (i + 1) % 10 == 0:
            save_results(results, cost_tracker, output_dir, intermediate=True)
    
    # Final results
    total_time = time.time() - start_time
    
    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)
    
    total_papers = len(results)
    successful_evals = sum(1 for r in results if r.error is None)
    hit_rate = hits / successful_evals * 100 if successful_evals > 0 else 0
    
    print(f"\nTotal papers evaluated: {total_papers}")
    print(f"Successful evaluations: {successful_evals}")
    print(f"Hits (at least one matching idea): {hits}")
    print(f"Hit@{K_IDEAS}: {hit_rate:.2f}%")
    print(f"\nTotal time: {total_time/60:.1f} minutes")
    print(f"\nAPI Cost Summary:")
    print(f"  Input tokens: {cost_tracker.input_tokens:,}")
    print(f"  Output tokens: {cost_tracker.output_tokens:,}")
    print(f"  Input cost: ${cost_tracker.input_cost:.4f}")
    print(f"  Output cost: ${cost_tracker.output_cost:.4f}")
    print(f"  Total cost: ${cost_tracker.total_cost:.4f}")
    
    # Save final results
    save_results(results, cost_tracker, output_dir, intermediate=False, total_time=total_time)
    
    return results, cost_tracker


def save_results(results: List[EvaluationResult], cost_tracker: CostTracker, 
                output_dir: str, intermediate: bool = False, total_time: float = 0):
    """Save evaluation results to JSON"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert results to dicts
    results_data = []
    for r in results:
        results_data.append({
            "paper_idx": r.paper_idx,
            "paper_title": r.paper_title,
            "paper_contribution": r.paper_contribution,
            "num_predecessors": r.num_predecessors,
            "predecessors_crawled": r.predecessors_crawled,
            "predecessor_content_length": r.predecessor_content_length,
            "generated_ideas": r.generated_ideas,
            "similarity_scores": r.similarity_scores,
            "hit_at_k": r.hit_at_k,
            "best_match_idx": r.best_match_idx,
            "best_match_reasoning": r.best_match_reasoning,
            "error": r.error
        })
    
    # Calculate summary stats
    successful = [r for r in results if r.error is None]
    hits = sum(1 for r in results if r.hit_at_k)
    
    summary = {
        "model": MODEL,
        "k": K_IDEAS,
        "total_papers": len(results),
        "successful_evaluations": len(successful),
        "hits": hits,
        "hit_rate_percent": round(hits / len(successful) * 100, 2) if successful else 0,
        "cost": cost_tracker.to_dict(),
        "total_time_seconds": round(total_time, 1),
        "timestamp": datetime.now().isoformat()
    }
    
    output_data = {
        "summary": summary,
        "results": results_data
    }
    
    suffix = "_intermediate" if intermediate else "_final"
    filename = f"evaluation_results_gpt52{suffix}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\nResults saved to: {filepath}")


if __name__ == "__main__":
    # Configuration
    DATA_DIR = "projects/synthesis_graph_pipeline/results/conferences/NeurIPS-2025-oral"
    OUTPUT_DIR = "projects/research_idea_evaluation/results"
    
    # Parse command line arguments
    max_papers = MAX_PAPERS
    use_crawling = False
    
    if len(sys.argv) > 1:
        try:
            max_papers = int(sys.argv[1])
        except:
            pass
    
    if len(sys.argv) > 2 and sys.argv[2] == "--crawl":
        use_crawling = True
    
    # Run evaluation
    results, cost_tracker = run_evaluation(
        DATA_DIR, 
        OUTPUT_DIR, 
        max_papers=max_papers,
        use_crawling=use_crawling
    )

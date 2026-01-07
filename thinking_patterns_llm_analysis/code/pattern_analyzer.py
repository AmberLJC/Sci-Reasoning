#!/usr/bin/env python3
"""
Thinking Patterns Analysis Engine
Uses GPT-5-mini to discover and classify thinking patterns in ML paper synthesis narratives.
"""

import os
import json
import random
import time
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Any, Tuple
import openai

# Configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = "gpt-5-mini"
BASE_PATH = Path("/home/orchestra/projects/synthesis_graph_pipeline/results/conferences")
OUTPUT_PATH = Path("/home/orchestra/projects/thinking_patterns_llm_analysis/results")

# Analysis parameters
NUM_DISCOVERY_BATCHES = 10
PAPERS_PER_DISCOVERY_BATCH = 35
CLASSIFICATION_BATCH_SIZE = 5

# Cost tracking
INPUT_COST_PER_M = 0.25  # $ per million input tokens
OUTPUT_COST_PER_M = 2.0  # $ per million output tokens

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
        self.calls.append({
            "phase": phase,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": cost
        })
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

def call_gpt(messages: List[Dict], phase: str, retry_count: int = 3) -> str:
    """Call GPT-5-mini API and track costs."""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    for attempt in range(retry_count):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages
            )
            
            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens
            cost = cost_tracker.add_call(input_tokens, output_tokens, phase)
            
            print(f"  [API] {phase}: in={input_tokens}, out={output_tokens}, cost=${cost:.4f}, total=${cost_tracker.get_total_cost():.4f}")
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"  [API Error] Attempt {attempt+1}/{retry_count}: {e}")
            if attempt < retry_count - 1:
                time.sleep(2 ** attempt)
            else:
                raise


def load_all_papers() -> List[Dict]:
    """Load all synthesis narratives from the conference directories."""
    papers = []
    
    for conf_dir in BASE_PATH.iterdir():
        if not conf_dir.is_dir():
            continue
        
        # Parse conference info from directory name
        parts = conf_dir.name.split("-")
        if len(parts) >= 3:
            conference = parts[0]
            year = parts[1]
            presentation_type = parts[2]
        else:
            continue
        
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
                    "presentation_type": presentation_type,
                    "synthesis_narrative": narrative,
                    "thinking_trajectory": synthesis_graph.get("thinking_trajectory", {}),
                    "file_path": str(json_file)
                })
            except Exception as e:
                print(f"Error loading {json_file}: {e}")
    
    return papers


def create_stratified_sample(papers: List[Dict], sample_size: int, seed: int = 42) -> List[Dict]:
    """Create a stratified sample across conferences, years, and presentation types."""
    random.seed(seed)
    
    # Group papers by strata
    strata = defaultdict(list)
    for paper in papers:
        key = (paper["conference"], paper["year"], paper["presentation_type"])
        strata[key].append(paper)
    
    # Calculate proportional sample sizes
    total = len(papers)
    sampled = []
    
    for key, group_papers in strata.items():
        proportion = len(group_papers) / total
        group_sample_size = max(1, int(sample_size * proportion))
        group_sample = random.sample(group_papers, min(group_sample_size, len(group_papers)))
        sampled.extend(group_sample)
    
    # If we need more samples, add randomly
    if len(sampled) < sample_size:
        remaining = [p for p in papers if p not in sampled]
        additional = random.sample(remaining, min(sample_size - len(sampled), len(remaining)))
        sampled.extend(additional)
    
    random.shuffle(sampled)
    return sampled[:sample_size]


def discover_patterns_batch(narratives: List[str], batch_num: int) -> Dict:
    """Use GPT-5-mini to discover patterns in a batch of narratives."""
    
    narratives_text = "\n\n---\n\n".join([f"Paper {i+1}:\n{n}" for i, n in enumerate(narratives)])
    
    system_prompt = """You are an expert research methodology analyst specializing in understanding how breakthrough ideas emerge. Your task is to analyze synthesis narratives from top ML research papers (oral/spotlight at NeurIPS, ICML, ICLR) and identify recurring THINKING PATTERNS.

Focus on the COGNITIVE STRATEGIES and INTELLECTUAL MOVES researchers make:
- How they identify gaps, tensions, or opportunities
- How they connect disparate ideas or domains
- How they challenge assumptions or reframe problems
- How they abstract, generalize, or specialize concepts
- How they leverage analogies or transfer insights
- How they navigate from observation to innovation

Be specific and actionable. Each pattern should be a learnable thinking strategy."""

    user_prompt = f"""Analyze these {len(narratives)} synthesis narratives from top ML papers and identify distinct THINKING PATTERNS.

{narratives_text}

For each pattern, provide:
1. NAME: Clear, memorable name (2-5 words)
2. DESCRIPTION: What this thinking strategy involves (2-3 sentences)
3. KEY_INDICATORS: Phrases/concepts that signal this pattern
4. COGNITIVE_MOVE: The core intellectual operation being performed
5. EXAMPLE: Brief example from the narratives

Output as JSON:
{{
    "patterns": [
        {{
            "name": "Pattern Name",
            "description": "Detailed description of the thinking strategy",
            "key_indicators": ["indicator1", "indicator2", "indicator3"],
            "cognitive_move": "The fundamental intellectual operation",
            "example_summary": "Brief example from narratives"
        }}
    ],
    "meta_observations": "High-level observations about research thinking in these papers"
}}"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response = call_gpt(messages, f"discovery_batch_{batch_num}")
    
    try:
        if "```json" in response:
            json_str = response.split("```json")[1].split("```")[0]
        elif "```" in response:
            json_str = response.split("```")[1].split("```")[0]
        else:
            json_str = response
        
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"  Warning: JSON parse error: {e}")
        return {"patterns": [], "raw_response": response}


def consolidate_patterns(all_discovered_patterns: List[Dict]) -> Dict:
    """Use GPT-5-mini to consolidate patterns into a unified taxonomy."""
    
    all_patterns = []
    all_meta = []
    for batch_result in all_discovered_patterns:
        patterns = batch_result.get("patterns", [])
        all_patterns.extend(patterns)
        if batch_result.get("meta_observations"):
            all_meta.append(batch_result["meta_observations"])
    
    patterns_text = json.dumps(all_patterns, indent=2)
    meta_text = "\n".join([f"- {m}" for m in all_meta])
    
    system_prompt = """You are an expert taxonomist specializing in research methodology and cognitive science. Create a comprehensive, well-organized taxonomy of thinking patterns from the discovered patterns."""

    user_prompt = f"""I discovered {len(all_patterns)} thinking patterns from analyzing 350 top ML papers. Many overlap or are variations.

DISCOVERED PATTERNS:
{patterns_text}

META-OBSERVATIONS FROM BATCHES:
{meta_text}

Create a FINAL TAXONOMY of 12-18 distinct, non-overlapping thinking patterns. Organize them into meaningful categories.

For each pattern provide:
1. ID: Short identifier (P01, P02, etc.)
2. NAME: Clear, memorable name
3. CATEGORY: Higher-level grouping (e.g., "Gap Identification", "Synthesis", "Reframing")
4. DESCRIPTION: Precise definition (2-3 sentences)
5. KEY_INDICATORS: Specific phrases that identify this pattern
6. COGNITIVE_MOVE: The core intellectual operation
7. VARIANTS_MERGED: Similar patterns consolidated into this one
8. EXAMPLE: Concrete example
9. LEARNABLE_INSIGHT: How a researcher can deliberately apply this pattern

Output as JSON:
{{
    "taxonomy": [
        {{
            "id": "P01",
            "name": "Pattern Name",
            "category": "Category Name",
            "description": "Detailed description",
            "key_indicators": ["indicator1", "indicator2"],
            "cognitive_move": "Core operation",
            "variants_merged": ["variant1", "variant2"],
            "example": "Concrete example",
            "learnable_insight": "How to apply this pattern"
        }}
    ],
    "categories": [
        {{
            "name": "Category Name",
            "description": "What patterns in this category share",
            "pattern_ids": ["P01", "P02"]
        }}
    ],
    "taxonomy_rationale": "How the taxonomy was organized"
}}"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response = call_gpt(messages, "consolidation")
    
    try:
        if "```json" in response:
            json_str = response.split("```json")[1].split("```")[0]
        elif "```" in response:
            json_str = response.split("```")[1].split("```")[0]
        else:
            json_str = response
        
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"  Warning: Consolidation JSON parse error: {e}")
        return {"taxonomy": [], "raw_response": response}


def classify_papers_batch(papers: List[Dict], taxonomy: List[Dict], batch_num: int) -> List[Dict]:
    """Classify a batch of papers using the discovered taxonomy."""
    
    taxonomy_ref = "\n".join([
        f"- {p['id']}: {p['name']} ({p['category']}) - {p['description']}"
        for p in taxonomy
    ])
    
    papers_text = "\n\n---\n\n".join([
        f"Paper {i+1}: \"{p['title'][:80]}\"\nNarrative: {p['synthesis_narrative']}"
        for i, p in enumerate(papers)
    ])
    
    system_prompt = """You are an expert at analyzing research thinking patterns. Classify each paper's synthesis narrative according to the provided taxonomy. Be precise and identify both primary and secondary patterns."""

    user_prompt = f"""TAXONOMY:
{taxonomy_ref}

PAPERS:
{papers_text}

For each paper, identify:
- PRIMARY_PATTERN: The dominant thinking pattern (most central to the innovation)
- SECONDARY_PATTERNS: Other patterns present (up to 3)
- CONFIDENCE: high/medium/low
- BRIEF_REASONING: One sentence explaining the classification

Output as JSON:
{{
    "classifications": [
        {{
            "paper_index": 1,
            "primary_pattern": "P01",
            "secondary_patterns": ["P03", "P05"],
            "confidence": "high",
            "reasoning": "Brief explanation"
        }}
    ]
}}"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
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
    except json.JSONDecodeError as e:
        print(f"  Warning: Classification JSON parse error: {e}")
        for paper in papers:
            paper["classification"] = {"primary_pattern": "unknown", "secondary_patterns": [], "error": str(e)}
        return papers


def generate_deep_insights(taxonomy: List[Dict], analysis: Dict, papers: List[Dict]) -> Dict:
    """Generate deep insights about the patterns discovered."""
    
    # Prepare summary data
    top_patterns = sorted(analysis["primary_pattern_counts"].items(), key=lambda x: x[1], reverse=True)[:10]
    pattern_names = analysis["pattern_names"]
    
    top_patterns_text = "\n".join([
        f"- {pid}: {pattern_names.get(pid, pid)} - {count} papers ({count/analysis['total_papers']*100:.1f}%)"
        for pid, count in top_patterns
    ])
    
    # Year trends
    year_trends = {}
    for year, patterns in analysis["by_year"].items():
        total = sum(patterns.values())
        year_trends[year] = {pid: count/total*100 for pid, count in patterns.items()}
    
    # Conference differences
    conf_patterns = {}
    for conf, patterns in analysis["by_conference"].items():
        total = sum(patterns.values())
        conf_patterns[conf] = {pid: count/total*100 for pid, count in patterns.items()}
    
    # Sample high-confidence classifications for examples
    high_conf_examples = [p for p in papers if p.get("classification", {}).get("confidence") == "high"][:20]
    examples_text = "\n".join([
        f"- \"{p['title'][:60]}...\" -> {p['classification']['primary_pattern']}: {p['classification'].get('reasoning', 'N/A')}"
        for p in high_conf_examples[:10]
    ])
    
    system_prompt = """You are a research strategist and cognitive scientist analyzing patterns in how top ML researchers think. Provide deep, actionable insights."""

    user_prompt = f"""Based on analyzing {analysis['total_papers']} top ML papers (NeurIPS, ICML, ICLR oral/spotlight 2023-2025), here are the findings:

TOP THINKING PATTERNS:
{top_patterns_text}

YEAR TRENDS (% of papers):
{json.dumps(year_trends, indent=2)}

CONFERENCE DIFFERENCES (% of papers):
{json.dumps(conf_patterns, indent=2)}

EXAMPLE CLASSIFICATIONS:
{examples_text}

CO-OCCURRENCE PATTERNS:
{json.dumps(dict(list(analysis['cooccurrence'].items())[:10]), indent=2)}

Provide DEEP INSIGHTS:

1. STRATEGIC INSIGHTS: What do these patterns reveal about how breakthrough ML research happens?

2. TEMPORAL TRENDS: How is ML research thinking evolving from 2023 to 2025?

3. CONFERENCE CULTURE: Do different venues favor different thinking styles?

4. PATTERN COMBINATIONS: Which patterns work well together? What are powerful "thinking recipes"?

5. ACTIONABLE ADVICE: For a researcher wanting to do impactful ML work, what thinking strategies should they cultivate?

6. GAPS & OPPORTUNITIES: What thinking patterns might be underutilized? Where are opportunities?

7. META-INSIGHTS: What does this analysis reveal about the nature of innovation in ML?

Be specific, cite the data, and provide actionable recommendations."""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response = call_gpt(messages, "deep_insights")
    
    return {
        "insights_text": response,
        "data_summary": {
            "top_patterns": top_patterns,
            "year_trends": year_trends,
            "conference_patterns": conf_patterns
        }
    }


def analyze_results(classified_papers: List[Dict], taxonomy: List[Dict]) -> Dict:
    """Analyze the classification results."""
    
    primary_counts = defaultdict(int)
    secondary_counts = defaultdict(int)
    total_counts = defaultdict(int)
    
    by_conference = defaultdict(lambda: defaultdict(int))
    by_year = defaultdict(lambda: defaultdict(int))
    by_type = defaultdict(lambda: defaultdict(int))
    
    cooccurrence = defaultdict(lambda: defaultdict(int))
    confidence_dist = defaultdict(int)
    
    for paper in classified_papers:
        classification = paper.get("classification", {})
        primary = classification.get("primary_pattern", "unknown")
        secondary = classification.get("secondary_patterns", [])
        confidence = classification.get("confidence", "unknown")
        
        primary_counts[primary] += 1
        total_counts[primary] += 1
        confidence_dist[confidence] += 1
        
        for s in secondary:
            secondary_counts[s] += 1
            total_counts[s] += 1
            cooccurrence[primary][s] += 1
        
        by_conference[paper["conference"]][primary] += 1
        by_year[paper["year"]][primary] += 1
        by_type[paper["presentation_type"]][primary] += 1
    
    pattern_names = {p["id"]: p["name"] for p in taxonomy}
    pattern_categories = {p["id"]: p.get("category", "Unknown") for p in taxonomy}
    
    return {
        "total_papers": len(classified_papers),
        "primary_pattern_counts": dict(primary_counts),
        "secondary_pattern_counts": dict(secondary_counts),
        "total_pattern_counts": dict(total_counts),
        "by_conference": {k: dict(v) for k, v in by_conference.items()},
        "by_year": {k: dict(v) for k, v in by_year.items()},
        "by_presentation_type": {k: dict(v) for k, v in by_type.items()},
        "cooccurrence": {k: dict(v) for k, v in cooccurrence.items()},
        "confidence_distribution": dict(confidence_dist),
        "pattern_names": pattern_names,
        "pattern_categories": pattern_categories
    }


def main():
    """Main analysis pipeline."""
    print("=" * 70)
    print("THINKING PATTERNS ANALYSIS ENGINE - GPT-5-mini")
    print("=" * 70)
    
    # Ensure output directory exists
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    
    # Phase 1: Load all papers
    print("\n[Phase 1] Loading all papers...")
    papers = load_all_papers()
    print(f"  ✓ Loaded {len(papers)} papers")
    
    stats = defaultdict(lambda: defaultdict(int))
    for p in papers:
        stats[p["conference"]][f"{p['year']}-{p['presentation_type']}"] += 1
    
    print("\n  Distribution:")
    for conf in sorted(stats.keys()):
        years = stats[conf]
        total = sum(years.values())
        print(f"    {conf}: {total} papers - {dict(sorted(years.items()))}")
    
    # Phase 2: Pattern Discovery
    print(f"\n[Phase 2] Pattern Discovery ({NUM_DISCOVERY_BATCHES} batches × {PAPERS_PER_DISCOVERY_BATCH} papers = {NUM_DISCOVERY_BATCHES * PAPERS_PER_DISCOVERY_BATCH} samples)...")
    
    all_discovered_patterns = []
    
    for batch_num in range(NUM_DISCOVERY_BATCHES):
        print(f"\n  Batch {batch_num + 1}/{NUM_DISCOVERY_BATCHES}...")
        
        sample = create_stratified_sample(papers, PAPERS_PER_DISCOVERY_BATCH, seed=42 + batch_num * 137)
        narratives = [p["synthesis_narrative"] for p in sample]
        
        batch_patterns = discover_patterns_batch(narratives, batch_num + 1)
        all_discovered_patterns.append(batch_patterns)
        
        num_patterns = len(batch_patterns.get("patterns", []))
        print(f"    → Found {num_patterns} patterns")
        
        time.sleep(0.5)
    
    with open(OUTPUT_PATH / "raw_discovered_patterns.json", "w") as f:
        json.dump(all_discovered_patterns, f, indent=2)
    print(f"\n  ✓ Saved raw patterns to raw_discovered_patterns.json")
    
    # Phase 3: Consolidate
    print("\n[Phase 3] Consolidating into taxonomy...")
    taxonomy_result = consolidate_patterns(all_discovered_patterns)
    taxonomy = taxonomy_result.get("taxonomy", [])
    print(f"  ✓ Created taxonomy with {len(taxonomy)} patterns")
    
    if taxonomy:
        print("\n  Pattern Taxonomy:")
        categories = defaultdict(list)
        for p in taxonomy:
            categories[p.get("category", "Other")].append(p)
        
        for cat, patterns in sorted(categories.items()):
            print(f"    [{cat}]")
            for p in patterns:
                print(f"      - {p['id']}: {p['name']}")
    
    with open(OUTPUT_PATH / "pattern_taxonomy.json", "w") as f:
        json.dump(taxonomy_result, f, indent=2)
    
    # Phase 4: Classify ALL papers
    print(f"\n[Phase 4] Classifying all {len(papers)} papers (batch size: {CLASSIFICATION_BATCH_SIZE})...")
    
    classified_papers = []
    total_batches = (len(papers) + CLASSIFICATION_BATCH_SIZE - 1) // CLASSIFICATION_BATCH_SIZE
    
    for i in range(0, len(papers), CLASSIFICATION_BATCH_SIZE):
        batch = papers[i:i + CLASSIFICATION_BATCH_SIZE]
        batch_num = i // CLASSIFICATION_BATCH_SIZE + 1
        
        if batch_num % 50 == 1 or batch_num == total_batches:
            print(f"\n  Batch {batch_num}/{total_batches} ({len(classified_papers)}/{len(papers)} done, cost: ${cost_tracker.get_total_cost():.4f})...")
        
        classified_batch = classify_papers_batch(batch, taxonomy, batch_num)
        classified_papers.extend(classified_batch)
        
        time.sleep(0.2)
    
    # Save classifications
    with open(OUTPUT_PATH / "classified_papers.json", "w") as f:
        save_data = [{
            "title": p["title"],
            "conference": p["conference"],
            "year": p["year"],
            "presentation_type": p["presentation_type"],
            "classification": p["classification"]
        } for p in classified_papers]
        json.dump(save_data, f, indent=2)
    print(f"\n  ✓ Saved classifications to classified_papers.json")
    
    # Phase 5: Analysis
    print("\n[Phase 5] Analyzing results...")
    analysis = analyze_results(classified_papers, taxonomy)
    
    with open(OUTPUT_PATH / "analysis_results.json", "w") as f:
        json.dump(analysis, f, indent=2)
    
    # Phase 6: Deep Insights
    print("\n[Phase 6] Generating deep insights...")
    insights = generate_deep_insights(taxonomy, analysis, classified_papers)
    
    with open(OUTPUT_PATH / "deep_insights.json", "w") as f:
        json.dump(insights, f, indent=2)
    
    with open(OUTPUT_PATH / "deep_insights.md", "w") as f:
        f.write("# Deep Insights: Thinking Patterns in Top ML Research\n\n")
        f.write(insights["insights_text"])
    
    # Final Summary
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    
    print(f"\n📊 RESULTS SUMMARY")
    print(f"   Total papers analyzed: {analysis['total_papers']}")
    print(f"   Patterns in taxonomy: {len(taxonomy)}")
    
    print(f"\n📈 TOP 10 PRIMARY PATTERNS:")
    sorted_patterns = sorted(analysis["primary_pattern_counts"].items(), key=lambda x: x[1], reverse=True)[:10]
    for rank, (pid, count) in enumerate(sorted_patterns, 1):
        name = analysis["pattern_names"].get(pid, pid)
        pct = count / analysis["total_papers"] * 100
        print(f"   {rank:2}. {pid}: {name}")
        print(f"       {count} papers ({pct:.1f}%)")
    
    print(f"\n📅 BY YEAR:")
    for year in sorted(analysis["by_year"].keys()):
        year_data = analysis["by_year"][year]
        total = sum(year_data.values())
        top_pattern = max(year_data.items(), key=lambda x: x[1])
        print(f"   {year}: {total} papers, top pattern: {analysis['pattern_names'].get(top_pattern[0], top_pattern[0])}")
    
    print(f"\n🏛️ BY CONFERENCE:")
    for conf in sorted(analysis["by_conference"].keys()):
        conf_data = analysis["by_conference"][conf]
        total = sum(conf_data.values())
        top_pattern = max(conf_data.items(), key=lambda x: x[1])
        print(f"   {conf}: {total} papers, top pattern: {analysis['pattern_names'].get(top_pattern[0], top_pattern[0])}")
    
    print(f"\n✅ CONFIDENCE DISTRIBUTION:")
    for conf, count in sorted(analysis["confidence_distribution"].items()):
        print(f"   {conf}: {count} ({count/analysis['total_papers']*100:.1f}%)")
    
    # Cost summary
    cost_summary = cost_tracker.get_summary()
    print(f"\n💰 API COST SUMMARY:")
    print(f"   Total API calls: {cost_summary['num_calls']}")
    print(f"   Input tokens: {cost_summary['total_input_tokens']:,}")
    print(f"   Output tokens: {cost_summary['total_output_tokens']:,}")
    print(f"   Total cost: ${cost_summary['total_cost_usd']:.4f}")
    
    with open(OUTPUT_PATH / "cost_tracking.json", "w") as f:
        json.dump({"summary": cost_summary, "calls": cost_tracker.calls}, f, indent=2)
    
    print(f"\n📁 Results saved to: {OUTPUT_PATH}")
    
    return taxonomy, classified_papers, analysis, insights


if __name__ == "__main__":
    main()

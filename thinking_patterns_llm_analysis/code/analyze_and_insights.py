#!/usr/bin/env python3
"""
Analysis and Deep Insights Generation
"""

import os
import json
from pathlib import Path
from collections import defaultdict
from typing import List, Dict
import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = "gpt-5-mini"
OUTPUT_PATH = Path("/home/orchestra/projects/thinking_patterns_llm_analysis/results")

INPUT_COST_PER_M = 0.25
OUTPUT_COST_PER_M = 2.0

class CostTracker:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
    
    def add_call(self, input_tokens: int, output_tokens: int):
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        return (input_tokens / 1_000_000 * INPUT_COST_PER_M + 
                output_tokens / 1_000_000 * OUTPUT_COST_PER_M)
    
    def get_total_cost(self):
        return (self.total_input_tokens / 1_000_000 * INPUT_COST_PER_M + 
                self.total_output_tokens / 1_000_000 * OUTPUT_COST_PER_M)

cost_tracker = CostTracker()

def call_gpt(messages: List[Dict]) -> str:
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(model=MODEL, messages=messages)
    cost = cost_tracker.add_call(response.usage.prompt_tokens, response.usage.completion_tokens)
    print(f"  API call: {response.usage.prompt_tokens} in, {response.usage.completion_tokens} out, ${cost:.4f}")
    return response.choices[0].message.content

def analyze_results(papers: List[Dict], taxonomy: List[Dict]) -> Dict:
    """Comprehensive analysis of classification results."""
    
    primary_counts = defaultdict(int)
    secondary_counts = defaultdict(int)
    total_counts = defaultdict(int)
    
    by_conference = defaultdict(lambda: defaultdict(int))
    by_year = defaultdict(lambda: defaultdict(int))
    by_type = defaultdict(lambda: defaultdict(int))
    by_conf_year = defaultdict(lambda: defaultdict(int))
    
    cooccurrence = defaultdict(lambda: defaultdict(int))
    confidence_dist = defaultdict(int)
    
    # Pattern pairs analysis
    pattern_pairs = defaultdict(int)
    
    for paper in papers:
        classification = paper.get("classification", {})
        primary = classification.get("primary_pattern", "unknown")
        secondary = classification.get("secondary_patterns", [])
        confidence = classification.get("confidence", "unknown")
        
        primary_counts[primary] += 1
        total_counts[primary] += 1
        confidence_dist[confidence] += 1
        
        for s in secondary:
            if isinstance(s, str):
                secondary_counts[s] += 1
                total_counts[s] += 1
                cooccurrence[primary][s] += 1
                # Track pairs
                pair = tuple(sorted([primary, s]))
                pattern_pairs[pair] += 1
        
        by_conference[paper["conference"]][primary] += 1
        by_year[paper["year"]][primary] += 1
        by_type[paper["presentation_type"]][primary] += 1
        by_conf_year[f"{paper['conference']}-{paper['year']}"][primary] += 1
    
    pattern_names = {p["id"]: p["name"] for p in taxonomy}
    pattern_categories = {p["id"]: p.get("category", "Unknown") for p in taxonomy}
    
    return {
        "total_papers": len(papers),
        "primary_pattern_counts": dict(primary_counts),
        "secondary_pattern_counts": dict(secondary_counts),
        "total_pattern_counts": dict(total_counts),
        "by_conference": {k: dict(v) for k, v in by_conference.items()},
        "by_year": {k: dict(v) for k, v in by_year.items()},
        "by_presentation_type": {k: dict(v) for k, v in by_type.items()},
        "by_conf_year": {k: dict(v) for k, v in by_conf_year.items()},
        "cooccurrence": {k: dict(v) for k, v in cooccurrence.items()},
        "pattern_pairs": {str(k): v for k, v in sorted(pattern_pairs.items(), key=lambda x: x[1], reverse=True)[:30]},
        "confidence_distribution": dict(confidence_dist),
        "pattern_names": pattern_names,
        "pattern_categories": pattern_categories
    }


def generate_deep_insights(taxonomy: List[Dict], analysis: Dict, papers: List[Dict]) -> str:
    """Generate comprehensive deep insights."""
    
    # Prepare data summaries
    total = analysis["total_papers"]
    
    # Top patterns with percentages
    sorted_primary = sorted(analysis["primary_pattern_counts"].items(), key=lambda x: x[1], reverse=True)
    top_patterns_text = "\n".join([
        f"  {i+1}. {analysis['pattern_names'].get(pid, pid)}: {count} ({count/total*100:.1f}%)"
        for i, (pid, count) in enumerate(sorted_primary[:15])
    ])
    
    # Year trends
    year_data = {}
    for year in sorted(analysis["by_year"].keys()):
        year_total = sum(analysis["by_year"][year].values())
        year_data[year] = {
            "total": year_total,
            "top_patterns": sorted(analysis["by_year"][year].items(), key=lambda x: x[1], reverse=True)[:5]
        }
    
    year_trends_text = ""
    for year, data in year_data.items():
        top = [(analysis["pattern_names"].get(p, p), c, c/data["total"]*100) for p, c in data["top_patterns"]]
        year_trends_text += f"\n  {year} ({data['total']} papers):\n"
        for name, count, pct in top:
            year_trends_text += f"    - {name}: {pct:.1f}%\n"
    
    # Conference comparison
    conf_data = {}
    for conf in sorted(analysis["by_conference"].keys()):
        conf_total = sum(analysis["by_conference"][conf].values())
        conf_data[conf] = {
            "total": conf_total,
            "top_patterns": sorted(analysis["by_conference"][conf].items(), key=lambda x: x[1], reverse=True)[:5]
        }
    
    conf_text = ""
    for conf, data in conf_data.items():
        top = [(analysis["pattern_names"].get(p, p), c/data["total"]*100) for p, c in data["top_patterns"]]
        conf_text += f"\n  {conf} ({data['total']} papers):\n"
        for name, pct in top:
            conf_text += f"    - {name}: {pct:.1f}%\n"
    
    # Oral vs Spotlight
    type_data = {}
    for ptype in analysis["by_presentation_type"]:
        type_total = sum(analysis["by_presentation_type"][ptype].values())
        type_data[ptype] = {
            "total": type_total,
            "patterns": {p: c/type_total*100 for p, c in analysis["by_presentation_type"][ptype].items()}
        }
    
    # Top co-occurring pairs
    pairs_text = "\n".join([
        f"  - {analysis['pattern_names'].get(eval(pair)[0], eval(pair)[0])} + {analysis['pattern_names'].get(eval(pair)[1], eval(pair)[1])}: {count}"
        for pair, count in list(analysis["pattern_pairs"].items())[:15]
    ])
    
    # Sample papers for each top pattern
    examples_by_pattern = defaultdict(list)
    for p in papers:
        primary = p.get("classification", {}).get("primary_pattern", "unknown")
        if len(examples_by_pattern[primary]) < 3:
            examples_by_pattern[primary].append(p["title"][:60])
    
    examples_text = ""
    for pid, _ in sorted_primary[:10]:
        examples = examples_by_pattern.get(pid, [])
        examples_text += f"\n  {analysis['pattern_names'].get(pid, pid)}:\n"
        for ex in examples[:2]:
            examples_text += f"    - {ex}...\n"
    
    system_prompt = """You are a research strategist analyzing thinking patterns in top ML research. Provide deep, actionable insights that would help researchers understand how breakthrough ideas emerge and how to cultivate effective research thinking."""

    user_prompt = f"""I analyzed {total} top ML papers (NeurIPS, ICML, ICLR oral/spotlight 2023-2025) and classified them by thinking patterns.

## PATTERN FREQUENCY (Primary Pattern)
{top_patterns_text}

## YEAR-BY-YEAR TRENDS
{year_trends_text}

## CONFERENCE COMPARISON
{conf_text}

## ORAL vs SPOTLIGHT
Oral papers: {type_data.get('oral', {}).get('total', 0)}
Spotlight papers: {type_data.get('spotlight', {}).get('total', 0)}

## TOP CO-OCCURRING PATTERN PAIRS
{pairs_text}

## EXAMPLE PAPERS BY PATTERN
{examples_text}

## TAXONOMY CATEGORIES
{json.dumps([{"name": c["name"], "patterns": c["pattern_ids"]} for c in taxonomy_data.get("categories", [])], indent=2)}

---

Please provide a COMPREHENSIVE ANALYSIS with the following sections:

1. **EXECUTIVE SUMMARY** (3-4 key takeaways)

2. **PATTERN LANDSCAPE ANALYSIS**
   - What do the most common patterns reveal about ML research?
   - What makes certain patterns more prevalent?
   - Are there underutilized patterns that might represent opportunities?

3. **TEMPORAL EVOLUTION (2023 → 2024 → 2025)**
   - How is ML research thinking evolving?
   - What patterns are rising or declining?
   - What does this suggest about the field's direction?

4. **CONFERENCE CULTURE ANALYSIS**
   - Do NeurIPS, ICML, and ICLR favor different thinking styles?
   - What might explain any differences?
   - Implications for paper submission strategy?

5. **ORAL vs SPOTLIGHT INSIGHTS**
   - Do oral papers show different pattern distributions?
   - What thinking patterns correlate with highest-impact work?

6. **POWERFUL PATTERN COMBINATIONS**
   - Which patterns frequently co-occur?
   - What "thinking recipes" emerge from the data?
   - How can researchers deliberately combine patterns?

7. **ACTIONABLE ADVICE FOR RESEARCHERS**
   - For PhD students starting research
   - For experienced researchers seeking impact
   - For industry researchers vs academic researchers

8. **META-INSIGHTS ABOUT ML INNOVATION**
   - What does this analysis reveal about how ML progress happens?
   - What are the "meta-patterns" of successful research?
   - Predictions for future research directions

Be specific, cite the data, and make recommendations concrete and actionable."""

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
    return call_gpt(messages)


def main():
    print("=" * 60)
    print("ANALYSIS AND DEEP INSIGHTS")
    print("=" * 60)
    
    # Load data
    print("\nLoading data...")
    with open(OUTPUT_PATH / "pattern_taxonomy.json") as f:
        global taxonomy_data
        taxonomy_data = json.load(f)
    taxonomy = taxonomy_data.get("taxonomy", [])
    
    with open(OUTPUT_PATH / "classified_papers.json") as f:
        papers = json.load(f)
    
    print(f"  Loaded {len(papers)} classified papers")
    print(f"  Taxonomy has {len(taxonomy)} patterns")
    
    # Run analysis
    print("\nAnalyzing results...")
    analysis = analyze_results(papers, taxonomy)
    
    with open(OUTPUT_PATH / "analysis_results.json", "w") as f:
        json.dump(analysis, f, indent=2)
    
    # Print summary
    print(f"\n{'='*60}")
    print("RESULTS SUMMARY")
    print('='*60)
    
    print(f"\nTotal papers: {analysis['total_papers']}")
    
    print("\nTOP 15 PRIMARY PATTERNS:")
    sorted_patterns = sorted(analysis["primary_pattern_counts"].items(), key=lambda x: x[1], reverse=True)
    for rank, (pid, count) in enumerate(sorted_patterns[:15], 1):
        name = analysis["pattern_names"].get(pid, pid)
        pct = count / analysis["total_papers"] * 100
        print(f"  {rank:2}. {pid} {name}: {count} ({pct:.1f}%)")
    
    print("\nBY YEAR:")
    for year in sorted(analysis["by_year"].keys()):
        total = sum(analysis["by_year"][year].values())
        top = max(analysis["by_year"][year].items(), key=lambda x: x[1])
        print(f"  {year}: {total} papers | Top: {analysis['pattern_names'].get(top[0], top[0])}")
    
    print("\nBY CONFERENCE:")
    for conf in sorted(analysis["by_conference"].keys()):
        total = sum(analysis["by_conference"][conf].values())
        top = max(analysis["by_conference"][conf].items(), key=lambda x: x[1])
        print(f"  {conf}: {total} papers | Top: {analysis['pattern_names'].get(top[0], top[0])}")
    
    print("\nCONFIDENCE DISTRIBUTION:")
    for conf, count in sorted(analysis["confidence_distribution"].items()):
        print(f"  {conf}: {count} ({count/analysis['total_papers']*100:.1f}%)")
    
    # Generate deep insights
    print("\n" + "="*60)
    print("GENERATING DEEP INSIGHTS...")
    print("="*60)
    
    insights = generate_deep_insights(taxonomy, analysis, papers)
    
    # Save insights
    with open(OUTPUT_PATH / "deep_insights.md", "w") as f:
        f.write("# Deep Insights: Thinking Patterns in Top ML Research (2023-2025)\n\n")
        f.write(f"*Analysis of {analysis['total_papers']} papers from NeurIPS, ICML, ICLR (oral & spotlight)*\n\n")
        f.write("---\n\n")
        f.write(insights)
    
    print("\n✓ Deep insights saved to deep_insights.md")
    
    # Save combined report data
    report_data = {
        "analysis": analysis,
        "taxonomy": taxonomy,
        "insights_text": insights
    }
    with open(OUTPUT_PATH / "full_report_data.json", "w") as f:
        json.dump(report_data, f, indent=2)
    
    # Cost summary
    print(f"\nAnalysis API cost: ${cost_tracker.get_total_cost():.4f}")
    
    return analysis, insights


if __name__ == "__main__":
    main()

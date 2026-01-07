# Prior Work Extraction Pipeline - Final Report

## Executive Summary

This report summarizes the results of the Prior Work Extraction Pipeline, which analyzed **3,451 high-quality AI research papers** from top-tier machine learning conferences (ICLR, ICML, NeurIPS) spanning 2023-2025. For each paper, the pipeline identified key prior works that directly influenced the paper's core innovation and documented their relationships.

**Key Metrics:**
- **Total Papers Analyzed:** 3,451
- **Success Rate:** 100%
- **Conferences Covered:** 8 conference-years
- **Model Used:** GPT-5
- **Processing Method:** OpenAI Batch API (50% cost savings)

---

## Dataset Overview

### Papers by Conference

| Conference | Year | Papers | Type |
|------------|------|--------|------|
| ICLR | 2024 | 453 | Oral/Spotlight |
| ICLR | 2025 | 593 | Oral/Spotlight |
| ICML | 2023 | 155 | Oral/Spotlight |
| ICML | 2024 | 335 | Oral/Spotlight |
| ICML | 2025 | 319 | Oral/Spotlight |
| NeurIPS | 2023 | 445 | Oral/Spotlight |
| NeurIPS | 2024 | 387 | Oral/Spotlight |
| NeurIPS | 2025 | 764 | Oral/Spotlight |
| **Total** | | **3,451** | |

### Distribution by Conference

```
NeurIPS 2025  ████████████████████████████████  764 (22.1%)
ICLR 2025     ███████████████████              593 (17.2%)
ICLR 2024     ██████████████                   453 (13.1%)
NeurIPS 2023  ██████████████                   445 (12.9%)
NeurIPS 2024  ████████████                     387 (11.2%)
ICML 2024     ██████████                       335 (9.7%)
ICML 2025     ██████████                       319 (9.2%)
ICML 2023     █████                            155 (4.5%)
```

---

## Analysis Methodology

### Prior Work Identification Criteria

The pipeline identifies **5-7 prior works** per paper that meet the following criteria:

1. **Direct Intellectual Lineage** - Papers that directly contributed to the core innovation
2. **Specific Contributions** - Papers with identifiable techniques, insights, or methods that were adopted
3. **Explicit Influence** - Papers cited as primary influences in the introduction or related work

### Role Classifications

Each prior work is assigned one of six roles:

| Role | Description | Icon |
|------|-------------|------|
| **Foundation** | Introduced core problem formulation, dataset, or theoretical framework | 🏗️ |
| **Inspiration** | Specific idea/approach that sparked the key innovation | 💡 |
| **Gap Identification** | Limitations that motivated the research direction | 🔍 |
| **Baseline** | Primary system/method being improved upon | 📊 |
| **Extension** | Method directly extended or modified | 🔧 |
| **Related Problem** | Similar problem with transferable solution approach | 🔗 |

### Exclusion Criteria

The following are explicitly excluded:
- Generic infrastructure/tools (PyTorch, CUDA, etc.)
- Complementary optimizations orthogonal to main contribution
- Standard baselines without deeper connection
- Well-known foundational works cited universally

---

## Output Structure

### Directory Organization

```
results/organized/
├── ICLR_2024/           # 453 papers
│   ├── {paper_id}.json  # Structured analysis
│   └── {paper_id}.md    # Markdown report
├── ICLR_2025/           # 593 papers
├── ICML_2023/           # 155 papers
├── ICML_2024/           # 335 papers
├── ICML_2025/           # 319 papers
├── NeurIPS_2023/        # 445 papers
├── NeurIPS_2024/        # 387 papers
├── NeurIPS_2025/        # 764 papers
└── REPORT.md            # This report
```

### Output Format

#### JSON Structure
```json
{
  "prior_works": [
    {
      "title": "Paper Title",
      "authors": "First Author et al.",
      "year": 2023,
      "role": "Foundation|Inspiration|Gap Identification|Baseline|Extension|Related Problem",
      "relationship_sentence": "Specific connection to current paper's innovation"
    }
  ],
  "synthesis_narrative": "200-300 word narrative explaining how prior works collectively led to this paper",
  "target_paper": {
    "title": "...",
    "authors": "...",
    "conference": "...",
    "year": "...",
    "abstract": "..."
  },
  "analysis_timestamp": "ISO timestamp"
}
```

#### Markdown Report
Each paper has a corresponding `.md` file with:
- Target paper metadata
- Prior works grouped by role with relationship descriptions
- Synthesis narrative

---

## Pipeline Technical Details

### Architecture

1. **Data Source:** OpenReview oral/spotlight papers from ICLR, ICML, NeurIPS (2023-2025)
2. **Analysis Engine:** GPT-5 via OpenAI API
3. **Processing:** Batch API for efficiency and cost savings
4. **Checkpointing:** Automatic resume capability with deduplication

### Processing Statistics

| Metric | Value |
|--------|-------|
| Total API Calls | ~3,500 |
| Batch Jobs | 19 |
| Processing Time | ~3 hours |
| Cost Savings | 50% (via Batch API) |

### Key Features

- **Retry Mechanism:** Exponential backoff for rate limits
- **Deduplication:** Checkpoint tracking prevents duplicate processing
- **Parallel Processing:** Multiple batches processed concurrently
- **Quality Focus:** Prompt engineered for direct intellectual lineage

---

## Sample Outputs

### Example 1: LLM Systems Paper

**Paper:** "Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services"

**Prior Works Identified:**
- 🏗️ **Pensieve** (2017) - QoE formulation from video streaming
- 💡 **BOLA** (2016) - Marginal utility view for resource allocation
- 📊 **vLLM** (2023) - Continuous batching baseline
- 📊 **SGLang** (2024) - High-performance serving baseline
- 🔍 **InferLine** (2020) - SLO vs QoE gap identification
- 🔗 **Size-Based Scheduling** (2003) - Preemptive scheduling insights

### Example 2: Transformer Architecture Paper

**Paper:** "Attention Is All You Need" style analysis would identify:
- 🏗️ Sequence-to-sequence foundations
- 💡 Attention mechanism inspirations
- 🔍 RNN/LSTM limitations addressed
- 📊 Neural machine translation baselines

---

## Usage Guide

### Accessing Results

```python
import json
from pathlib import Path

# Load a specific paper's analysis
paper_id = "abc123"
conference = "ICLR_2024"

with open(f"results/organized/{conference}/{paper_id}.json") as f:
    analysis = json.load(f)

# Access prior works
for pw in analysis["prior_works"]:
    print(f"{pw['role']}: {pw['title']} ({pw['year']})")
    print(f"  Connection: {pw['relationship_sentence']}")

# Read synthesis narrative
print(analysis["synthesis_narrative"])
```

### Bulk Analysis

```python
from pathlib import Path
import json
from collections import Counter

# Analyze role distribution across all papers
role_counts = Counter()

for conf_dir in Path("results/organized").iterdir():
    if conf_dir.is_dir():
        for json_file in conf_dir.glob("*.json"):
            with open(json_file) as f:
                analysis = json.load(f)
            for pw in analysis.get("prior_works", []):
                role_counts[pw.get("role", "Unknown")] += 1

print("Role Distribution:")
for role, count in role_counts.most_common():
    print(f"  {role}: {count}")
```

---

## Limitations & Considerations

1. **Abstract-Only Analysis:** Full paper PDFs were not available; analysis based on title, abstract, and keywords
2. **Model Knowledge Cutoff:** GPT-5's training data may not include the most recent papers
3. **Citation Inference:** Prior works are inferred from content, not extracted from actual citations
4. **Subjective Classification:** Role assignments involve judgment calls

---

## Future Improvements

1. **PDF Integration:** Extract full paper text for deeper analysis
2. **Citation Verification:** Cross-reference with actual paper citations
3. **Graph Construction:** Build citation/influence graphs across papers
4. **Trend Analysis:** Identify emerging research directions from prior work patterns

---

## Conclusion

The Prior Work Extraction Pipeline successfully analyzed 3,451 high-quality AI research papers, identifying the intellectual lineage and key influences for each. The structured output enables:

- **Literature Review:** Quickly understand a paper's research context
- **Trend Analysis:** Identify influential works across the field
- **Research Planning:** Discover gaps and opportunities
- **Knowledge Graphs:** Build paper relationship networks

All results are organized by conference and year, with both structured JSON and readable Markdown formats.

---

*Report Generated: 2026-01-07*
*Pipeline Version: 2.0 (Batch API)*

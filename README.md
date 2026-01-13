# Sci-Reasoning: A Dataset Decoding AI Innovation Patterns

[![arXiv](https://img.shields.io/badge/arXiv-2601.04577-b31b1b.svg)](https://arxiv.org/abs/2601.04577v1)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/AmberLJC/Sci-Reasoning)
[![Blog](https://img.shields.io/badge/Blog-Post-blue)](https://www.orchestra-research.com/perspectives/sci-reasoning-story)
[![Platform](https://img.shields.io/badge/Platform-Orchestra-purple)](https://www.orchestra-research.com/)

A dataset capturing the structured intellectual synthesis behind high-quality AI research.

## Overview

**Sci-Reasoning** is the first dataset designed to capture reasoning patterns behind AI breakthroughs in a structured format.

- **3,819 papers** (999 Oral, 2,820 Spotlight) from NeurIPS, ICML, and ICLR (2023-2025)
- **Structured Lineage Graphs** capturing intellectual predecessors and relationships
- **15 Distinct Thinking Patterns** identified through systematic analysis

## Repository Structure

```
sci-reasoning/
├── ml_paper_acquisition/           # Stage 1: Paper Collection
│   └── code/
│       ├── extract_papers.py
│       └── generate_report.py
│
├── prior_work_extraction/          # Stage 2: Lineage Tracing
│   └── code/
│       ├── prior_work_pipeline.py
│       └── batch_api_processor.py
│
├── thinking_patterns_llm_analysis/ # Stage 3: Pattern Analysis
│   └── code/
│       ├── pattern_analyzer.py
│       ├── classify_all.py
│       └── visualize.py
│
├── research_idea_evaluation/       # Stage 4: LLM Evaluation
│   └── code/
│       ├── evaluate_idea_generation_v4_exa_improved.py
│       ├── evaluate_claude_sonnet.py
│       └── evaluate_gemini_pro.py
│
└── paper.pdf
```

## Dataset Schema

```json
{
  "target_paper": { "title": "...", "venue": "...", "year": 2024 },
  "intellectual_predecessors": [
    {
      "title": "Predecessor title",
      "role": "BASELINE|INSPIRATION|GAP_IDENTIFICATION|FOUNDATION",
      "relationship_type": "EXTENDS|COMBINES_WITH|ADDRESSES_LIMITATION_OF"
    }
  ],
  "synthesis_narrative": "...",
  "primary_pattern": "Gap-Driven Reframing",
  "secondary_pattern": "Representation Shift"
}
```

## Innovation Patterns

| Pattern | % | Description |
|---------|---|-------------|
| Gap-Driven Reframing | 24.2 | Reframing problems to map onto better-suited methods |
| Cross-Domain Synthesis | 18.0 | Importing ideas from other fields |
| Representation Shift | 10.5 | Replacing primitives to simplify the problem |

## Citation

```bibtex
@article{liu2025scireasoning,
  title={Sci-Reasoning: A Dataset Decoding AI Innovation Patterns},
  author={Liu, Jiachen and Harmon, Maestro and Zhang, Zechen},
  year={2025}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.

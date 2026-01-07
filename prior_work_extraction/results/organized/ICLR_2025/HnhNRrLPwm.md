# Prior Work Analysis Report

## Target Paper
**Title:** HnhNRrLPwm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MMIE’s core contribution—a large-scale, knowledge-intensive benchmark that evaluates interleaved multimodal comprehension and generation with both multiple-choice and open-ended formats—emerges from two converging lines of prior work. On the modeling side, Flamingo established the interleaved image–text paradigm, and IDEFICS open-sourced this capability, making multi-image, multi-turn interleaving common in practice. LLaVA further pushed conversational, instruction-following LVLMs and popularized open-ended evaluation with LLM-as-judge, which revealed practical concerns about grading cost and bias.

On the benchmarking side, MMBench demonstrated the value of fine-grained, taxonomy-driven multiple-choice evaluation for reliability and comparability, while MMMU showed that broad, academically grounded, knowledge-intensive tasks are crucial for holistic assessment. Complementing these, MM-Vet highlighted open-ended capability testing and the pitfalls of automated judging, and MathVista exemplified rigorous domain-specific reasoning in visual contexts.

MMIE synthesizes these strands: it centers explicitly on interleaved input/output scenarios born from Flamingo/IDEFICS-style modeling; adopts MMBench/MMMU’s breadth and structure to cover many disciplines and subfields; and incorporates both MC and open-ended formats, informed by LLaVA-Bench and MM-Vet, while improving evaluation reliability and cost. The result is a benchmark that simultaneously captures the practical interleaved use cases of modern LVLMs and the depth of knowledge-intensive reasoning demanded by real-world applications.

---
*Generated: 2026-01-06T23:42:48.092076*

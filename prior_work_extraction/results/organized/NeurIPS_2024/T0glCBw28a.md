# Prior Work Analysis Report

## Target Paper
**Title:** T0glCBw28a
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ALCHEmist’s core idea—replace repeated LLM annotations with LLM-generated, reusable labeling programs—stands squarely on the foundations of programmatic weak supervision and recent advances in LM-driven program synthesis. Data Programming introduced labeling functions and label models as a way to supervise models without manual instance-level labels, and Snorkel systematized this workflow for practical use, emphasizing reusability, auditable heuristics, and label aggregation. Snuba took the next step by automating labeling function generation, demonstrating that LF creation itself can be algorithmically assisted; ALCHEmist extends this automation by using modern LLMs to synthesize executable labeling code tailored to tasks. BabbleLabble connected natural language to labeling functions, showing that high-level descriptions can be translated into operational supervision, a conversion ALCHEmist performs with LLMs to produce concrete, auditable programs. Tooling such as skweak reinforced the viability of rule-based, locally executable pipelines with aggregation, properties ALCHEmist seeks to preserve while drastically reducing cost. On the modeling side, PAL established that LMs can reliably produce and delegate to external code for improved performance and efficiency—a paradigm ALCHEmist applies to the labeling problem. Finally, the LLM-as-a-Judge line provided an immediate baseline and motivation: while direct LLM annotation is effective, it is costly and hard to audit; ALCHEmist’s program-generation approach achieves comparable or better quality while delivering orders-of-magnitude cost savings and persistent, inspectable labelers.

---
*Generated: 2026-01-06T23:33:35.562344*

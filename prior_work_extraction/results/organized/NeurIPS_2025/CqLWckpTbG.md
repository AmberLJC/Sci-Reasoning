# Prior Work Analysis Report

## Target Paper
**Title:** CqLWckpTbG
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DeepDiver’s core idea—Search Intensity Scaling (SIS) learned via reinforcement learning to adaptively escalate web-search frequency and depth—sits at the intersection of three lines of prior work: browser-based QA with RL, reasoning–tool interleaving, and adaptive computation. WebGPT pioneered reinforcement learning over a browser environment with citation-sensitive rewards, demonstrating that RL can govern open-web actions for QA. Building on this, ReAct provided the control structure to interleave reasoning and tool use, enabling policies that decide when to think versus act, while Self-Ask showed that complex questions benefit from iterative decomposition and repeated search calls when single-shot retrieval is inadequate.
Self-RAG advanced this further by learning retrieval scheduling and critique loops, offering a template for verifiability-driven decision gates—precisely the kind of learned trigger DeepDiver needs to scale search intensity under uncertainty. Reflexion contributed the idea that agents should use reflective feedback from prior steps to guide future exploration, which naturally supports DeepDiver’s decision to deepen searches after weak or unsupported intermediate findings. Complementing these, Adaptive Computation Time gave the foundational principle for dynamically allocating computational steps—transposed here into dynamically allocating web-search steps. Finally, Toolformer’s demonstration that models can learn when to invoke external tools informs DeepDiver’s calibrated action-space for live web queries. Together, these works directly enable DeepDiver’s RL-trained policy that adaptively increases search depth and frequency on the live internet, moving beyond fixed prompts or static SFT corpora.

---
*Generated: 2026-01-07T00:21:32.244552*

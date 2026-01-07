# Prior Work Analysis Report

## Target Paper
**Title:** neZSGqhxDa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Absolute Zero fuses three lines of prior work into a single, closed-loop framework: (1) tabula rasa self-play, (2) autonomous curriculum via learning progress, and (3) reinforcement learning with verifiable rewards (RLVR). AlphaZero provided the core blueprint that strong policies can emerge without human data through self-play. PowerPlay, ALP-GMM, and POET supplied the missing ingredient for open-ended domains: a mechanism to autonomously propose tasks at the competence frontier, using learning progress as the driving signal and co-evolving the problem distribution with the solver. In parallel, Self-Instruct and STaR showed that language models can bootstrap from their own outputs—generating tasks or rationales and using verifiable end signals (correct final answers) to filter supervision—reducing reliance on human-labeled data.

Absolute Zero integrates these insights and replaces supervised filtering with RLVR: rule-based outcome checks act as rewards, akin to execution feedback in CodeRL, allowing the system to optimize directly for correctness. The result is a self-contained loop where a single model proposes tasks to maximize its learning progress, solves them under verifiable rewards, and improves without any externally curated Q&A. This synthesis bridges game-centric self-play with LLM reasoning, grounding task generation in measurable learning progress and using programmatic verification to stably train beyond the limitations of human-provided datasets.

---
*Generated: 2026-01-07T00:21:32.315835*

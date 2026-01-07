# Prior Work Analysis Report

## Target Paper
**Title:** 2xTkeyJFJb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

GR^2 directly extends the encoder–decoder paradigm for generative retrieval introduced by DSI, where a model learns to map queries to document identifiers under a sequence likelihood objective. While DSI established the feasibility and benefits of generating docids, GR^2 addresses two shortcomings left open in that line: dependence on binary supervision and instability from identifier conflicts. GENRE’s success in generating semantically meaningful identifiers for entities motivates GR^2’s first pillar—learning identifiers that are both semantically aligned with content and sufficiently distinct to avoid collisions and ambiguity at inference.
At the training-objective level, GR^2 imports decades of graded relevance reasoning from classic learning-to-rank. nDCG (Järvelin & Kekäläinen) provides the grading semantics and evaluation target, while LambdaRank/LambdaMART contributes the key insight that pairwise/listwise gradients should be proportional to gains induced by relevance differences. GR^2 operationalizes this inside a generative likelihood framework via a grade-aware constrained contrastive objective.
Methodologically, the contrastive backbone inherits from InfoNCE and its supervised extension (SupCon), enabling multiple positives per query; GR^2 augments these with relevance-grade–conditioned weights and constraints. Finally, principles from margin-aware metric learning (e.g., Circle Loss) inspire the model’s repulsive forces that enforce identifier distinctness, mitigating docid collisions noted in generative indexers. Together, these threads yield a generative retriever that natively models multi-graded relevance while ensuring identifiers are both informative and uniquely assigned.

---
*Generated: 2026-01-06T23:33:35.571922*

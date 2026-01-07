# Prior Work Analysis Report

## Target Paper
**Title:** 0A9f2jZDGW
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution—showing that task arithmetic improves when models are edited in their tangent space and that weight disentanglement underlies its effectiveness—builds directly upon two intertwined threads: weight-space composition and linearized training. Ilharco et al.’s task arithmetic crystallized the empirical fact that adding or subtracting task-specific deltas can compose or erase capabilities, while model soups and mode connectivity established that simple linear operations in parameter space can preserve and even enhance function. These empirical precedents suggest a latent linear structure in pre-trained networks that the NeurIPS 2023 paper seeks to explain through disentangled directions in weight space.

The theoretical machinery enabling this explanation comes from the Neural Tangent Kernel and subsequent work showing that wide networks evolve as linear models under gradient descent. By adopting a linearization around pre-trained weights, the paper effectively treats fine-tuning as optimization in a fixed tangent feature space, which both clarifies and strengthens disentanglement: task updates align with approximately orthogonal Jacobian features, reducing interference and boosting arithmetic performance. ROME complements this perspective by demonstrating that Jacobian-based, locally linear edits can target functions while limiting collateral changes, reinforcing the merits of operating in tangent space for controlled model editing. Finally, CLIP provides the practical substrate: large, pre-trained vision-language models where pretraining induces the emergent disentanglement the paper measures and exploits. Together, these works motivate and technically ground the shift from naive weight addition to principled tangent-space editing for robust task arithmetic.

---
*Generated: 2026-01-07T00:02:04.819757*

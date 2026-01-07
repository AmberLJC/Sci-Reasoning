# Prior Work Analysis Report

## Target Paper
**Title:** dheDf5EpBT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper situates its key contribution—unifying gradient-based machine unlearning as a steepest-descent problem in output KL space and enhancing it with remaining-data geometry—at the confluence of unlearning, influence analysis, and information geometry. Foundationally, Cao and Yang (2015) and Bourtoule et al. (2021) establish the unlearning objective and the practical reference of exact retraining on remaining data. This work makes that reference explicit by minimizing the output KL divergence to exact MU within a local parameter neighborhood, yielding a principled steepest-descent direction that decomposes into a forgetting gradient, a retaining gradient, and a weight saliency matrix.

Golatkar et al. (CVPR’20; NeurIPS’20) directly motivate both the decomposition and its geometry: they show how Fisher/Hessian structure and KL considerations enable selective forgetting while protecting retained knowledge, foreshadowing the present paper’s unification of many gradient-based MU methods under an Euclidean metric. Koh and Liang’s influence functions provide the local, first/second-order lens for approximating the effect of removing data points, aligning with the paper’s parameter-neighborhood optimization.

The paper’s core advance is to move beyond Euclidean updates to manifold-aware updates, drawing on Amari’s natural gradient to align steps with the geometry of output distributions. By instantiating curvature from the remaining-data Hessian/Fisher—conceptually akin to EWC’s Fisher-based saliency to prevent interference—the method steers updates along directions that maximally forget while safeguarding performance on the remaining data, thereby improving iterative unlearning trajectories.

---
*Generated: 2026-01-06T23:42:49.036055*

# Prior Work Analysis Report

## Target Paper
**Title:** eTHawKFT4h
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—establishing a rigorous link between deep ensembles and (variational) Bayesian methods by reformulating neural training as convex optimization over probability measures and analyzing it via Wasserstein gradient flows—rests on three intellectual pillars. First, empirical and methodological motivation comes from deep ensembles (Lakshminarayanan et al.), whose strong uncertainty estimates needed a principled Bayesian explanation, and from parametric variational Bayes for neural nets (Blundell et al.), which provides the contrasting baseline that the present work seeks to subsume and, in some regimes, surpass.
Second, the mathematical machinery arises from the optimal transport and gradient-flow literature. The JKO framework (Jordan–Kinderlehrer–Otto) establishes KL-driven dynamics as Wasserstein gradient flows, enabling the authors to cast generalized VI objectives as flows on probability measures. The optimal-transport viewpoint on neural network training (Chizat & Bach) and the mean-field PDE perspective for parameter distributions (Mei–Montanari–Nguyen) supply the precise measure-space representation and convexification tools that make the nonconvex parameter problem tractable in distribution space.
Third, particle-based variational inference links these ideas to practical ensemble procedures. SVGD (Liu & Wang) shows how interacting particles can deterministically follow a variational objective, directly inspiring the paper’s interpretation of deep ensembles as interacting particle systems and its derivation of new ensemble dynamics with convergence guarantees. Finally, generalized VI objectives (Li & Turner’s Rényi VI) situate the analysis beyond KL, allowing the authors to unify ensembles with a broad class of Bayesian and variational methods within a single Wasserstein-flow framework.

---
*Generated: 2026-01-06T23:42:49.135453*

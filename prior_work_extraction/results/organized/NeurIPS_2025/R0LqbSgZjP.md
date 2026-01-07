# Prior Work Analysis Report

## Target Paper
**Title:** R0LqbSgZjP
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—a unified framework to measure and control solution degeneracy across behavior, neural dynamics, and weight space—stands on three converging lines of prior work. First, the dynamical-systems program for task-trained RNNs, inaugurated by Sussillo and Barak, established fixed-point analysis and low-dimensional manifolds as the language for mechanistic interpretation, enabling principled comparisons of internal dynamics across independently trained models. Complementing this, Yang et al. showed that RNNs trained on neuroscience tasks can achieve similar behavior with different internal solutions, motivating the need to quantify degeneracy beyond single exemplars. Second, representational-comparison methods such as CKA (Kornblith et al.) furnish robust metrics for cross-network similarity, which this paper adapts to the neural-dynamics level to separate shared computations from divergent implementations. The mapping from connectivity to dynamics developed by Mastrogiuseppe and Ostojic links weight structure to dynamical motifs, guiding the paper’s cross-level metrics and its use of structural/regularization controls. Third, weight-space geometry—via mode connectivity (Garipov et al.) and permutation-aware re-basinning (Ainsworth et al.)—demonstrates that many apparent minima are connected or symmetry-related, informing the paper’s permutation-aware weight comparisons and interpretation of degeneracy in parameter space. Finally, theory distinguishing lazy from feature-learning regimes (Chizat & Bach) underpins the paper’s interventions showing how task complexity and feature learning reduce degeneracy in neural dynamics yet increase it in weight space. Together, these works directly enable a scalable, cross-level quantification and control of solution degeneracy in task-trained RNNs.

---
*Generated: 2026-01-07T00:21:32.254461*

# Prior Work Analysis Report

## Target Paper
**Title:** RF3miSqdXa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—characterizing and empirically validating linear mode connectivity (LMC) in Mixture-of-Experts (MoE) architectures by explicitly accounting for expert and gate permutations—sits at the intersection of two lines of work: mode connectivity in standard networks and the architectural symmetries of MoE. Foundational LMC studies by Garipov et al. and Draxler et al. established that seemingly isolated minima can be connected by low-loss paths, setting the methodological blueprint for probing connectivity via linear or simple curves in parameter space. Frankle et al. further clarified when LMC emerges across training runs, informing the paper’s experimental design (e.g., independence of runs, initialization, and training protocol controls).
On the architectural side, Jacobs et al.’s original MoE formulation defines gating and expert exchangeability, making clear that permutations of experts (and their associated gating parameters) are intrinsic symmetries—precisely the invariances the paper formalizes for MoE LMC. Modern scalable MoE implementations by Shazeer et al. (sparsely gated MoE) and Fedus et al. (Switch Transformers) supply the concrete sparse and extreme-sparse routing regimes the authors analyze, highlighting practical training dynamics and permutation structure at scale. Finally, Wortsman et al.’s model soups demonstrate the practical benefits of weight-space interpolation and suggest that achieving low-loss linear combinations in complex models is useful for ensembling—providing motivation to resolve permutation symmetries in MoE so that interpolation (and thus LMC) is realized in practice for both dense and sparse gating cases.

---
*Generated: 2026-01-07T00:05:12.541572*

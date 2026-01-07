# Prior Work Analysis Report

## Target Paper
**Title:** KurYdcCbjv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—generalizing linear mode connectivity (LMC) by unifying permutations, semi-permutations, orthogonal transformations, and general invertible maps—emerges from two intertwined lines of prior work. First, Garipov et al. and Draxler et al. established that independently trained networks often lie on connected low-loss manifolds, catalyzing the search for mechanisms that render these paths simple and, ideally, linear. Subsequent work identified hidden symmetries as the culprit obscuring linear paths. Entezari et al. demonstrated that neuron permutations alone can reconcile many apparent discrepancies and recover linear connectors, while Ainsworth et al.’s Git Re-Basin operationalized this idea with practical neuron-matching to merge models. However, both are limited to permutation invariances.
Second, representation-similarity and function-preservation studies expanded the symmetry lens. SVCCA showed that representations are comparable up to invertible linear transforms, naturally suggesting orthogonal and more general linear reparameterizations as function-preserving symmetries. Net2Net formalized function-preserving mappings (including permutations and linear maps) across layers, offering a constructive view of reparameterization equivalences.
In Transformers specifically, Matena and Raffel revealed that naive weight-space averaging is fragile—often failing without proper alignment—highlighting richer symmetries (e.g., head reindexing, basis rotations within subspaces, and scale/normalization effects). Building on these insights, the present work codifies a unified symmetry framework—permutations through general invertible maps—that subsumes prior alignment methods and exposes linear, low-barrier connectors between independently trained Transformers, thereby generalizing LMC to modern architectures.

---
*Generated: 2026-01-06T23:42:48.105837*

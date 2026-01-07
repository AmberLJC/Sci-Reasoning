# Prior Work Analysis Report

## Target Paper
**Title:** wBJIO15pBV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core idea—formalizing a continuous rotation symmetry in transformer parameter space and leveraging it for optimal parameter matching in model fusion—builds on two intertwined threads: symmetry-aware model alignment and representational equivalences up to orthogonal transforms. Early evidence that distinct solutions are connectable in weight space (Garipov et al.; Frankle et al.) motivated reparameterizations that make models compatible for interpolation or fusion. Concrete mechanisms appeared with Git Re-Basin, which aligned neurons via permutations to merge models, but its discrete symmetry is often brittle for transformers with structured self-attention. In parallel, representation-similarity work (SVCCA, CKA) showed that learned features across networks are frequently equivalent up to orthogonal transformations—crucially, transformations that preserve inner products. Since dot-product self-attention depends only on inner products of queries and keys, these results imply an inherent rotational degree of freedom in attention projections. Model Soup and Fisher-weighted merging highlighted practical gains from weight-space averaging yet exposed failures when parameters are misaligned, underscoring the need for principled alignment before fusion. This paper synthesizes these insights by elevating symmetry from permutations to rotations in attention layers, thereby enlarging the equivalence class from discrete to continuous and better matching transformers’ inductive structure. It then operationalizes this symmetry with a theoretically optimal parameter-matching algorithm, providing a plug-and-play module that complements and improves existing fusion strategies.

---
*Generated: 2026-01-07T00:21:33.198452*

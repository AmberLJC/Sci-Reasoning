# Prior Work Analysis Report

## Target Paper
**Title:** crczm2smVo
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—constructing projective equivariant networks via second-order fundamental differential invariants—sits at the intersection of equivariant deep learning and the classical moving frame theory of differential invariants. On the deep learning side, group equivariant and steerable CNNs established the modern recipe for embedding symmetry into architectures (Cohen & Welling, 2016; Weiler & Cesa, 2019). Yet these approaches assume relatively linear, homogeneous group actions and tractable representation theory; the projective group’s highly non-linear action on images stretches these assumptions. Finzi et al. (2020) advanced equivariance to general Lie groups with coordinate-based kernels, but practical obstacles for projective transformations remain, motivating an alternative path.

That alternative is grounded in the moving frame program. Olver’s monograph (1995) and the Fels–Olver algorithm (1998/1999) provide the constructive machinery—cross-sections, invariantization, invariant derivations, and completeness proofs—to derive a generating set of differential invariants for a prescribed group action. Building on these, the present paper tailors a cross-section for multi-dimensional functions and rigorously analyzes the resulting projective invariants and their interrelations to obtain a simplified fundamental second-order set. Ovsienko & Tabachnikov (2005) contributes the projective differential geometry background (e.g., Schwarzian-type invariants and invariant operators) that informs the identification and reduction of invariants. Finally, Calabi et al. (1998) bridge theory to practice by showing how differential invariant signatures can be made numerically stable for vision tasks. Together, these works directly enable the paper’s strategy: replacing steerable or group-convolutional mechanisms with a principled invariantization pipeline that yields projective-equivariant architectures built from fundamental differential invariants.

---
*Generated: 2026-01-07T00:02:04.918646*

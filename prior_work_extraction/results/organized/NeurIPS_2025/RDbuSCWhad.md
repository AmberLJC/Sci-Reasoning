# Prior Work Analysis Report

## Target Paper
**Title:** RDbuSCWhad
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PD-SSM targets the core tension in state-space models between computational efficiency and expressivity. S4 established the modern SSM blueprint—linear recurrences discretized from continuous-time dynamics with structured transition operators that enable parallel convolution—while HiPPO provided stability and complex-eigenvalue machinery that made such discretizations robust. Mamba advanced this line with hardware-friendly, linear-time scan-based inference, showing state updates can be parallelized without sacrificing sequential fidelity. PD-SSM embraces these efficiency and stability pillars but rethinks the transition matrix: instead of dense or purely diagonal structures, it uses a product of a column one-hot (routing/permutation-like) matrix and a complex diagonal, achieving the O(n)-per-scan cost characteristic of diagonal SSMs.

This P·D parameterization draws directly on the structured-matrix literature typified by Monarch, where alternating permutation and diagonal factors yield expressive yet fast linear maps. Crucially, PD-SSM links SSM dynamics to automata theory: the WFST/WFA perspective (Mohri–Pereira–Riley) casts state transitions as weighted linear operators; spectral WFA results (Balle–Carreras–Quattoni) further ground their linear-algebraic realization; and Myhill–Nerode minimality justifies the claim of optimal state size for tracking N-state FSAs. The result is an SSM layer that preserves diagonal-level compute and stability while restoring the discrete state-tracking power of finite automata via a sparse, permutation–diagonal transition—providing provable expressive guarantees and practical parallelism.

---
*Generated: 2026-01-06T23:42:48.105360*

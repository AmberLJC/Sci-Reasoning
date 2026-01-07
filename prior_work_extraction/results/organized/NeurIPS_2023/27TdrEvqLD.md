# Prior Work Analysis Report

## Target Paper
**Title:** 27TdrEvqLD
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper addresses a core gap between the well-understood expressivity of message-passing GNNs and the comparatively opaque discriminative scope of persistent homology when applied to attributed graphs. Xu et al. (2019) establish the 1-WL ceiling for MP-GNNs, motivating the need for complementary invariants. Foundational PH theory by Cohen-Steiner, Edelsbrunner, and Harer (2007), together with the Edelsbrunner–Harer monograph (2010), provides the precise sublevel-set filtration framework and 0D persistence machinery needed to analyze distinguishability induced by filter functions on vertices and edges. Early graph-focused PH studies, notably Horak et al. (2009) and Giusti et al. (2015), demonstrated that different graph filtrations (edge-thresholding, clique/flag complexes, vertex functions) capture distinct structures, foreshadowing the present work’s key insight: vertex-level and edge-level PH are fundamentally incomparable.
Building on these theoretical pillars, the learning component of the paper (RePHINE) connects to the maturation of PH in machine learning. Stable, differentiable surrogates for persistence diagrams—via multi-scale kernels (Reininghaus et al., 2015) and Wasserstein-based kernels (Carrière, Cuturi, Oudot, 2017)—made PH-based features practical and trainable. The present work uses its new concept of color-separating sets to deliver necessary and sufficient conditions for PH-based graph distinguishability, explicitly proving the limits of vertex- and edge-level PH and showing neither subsumes the other. Leveraging these insights, RePHINE efficiently combines both PH channels into a provably stronger, learnable representation, thereby extending PH’s role from an ad hoc augmentation to a theoretically grounded, synergistic complement to WL-bounded MP-GNNs.

---
*Generated: 2026-01-06T23:42:49.079203*

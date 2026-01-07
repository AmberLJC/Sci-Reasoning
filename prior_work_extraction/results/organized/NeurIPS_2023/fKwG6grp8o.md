# Prior Work Analysis Report

## Target Paper
**Title:** fKwG6grp8o
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—an O(1/√width) fluctuation theory for kernels and predictions that is non-perturbative in feature learning—sits at the intersection of three lines of prior work. First, NTK theory (Jacot et al.) and its formalization of the lazy regime (Chizat et al.) established the infinite-width baseline where kernels remain static and predictions follow a linear model, furnishing the reference point whose universal prediction-variance form this paper recovers in the lazy limit. Second, mean-field analyses of training dynamics in the rich, feature-learning regime for two-layer networks (Mei–Montanari–Nguyen; Rotskoff–Vanden-Eijnden) provided the self-consistent, distributional evolution of network features and kernels at infinite width. Building directly on this, recent DMFT for SGD (Mignacco–Loureiro–Krzakala–Zdeborová) supplied a practical framework to track time-dependent order parameters and predictions during learning, which this work adopts as its infinite-width backbone. Third, finite-width theory (Yaida; Yang) quantified how wide-but-finite networks deviate from their infinite-width limits, identifying 1/width corrections and O(1/√width) fluctuations—insights this paper extends from initialization and lazy settings to fully dynamic, feature-learning regimes. By synthesizing DMFT with finite-width perturbations, the authors derive self-consistent equations for the coupled fluctuations of kernels and predictions, revealing that feature learning can dynamically suppress prediction variance, especially in two-layer networks, and characterizing how initialization and learning-rate choices control these fluctuations.

---
*Generated: 2026-01-07T00:02:04.868924*

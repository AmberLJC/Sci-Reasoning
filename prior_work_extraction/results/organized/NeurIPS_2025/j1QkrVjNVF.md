# Prior Work Analysis Report

## Target Paper
**Title:** j1QkrVjNVF
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—casting 3D Gaussian Splatting (3DGS) compaction as a global Gaussian mixture reduction problem optimized via optimal transport—sits at the intersection of three lines of work. First, Kerbl et al. introduced 3DGS as a high-fidelity, real-time radiance field representation whose millions of Gaussians motivate compaction; their parameterization (positions, covariances, opacity, SH colors) defines the variables the new method reduces and then fine-tunes. Second, classical Gaussian mixture reduction (GMR), epitomized by Runnalls’ KL-driven framework, provides the blueprint for principled, fidelity-aware shrinking of mixtures. The present paper extends this paradigm by replacing KL with transport-based divergences that better capture geometric displacement and mass rearrangement among spatial Gaussians. This is enabled mathematically by the closed-form 2-Wasserstein/Bures metrics between Gaussians (Takatsu), and computationally by modern OT machinery such as Sinkhorn divergences (Genevay–Peyré–Cuturi) that deliver stable, differentiable objectives for large-scale optimization. To make global transport tractable over massive 3DGS sets, the method borrows from hierarchical OT approximations—tree-sliced Wasserstein ideas (Le–Yamada–Kashima) and fast EMD principles (Pele–Werman)—operationalized here as a KD-tree partition guiding composite transport. Finally, the ‘herding’ intuition traces to kernel herding (Chen–Welling): deterministically relocating a small set of weighted atoms to approximate a target distribution. The paper adapts this notion from MMD to OT, using “Gaussian herding across pens” to globally reallocate and merge primitives, then decouple geometry from appearance via lightweight color/opacity fine-tuning.

---
*Generated: 2026-01-07T00:05:12.517929*

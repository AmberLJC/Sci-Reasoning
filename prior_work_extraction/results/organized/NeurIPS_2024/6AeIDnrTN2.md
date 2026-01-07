# Prior Work Analysis Report

## Target Paper
**Title:** 6AeIDnrTN2
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LightGaussian targets the practical bottleneck of 3D Gaussian Splatting: millions of SfM-seeded Gaussians and high-order SH appearance that impose gigabyte-level storage and hamper splatting efficiency, especially in unbounded scenes. The core idea is to import mature compression principles from deep model optimization into the 3DGS primitive space. From Han et al., LightGaussian borrows an iterative prune–recover paradigm, but applies it to scene primitives: Gaussians with minimal global significance to reconstruction are pruned and the scene is re-optimized to recover fidelity. Molchanov et al.’s saliency-driven pruning motivates a global importance metric to rank primitives, ensuring removals minimally affect photometric error. To reduce appearance parameters, LightGaussian turns to Hinton et al.’s knowledge distillation, transferring a teacher’s high-degree spherical harmonics to a student with a lower SH degree; pseudo-view augmentation supplies dense, view-diverse supervision, akin to distillation practices in PlenOctrees’ SH-based radiance representation. Finally, codebook-based vector quantization (VQ-VAE) inspires LightGaussian’s Gaussian Vector Quantization, discretizing attributes with significance-aware strength to compress further without uniform quality degradation. Together with the foundational 3DGS target and the practical scale introduced by COLMAP SfM pipelines, these strands converge into a unified compress–recover–distill–quantize pipeline. The result is a compact, fast 3DGS representation that maintains visual fidelity while achieving the reported 15× size reduction and 200+ FPS rendering.

---
*Generated: 2026-01-06T23:33:36.287920*

# Prior Work Analysis Report

## Target Paper
**Title:** M7KyLjuN0A
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

DynamicCity’s core advances—compact 4D representation via hex-planes with a learned Projection Module and an Expansion & Squeeze strategy for fast volume reconstruction—sit at the intersection of three threads of prior work. First, the higher-dimensional modeling of dynamics pioneered by HyperNeRF establishes the value of treating time as an additional coordinate, motivating DynamicCity’s 4D occupancy formulation. Second, planar factorization methods, notably EG3D’s tri-planes and K-Planes’ general multi-plane factorization for N-D fields, demonstrate that projecting high-dimensional fields onto axis-aligned planes yields tractable generative models. DynamicCity directly builds on this idea but replaces the field-to-plane mapping’s naive feature averaging with a learned Projection Module tuned for 4D occupancy semantics, substantially improving fitting quality. Third, tensor-factorized neural fields such as TensoRF reveal that dense volumes can be reconstructed efficiently from compact factors; DynamicCity operationalizes this insight for 4D occupancy by introducing a parallel Expansion & Squeeze step that reconstructs 3D feature volumes without expensive per-point queries.
Complementing these representation advances, large-scale scene efforts like Block-NeRF and SceneDreamer underscore the need for scalable generative pipelines in expansive urban environments. DynamicCity fuses these strands—higher-dimensional dynamics, multi-plane factorization, and efficient factor-to-volume reconstruction—to deliver a practical, semantically aware 4D occupancy generator capable of modeling large, dynamic city scenes.

---
*Generated: 2026-01-06T23:42:48.095725*

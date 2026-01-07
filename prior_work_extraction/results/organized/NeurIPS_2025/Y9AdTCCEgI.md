# Prior Work Analysis Report

## Target Paper
**Title:** Y9AdTCCEgI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

OnlineSplatter’s core innovation—pose-free, online reconstruction of a moving object as a compact field of 3D Gaussians powered by a dual-key memory—sits at the intersection of three lines of work. First, 3D Gaussian Splatting provides the computational and representational backbone: efficient Gaussian primitives with SH-based view dependence, together with densification and pruning strategies that OnlineSplatter repurposes for continuous online updates at constant cost. Second, ideas from neural rendering guide how appearance and viewpoint are handled without poses. NeRF established conditioning on viewing direction, while NeRF in the Wild introduced appearance embeddings to decouple lighting/appearance from geometry. OnlineSplatter translates these into a dual-key memory: latent appearance-geometry keys maintain a stable object state across frames, and explicit directional keys enable correct view-dependent readout during fusion. Handling free motion draws from dynamic/canonicalization works: Nerfies shows how to maintain an object-centric canonical space under deformation, and DynamicFusion pioneered anchoring to the first frame with incremental fusion—both principles that OnlineSplatter adapts to monocular RGB and Gaussian primitives without optimization over deformations or poses. Finally, online correspondence/tracking insights from DROID-SLAM motivate eschewing bundle adjustment in favor of feed-forward, memory-based aggregation, aligning with the paper’s spatially guided readout and sparsification mechanism. Collectively, these works directly enable OnlineSplatter’s design: a memory-augmented, direction-aware Gaussian field that fuses per-frame features into a canonical, compact object reconstruction without camera poses or depth priors.

---
*Generated: 2026-01-07T00:21:32.346809*

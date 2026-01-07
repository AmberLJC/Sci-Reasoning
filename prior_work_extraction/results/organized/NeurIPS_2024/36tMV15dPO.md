# Prior Work Analysis Report

## Target Paper
**Title:** 36tMV15dPO
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

X-Ray’s core idea—a camera-centric, sequential representation that records all surface intersections along each ray—stands on the lineage of layered scene representations and ray-based rendering. Layered Depth Images (Shade et al., 1998) introduced storing multiple samples along a ray to represent occlusions; Stereo Magnification’s Multiplane Images (Zhou et al., 2018) operationalized layered depth for learning-based view synthesis. X-Ray adopts this layered philosophy but replaces coarse depth planes with actual per-ray surface hits, packaging depth, normal, and color into succinct, surface-only layers. From NeRF (Mildenhall et al., 2020), X-Ray inherits the insight that camera-ray parameterizations elegantly couple geometry, appearance, and visibility; yet it departs from volumetric integration to a sparse, surface-centric sequence that is both compact and well-aligned with discriminative and generative supervision.
Crucially, representing a 3D object as an ordered set of frames enables reusing Video Diffusion Models (Ho et al., 2022), whose temporal U-Nets are designed for dependencies across frames; X-Ray treats layer order as a temporal dimension, making video diffusion a natural fit. To reach high fidelity, X-Ray adopts a cascaded diffusion strategy akin to SR3 (Saharia et al., 2021), first generating a coarse sequential representation and then refining it with an upsampler. Finally, EG3D (Chan et al., 2022) demonstrated that converting 3D structure into 2D-friendly factorized representations lets 2D generative architectures scale effectively; X-Ray extends this principle by turning 3D surfaces into a multi-frame sequence, unlocking the capabilities of state-of-the-art video diffusion for single-image 3D reconstruction with both visible and hidden surfaces.

---
*Generated: 2026-01-06T23:33:35.577052*

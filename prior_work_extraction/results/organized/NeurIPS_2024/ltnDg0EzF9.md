# Prior Work Analysis Report

## Target Paper
**Title:** ltnDg0EzF9
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s key contribution—replacing explicit inverse graphics with a purely data-driven relighting model where intrinsics and lighting are represented as latent variables—stands on two intellectual pillars: intrinsic image theory and neural rendering/factorization. Retinex formalized the decomposition of images into reflectance (albedo) and illumination, a conceptual foundation the authors embrace while rejecting hand-crafted photometric constraints. Classical inverse graphics, epitomized by SIRFS, showed that jointly estimating shape, reflectance, and lighting is possible but brittle, with difficult error control and limited to chosen intrinsics—precisely the limitations the paper seeks to avoid.

On the learning side, Direct Intrinsics proved that deep models can separate albedo and shading from single images, though it relied on supervision. Intrinsic Images in the Wild provided the evaluation protocol and supervision signals that shaped progress in albedo recovery; the present work notably achieves competitive albedo without using such labels, indicating the strength of its latent factorization. NeRF ushered in neural scene representations suitable for rendering, inspiring a broader move from explicit geometry to learned, differentiable representations. Building on that trajectory, NeRD demonstrated that reflectance and illumination can be disentangled for relighting when sufficient multi-image supervision is available. The new paper synthesizes these lines by training on relighting supervision while encoding intrinsics and lighting as latents, enabling state-of-the-art relighting of real scenes and showing that an albedo representation can emerge from the learned intrinsics without any direct albedo examples.

---
*Generated: 2026-01-06T23:33:36.258563*

# Prior Work Analysis Report

## Target Paper
**Title:** EyFrTjaYU3
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

TGA’s core insight—making dynamic Gaussian avatars perspective-aware while keeping deformations geometry-consistent—emerges from the confluence of advances in Gaussian splatting, dynamic warping, and classic splat rendering theory. 3D Gaussian Splatting established the high-fidelity, real-time ellipsoidal representation but relies on a local affine projection that is not strictly perspective-correct, which can blur fine geometry when color cues are ambiguous. 4D Gaussian Splatting showed how to extend Gaussians to dynamic scenes, yet continued to treat projection largely as an affine approximation detached from the deformation model. Human-centric pipelines such as HUGS exposed this shortcoming most acutely: subtle facial motions and skin-tone similarity demand higher geometric sensitivity than standard Gaussian pipelines provide.

TGA bridges these gaps by combining deformation-field Gaussians with Jacobian-aware guidance, inspired by Nerfies’ use of Jacobian regularization to preserve structure under motion. Crucially, TGA integrates both temporal deformation and spatial projection in a homogeneous, perspective-aware formulation, aligning the deformation Jacobian with the camera projection Jacobian. This echoes the EWA surface splatting principle of using differential projection for perspective-correct footprints, but recast for 3D Gaussian radiance fields and coupled to time-varying deformations. The result is a color-sensitive, geometry-faithful 4D Gaussian avatar representation that captures fine facial variations under subtle appearance changes where prior Gaussian and avatar methods falter.

---
*Generated: 2026-01-07T00:29:41.028810*

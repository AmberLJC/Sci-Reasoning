# Prior Work Analysis Report

## Target Paper
**Title:** rheCTpRrxI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DreamHuman’s core contribution—text-driven generation of realistic, re-posable 3D human avatars—emerges from the synthesis of three pivotal research threads. First, DreamFusion established score distillation sampling (SDS), showing that powerful 2D text-to-image diffusion models can supervise 3D optimization; DreamHuman inherits this mechanism while specializing it to the human domain. Leveraging Latent Diffusion (Stable Diffusion) as the text prior supplies the high-capacity semantic and appearance guidance needed to produce diverse, photorealistic human textures directly from language. Second, NeRF provides the photorealistic, differentiable volumetric 3D representation that DreamHuman optimizes under diffusion guidance, addressing view consistency that CLIP-based mesh methods struggled with. Third, statistical human body models, particularly SMPL, inject structure: a rigged skeleton, skinning, and anthropometric regularization that make re-posing feasible. Building on A‑NeRF’s canonical-to-posed mapping, DreamHuman adopts skeleton-driven warping to animate a canonical radiance field. Complementing this, SCANimate’s SMPL+D perspective informs DreamHuman’s learned per-instance rigid and non-rigid offsets, capturing clothing and hair deformations while maintaining pose control. Finally, AvatarCLIP demonstrated the possibility of text-driven animatable avatars with parametric bodies; DreamHuman advances this by uniting diffusion guidance with a NeRF-based, SMPL-conditioned deformation framework, achieving markedly higher realism and multi-view fidelity while preserving full animatability from text alone.

---
*Generated: 2026-01-07T00:02:04.842721*

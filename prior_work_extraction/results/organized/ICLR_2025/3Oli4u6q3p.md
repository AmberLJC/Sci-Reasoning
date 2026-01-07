# Prior Work Analysis Report

## Target Paper
**Title:** 3Oli4u6q3p
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

RelitLRM fuses three influential threads in neural rendering. First, it adopts 3D Gaussian Splatting as the explicit, real-time renderable backbone, but goes beyond its original optimization-centric, view-dependent radiance to predict Gaussians in a feed-forward manner that remain editable under novel lighting. Second, it leverages the Large Reconstruction Model paradigm—pioneered by LRM—showing that a transformer trained at scale can infer high-quality 3D from sparse posed views. This is rooted in earlier feed-forward generalization efforts like pixelNeRF, which demonstrated conditioning on few images to regress a radiance field; RelitLRM modernizes this by predicting explicit Gaussians and by architecturally separating geometry and appearance modules.
A third pillar is physically based relightability. Works such as NeRV and NeRFactor established that disentangling geometry, reflectance, and illumination (often via multi-illumination supervision) is key to avoiding highlight/shadow baking and achieving plausible relighting. RelitLRM inherits this factorization insight but replaces slow, per-scene inverse rendering with an end-to-end learned model trained on synthetic scenes with known illuminations. To capture the inherent multi-modality of cast shadows and specular highlights from sparse inputs, RelitLRM introduces a diffusion-based appearance generator, drawing on DDPM’s strength in modeling complex, uncertain distributions. Finally, optimization-heavy baselines like nvdiffrec motivate RelitLRM’s design by highlighting the cost and data requirements of classical inverse rendering; RelitLRM matches their relighting fidelity with a single, fast forward pass and an explicit Gaussian output suited for real-time rendering and editing.

---
*Generated: 2026-01-06T23:42:48.084295*

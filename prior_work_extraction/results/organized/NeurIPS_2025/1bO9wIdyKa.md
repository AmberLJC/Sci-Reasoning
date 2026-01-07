# Prior Work Analysis Report

## Target Paper
**Title:** 1bO9wIdyKa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

UniRelight’s core idea—jointly estimating an illumination-invariant intrinsic (albedo) representation while synthesizing relit images/videos in a single generative pass—sits at the intersection of intrinsic decomposition, inverse rendering, and modern diffusion-based video generation. Retinex theory established reflectance–illumination factorization as the canonical lens on appearance, and SIRFS made explicit the benefits of coupling reflectance and illumination estimation to reduce under-determined ambiguities. The IIW line of work demonstrated that intrinsic signals can be learned under weak supervision, a crucial pathway when fully paired multi-illumination datasets are scarce.

On the rendering side, NeRF and its relightable descendants such as NeRV showed that factorizing scene properties (reflectance, visibility, and lighting) enables realistic relighting but typically through two-stage inverse-plus-forward pipelines that are fragile to error accumulation and data coverage. UniRelight adopts the factorization spirit (explicit albedo) but collapses the pipeline: instead of estimating a full physical scene model then re-rendering, it conditions a powerful generator to synthesize the relit result while jointly predicting albedo, improving robustness in complex materials and lighting.

This collapse is enabled by latent and video diffusion models. Latent Diffusion provides efficient, controllable, high-fidelity image synthesis that can be guided by intrinsic cues, while Video Diffusion Models contribute temporal consistency across frames. Together they supply a strong generative prior that compensates for limited paired supervision and can hallucinate realistic light transport effects—shadows, reflections, and transparency—under diverse target illuminations.

---
*Generated: 2026-01-07T00:21:32.298708*

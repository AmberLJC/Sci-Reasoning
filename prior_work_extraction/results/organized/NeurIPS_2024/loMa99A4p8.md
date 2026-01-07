# Prior Work Analysis Report

## Target Paper
**Title:** loMa99A4p8
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core idea of Diffusion Models With Learned Adaptive Noise is to learn the forward diffusion process as an input-conditional, multivariate noise mechanism that functions as an approximate variational posterior, thereby tightening the ELBO and improving likelihood. This builds directly on the foundational variational view of diffusion probabilistic models introduced by Sohl-Dickstein et al., which cast diffusion as a Markov chain optimized via an ELBO. DDPM operationalized this framework with fixed forward schedules and a practical training objective, seeding a widely held belief that the ELBO is effectively invariant to the chosen forward noise process. Subsequent empirical work by Nichol and Dhariwal, and the broader design-space analysis of Karras et al. (EDM), demonstrated that schedule and parameterization choices materially influence both likelihood and synthesis, motivating a departure from fixed, isotropic noise.

Song et al.’s SDE formulation supplied a unifying continuous-time perspective, legitimizing flexible diffusion coefficients and clarifying links to likelihood, which the new paper leverages to justify input-conditional, spatially varying forward noise. Crucially, Flow++ provided the conceptual blueprint that learned noise can be treated as a variational posterior to tighten likelihood bounds; the present work transposes this idea from flow-based dequantization to diffusion’s forward process. Finally, techniques from Auxiliary Deep Generative Models inform the introduction of auxiliary variables, enriching the variational family and breaking the ELBO invariance associated with fixed forward processes. Together, these strands culminate in MuLAN’s learned multivariate schedules, adaptive per-input diffusion, and auxiliary variables, directly addressing ELBO tightness and performance.

---
*Generated: 2026-01-07T00:02:04.742645*

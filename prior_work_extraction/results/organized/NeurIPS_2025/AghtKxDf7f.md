# Prior Work Analysis Report

## Target Paper
**Title:** AghtKxDf7f
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

STITCH-OPE’s core innovation—synthesizing long-horizon, high-dimensional target-policy trajectories from behavior data via guided diffusion—emerges at the intersection of trajectory diffusion, guidance mechanisms, and distribution correction for OPE. The denoising diffusion foundation of Ho et al. provides the scalable generative backbone for modeling complex trajectory distributions, while the score-based SDE view from Song et al. formalizes how external gradients can be injected into the generative dynamics. Dhariwal and Nichol’s classifier guidance directly informs STITCH-OPE’s replacement of classifier gradients with target-policy scores, transforming conditional image guidance into policy-conditioned trajectory synthesis. Ho and Salimans’ classifier-free guidance motivates subtracting a neutral score to avoid over-regularization; STITCH-OPE analogously subtracts the behavior-policy score, stabilizing guidance strength and preventing collapse back to the behavior distribution.
Diffuser demonstrates that diffusion can operate over trajectories and be guided for control, which STITCH-OPE repurposes for evaluation: rather than conditioning on rewards or goals, it uses the target policy’s score to generate rollouts reflective of the target distribution. Finally, OPE-specific insights from DualDICE inform the need for distribution shift from behavior to target without high-variance importance sampling; STITCH-OPE achieves a principled, low-variance correction by performing this shift in score space during generation. The stitching perspective, popularized in IQL, influences STITCH-OPE’s emphasis on composing plausible segments into full trajectories, now realized through policy-guided generative sampling tailored to OPE.

---
*Generated: 2026-01-07T00:21:32.336679*

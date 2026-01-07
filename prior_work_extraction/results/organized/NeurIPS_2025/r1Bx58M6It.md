# Prior Work Analysis Report

## Target Paper
**Title:** r1Bx58M6It
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

SW-Guidance’s key contribution—training-free, palette-consistent image generation by injecting a differentiable sliced 1-Wasserstein color objective into the diffusion sampler—emerges from two converging lines of work: gradient-based diffusion guidance and optimal-transport color alignment. The diffusion backbone of Ho et al. (DDPM) provides the reverse-time update rule that can be perturbed by auxiliary gradients. Dhariwal and Nichol’s classifier guidance establishes the general recipe for steering the sampling path using ∇x log p(y|x), while Ho and Salimans’ classifier-free guidance clarifies how guidance strength modulates semantic adherence during sampling. In parallel, the optimal-transport literature on color manipulation—particularly Ferradans et al.—demonstrates that 1-Wasserstein distances capture perceptually meaningful discrepancies between color distributions, yielding stable color transfer. Bonneel et al. supply the computational tool: sliced Wasserstein computes these OT objectives efficiently and differentiably via random projections, making them amenable to backpropagation.
Bridging these threads, Chung and Ye’s diffusion posterior sampling shows how to incorporate arbitrary differentiable data-consistency terms into the reverse dynamics without retraining, effectively treating them as likelihood energies. SW-Guidance instantiates this idea for color conditioning: it defines a sliced 1-Wasserstein energy between the generated image’s color distribution and the reference palette and injects its gradient into each denoising step. The result is a principled, training-free sampler that aligns colors while preserving semantic fidelity to the text prompt, improving over post-hoc color transfer or ad-hoc heuristics.

---
*Generated: 2026-01-07T00:21:32.230416*

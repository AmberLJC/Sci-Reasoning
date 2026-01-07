# Prior Work Analysis Report

## Target Paper
**Title:** 8viuf9PdzU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

SNPSE fuses two lines of work: score-based diffusion modeling and sequential neural simulation-based inference. On the generative modeling side, Hyvärinen’s score matching established how to learn gradients of log densities without access to normalizing constants, while Vincent’s denoising perspective made this practical by perturbing data with noise. Building on these, Song and Ermon introduced score-based generative models with multi-noise training and annealed Langevin dynamics, later unified by the SDE framework that supplies robust predictor–corrector sampling. SNPSE directly ports these ideas to posterior inference by training a conditional score network sθ(·|x) to approximate ∇θ log p(θ|x), and then sampling θ via diffusion/SDE methods conditioned on the observation.

From the SBI side, Papamakarios and Murray’s BCDE/SNPE-A pioneered learning amortized posteriors from simulations with a sequential scheme that concentrates simulations where the posterior has mass. Greenberg et al. (APT/SNPE-C) refined this into a strong, practical baseline using expressive flows and robust training, defining today’s standard for sequential amortized SBI. Papamakarios et al.’s SNL further crystallized the benefit of adapting proposals to the evolving posterior approximation to reduce simulation cost. SNPSE adopts this sequential scaffolding—guiding simulations with the current posterior approximation—but replaces density/ration-based targets with a learned posterior score, enabling diffusion-based posterior sampling. The result is a method that retains the simulation efficiency and amortization of SNPE/SNL while exploiting the robustness and sample quality of score-based diffusion models.

---
*Generated: 2026-01-06T23:42:48.060497*

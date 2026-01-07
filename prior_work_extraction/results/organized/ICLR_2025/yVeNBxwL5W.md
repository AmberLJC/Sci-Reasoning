# Prior Work Analysis Report

## Target Paper
**Title:** yVeNBxwL5W
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

MaRS targets the problem of accelerating sampling for Mean Reverting (MR) diffusion, where controllability is built into the SDE structure rather than via score modifications. Its key technical move is to derive semi-analytical solutions for both the reverse-time SDE and the probability flow ODE of the MR process: a closed-form deterministic component plus an integral term evaluated with the neural network. This formulation rests squarely on the score-based SDE/PF-ODE framework of Song et al., which formalized reverse-time SDEs, PF-ODEs, and predictor–corrector sampling. DDPM provides the variance-preserving diffusion family and noise schedules that MR generalizes by adding a mean-reverting drift, while DDIM’s deterministic ODE viewpoint motivates solving the PF-ODE directly for efficiency.

The most direct algorithmic influence is DPM-Solver, whose exponential-integrator strategy analytically integrates the linear time-varying part of the diffusion ODE and numerically approximates the network-dependent residual. MaRS adopts this semi-analytical separation but re-derives it for the MR SDE/ODE, whose drift and covariance have different structure from standard VP/DDIM forms. Practical design choices for stable few-step integration and parameterization are informed by EDM, which clarified sigma/LogSNR parameterizations and robust step schedules. Finally, classifier-free guidance frames the motivation: rather than manipulating scores to impose conditions (the prevailing controllability route), MR encodes conditions in the SDE itself. MaRS makes that structurally controlled formulation computationally practical by supplying matching fast SDE/ODE solvers with low NFE.

---
*Generated: 2026-01-06T23:42:48.097263*

# Prior Work Analysis Report

## Target Paper
**Title:** voG6nEW9BV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—amortized conditional score-based diffusion models for Bayesian linear inverse problems in infinite-dimensional function spaces—builds on two pillars: (i) score-based generative modeling with denoising objectives and (ii) rigorous infinite-dimensional Bayesian analysis. Hyvärinen’s score matching laid the fundamental principle for estimating gradients of log densities without normalized likelihoods. Vincent’s denoising formulation then provided a practical, theoretically grounded estimator—central to modern diffusion training—by relating denoising to score estimation. Ho et al. operationalized these ideas via DDPMs, widely adopting denoising objectives that naturally extend to conditional settings. Song et al. supplied the continuous-time SDE framework and sampling theory for SDMs, which the present work leverages while moving to function spaces.

On the inverse problems side, Stuart’s measure-theoretic treatment of Bayesian inverse problems in infinite dimensions enables defining posteriors and their scores on Hilbert spaces; this is essential for proving the validity of a conditional denoising estimator beyond finite dimensions. Meanwhile, recent diffusion-based inverse methods such as DDRM (Kawar et al.) and DPS (Chung et al.) showed how unconditional score priors can be combined with data-consistency or likelihood gradients to approximate posteriors. However, these methods require repeated forward-operator evaluations, which are costly and heuristic in infinite-dimensional settings. The present paper unifies these strands by giving a rigorous infinite-dimensional justification for the conditional denoising estimator and proposing an amortized conditional SDM that directly learns p(x|y) scores, thus enabling posterior sampling without iterative, expensive forward solves.

---
*Generated: 2026-01-07T00:02:04.814637*

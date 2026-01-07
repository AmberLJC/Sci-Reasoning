# Prior Work Analysis Report

## Target Paper
**Title:** OuKW8cUiuY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—adaptive likelihood estimation and MAP inference with a diffusion prior for real-world, signal-dependent noise—rests on three converging lines of work. First, diffusion generative modeling (Ho et al., 2020; Song et al., 2021) provides the learned score/denoiser and reverse-time dynamics that serve as a powerful image prior and a mechanism to inject log-likelihood guidance into sampling. Second, diffusion-for-inverse-problems frameworks (DDRM; Chung et al.’s Diffusion Posterior Sampling) show how to incorporate measurement models and likelihood terms into diffusion trajectories. However, these typically assume simple, homoscedastic Gaussian noise and known noise levels. The present paper generalizes this by introducing an independent, non-identically distributed (heteroscedastic) likelihood and performing adaptive, per-pixel precision inference during the reverse process.
A third strand comes from real-noise modeling and Bayesian restoration. Foi et al. (2008) established Poisson–Gaussian camera noise as a practical, signal-dependent model, motivating the i.n.i.d. likelihood and the need to estimate local noise statistics. CBDNet (Guo et al., 2019) demonstrated the utility of spatially varying noise maps for blind denoising and the benefit of smoothing/regularizing such maps—ideas echoed here via a precision prior and local Gaussian convolution to stabilize variance estimates. Finally, EPLL (Zoran & Weiss, 2011) provides the blueprint for MAP restoration with a learned generative prior and adaptive noise parameter updates; this work transposes that MAP-and-adaptation paradigm into the diffusion setting, replacing GMM patch priors with a diffusion prior and using variational Bayes to infer per-pixel noise precision on-the-fly.

---
*Generated: 2026-01-06T23:33:36.275282*

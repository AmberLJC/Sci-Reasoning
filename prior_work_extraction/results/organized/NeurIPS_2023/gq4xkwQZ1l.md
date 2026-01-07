# Prior Work Analysis Report

## Target Paper
**Title:** gq4xkwQZ1l
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central advance—training diffusion models to sample from distributions never directly observed by incorporating a known differentiable forward model into denoising—arises at the intersection of three lines of work. First, DDPM and the score-based SDE framework supply the core mechanics of diffusion generative modeling and the score-matching perspective that enables augmenting the reverse dynamics with likelihood gradients. Second, a body of inverse-problem methods with diffusion priors (DDRM) and forward-model-guided sampling (DPS) demonstrate how to enforce data consistency by injecting gradients stemming from a measurement operator into the diffusion trajectory; these works operate at sampling time using a pre-trained prior, whereas the present paper embeds such guidance into the training/denoising objective to learn the prior itself from measurements. Third, AmbientGAN and Noise2Noise established that generative or restoration models can be learned from measurements alone by simulating the corruption/forward process; the current work transfers this paradigm to diffusion models, directly integrating the forward operator in each denoising step rather than relying on paired supervision. Finally, guidance ideas popularized by Dhariwal and Nichol generalize to using a forward-model likelihood as the steering signal. Together, these contributions shape a method that unifies diffusion denoising with differentiable forward models, enabling unsupervised learning of complex signal distributions from partial, indirect observations.

---
*Generated: 2026-01-07T00:02:04.812730*

# Prior Work Analysis Report

## Target Paper
**Title:** SDhOClkyqC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—an exact, analytical account of spectral bias in the training dynamics of diffusion denoisers and the resulting evolution of the generated distribution—rests on three pillars: the denoising diffusion/score-matching training objective, eigenmode-resolved learning dynamics in linear architectures, and Fourier diagonalization of convolution. The DDPM objective (Ho et al.) and the score-based formulation (Song et al.) establish the denoising loss and its link to generative modeling, while the denoising–score matching equivalence (Vincent) supplies the theoretical bridge needed to map denoiser training at each noise level to the score of a perturbed distribution. Building on the Saxe et al. framework, the authors solve gradient-flow dynamics exactly for linear denoisers, revealing decoupled evolution along principal components with mode-dependent time scales. The kernel regression theory of spectral bias and eigen-spectrum–dependent learning rates (Bordelon, Canatar, Pehlevan) provides a mathematically aligned precedent for inverse-eigenvalue time scales; this paper translates that intuition to diffusion denoisers and to the generated distribution itself, deriving closed-form KL trajectories. For convolutional denoisers, the Fourier-domain diagonalization of convolutional operators (Sedghi, Gupta, Long) enables an analogous mode-wise analysis, now in the frequency domain. Finally, prior observations of spectral/frequency bias in neural networks (Rahaman et al.) are placed on firm analytical footing: the paper proves a pronounced, power-law spectral bias—convergence time inversely scaling with mode variance—robust across linear and convolutional settings and persisting empirically in deeper architectures.

---
*Generated: 2026-01-07T00:02:04.941896*

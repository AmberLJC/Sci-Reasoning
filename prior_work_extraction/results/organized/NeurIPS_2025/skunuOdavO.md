# Prior Work Analysis Report

## Target Paper
**Title:** skunuOdavO
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central claim—that locality in image diffusion denoisers emerges from image data statistics rather than convolutional inductive bias—rests on two intertwined lines of prior work: the theory of denoising-as-score-estimation and the statistics of natural images. DDPM provides the canonical denoising training setup and architecture whose locality properties are under scrutiny. The score-based perspective of diffusion (Song et al.) together with Vincent’s connection between denoising and score matching formalizes that an optimal denoiser is determined by the score of the noise-perturbed data distribution; hence, its behavior should fundamentally reflect data statistics. Classical natural image statistics (Simoncelli & Olshausen) describe the 1/f spectral structure and rapidly decaying spatial correlations of images, implying that optimal estimators of pixel intensities weigh nearby pixels more heavily. This intuition is made precise by Wiener’s theory of optimal linear MMSE estimation, which links the optimal linear denoiser to the signal covariance and thereby predicts spatially local filters when correlations decay with distance. Methodologically, the paper’s measurement and interpretation of locality patterns draw on effective receptive field analyses (Luo et al.), enabling precise comparisons between deep and linear denoisers. Finally, evidence that diffusion models need not be convolutional—exemplified by DiT’s Transformer-based denoisers—reinforces the authors’ premise that locality is not a mere byproduct of convolutional inductive bias. Together, these works motivate and enable the paper’s key contribution: demonstrating that a suitably optimized linear denoiser reproduces the locality patterns of deep diffusion models, attributing locality to data statistics.

---
*Generated: 2026-01-07T00:21:32.253421*

# Prior Work Analysis Report

## Target Paper

**Title:** Multi-Source Diffusion Models for Simultaneous Music Generation and Separation

**Conference:** ICLR 2024 (oral)

**Authors:** Giorgio Mariani, Irene Tallini, Emilian Postolache, Michele Mancusi, Luca Cosmo, Emanuele Rodolà

**Keywords:** source separation, probabilistic diffusion models, music generation

**Abstract:** 
> In this work, we define a diffusion-based generative model capable of both music generation and source separation by learning the score of the joint probability density of sources sharing a context. Alongside the classic total inference tasks (i.e., generating a mixture, separating the sources), we also introduce and experiment on the partial generation task of source imputation, where we generate a subset of the sources given the others (e.g., play a piano track that goes well with the drums). ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Direct Connection:* The paper provides the score-based SDE framework and sampling procedures that this work uses to learn and sample from the joint score of multiple audio sources.

**Slakh2100: A Synthetic Dataset for Audio Source Separation** (2019)
- *Authors:* Ethan Manilow et al.
- *Direct Connection:* This dataset defines the multi-instrument stem setup and evaluation protocol the paper adopts for jointly modeling sources and testing generation, imputation, and separation.

### 💡 Inspiration

**Diffusion Posterior Sampling for General Noisy Inverse Problems** (2022)
- *Authors:* Hyungjin Chung et al.
- *Direct Connection:* DPS’s incorporation of measurement likelihood gradients into reverse diffusion inspires treating source separation as Bayesian inference with a diffusion prior, which this work operationalizes via a Dirac likelihood.

### 📊 Baseline

**Music Source Separation in the Waveform Domain** (2019)
- *Authors:* Alexandre Défossez et al.
- *Direct Connection:* Demucs serves as the main separation baseline whose strong performance but task-specific nature motivates a unified generative model that also handles music generation and source imputation.

### 🔧 Extension

**Denoising Diffusion Restoration Models** (2022)
- *Authors:* Bahjat Kawar et al.
- *Direct Connection:* Their data-consistency formulation for inverse problems directly motivates the paper’s Dirac-likelihood separation inference as a projection onto the constraint set defined by the mixture operator.

### 🔗 Related Problem

**RePaint: Inpainting using Denoising Diffusion Probabilistic Models** (2022)
- *Authors:* Andreas Lugmayr et al.
- *Direct Connection:* RePaint’s clamping of known pixels (a Dirac-like conditioning) informs the paper’s hard-likelihood conditioning strategy, adapted from pixel inpainting to the linear sum constraint of audio source separation.

---

## Synthesis: How Prior Work Led to This Paper

Score-based generative modeling via stochastic differential equations established how to learn noise-conditioned score functions and sample from complex data distributions; critically, it showed that scores of joint distributions can be learned and exploited for flexible conditional sampling. Denoising Diffusion Restoration Models extended diffusion to inverse problems by interleaving denoising with exact data-consistency projections under known forward operators, illustrating how hard measurement constraints can be enforced within diffusion inference. RePaint demonstrated a closely related idea in image inpainting by repeatedly clamping observed pixels during the reverse process, effectively imposing a Dirac-like likelihood on known data. Diffusion Posterior Sampling framed inverse problems as sampling from posteriors defined by a diffusion prior and an explicit likelihood, injecting gradients of log-likelihood into the reverse dynamics. Slakh2100 provided a standardized multi-stem music corpus with aligned sources and mixtures, enabling consistent training and evaluation across separation and generative tasks. Demucs delivered a strong waveform-domain separation baseline, but its specialization to separation highlighted the absence of a single model capable of both generating mixtures/sources and separating them. Together, these works suggest training a single diffusion model on the joint distribution of stems to support unconditional generation, conditional imputation, and separation as posterior inference. By combining joint score learning with inference-time enforcement of exact mixture consistency—generalizing data-consistency and clamping ideas into a Dirac-likelihood formulation—the current approach naturally unifies music generation and source separation within one probabilistic model.

---

*Analysis generated on: 2026-01-06T16:01:41.539319*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

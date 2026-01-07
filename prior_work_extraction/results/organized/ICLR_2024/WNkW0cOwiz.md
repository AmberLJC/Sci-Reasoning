# Prior Work Analysis Report

## Target Paper

**Title:** Lipschitz Singularities in Diffusion Models

**Conference:** ICLR 2024 (oral)

**Authors:** Zhantao Yang, Ruili Feng, Han Zhang, Yujun Shen, Kai Zhu, Lianghua Huang, Yifei Zhang, Yu Liu, Deli Zhao, Jingren Zhou, Fan Cheng

**Keywords:** Image Generation, Generative models, Diffusion models

**Abstract:** 
> Diffusion models, which employ stochastic differential equations to sample images through integrals, have emerged as a dominant class of generative models. However, the rationality of the diffusion process itself receives limited attention, leaving the question of whether the problem is well-posed and well-conditioned. In this paper, we uncover a vexing propensity of diffusion models: they frequently exhibit the infinite Lipschitz near the zero point of timesteps. We provide theoretical proofs t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Direct Connection:* By formulating diffusion models as SDEs/ODEs with time-dependent noise and score scaling, this work exposes the 1/σ(t)-type behavior as t→0 that the current paper formally shows yields infinite Lipschitz constants and then mitigates via time reparameterization.

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* This paper’s discrete-time diffusion formulation and variance schedules define the standard training/inference setup in which the near-zero timestep regime appears, providing the baseline setting where the identified Lipschitz singularity arises.

### 💡 Inspiration

**Elucidating the Design Space of Diffusion-Based Generative Models** (2022)
- *Authors:* Tero Karras et al.
- *Direct Connection:* Their log-SNR parameterization, Karras timestep schedule, and use of a lower noise bound (σ_min) to prevent instability near zero noise directly motivate the present work’s principled analysis of the t→0 pathology and its E‑TSDM time-scaling remedy.

### 📊 Baseline

**Improved Denoising Diffusion Probabilistic Models** (2021)
- *Authors:* Alex Nichol et al.
- *Direct Connection:* Its v-prediction and SNR-based loss weighting are key baselines aimed at stabilizing small-t regimes that the current work supersedes by directly targeting the underlying Lipschitz singularity rather than heuristically reweighting the loss.

### 🔧 Extension

**DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling** (2022)
- *Authors:* Lu et al.
- *Direct Connection:* By integrating the probability-flow ODE in log-SNR time (λ) to reduce stiffness, this method provides the specific change-of-variables idea that the present work extends to regularize the Lipschitz behavior through an explicit time rescaling during training and sampling.

### 🔗 Related Problem

**Rectified Flow: Straightening the Flow of Nonlinear Sample Paths** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* By reparameterizing generative dynamics to produce well-conditioned velocity fields with bounded derivatives, this work highlights the conditioning issue near endpoints that the present paper addresses within the diffusion paradigm by removing the t→0 Lipschitz blow-up.

---

## Synthesis: How Prior Work Led to This Paper

Score-based generative modeling through SDEs established continuous-time diffusion and probability-flow ODEs, making clear how the score and drift scale with the noise level and revealing the potential for unbounded behavior as the noise vanishes. The original DDPM framework defined the discrete schedules and training objective used broadly in practice, where extremely small timesteps concentrate error and instability. Improved DDPM later introduced SNR-based loss weighting and v-prediction to curb instabilities at very high or low noise, offering practical but heuristic mitigation of edge regimes. Elucidating the Design Space (EDM) systematized design choices, introducing log-SNR parameterization, a Karras timestep schedule, and a lower noise floor σ_min that pragmatically avoids the zero-noise regime. Complementarily, DPM-Solver showed that integrating the ODE in log-SNR time reduces stiffness, providing a concrete time change that improves numerical behavior. Rectified Flow further demonstrated that reparameterizing dynamics to straighten trajectories yields better conditioning with bounded derivatives near endpoints. Together, these works expose that instability accumulates near vanishing noise, that loss weighting and hard cutoffs can alleviate it, and that appropriate time reparameterization improves both conditioning and integration. However, a principled diagnosis of the root singularity in diffusion dynamics remained missing. The present paper closes this gap by proving an infinite Lipschitz phenomenon as t→0 and synthesizing the insights from log-SNR parameterization and stiff ODE integration into a time-scaling scheme (E‑TSDM) that regularizes the Lipschitz behavior during both training and sampling, surpassing heuristic SNR weighting and σ cutoffs.

---

*Analysis generated on: 2026-01-06T23:06:26.184330*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

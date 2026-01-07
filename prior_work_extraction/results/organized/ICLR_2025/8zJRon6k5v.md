# Prior Work Analysis Report

## Target Paper

**Title:** Amortized Control of Continuous State Space Feynman-Kac Model for Irregular Time Series

**Conference:** ICLR 2025 (oral)

**Authors:** Byoungwoo Park, Hyungi Lee, Juho Lee

**Keywords:** stochastic optimal control, variational inference, state space model, irregular time series

**Abstract:** 
> Many real-world datasets, such as healthcare, climate, and economics, are often collected as irregular time series, which poses challenges for accurate modeling. In this paper, we propose the Amortized Control of continuous State Space Model (ACSSM) for continuous dynamical modeling of time series for irregular and discrete observations. We first present a multi-marginal Doob's $h$-transform to construct a continuous dynamical system conditioned on these irregular observations. Following this, w...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Variational Sequential Monte Carlo** (2018)
- *Authors:* Christian A. Naesseth et al.
- *Direct Connection:* This paper formalized the Feynman–Kac path-measure view of latent variable models and introduced a tight ELBO via SMC-style variational inference, which ACSSM adopts and strengthens by replacing particle proposals with an SOC-based amortized control that targets the Doob h-transform.

**Guided proposals for simulating diffusion bridges** (2017)
- *Authors:* Moritz Schauer et al.
- *Direct Connection:* This work uses Doob’s h-transform to construct guided drifts that simulate SDEs conditioned on observations, directly underpinning ACSSM’s multi-marginal Doob transform for continuous-time conditioning between irregular observations.

### 💡 Inspiration

**Diffusion Schrödinger Bridge with Score Matching** (2021)
- *Authors:* Guillaume De Bortoli et al.
- *Direct Connection:* By casting conditioning as a Schrödinger bridge (variational control) problem over path measures, this work motivates ACSSM’s SOC-based approximation of the intractable Doob h-transform to simulate posterior-conditioned dynamics.

### 🔍 Gap Identification

**Neural Controlled Differential Equations for Irregular Time Series** (2020)
- *Authors:* Patrick Kidger et al.
- *Direct Connection:* While NCDEs handle irregular sampling with controlled paths, they do not provide a principled multi-marginal conditioning mechanism or a tight ELBO over path measures, a gap ACSSM fills via the Doob h-transform and SOC-driven variational inference.

### 📊 Baseline

**Latent ODEs for Irregularly-Sampled Time Series** (2019)
- *Authors:* Yulia Rubanova et al.
- *Direct Connection:* Latent ODEs defined the continuous-time latent modeling setup for irregular observations that ACSSM targets, and ACSSM improves upon it by explicitly constructing posterior-conditioned dynamics via an h-transform and control, rather than unconditioned forward flows.

### 🔧 Extension

**Controlled Sequential Monte Carlo** (2019)
- *Authors:* Jeremy Heng et al.
- *Direct Connection:* Heng et al. variationally approximate the optimal Doob h-transform (twisting) within discrete-time Feynman–Kac models, and ACSSM generalizes this control-as-inference idea to continuous-time multi-marginal conditioning with amortized neural controls and a tight ELBO.

### 🔗 Related Problem

**Conditional Flow Matching: Simulation-Free Training of Conditional Continuous Normalizing Flows** (2023)
- *Authors:* Alexander Tong et al.
- *Direct Connection:* This work introduced simulation-free training for conditional continuous-time flows, informing ACSSM’s simulation-free latent dynamics component that amortizes control between irregular observation constraints.

---

## Synthesis: How Prior Work Led to This Paper

Variational Sequential Monte Carlo framed latent variable learning in terms of Feynman–Kac path measures and introduced a tight ELBO using sequential proposals, establishing the variational machinery and objective that enable path-space inference. Building on the same Feynman–Kac formalism, Controlled Sequential Monte Carlo showed that the optimal way to condition on observations is via the Doob h-transform and proposed a variational control approximation, clarifying that ‘twisting’ can be learned. In continuous time, guided diffusion bridge methods make the Doob h-transform concrete by adjusting SDE drifts to target observation-conditioned trajectories, providing a constructive blueprint for conditioning dynamics. Schrödinger bridge methods further recast conditioning as a stochastic optimal control problem over path measures, linking desirability functions to the Doob transform and suggesting variational objectives that target the posterior dynamics. Meanwhile, Latent ODEs and Neural CDEs established continuous-time latent modeling for irregular sampling but lacked a principled multi-marginal conditioning mechanism and typically relied on forward simulation rather than posterior-driven dynamics. Conditional Flow Matching introduced simulation-free training for conditional flows, showing how to learn vector fields that satisfy boundary constraints without trajectory simulation.
These strands together exposed a natural opportunity: use the Doob h-transform as the canonical target for observation-conditioned dynamics, approximate it via stochastic optimal control in a variational framework compatible with Feynman–Kac ELBOs, and implement it in a continuous-time model for irregular observations with simulation-free training. ACSSM synthesizes these insights by formulating a multi-marginal Doob transform for irregularly sampled constraints, amortizing the associated control to yield scalable inference and learning, and incorporating a simulation-free latent dynamics parameterization to improve efficiency while preserving a tight ELBO.

---

*Analysis generated on: 2026-01-06T17:21:33.923322*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

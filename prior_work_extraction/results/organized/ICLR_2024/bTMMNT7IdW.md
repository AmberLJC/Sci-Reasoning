# Prior Work Analysis Report

## Target Paper

**Title:** Latent Trajectory Learning for Limited Timestamps under Distribution Shift over Time

**Conference:** ICLR 2024 (oral)

**Authors:** QIUHAO Zeng, Changjian Shui, Long-Kai Huang, Peng Liu, Xi Chen, Charles Ling, Boyu Wang

**Keywords:** Distribution Shift, Temporal Distribution Shift

**Abstract:** 
> Distribution shifts over time are common in real-world machine-learning applications. This scenario is formulated as Evolving Domain Generalization (EDG), where models aim to generalize well to unseen target domains in a time-varying system by learning and leveraging the underlying evolving pattern of the distribution shifts across domains. However, existing methods encounter challenges due to the limited number of timestamps (every domain corresponds to a timestamp) in EDG datasets, leading to ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Latent ODEs for Irregularly-Sampled Time Series** (2019)
- *Authors:* Yulia Rubanova et al.
- *Direct Connection:* Latent ODEs establish the idea of learning continuous latent trajectories from sparse time-stamped observations, which SDE-EDG generalizes to stochastic latent dynamics at the distribution level under temporal shift.

**WILDS: A Benchmark of In-the-Wild Distribution Shifts** (2021)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* WILDS formalizes temporally evolving distribution shifts in realistic datasets (e.g., time-indexed domains), grounding the EDG problem setting that SDE-EDG targets and highlighting the scarcity of timestamps in practice.

### 💡 Inspiration

**CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation** (2021)
- *Authors:* Yuta Tashiro et al.
- *Direct Connection:* CSDI shows that score-based diffusion can impute unobserved time points from sparse observations, inspiring SDE-EDG’s use of SDE-driven interpolation to bridge temporal gaps between EDG domains.

**Diffusion Schrödinger Bridge with Applications to Score-Based Generative Modeling** (2021)
- *Authors:* Guillaume De Bortoli et al.
- *Direct Connection:* By formulating stochastic bridges that interpolate between endpoint distributions using score information, this work motivates SDE-EDG’s bridge-style interpolation between consecutive domains to densify the temporal trajectory.

### 🔧 Extension

**Score-Based Generative Modeling through Stochastic Differential Equations** (2020)
- *Authors:* Yang Song et al.
- *Direct Connection:* This work provides the SDE-based generative framework and reverse-time sampling that SDE-EDG directly adapts to synthesize continuous-interpolated samples between sparse timestamps for constructing an infinitely fine-grained distribution trajectory.

### 🔗 Related Problem

**TrajectoryNet: A Dynamic Optimal Transport Network for Modeling Cellular Dynamics** (2020)
- *Authors:* Alexander Tong et al.
- *Direct Connection:* TrajectoryNet learns continuous flows between time-stamped empirical distributions, a paradigm SDE-EDG adapts to EDG by replacing deterministic CNF/ODE flows with SDE-based latent trajectories to avoid overfitting with few timestamps.

---

## Synthesis: How Prior Work Led to This Paper

Score-based generative modeling through stochastic differential equations showed how a forward diffusion and reverse-time SDE can generate samples along a continuous time axis, establishing a principled way to traverse intermediate times between observed snapshots. Building on this, CSDI demonstrated that score-based diffusion can impute missing time points from sparse observations, directly evidencing that diffusion/SDE machinery can bridge temporal gaps. Latent ODEs introduced the notion of learning continuous latent trajectories from irregularly sampled data, enabling interpolation and extrapolation from few timestamps via latent dynamics. TrajectoryNet extended continuous-time modeling to distributional snapshots, learning flows that connect empirical distributions across observed times with CNF/ODE dynamics. Diffusion Schrödinger bridges further showed that stochastic bridges guided by scores can interpolate between endpoint distributions, offering a robust alternative to deterministic flows when data are sparse or noisy. Complementing these modeling advances, WILDS crystallized real-world, time-indexed distribution shifts that motivate methods capable of generalizing to unseen future domains despite limited timestamps.
Together these works reveal a gap: deterministic flows and per-series imputers falter when only a few domain timestamps exist and the goal is distribution-level generalization to future times. The present paper synthesizes score-SDE generation, bridge-style interpolation, and continuous latent dynamics to learn a stochastic latent trajectory of the evolving distribution, densifying the timeline with continuous-interpolated samples (an infinitely fine grid) and thereby mitigating overfitting to sparse timestamps and improving EDG generalization.

---

*Analysis generated on: 2026-01-06T18:30:38.076943*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

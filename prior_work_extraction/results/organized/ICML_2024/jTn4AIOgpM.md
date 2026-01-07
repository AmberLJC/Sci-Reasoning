# Prior Work Analysis Report

## Target Paper
**Title:** jTn4AIOgpM
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Variational Learning of Inducing Variables in Sparse Gaussian Processes** (2009)
- *Authors:* Michalis Titsias
- *Connection:* This paper introduced the inducing-variable framework and variational objective that define the very posterior over inducing points that the present work seeks to sample via diffusion rather than approximate with a biased variational family.

**Gaussian Processes for Big Data** (2013)
- *Authors:* James Hensman et al.
- *Connection:* By developing stochastic variational inference for inducing-point GPs, this work established the scalable VI machinery whose bias and factorization assumptions the current paper replaces with diffusion-based posterior sampling for inducing variables.

**Deep Gaussian Processes** (2013)
- *Authors:* Andreas C. Damianou et al.
- *Connection:* This paper formulated Deep Gaussian Processes—the hierarchical GP model and inducing-variable setup that define the problem setting in which the proposed DDVI method operates.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Connection:* The paper’s SDE formulation of diffusion models supplies the exact denoising diffusion SDE machinery the current work leverages to generate posterior samples of inducing variables and connect to KL objectives via SDE theory.

### 💡 Inspiration

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Jonathan Ho et al.
- *Connection:* This work provided the denoising diffusion framework and training perspective that inspired using denoising-based objectives to approximate gradients (scores) for sampling from complex posteriors.

### 📊 Baseline

**Doubly Stochastic Variational Inference for Deep Gaussian Processes** (2017)
- *Authors:* Hugh Salimbeni et al.
- *Connection:* As the dominant inference method for DGPs using variational posteriors over inducing points, DSVI is the primary baseline whose limitations (variational bias) the proposed DDVI directly addresses by replacing the variational posterior with diffusion-SDE–based sampling.

### 🔧 Extension

**Generative Modeling by Estimating Gradients of the Data Distribution** (2019)
- *Authors:* Yang Song et al.
- *Connection:* The noise-conditioned score network and denoising score matching objective from this paper are directly adapted to learn the intractable score of the inducing-variable posterior needed for DDVI sampling.

---

## Synthesis

The core contribution—using a denoising diffusion SDE with score matching to infer the posterior of inducing variables in deep Gaussian processes—stands on two intertwined lineages. From the GP side, Titsias (2009) formalized inducing variables and a variational objective for sparse GPs, defining the posterior over inducing points that modern scalable methods approximate. Hensman et al. (2013) extended this to stochastic variational inference, making large-scale GP training feasible but preserving variational assumptions that can bias posteriors. Damianou and Lawrence (2013) introduced Deep Gaussian Processes, and Salimbeni and Deisenroth (2017) provided the DSVI framework, which became the standard baseline for DGP inference yet inherits variational bias—precisely the gap this paper targets.
From the diffusion/score-based modeling side, Song and Ermon (2019) introduced noise-conditioned score networks and denoising score matching, the practical recipe used here to approximate otherwise intractable score functions. Ho et al. (2020) popularized denoising diffusion training as a robust generative framework, motivating the use of denoising objectives to parameterize reverse dynamics. Crucially, Song et al. (2021) recast diffusion as stochastic differential equations, providing the continuous-time SDE formalism and theoretical tools that this paper directly employs to sample from the inducing-variable posterior and couple these dynamics with a KL-based objective. Together, these works enable the shift from biased variational approximations in DGPs to diffusion-SDE–driven posterior sampling with learned scores, yielding more faithful inducing-point inference.

---
*Generated: 2026-01-06T23:09:26.471964*

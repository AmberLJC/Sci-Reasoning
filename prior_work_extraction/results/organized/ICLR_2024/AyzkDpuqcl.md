# Prior Work Analysis Report

## Target Paper

**Title:** Learning Energy-Based Models by Cooperative Diffusion Recovery Likelihood

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yaxuan Zhu, Jianwen Xie, Ying Nian Wu, Ruiqi Gao

**Keywords:** Energy-based model, recovery-likelihood, cooperative learning

**Abstract:** 
> Training energy-based models (EBMs) on high-dimensional data can be both challenging and time-consuming, and there exists a noticeable gap in sample quality between EBMs and other generative frameworks like GANs and diffusion models. To close this gap, inspired by the recent efforts of learning EBMs by maximimizing diffusion recovery likelihood (DRL), we propose cooperative diffusion recovery likelihood (CDRL), an effective approach to tractably learn and sample from a series of EBMs defined on ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Generative Modeling by Estimating Gradients of the Data Distribution** (2019)
- *Authors:* Yang Song et al.
- *Direct Connection:* CDRL adopts the noise-conditional, multi-level formulation and few-step Langevin refinement strategy introduced for score-based models to define and sample a family of EBMs across increasing noise levels.

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* The diffusion forward-noising schedule and per-step denoising (recovery) perspective from DDPM provide the corruption ladder and recovery interpretation that CDRL uses to define EBMs at each noise level.

**A Connection Between Score Matching and Denoising Autoencoders** (2011)
- *Authors:* Pascal Vincent
- *Direct Connection:* The denoising-as-likelihood insight underpins CDRL’s recovery-likelihood objective by linking learning from corrupted data to estimating clean data statistics.

### 💡 Inspiration

**Variational Diffusion Models** (2021)
- *Authors:* Diederik P. Kingma et al.
- *Direct Connection:* VDM’s likelihood-based view of diffusion training motivates CDRL’s use of diffusion recovery likelihood as a tractable objective for fitting EBMs on noisy data states.

### 🔍 Gap Identification

**Learning Energy-Based Models by Short-Run MCMC Sampling** (2019)
- *Authors:* Erik Nijkamp et al.
- *Direct Connection:* Short-run MCMC exposed the difficulty and bias of few-step EBM learning in high dimensions, a limitation CDRL addresses by grounding refinement in diffusion recovery likelihood and amortizing initialization.

### 🔧 Extension

**Cooperative Training of Descriptor and Generator Networks** (2016)
- *Authors:* Jianwen Xie et al.
- *Direct Connection:* The paper directly extends CoopNets’ MCMC-teaching idea by pairing each noise-level EBM with an initializer model that learns from the difference between EBM-refined samples and its own outputs.

---

## Synthesis: How Prior Work Led to This Paper

CoopNets established a cooperative learning paradigm where a generator initializes samples that a descriptor (EBM) refines via short MCMC steps, and the generator learns from the refinement—an MCMC teaching mechanism that amortizes sampling. Score-based generative modeling introduced a noise-conditional formulation: learn a family of objectives tied to increasing corruption levels and use few-step Langevin refinement, operationalizing multi-level modeling and annealed sampling. DDPM formalized a forward noising process and reverse denoising view, providing the corruption ladder and per-step recovery interpretation that align naturally with defining models over noisy states. Variational Diffusion Models reframed diffusion training as likelihood maximization, clarifying how per-step denoising terms constitute a tractable likelihood surrogate. Vincent’s denoising–score matching connection grounded learning from corrupted observations as estimating clean data structure through recovery. Meanwhile, short-run MCMC highlighted the instability and bias of few-step refinement when used to train EBMs directly in high dimensions, revealing a gap between practicality and fidelity. Together, these works suggested that EBMs could be trained more stably on noise-conditional targets defined by diffusion corruption while retaining fast refinement through amortized initialization. The current approach synthesizes this by defining EBMs at each diffusion noise level and optimizing them via diffusion recovery likelihood, while jointly training an initializer at every level through cooperative learning so that a few MCMC steps suffice for high-quality refinement and efficient sampling.

---

*Analysis generated on: 2026-01-06T23:03:52.259488*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

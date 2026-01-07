# Prior Work Analysis Report

## Target Paper

**Title:** Monte Carlo guided Denoising Diffusion models for Bayesian linear inverse problems.

**Conference:** ICLR 2024 (oral)

**Authors:** Gabriel Cardoso, Yazid Janati el idrissi, Sylvain Le Corff, Eric Moulines

**Keywords:** Monte Carlo, Denoising Diffusion model, score-based generative models, Sequential Monte Carlo, Bayesian Inverse Problems, Generative Models.

**Abstract:** 
> Ill-posed linear inverse problems arise frequently in various applications, from computational photography to medical imaging.
A recent line of research exploits Bayesian inference with informative priors to handle the ill-posedness of such problems.
Amongst such priors, score-based generative models (SGM) have recently been successfully applied to several different inverse problems.
In this study, we exploit the particular structure of the prior defined by the SGM to define a sequence of interm...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Generative Modeling by Estimating Gradients of the Data Distribution** (2019)
- *Authors:* Yang Song et al.
- *Direct Connection:* This work introduced learning scores ∇x log pσ(x) for a ladder of Gaussian-smoothed priors pσ, which the present paper exploits to define the intermediate posteriors pσ(x|y) and to evaluate the prior-score component at each SMC stage.

**Sequential Monte Carlo Samplers** (2006)
- *Authors:* Pierre Del Moral et al.
- *Direct Connection:* Provides the SMC sampler framework—importance weighting, resampling, and rejuvenation over a sequence of target distributions—that the present work instantiates on the diffusion-induced ladder of posteriors.

**Inverse Problems: A Bayesian Perspective** (2010)
- *Authors:* Andrew M. Stuart
- *Direct Connection:* Establishes the Bayesian formulation for linear inverse problems with Gaussian noise, defining the likelihood and target posterior measure that the proposed SMC-over-σ scheme is designed to approximate.

### 💡 Inspiration

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Direct Connection:* By formalizing diffusion as a continuous-time process with predictor–corrector moves across decreasing noise levels, this paper motivates using learned score-guided Markov transitions along a decreasing-σ sequence—an idea the current work adapts for SMC over posterior targets.

**Annealed Importance Sampling** (2001)
- *Authors:* Radford M. Neal
- *Direct Connection:* Introduces bridging from prior to posterior via a tempered sequence, directly inspiring the idea of replacing temperature with diffusion noise levels as the annealing schedule inside an SMC scheme.

### 🔍 Gap Identification

**Denoising Diffusion Restoration Models** (2022)
- *Authors:* Bahjat Kawar et al.
- *Direct Connection:* Shows diffusion-based restoration for linear inverse problems via data-consistency operations but yields deterministic reconstructions without posterior uncertainty, a gap the present work fills by sampling the full Bayesian posterior.

### 📊 Baseline

**Diffusion Posterior Sampling for General Noisy Inverse Problems** (2023)
- *Authors:* Hyungjin Chung et al.
- *Direct Connection:* Proposes sampling p(x|y) by approximating the posterior score with the sum of a learned prior score and the likelihood score, which the current work replaces with a principled SMC over σ-indexed posteriors to improve robustness in ill-posed settings.

---

## Synthesis: How Prior Work Led to This Paper

A key ingredient for recent inverse-problem solvers is the ability to evaluate scores of Gaussian-smoothed data distributions across a noise ladder; this comes from Song et al.’s noise-conditional score networks, which learn ∇x log pσ(x) for multiple σ and enable annealed sampling. The SDE view of diffusion further systematized sampling along decreasing noise with predictor–corrector moves, clarifying how learned scores guide transitions as σ decreases. On the Bayesian side, Del Moral, Doucet, and Jasra established Sequential Monte Carlo samplers, which transport a particle system through a sequence of intermediate targets using importance weighting, resampling, and rejuvenation kernels. Neal’s annealed importance sampling highlighted the power of bridging distributions, typically via temperature schedules, to connect prior and posterior. In inverse problems, Diffusion Posterior Sampling (DPS) leveraged the decomposition ∇x log p(x|y)=∇x log p(x)+∇x log p(y|x) to steer reverse diffusion with likelihood gradients, while Denoising Diffusion Restoration Models (DDRM) solved linear inverse problems with data-consistency operations but produced point estimates rather than posterior samples. Stuart’s Bayesian formulation provides the likelihood and posterior measure for linear inverse problems under Gaussian noise. Together, these works reveal a gap: diffusion priors give a natural σ-indexed family pσ(x), but posterior samplers either rely on heuristic guidance (DPS) or forgo uncertainty (DDRM), while SMC offers a principled pathway if one can specify an appropriate sequence. The natural synthesis is to replace temperature with diffusion noise levels and define σ-indexed posteriors pσ(x|y), then use SMC with score-guided Markov moves to traverse this ladder, yielding theoretically grounded Bayesian posterior sampling even in ill-posed regimes.

---

*Analysis generated on: 2026-01-06T17:16:12.562546*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

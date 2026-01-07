# Prior Work Analysis Report

## Target Paper
**Title:** IJLqUjtrls
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Denoising Diffusion Restoration Models** (2022)
- *Authors:* Bahjat Kawar et al.
- *Connection:* DDRM established the paradigm of solving inverse problems by combining a pretrained diffusion prior with a measurement model without retraining; the present work adopts this decoupling and generalizes it via adaptive likelihood updates for arbitrary measurements.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Connection:* The SDE framework and predictor–corrector sampling provide the backbone on which the paper inserts its adaptive likelihood ‘corrector’; FCM supplies a principled step size for that correction based on local curvature.

**Plug-and-Play Priors for Model Based Reconstruction** (2013)
- *Authors:* Sreehari Venkatakrishnan et al.
- *Connection:* PnP introduced decoupling a learned prior from a data-consistency update; the new method follows this separation but replaces heuristic data-consistency step sizes with curvature-matched updates computed on-the-fly.

### 💡 Inspiration

**Diffusion Models Beat GANs on Image Synthesis** (2021)
- *Authors:* Prafulla Dhariwal et al.
- *Connection:* Classifier guidance formalized adding a log-likelihood gradient to diffusion sampling with a tunable scale; FCM generalizes this idea by choosing the guidance scale optimally per step via forward curvature matching for measurement likelihoods.

**Two-Point Step Size Gradient Methods** (1988)
- *Authors:* Jonathan Barzilai et al.
- *Connection:* The proposed curvature-matching step selection extends the secant/finite-difference curvature ideas of Barzilai–Borwein to the diffusion-guided likelihood update, yielding adaptive step sizes without explicit Hessians.

### 📊 Baseline

**Diffusion Posterior Sampling for Inverse Problems** (2022)
- *Authors:* Hyeongjin Chung et al.
- *Connection:* The proposed Forward Curvature-Matching (FCM) directly replaces DPS’s heuristic, fixed-size likelihood updates with an adaptive, curvature-matched step that improves convergence and reconstruction fidelity.

### 🔧 Extension

**Fast Exact Multiplication by the Hessian** (1994)
- *Authors:* Barak A. Pearlmutter
- *Connection:* FCM leverages forward-mode automatic differentiation/JVPs for efficient directional curvature estimation, a direct practical application of Pearlmutter’s Hessian–vector product technique to tune diffusion likelihood steps.

---

## Synthesis

The paper’s core contribution—Forward Curvature-Matching (FCM) for adaptive likelihood updates inside diffusion sampling—emerges directly from the diffusion-with-likelihood lineage and classical curvature-based step selection. Diffusion Posterior Sampling (DPS) is the immediate baseline: it couples a pretrained diffusion prior with measurement-consistency gradients but uses heuristic, fixed step sizes that can slow convergence and degrade reconstructions. The current work targets this precise gap by replacing DPS’s fixed updates with curvature-matched, per-step step sizes. The broader foundation is the score-based SDE framework and predictor–corrector samplers, which establish where and how a likelihood ‘corrector’ integrates into diffusion sampling; FCM becomes a principled corrector that adapts its strength using local curvature. Classifier guidance in diffusion models showed that adding a likelihood gradient with a tunable scale can steer sampling; FCM generalizes this idea by computing the optimal scale automatically for measurement likelihoods rather than hand-tuning. DDRM and Plug-and-Play Priors provide the conceptual grounding of decoupling the prior from the measurement model to avoid retraining and fixed conditioning, a paradigm this paper embraces while improving the likelihood update itself. Technically, FCM is enabled by Pearlmutter’s Hessian–vector products via forward-mode AD to obtain efficient directional curvature, and it is inspired by Barzilai–Borwein’s finite-difference curvature matching to set step sizes without explicit Hessians. Together, these works directly shape the proposed adaptive likelihood update that yields faster, higher-fidelity 3D reconstructions.

---
*Generated: 2026-01-06T23:08:23.938444*

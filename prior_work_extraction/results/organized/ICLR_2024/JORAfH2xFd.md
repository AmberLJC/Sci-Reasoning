# Prior Work Analysis Report

## Target Paper

**Title:** On the Stability of Iterative Retraining of Generative Models on their own Data

**Conference:** ICLR 2024 (spotlight)

**Authors:** Quentin Bertrand, Joey Bose, Alexandre Duplessis, Marco Jiralerspong, Gauthier Gidel

**Keywords:** Generative Models, Iterative Training, Diffusion

**Abstract:** 
> Deep generative models have made tremendous progress in modeling complex data, often exhibiting generation quality that surpasses a typical human's ability to discern the authenticity of samples. Undeniably, a key driver of this success is enabled by the massive amounts of web-scale data consumed by these models. Due to these models' striking performance and ease of availability, the web will inevitably be increasingly populated with synthetic content. Such a fact directly implies that future it...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Estimation of Non-Normalized Statistical Models by Score Matching** (2005)
- *Authors:* Aapo Hyvärinen
- *Direct Connection:* The stability analysis rests on Fisher divergence and the geometry of score matching introduced here, modeling iterative retraining as repeated projection of true scores onto a model class.

**A Connection Between Score Matching and Denoising Autoencoders** (2011)
- *Authors:* Pascal Vincent
- *Direct Connection:* The equivalence between denoising and score matching for Gaussian corruption provides the exact training objective whose behavior under mixed real/synthetic data the paper studies.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Direct Connection:* The noise-conditioned score learning and multi-sigma training formalized here define the diffusion/score-based objectives to which the paper’s stability guarantees apply.

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* The denoising loss and noise schedule of DDPMs are the concrete objective the paper analyzes when retraining on mixtures of real and synthetic data.

### 💡 Inspiration

**What Regularized Auto-Encoders Learn from the Data-Generating Distribution** (2014)
- *Authors:* Guillaume Alain et al.
- *Direct Connection:* The result that denoising/regularized autoencoders estimate the data score underpins the paper’s view of retraining as score projection, enabling a self-consistency argument across iterations.

### 🔍 Gap Identification

**The Curse of Recursion: Training on Generated Data Makes Models Forget** (2023)
- *Authors:* Ilia Shumailov et al.
- *Direct Connection:* This work documented collapse when models are iteratively retrained on their own samples, and the present paper directly targets this exact self-consuming retraining setting by proving conditions under which it is in fact stable.

**Self-Consuming Generative Models Go MAD** (2023)
- *Authors:* Rima Somepalli et al.
- *Direct Connection:* By introducing Model Autophagy Disorder and showing support shrinkage from training on synthetic data, this paper crystallized the failure mode that the current work explains and mitigates via a formal stability framework.

---

## Synthesis: How Prior Work Led to This Paper

Empirical work on feedback loops first showed concrete failure modes when generative models repeatedly train on their own outputs: one study demonstrated progressive forgetting and coverage loss under recursive retraining, while another introduced Model Autophagy Disorder to describe support shrinkage caused by self-consumption of synthetic data. Separately, the theory of score matching established Fisher divergence as a principled objective for learning unnormalized distributions by matching data scores, giving a geometric view of training as projection in score space. Its denoising variant rigorously connected Gaussian denoising to score estimation, and further results on regularized autoencoders proved that denoising objectives estimate the gradient of the log-density, suggesting a self-consistency structure for noisy data. Modern diffusion and score-based generative modeling then operationalized these insights: DDPMs defined a practical denoising loss under a noise schedule, and the SDE formulation generalized this to noise-conditioned score learning across multiple sigmas. Together, these lines defined both the practical training objective and the mathematical geometry of scores.
Bringing these threads together, the current work views iterative retraining on mixed real/synthetic datasets through the geometry of score projections induced by denoising/score-matching objectives. The empirical reports of collapse posed a clear gap—no formal conditions explained when feedback loops should fail versus remain stable. By leveraging Fisher-divergence projection properties and the noise-conditioned training structure from diffusion/score-based models, the paper shows that with sufficiently accurate initialization and a nontrivial fraction of real data, retraining constitutes a contraction toward the true score, thereby establishing provable stability and precisely delineating regimes where the empirically observed collapse can or cannot arise.

---

*Analysis generated on: 2026-01-06T17:13:42.503430*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

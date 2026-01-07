# Prior Work Analysis Report

## Target Paper

**Title:** Solving Inverse Problems with Latent Diffusion Models via Hard Data Consistency

**Conference:** ICLR 2024 (spotlight)

**Authors:** Bowen Song, Soo Min Kwon, Zecheng Zhang, Xinyu Hu, Qing Qu, Liyue Shen

**Keywords:** Diffusion models, inverse problems

**Abstract:** 
> Latent diffusion models have been demonstrated to generate high-quality images, while offering efficiency in model training compared to diffusion models operating in the pixel space. However, incorporating latent diffusion models to solve inverse problems remains a challenging problem due to the nonlinearity of the encoder and decoder. To address these issues, we propose ReSample, an algorithm that can solve general inverse problems with pre-trained latent diffusion models. Our algorithm incorpo...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Direct Connection:* This work introduced the latent diffusion framework and non-linear VAE encoder/decoder that ReSample explicitly builds upon and must reconcile with when enforcing measurement consistency.

**Plug-and-Play Priors for Model Based Reconstruction** (2013)
- *Authors:* S. H. Venkatakrishnan et al.
- *Direct Connection:* The plug-and-play paradigm of alternating a data-fidelity proximal (projection) step with a learned denoiser underlies ReSample’s hard data consistency subproblem embedded at each diffusion timestep.

### 💡 Inspiration

**ILVR: Conditioning Method for Denoising Diffusion Probabilistic Models** (2021)
- *Authors:* Jooyoung Choi et al.
- *Direct Connection:* ILVR shows that repeatedly enforcing a degradation-consistent constraint inside the reverse process improves conditioning, inspiring ReSample’s projection/optimization-style enforcement of measurement consistency within diffusion steps.

**SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations** (2022)
- *Authors:* Chenlin Meng et al.
- *Direct Connection:* SDEdit’s principle of adding the appropriate noise and then denoising to stay on the correct diffusion trajectory directly informs ReSample’s resampling step that maps a measurement-consistent update back to the noisy data manifold.

### 🔍 Gap Identification

**Denoising Diffusion Restoration Models** (2022)
- *Authors:* Nimrod Kawar et al.
- *Direct Connection:* DDRM achieves exact (hard) data consistency for linear degradations with pixel-space diffusion models, whose linearity and pixel-domain restrictions motivate ReSample’s generalization to latent diffusion and nonlinear forward models.

### 📊 Baseline

**Diffusion Posterior Sampling for General Noisy Inverse Problems** (2022)
- *Authors:* Hyungjin Chung et al.
- *Direct Connection:* DPS adds a likelihood-gradient (soft data consistency) term during reverse diffusion, which ReSample directly replaces with an optimization-based hard data consistency step and subsequently improves with a resampling back to the noise manifold.

---

## Synthesis: How Prior Work Led to This Paper

Latent diffusion models introduced the idea of performing generative modeling in a learned VAE latent space, where a non-linear encoder/decoder trades sample quality and efficiency against the difficulty of imposing constraints in image space. Diffusion Posterior Sampling established a practical way to solve inverse problems by injecting the likelihood gradient as a soft data-consistency correction within reverse diffusion. Denoising Diffusion Restoration Models demonstrated that hard data consistency can be achieved in the diffusion loop for linear degradations with pixel-space models via closed-form conditioning, highlighting both the power and the limitations of exact consistency. ILVR showed that repeatedly enforcing a degradation-driven constraint during sampling (e.g., by replacing low-frequency components) can strongly condition the generation process, pointing to projection-style updates as effective controls. SDEdit clarified how adding the correct amount of forward noise and then denoising keeps samples on the appropriate noise manifold, a key consideration when interleaving external constraints. Finally, Plug-and-Play Priors provided the core algorithmic pattern of alternating a data-fidelity proximal step with a learned prior, foreshadowing optimization-in-the-loop conditioning.
Together, these works exposed a gap: soft guidance can be unstable or biased for challenging operators, while hard consistency was confined to pixel-space and linear models, and naive projections can drift off the diffusion trajectory. The current paper synthesizes these elements by embedding an optimization-based hard data-consistency step inside latent diffusion and immediately resampling to return to the noisy manifold, thus generalizing the ILVR/DDRM-style exact conditioning to nonlinear and latent settings while preserving the principled trajectory control suggested by SDEdit and the PnP paradigm.

---

*Analysis generated on: 2026-01-06T12:53:30.641588*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

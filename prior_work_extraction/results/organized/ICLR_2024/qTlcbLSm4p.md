# Prior Work Analysis Report

## Target Paper

**Title:** Relay Diffusion: Unifying diffusion process across resolutions for image synthesis

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jiayan Teng, Wendi Zheng, Ming Ding, Wenyi Hong, Jianqiao Wangni, Zhuoyi Yang, Jie Tang

**Keywords:** generative models, diffusion model, image synthesis

**Abstract:** 
> Diffusion models achieved great success in image synthesis, but still face challenges in high-resolution generation. Through the lens of discrete cosine transformation, we find the main reason is that *the same noise level on a higher resolution results in a higher Signal-to-Noise Ratio in the frequency domain*. In this work, we present Relay Diffusion Model (RDM), which transfers a low-resolution image or noise into an equivalent high-resolution one for diffusion model via blurring diffusion an...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Image Super-Resolution via Iterative Refinement (SR3)** (2021)
- *Authors:* Chitwan Saharia et al.
- *Direct Connection:* RDM builds on the diffusion-based super-resolution formulation of SR3 but replaces starting from pure high-resolution noise with a continuation from a matched noisy state constructed from the low-resolution sample.

**Denoising Diffusion Implicit Models (DDIM)** (2020)
- *Authors:* Jiaming Song et al.
- *Direct Connection:* RDM relies on the DDIM notion of timestep/state equivalence—matching signal-to-noise across steps—to justify continuing the diffusion trajectory when switching resolutions.

### 💡 Inspiration

**SDEdit: Image Synthesis and Editing with Stochastic Differential Equations** (2022)
- *Authors:* Chenlin Meng et al.
- *Direct Connection:* RDM generalizes SDEdit’s idea of adding noise to an existing image to continue denoising by devising blurring diffusion plus block-noise to create a high-resolution image that is at the same effective timestep as the low-resolution state.

**Elucidating the Design Space of Diffusion-Based Generative Models** (2022)
- *Authors:* Tero Karras et al.
- *Direct Connection:* RDM adopts the SNR-centric perspective from EDM and extends it to the frequency domain, identifying and correcting the resolution-dependent SNR mismatch that harms high-resolution sampling.

### 🔍 Gap Identification

**Cascaded Diffusion Models for High Fidelity Image Generation** (2022)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* RDM explicitly eliminates the need to restart denoising at each scale introduced by cascaded diffusion, instead relaying the same diffusion state across resolutions via an "equivalent" high-resolution noisy state.

### 📊 Baseline

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Direct Connection:* As a principal high-resolution baseline, LDM is contrasted with RDM, which achieves comparable or better fidelity without relying on a latent autoencoder by relaying a single diffusion process across resolutions.

**Diffusion Models Beat GANs on Image Synthesis** (2021)
- *Authors:* Prafulla Dhariwal et al.
- *Direct Connection:* ADM serves as a core pixel-space baseline that RDM surpasses while explaining ADM’s high-resolution limitations via the frequency-domain SNR disparity that RDM corrects.

---

## Synthesis: How Prior Work Led to This Paper

Cascaded Diffusion Models introduced a coarse-to-fine pipeline with a base generator followed by super-resolution diffusion upsamplers, but each stage began from fresh noise, severing any continuity in the diffusion trajectory. SR3 established the diffusion formulation for super-resolution, defining how to condition on a low-resolution input while denoising at the target resolution, yet it also operated from pure high-resolution noise. SDEdit demonstrated that one can inject noise into an existing image and then continue denoising, effectively treating an image as a valid intermediate state in the diffusion process. DDIM formalized the idea that diffusion states are characterized by their timestep-dependent signal-to-noise ratios, enabling deterministic mappings and consistent continuation between timesteps. EDM elevated SNR to the central lens for designing diffusion training and sampling, showing that aligning signal-to-noise across steps is key to stable generation. Latent Diffusion offered a strong high-resolution path via a lower-resolution latent space, serving as a practical baseline for fidelity and efficiency, while ADM established a pixel-space reference point for unconditional image quality. Together, these works revealed a gap: high-resolution methods either restart the stochastic process at each scale or avoid pixel space entirely, and none account for how the same nominal noise behaves differently across resolutions in the frequency domain. Relay Diffusion synthesizes these insights by treating diffusion states as SNR-defined entities and, inspired by SDEdit’s continuation mechanism, constructs an equivalent high-resolution noisy state via blurring diffusion and block noise, allowing a single trajectory to persist seamlessly across resolutions and models.

---

*Analysis generated on: 2026-01-06T15:58:02.614485*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

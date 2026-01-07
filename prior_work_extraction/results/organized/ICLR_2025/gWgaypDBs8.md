# Prior Work Analysis Report

## Target Paper

**Title:** Representative Guidance: Diffusion Model Sampling with Coherence

**Conference:** ICLR 2025 (spotlight)

**Authors:** Anh-Dung Dinh, Daochang Liu, Chang Xu

**Keywords:** generative models, diffusion model

**Abstract:** 
> The diffusion sampling process faces a persistent challenge stemming from its incoherence, attributable to varying noise directions across different timesteps.
Our Representative Guidance (RepG) offers a new perspective to address this issue by reformulating the sampling process with a coherent direction toward a representative target.
From this perspective, classic classifier guidance reveals its drawback in lacking meaningful representative information, as the features it relies on are optimiz...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Emerging Properties in Self-Supervised Vision Transformers (DINO)** (2021)
- *Authors:* Mathilde Caron et al.
- *Direct Connection:* RepG leverages DINO-like self-supervised features as the coherent, category-agnostic target because they capture holistic semantics and remain stable across views—precisely the representative signal needed for timestep-consistent guidance.

### 💡 Inspiration

**Perceptual Losses for Real-Time Style Transfer and Super-Resolution** (2016)
- *Authors:* Justin Johnson et al.
- *Direct Connection:* RepG borrows the core insight of optimizing in deep feature space (perceptual objectives) and translates it into a timestep-wise guidance signal that steers diffusion sampling toward semantically faithful, detailed reconstructions.

**Blended Diffusion: Text-Driven Editing of Natural Images** (2022)
- *Authors:* Omri Avrahami et al.
- *Direct Connection:* RepG generalizes the idea demonstrated by Blended Diffusion that injecting gradients from a pretrained representation (e.g., CLIP) can steer diffusion trajectories, but replaces text/classifier cues with a coherent self-supervised feature target.

### 🔍 Gap Identification

**Adversarial Examples Are Not Bugs, They Are Features** (2019)
- *Authors:* Andrew Ilyas et al.
- *Direct Connection:* RepG addresses the limitation identified by Ilyas et al. that discriminative classifiers rely on non-robust, narrow cues by avoiding classifier gradients and instead guiding with robust self-supervised representations.

### 📊 Baseline

**Classifier-Free Diffusion Guidance** (2022)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* RepG positions itself against CFG as the primary conditional sampling baseline, offering a principled alternative that guides toward a single representative target rather than relying on scale-tuning a conditional/unconditional mixture.

### 🔧 Extension

**Diffusion Models Beat GANs** (2021)
- *Authors:* Prafulla Dhariwal et al.
- *Direct Connection:* RepG directly extends the guided-diffusion formulation of adding ∇x log p(y|x_t) to the reverse dynamics by replacing the classifier gradient with a feature-space target from self-supervised representations to fix the discriminative-bias and incoherence issues.

---

## Synthesis: How Prior Work Led to This Paper

Guided diffusion established that the reverse process can be steered by adding a gradient term from an auxiliary model, with classifier guidance improving fidelity via ∇x log p(y|x_t) but often narrowing diversity and exposing adversarial vulnerabilities. Classifier-free guidance became the de facto conditional baseline by mixing conditional and unconditional scores, trading controllability for scale-tuned heuristics rather than an explicit target. Concurrently, self-supervised vision transformers like DINO revealed representations that capture holistic, object-centric semantics, stable across augmentations and not tied to narrow discriminative cues. Work on adversarial features formalized why discriminative classifiers can emphasize non-robust, spurious signals, explaining the brittleness observed when using classifier gradients to guide generation. Earlier perceptual loss research showed that optimizing in deep feature spaces yields coherent, semantically aligned improvements over pixel-wise objectives, and subsequent diffusion editing demonstrated that injecting representation gradients (e.g., CLIP) can reliably steer sampling trajectories.
These strands collectively exposed a gap: conditional diffusion lacked a coherent, semantically representative target to align updates across timesteps, and classifier-based guidance was intrinsically biased toward non-robust cues. The natural next step was to retain the guided-diffusion update rule but replace the classifier energy with a self-supervised feature objective, turning sampling into a downstream refinement task aimed at a fixed representative embedding. By anchoring all denoising steps to this target, Representative Guidance enforces directional coherence, preserves diversity, and mitigates adversarial tendencies—reaping the controllability of guidance while leveraging the semantic breadth and robustness of self-supervised representations.

---

*Analysis generated on: 2026-01-06T12:55:42.342773*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Idempotence and Perceptual Image Compression

**Conference:** ICLR 2024 (spotlight)

**Authors:** Tongda Xu, Ziran Zhu, Dailan He, Yanghao Li, Lina Guo, Yuanyuan Wang, Zhe Wang, Hongwei Qin, Yan Wang, Jingjing Liu, Ya-Qin Zhang

**Keywords:** perceptual image compression, neural image compression

**Abstract:** 
> Idempotence is the stability of image codec to re-compression. At the first glance, it is unrelated to perceptual image compression. However, we find that theoretically: 1) Conditional generative model-based perceptual codec satisfies idempotence; 2) Unconditional generative model with idempotence constraint is equivalent to conditional generative codec. Based on this newfound equivalence, we propose a new paradigm of perceptual image codec by inverting unconditional generative model with idempo...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Generative Adversarial Networks for Extreme Learned Image Compression** (2019)
- *Authors:* Eirikur Agustsson et al.
- *Direct Connection:* This work established the paradigm of perceptual image compression via conditional GAN decoders at very low rates, providing the specific conditional generative formulation that the current paper proves is equivalent to enforcing idempotence on an unconditional generator.

**The Rate-Distortion-Perception Tradeoff** (2019)
- *Authors:* Yochai Blau et al.
- *Direct Connection:* By formalizing the rate–distortion–perception objective and motivating perceptual metrics like FID, this work underpins the paper’s focus on perceptual codecs and frames why an idempotence-based generative approach can prioritize perception over pixel distortion.

### 💡 Inspiration

**Compressed Sensing using Generative Models** (2017)
- *Authors:* Ashish Bora et al.
- *Direct Connection:* This paper’s blueprint—recovering signals by inverting an unconditional generative model under a measurement-consistency constraint—directly inspires treating a codec as the constraint and performing generator inversion under idempotence.

### 📊 Baseline

**High-Fidelity Image Compression with Generative Adversarial Networks (HiFiC)** (2020)
- *Authors:* Fabian Mentzer et al.
- *Direct Connection:* HiFiC instantiated the dominant conditional generative codec for perceptual quality that this paper both analyzes (proving such codecs are idempotent) and surpasses while replacing the conditional generator with an unconditional model plus an idempotence constraint.

### 🔧 Extension

**Diffusion Posterior Sampling for General Noisy Linear Inverse Problems** (2023)
- *Authors:* Hyungjin Chung et al.
- *Direct Connection:* DPS provides an algorithmic template for enforcing data-consistency while sampling from an unconditional diffusion prior, which the current work extends to the codec setting by using idempotence as the consistency constraint during inversion.

### 🔗 Related Problem

**Plug-and-Play Priors for Model Based Reconstruction** (2013)
- *Authors:* Sreehari Venkatakrishnan et al.
- *Direct Connection:* PnP introduced the principle of combining a pre-trained prior with a measurement-consistency constraint without retraining, a philosophy mirrored by coupling a fixed MSE codec with a pre-trained unconditional generator under idempotence.

---

## Synthesis: How Prior Work Led to This Paper

Conditional generative codecs for perceptual image compression were first crystallized by GAN-based approaches that optimized for realism rather than pixel fidelity. HiFiC demonstrated a practical conditional generator conditioned on quantized latents to yield high perceptual quality, and earlier work on extreme learned compression with GANs formalized the low-bit-rate, generator-driven reconstruction paradigm. The theoretical groundwork for prioritizing perception came from the rate–distortion–perception framework, which clarified why metrics like FID are appropriate targets and legitimized abandoning strict MSE in favor of perceptual realism. In parallel, the inverse-problems community showed that one can invert an unconditional generative model by enforcing measurement consistency: compressed sensing with generative models introduced latent inversion onto a generator’s range, and diffusion posterior sampling provided concrete sampling algorithms that maintain data-consistency with an unconditional diffusion prior. Plug-and-Play Priors established the general tactic of coupling fixed priors with consistency constraints without retraining.

Taken together, these works suggest a path where a codec can be viewed as a forward operator and reconstruction can be obtained by inverting an unconditional generator while enforcing consistency with the compressed representation. The current paper identifies idempotence as the precise consistency condition and proves that enforcing idempotence on an unconditional generator is theoretically equivalent to using a conditional generative codec. This insight enables a new, training-free perceptual compression paradigm that pairs a pre-trained MSE codec with an unconditional generative model, achieving SOTA perceptual quality while bypassing training a conditional generator.

---

*Analysis generated on: 2026-01-06T23:31:57.592296*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

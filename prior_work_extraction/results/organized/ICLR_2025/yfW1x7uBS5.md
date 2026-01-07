# Prior Work Analysis Report

## Target Paper

**Title:** Adversarial Perturbations Cannot Reliably Protect Artists From Generative AI

**Conference:** ICLR 2025 (spotlight)

**Authors:** Robert Hönig, Javier Rando, Nicholas Carlini, Florian Tramèr

**Keywords:** security, adversarial, style mimicry, generative ai

**Abstract:** 
> Artists are increasingly concerned about advancements in image generation models that can closely replicate their unique artistic styles.
In response, several protection tools against style mimicry have been developed that incorporate small adversarial perturbations into artworks published online. In this work, we evaluate the effectiveness of popular protections---with millions of downloads---and show they only provide a false sense of security. We find that low-effort and "off-the-shelf" techn...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation** (2023)
- *Authors:* Nataniel Ruiz et al.
- *Direct Connection:* The paper’s robust mimicry pipeline builds on the DreamBooth-style personalization setup, demonstrating that fine-tuning with standard augmentations on pre-processed (uncloaked) images defeats perturbation-based protections.

**An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion** (2022)
- *Authors:* Rinon Gal et al.
- *Direct Connection:* The threat model of style personalization via data-efficient methods is grounded in textual inversion, which the paper treats as a key mechanism that can still learn styles after low-effort pre-processing removes added perturbations.

### 💡 Inspiration

**Fawkes: Protecting Privacy against Unauthorized Deep Learning Models** (2020)
- *Authors:* Shawn Shan et al.
- *Direct Connection:* Fawkes introduced the ‘cloaking’ paradigm—imperceptible perturbations to poison downstream training—which directly inspired Glaze/Mist-style protections that this paper systematically evaluates and shows to fail in practice.

### 🔍 Gap Identification

**Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adversarial Examples** (2018)
- *Authors:* Anish Athalye et al.
- *Direct Connection:* This work’s key insight—that many defenses fail under realistic transformations—directly motivates testing simple pre-processing (e.g., resizing/upscaling) as a principled way to invalidate perturbation-based art protections.

### 📊 Baseline

**Glaze: Protecting Artists from Style Mimicry** (2023)
- *Authors:* Shawn Shan et al.
- *Direct Connection:* This work’s core evaluation and bypass directly target Glaze’s perturbation-based style-mimicry protection, showing that simple pre-processing (e.g., upscaling) combined with robust mimicry training nullifies the cloak’s intended effect.

### 🔗 Related Problem

**PhotoGuard: Robust Image Perturbation Against Unauthorized Image Editing** (2023)
- *Authors:* Hadi Salman et al.
- *Direct Connection:* PhotoGuard established the broader idea of using adversarial perturbations to shield content from diffusion models, a protection class this paper demonstrates can be bypassed with simple, off-the-shelf image transformations.

---

## Synthesis: How Prior Work Led to This Paper

Glaze proposed adding imperceptible perturbations to artists’ images to induce mislearning of style by text-to-image models, operationalizing ‘cloaks’ specifically against style mimicry. DreamBooth established a practical personalization pipeline whereby a small set of images can fine-tune a diffusion model to capture a subject or style, forming a standard mechanism for style replication. Textual inversion showed an even lighter-weight path to personalization by optimizing an embedding to capture an artist’s style, highlighting that minimal data and adaptation suffice to encode stylistic attributes. Earlier, Fawkes introduced the cloaking paradigm for training-time misuse—perturbing public images so downstream models learn the wrong identity signals—providing the conceptual blueprint later adopted for style protection. PhotoGuard generalized the notion of adversarially shielding images from diffusion models, proposing robust, invisible perturbations to block unauthorized edits, further cementing the defense class this paper scrutinizes. Athalye et al. revealed that defenses often collapse under benign transformations, arguing for evaluation protocols that incorporate simple, realistic pre-processing.

Taken together, these works defined both the offense (personalization methods like DreamBooth/textual inversion) and the defense (training-time cloaks/perturbations like Glaze/PhotoGuard) for generative models. The evident gap was whether these perturbation-based protections withstand low-effort attacker pre-processing and standard robust training. Building on Athalye’s evaluation principle, the paper systematically applies off-the-shelf transformations (e.g., upscaling) and routine augmentation during personalization to show that style mimicry remains successful in user studies, thereby demonstrating that adversarial perturbations cannot reliably protect artists.

---

*Analysis generated on: 2026-01-06T08:23:43.357680*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

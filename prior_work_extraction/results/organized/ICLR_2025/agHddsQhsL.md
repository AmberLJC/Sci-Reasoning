# Prior Work Analysis Report

## Target Paper

**Title:** Targeted Attack Improves Protection against Unauthorized Diffusion Customization

**Conference:** ICLR 2025 (spotlight)

**Authors:** Boyang Zheng, Chumeng Liang, Xiaoyu Wu

**Keywords:** Protection, Unauthorized Diffusion Customization, Adversarial Attack, Diffusion Model, Privacy

**Abstract:** 
> Diffusion models build a new milestone for image generation yet raising public concerns, for they can be fine-tuned on unauthorized images for customization. Protection based on adversarial attacks rises to encounter this unauthorized diffusion customization, by adding protective watermarks to images and poisoning diffusion models. However, current protection, leveraging untargeted attacks, does not appear to be effective enough. In this paper, we propose a simple yet effective improvement for t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation** (2022)
- *Authors:* Ruiz et al.
- *Direct Connection:* DreamBooth establishes the subject-driven fine-tuning protocol that constitutes the unauthorized customization threat model our protection targets and is a primary setting for our attack design and evaluation.

**An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion** (2022)
- *Authors:* Gal et al.
- *Direct Connection:* Textual Inversion defines a mainstream personalization mechanism via learned token embeddings that our protection seeks to degrade, shaping the problem setup and core evaluation.

**Unlearnable Examples: Making Personal Data Unexploitable** (2021)
- *Authors:* Huang et al.
- *Direct Connection:* Unlearnable Examples established the training-time protection paradigm of adding imperceptible perturbations to poison learning, which we adapt to diffusion customization while shifting from untargeted to targeted objectives.

### 💡 Inspiration

**Nightshade: Prompt-Specific Poisoning of Text-to-Image Models** (2023)
- *Authors:* Shan et al.
- *Direct Connection:* Nightshade shows that prompt-specific targeted poisoning can more effectively steer generative models than untargeted noise, directly motivating our targeted objective and careful target selection for diffusion customization.

### 📊 Baseline

**Glaze: Protecting Artists from Style Mimicry by Text-to-Image Models** (2023)
- *Authors:* Shan et al.
- *Direct Connection:* Glaze provides the primary untargeted cloaking baseline for safeguarding against diffusion fine-tuning, whose limited efficacy we directly improve upon by replacing untargeted perturbations with targeted attacks.

### 🔗 Related Problem

**PhotoGuard: Robust Tools for Securing Images Against AI-Mediated Manipulation** (2023)
- *Authors:* Salman et al.
- *Direct Connection:* PhotoGuard introduces target-conditioned adversarial losses within diffusion pipelines for edit prevention, informing our formulation of targeted perturbations even though it addresses inference-time rather than fine-tuning threats.

---

## Synthesis: How Prior Work Led to This Paper

Subject-driven customization for diffusion models was crystallized by DreamBooth, which fine-tunes a generative model on a small set of images to bind a unique subject identity to a text token, and by Textual Inversion, which personalizes generation by optimizing a token embedding in the text encoder. To counter unauthorized customization, Glaze introduced adversarial cloaks on images published online that disrupt style mimicry during downstream fine-tuning, largely relying on untargeted or heuristic perturbations that push features away from artists’ styles. In parallel, PhotoGuard demonstrated that target-conditioned adversarial objectives within diffusion pipelines can reliably prevent specific edits at inference time, providing concrete loss formulations for steering diffusion behavior. More broadly, Unlearnable Examples established the principle of training-time protective perturbations that poison learning while remaining imperceptible, sparking a line of defenses predicated on small input modifications that persist through training. Crucially, Nightshade showed in the T2I pretraining setting that prompt-specific, targeted poisoning can redirect model behavior much more effectively than untargeted noise, highlighting the power of explicit target selection. Together these works expose a gap: defenses against unauthorized diffusion customization largely rely on untargeted cloaks, despite evidence that targeted poisoning is more potent and controllable. Building on the customization protocols (DreamBooth, Textual Inversion), adopting the training-time cloaking paradigm (Unlearnable Examples, Glaze), and leveraging targeted objective design insights (PhotoGuard, Nightshade), this paper advances a targeted poisoning strategy with careful target selection to markedly degrade customization quality.

---

*Analysis generated on: 2026-01-06T14:57:23.376381*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

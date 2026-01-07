# Prior Work Analysis Report

## Target Paper

**Title:** Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Erfan Shayegani, Yue Dong, Nael Abu-Ghazaleh

**Keywords:** Adversarial attacks, Vision encoders, Jailbreak, Prompt Injection, Security, Embedding space attacks, Black box, LLM, Vision-Language Models, Multi-Modal Models, VLM, Alignment, Cross-Modality alignment

**Abstract:** 
> We introduce new jailbreak attacks on vision language models (VLMs), which use aligned LLMs and are resilient to text-only jailbreak attacks. Specifically, we develop cross-modality attacks on alignment where we pair adversarial images going through the vision encoder with textual prompts to break the alignment of the language model. Our attacks employ a novel compositional strategy that combines an image, adversarially targeted towards toxic embeddings, with generic prompts to accomplish the ja...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning Transferable Visual Models From Natural Language Supervision** (2021)
- *Authors:* Alec Radford et al.
- *Direct Connection:* This work’s CLIP-style cross-modal embedding space is the mechanism the paper targets—adversarial images are optimized to land near toxic text embeddings using only the vision encoder, exploiting CLIP’s image–text alignment.

### 💡 Inspiration

**Adversarial manipulation of deep representations** (2016)
- *Authors:* Sara Sabour et al.
- *Direct Connection:* The idea of crafting inputs by matching internal feature vectors inspires the paper’s embedding-space image optimization that targets specific (toxic) text-aligned embeddings without querying the LLM.

**More than you’ve asked for: A Comprehensive Analysis of Indirect Prompt Injection Attacks on LLMs** (2023)
- *Authors:* Konrad Greschake et al.
- *Direct Connection:* This work established that benign user prompts can be overridden by malicious context, directly inspiring the paper’s compositional strategy of combining benign text with a malicious (adversarial) image as the controlling context.

### 🔍 Gap Identification

**Universal and Transferable Adversarial Attacks on Aligned Language Models** (2023)
- *Authors:* Andy Zou et al.
- *Direct Connection:* This paper showed text-only jailbreaks via optimized suffixes but relies on direct LLM access and fails to exploit visual context, motivating a cross-modal attack that requires no LLM access.

### 📊 Baseline

**LLaVA: Large Language and Vision Assistant** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* LLaVA’s architecture—projecting vision features into an aligned LLM and conditioning generation on the image—provides the primary VLM baseline whose alignment is broken by pairing generic prompts with adversarially targeted images.

**MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models** (2023)
- *Authors:* Deyao Zhu et al.
- *Direct Connection:* MiniGPT-4’s frozen-LLM + visual-encoder connector design is directly exploited by the attack, which manipulates only the vision side to steer the downstream LLM despite safety alignment.

---

## Synthesis: How Prior Work Led to This Paper

Cross-modal alignment via contrastive learning showed that images and text can share a joint semantic space; specifically, CLIP established that vision encoder outputs and text embeddings can be closely aligned, enabling images to effectively serve as context for language generation. LLaVA demonstrated a practical pipeline where projected visual features condition an aligned large language model during multi-modal dialogue, making downstream generation highly sensitive to the image embedding. MiniGPT-4 similarly integrated a frozen LLM with a visual encoder through a lightweight connector, highlighting a common design pattern where the vision side can steer the LLM without changing its parameters. Separately, jailbreak work on aligned LLMs revealed that targeted optimization can bypass safety with crafted prompts, but these methods typically assume text-only access and gradients from the LLM. Earlier research on feature-space adversaries established that one can manipulate inputs to match desired internal representations, suggesting a way to target embeddings rather than outputs. Finally, the prompt-injection literature showed that benign user instructions can be subverted by malicious external context, a compositional insight about control via conditioning. Taken together, these strands expose an opportunity: if images and text share a controllable embedding space and VLMs condition strongly on that space, then a feature-space attack on the vision encoder can implant “toxic” semantics as context. By composing such adversarial images with innocuous prompts, one can override safety alignment in the LLM, while requiring no access to the LLM itself—an inevitable next step given multimodal conditioning and indirect prompt-injection dynamics.

---

*Analysis generated on: 2026-01-06T09:40:55.829096*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

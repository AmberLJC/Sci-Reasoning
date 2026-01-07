# Prior Work Analysis Report

## Target Paper

**Title:** An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Haochen Luo, Jindong Gu, Fengyuan Liu, Philip Torr

**Keywords:** Vision Language Model, Adversarial Transferability, Prompt Tuning

**Abstract:** 
> Different from traditional task-specific vision models, recent large VLMs can readily adapt to different vision tasks by simply using different textual instructions, i.e., prompts. However, a well-known concern about traditional task-specific vision models is that they can be misled by imperceptible adversarial perturbations. Furthermore, the concern is exacerbated by the phenomenon that the same adversarial perturbations can fool different task-specific models. Given that VLMs rely on prompts t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Universal Adversarial Perturbations** (2017)
- *Authors:* Seyed-Mohsen Moosavi-Dezfooli et al.
- *Direct Connection:* The concept that a single perturbation can generalize across many inputs directly inspires CroPA’s goal of crafting a single adversarial image that generalizes across many textual prompts (a new axis of universality).

**LLaVA: Large Language-And-Vision Assistant** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* By establishing instruction-following VLMs where different prompts define different tasks, LLaVA provides the prompt-driven setting and targets in which CroPA formulates and evaluates cross-prompt adversarial transfer.

### 💡 Inspiration

**Synthesizing Robust Adversarial Examples** (2018)
- *Authors:* Anish Athalye et al.
- *Direct Connection:* CroPA mirrors EOT’s principle by optimizing the perturbation under an expectation over a prompt distribution (instantiated via learnable prompts), yielding invariance of the attack to prompt variations.

**Improving Transferability of Adversarial Examples with Input Diversity** (2019)
- *Authors:* Cihang Xie et al.
- *Direct Connection:* The input-diversity mechanism that boosts transferability motivates CroPA’s explicit prompt diversity during optimization, replacing image transformations with learned prompt variations to generalize across prompts.

### 📊 Baseline

**Boosting Adversarial Attacks with Momentum** (2018)
- *Authors:* Yinpeng Dong et al.
- *Direct Connection:* MI-FGSM serves as a primary transferability baseline that CroPA is designed to surpass under multi-prompt VLM settings, highlighting the added benefit of prompt-aware optimization beyond momentum methods.

### 🔧 Extension

**Learning to Prompt for Vision-Language Models** (2022)
- *Authors:* Kaiyang Zhou et al.
- *Direct Connection:* CroPA directly adopts CoOp’s idea of learnable continuous text context by co-optimizing soft textual prompts together with the image perturbation so the crafted adversarial image remains effective across diverse natural-language prompts.

---

## Synthesis: How Prior Work Led to This Paper

Learnable text prompting for VLMs demonstrated that continuous context tokens can replace hand-crafted templates, letting models adapt to downstream tasks by optimizing textual embeddings directly in the text encoder. Expectation-over-transformation showed that adversarial perturbations can be made robust to nuisance variations by optimizing under a distribution, rendering attacks stable across transformations at test time. Building on this idea of diversity for transferability, input-diverse attacks emphasized sampling variations during optimization—random resizing and padding—to craft perturbations that generalize beyond a specific input configuration. Momentum-based iterative attacks further improved transferability by stabilizing the update direction across steps, becoming a standard strong baseline for black-box transfer. Earlier still, universal adversarial perturbations revealed that a single small perturbation can fool many inputs and even multiple models, crystallizing the notion of “shared vulnerabilities” that can be exploited with a single adversarial pattern. In parallel, instruction-following VLMs such as LLaVA established that prompts themselves define tasks, with a single model shifting behavior based on natural-language instructions. Together, these works expose a gap: transferability has been pursued across images, models, and transformations, but not across the prompt dimension that governs VLM behavior. By treating prompts as the key nuisance variable and parameterizing them with learnable soft tokens, one can extend expectation/diversity principles to prompt space, yielding a single adversarial image whose effectiveness persists across many instructions—precisely the synthesis realized by CroPA.

---

*Analysis generated on: 2026-01-06T16:58:44.081401*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

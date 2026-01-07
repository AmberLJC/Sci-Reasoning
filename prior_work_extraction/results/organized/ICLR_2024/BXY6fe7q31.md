# Prior Work Analysis Report

## Target Paper

**Title:** Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions

**Conference:** ICLR 2024 (spotlight)

**Authors:** Juncheng Li, Kaihang Pan, Zhiqi Ge, Minghe Gao, Wei Ji, Wenqiao Zhang, Tat-Seng Chua, Siliang Tang, Hanwang Zhang, Yueting Zhuang

**Keywords:** Multimodal Large Language Models, Demonstrative Instruction

**Abstract:** 
> Recent advancements in Multimodal Large Language Models (MLLMs) have been utilizing Visual Prompt Generators (VPGs) to convert visual features into tokens that LLMs can recognize. This is achieved by training the VPGs on millions of image-caption pairs, where the VPG-generated tokens of images are fed into a frozen LLM to generate the corresponding captions. However, this image-captioning based training objective inherently biases the VPG to concentrate solely on the primary visual contents suff...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Multimodal Few-Shot Learning with Frozen Language Models** (2021)
- *Authors:* Yannis Tsimpoukelli et al.
- *Direct Connection:* This work introduced the core formulation of feeding visual features as prompts to a frozen LLM via a learned adapter, a formulation that VPG-C retains while augmenting the adapter with a completion capability.

### 🔍 Gap Identification

**BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models** (2023)
- *Authors:* Junnan Li et al.
- *Direct Connection:* BLIP-2 established the now-standard practice of training a visual-to-LLM bridge on image–caption pairs with a frozen LLM, and its saliency-biased caption objective is the explicit limitation VPG-C targets by completing non-salient, missing visual details needed for instruction following.

### 📊 Baseline

**Visual Instruction Tuning (LLaVA: Large Language and Vision Assistant)** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* LLaVA is the primary MLLM baseline that maps image features to a frozen LLM via a lightweight projector and is instruction-tuned, and VPG-C is designed to plug into this pipeline to remedy LLaVA’s failures on demonstrative, interleaved instructions due to missing fine-grained visual cues.

**MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models** (2023)
- *Authors:* Deyao Zhu et al.
- *Direct Connection:* MiniGPT-4 exemplifies the linear visual projector + frozen LLM recipe and serves as a key competitor that VPG-C directly augments to recover overlooked visual details that hinder following multi-step demonstrative instructions.

**InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning** (2023)
- *Authors:* Junnan Li et al.
- *Direct Connection:* InstructBLIP extends BLIP-2 with broad instruction tuning yet inherits the caption-pretraining bias, and VPG-C addresses this by explicitly completing visual context so the model can follow complex instructions without additional task-specific supervision.

### 🔗 Related Problem

**KOSMOS-2: Grounding Multimodal Large Language Models to the World** (2023)
- *Authors:* Xiao et al.
- *Direct Connection:* KOSMOS-2 formalized interleaved image–text modeling and grounding, underscoring the need for models to capture fine-grained, referential details in multimodal instructions—the very kind of missing information VPG-C is designed to infer and complete.

---

## Synthesis: How Prior Work Led to This Paper

Frozen-language-model pipelines first showed that a small visual adapter can feed image-derived prompts to a powerful, frozen LLM, framing multimodal reasoning as prompting rather than end-to-end fusion. BLIP-2 refined this bridge with a Q-Former trained on image–caption pairs to produce LLM-consumable tokens, but its caption-centric supervision emphasized only salient content sufficient for generic descriptions. LLaVA demonstrated that adding visual instruction tuning atop a lightweight visual projector yields impressive interactive abilities, yet it still relies on caption-style pretraining for the visual prompt generator. MiniGPT-4 followed a similar connector-plus-instruction-tuning recipe, exposing the same weakness when instructions require exhaustive, fine-grained details. InstructBLIP broadened the instruction-tuning spectrum while largely inheriting the caption-pretraining bias embedded in the visual-to-LLM bridge. In parallel, KOSMOS-2 highlighted interleaved image–text sequences and grounding, making clear that understanding referential, context-rich instructions demands capturing non-salient visual cues beyond what caption objectives typically enforce. Together, these works established the standard VPG-to-frozen-LLM paradigm and revealed a systematic gap: caption-trained bridges under-represent details crucial for following demonstrative, interleaved instructions. The current paper synthesizes these insights by introducing VPG-C, a lightweight module that augments the existing visual prompt generator to infer and complete missing visual details, slotting seamlessly into LLaVA/MiniGPT-4/BLIP-2 style pipelines and enabling zero-shot compliance with demonstrative instructions without overhauling the underlying architectures.

---

*Analysis generated on: 2026-01-07T00:21:26.168718*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

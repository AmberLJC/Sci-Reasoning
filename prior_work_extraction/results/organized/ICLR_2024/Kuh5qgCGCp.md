# Prior Work Analysis Report

## Target Paper

**Title:** Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jinyi Hu, Yuan Yao, Chongyi Wang, SHAN WANG, Yinxu Pan, Qianyu Chen, Tianyu Yu, Hanghao Wu, Yue Zhao, Haoye Zhang, Xu Han, Yankai Lin, Jiao Xue, dahai li, Zhiyuan Liu, Maosong Sun

**Keywords:** Large Multimodal Models, Multilingual Transfer

**Abstract:** 
> Recently there has been a significant surge in multimodal learning in terms of both image-to-text and text-to-image generation. However, the success is typically limited to English, leaving other languages largely behind. Building a competitive counterpart in other languages is highly challenging due to the low-resource nature of non-English multimodal data (i.e., lack of large-scale, high-quality image-text data). In this work, we propose MPM, an effective training paradigm for training large m...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**BLOOMZ: Cross-lingual Generalization through Instruction Tuning** (2022)
- *Authors:* N. Muennighoff et al.
- *Direct Connection:* MPM leverages BLOOMZ’s core finding that instruction-tuned multilingual LMs can follow prompts across languages, using that capability as the pivot for multilingual multimodal understanding and generation.

### 💡 Inspiration

**M-CLIP: Multilingual CLIP via Cross-lingual Transfer** (2022)
- *Authors:* Marius Muennighoff et al.
- *Direct Connection:* MPM generalizes M-CLIP’s insight—that multilingual text models can inherit English-trained visual alignment—to LMMs by using a multilingual LLM as the pivot across languages.

### 🔍 Gap Identification

**PaLI: A Jointly-Scaled Multilingual Language-Image Model** (2022)
- *Authors:* Xi Chen et al.
- *Direct Connection:* MPM targets PaLI’s multilingual vision–language objectives while explicitly addressing its limitation of requiring massive multilingual image–text corpora by relying only on English visual data plus a multilingual LLM.

**UC^2: Universal Cross-lingual Cross-modal Vision-and-Language Pretraining** (2021)
- *Authors:* Luowei Zhou et al.
- *Direct Connection:* MPM removes UC^2’s dependence on machine-translated non-English captions for cross-lingual VLP by letting a multilingual LLM supply the language bridge with zero non-English visual supervision.

### 📊 Baseline

**Visual Instruction Tuning (LLaVA)** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* MPM builds on LLaVA’s instruction-tuning recipe for aligning visual features to an LLM, showing that using a multilingual LLM yields zero-shot multilingual multimodal ability without any non-English image–text training.

### 🔧 Extension

**BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models** (2023)
- *Authors:* Junnan Li et al.
- *Direct Connection:* MPM adopts BLIP-2’s frozen-vision-encoder + LLM bridging strategy and extends it by swapping in a multilingual LLM so English-only visual pretraining pivots to other languages.

### 🔗 Related Problem

**MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models** (2023)
- *Authors:* Deyao Zhu et al.
- *Direct Connection:* MPM follows MiniGPT-4’s practical connector-plus-instruction-tuning pipeline but replaces the monolingual LLM with a multilingual one to realize cross-lingual transfer from English-only multimodal supervision.

---

## Synthesis: How Prior Work Led to This Paper

BLIP-2 showed that strong multimodal capability can be achieved by freezing a vision encoder and language model while learning a lightweight cross-modal bridge, establishing a modular recipe where the language component can be swapped. LLaVA demonstrated that instruction tuning effectively aligns visual features to an LLM’s conversational interface, yielding robust vision–language reasoning with simple connectors trained on English-only data. MiniGPT-4 refined this connector-plus-instruction-tuning pipeline using a BLIP-2-style bridge to enable open-ended image dialog, further validating that most multimodal supervision can be English. In parallel, M-CLIP proved that multilingual text encoders can inherit the visual semantics of English-trained CLIP via cross-lingual transfer, enabling multilingual zero-shot retrieval without multilingual image–text pairs. PaLI established the value of multilingual vision–language models at scale, but did so by consuming massive multilingual image–text corpora, while UC^2 relied on machine-translated captions to cover non-English modalities. Separately, BLOOMZ showed that instruction-tuned multilingual LMs naturally generalize tasks across languages, suggesting they can act as a linguistic bridge.
Together these works reveal a gap: multilingual multimodal ability typically requires non-English visual-text supervision or translation, even though English-trained visual alignment and multilingual language competence already exist. The natural next step is to keep visual pretraining purely English, preserve the LLM–vision modularity of BLIP-2/LLaVA, and rely on an instruction-tuned multilingual LLM (as evidenced by BLOOMZ and M-CLIP’s cross-lingual transfer) to pivot outputs and understanding across languages. This synthesis yields a quasi-zero-shot multilingual multimodal paradigm powered by the LLM’s multilinguality rather than multilingual image–text data.

---

*Analysis generated on: 2026-01-06T15:12:00.755627*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

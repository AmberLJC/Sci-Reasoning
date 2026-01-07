# Prior Work Analysis Report

## Target Paper

**Title:** Selective Visual Representations Improve Convergence and Generalization for Embodied AI

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ainaz Eftekhar, Kuo-Hao Zeng, Jiafei Duan, Ali Farhadi, Aniruddha Kembhavi, Ranjay Krishna

**Keywords:** Embodied-AI, Task-conditioned Representations, Visual Navigation, Reinforcement Learning

**Abstract:** 
> Embodied AI models often employ off the shelf vision backbones like CLIP to encode their visual observations. Although such general purpose representations encode rich syntactic and semantic information about the scene, much of this information is often irrelevant to the specific task at hand. This introduces noise within the learning process and distracts the agent's focus from task-relevant visual cues.
Inspired by selective attention in humans—the process through which people filter their per...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Object Goal Navigation using Goal-Oriented Semantic Exploration** (2020)
- *Authors:* Devendra Singh Chaplot et al.
- *Direct Connection:* This paper formalized Object-Goal Navigation with semantic priors and established the task setup and metrics that the current work targets when evaluating task-conditioned selective visual representations.

**ManipulaTHOR: A Framework for Visual Object Manipulation** (2021)
- *Authors:* Kuo-Hao Zeng et al.
- *Direct Connection:* ManipulaTHOR defined interactive object displacement/manipulation tasks and benchmarks used to assess whether selective, task-conditioned visual representations improve policy learning beyond navigation.

### 💡 Inspiration

**FiLM: Visual Reasoning with a General Conditioning Layer** (2018)
- *Authors:* Ethan Perez et al.
- *Direct Connection:* This work introduced task/instruction-conditioned feature modulation; the current paper borrows the conditioning principle but replaces dense FiLM-style modulation with a compact, task-conditioned selective bottleneck to filter visual features.

**Neural Discrete Representation Learning (VQ-VAE)** (2017)
- *Authors:* Aaron van den Oord et al.
- *Direct Connection:* VQ-VAE showed how a learnable codebook can serve as a compact, trainable bottleneck; the current paper adapts this idea to build a small task-conditioned codebook that selectively routes visual information relevant to the embodied task.

### 🔍 Gap Identification

**Zero-Shot Object-Goal Navigation using Multimodal Foundation Models (ZSON)** (2022)
- *Authors:* Kushal K. Ramrakhya et al.
- *Direct Connection:* ZSON demonstrated that off-the-shelf CLIP features enable ObjectNav but also carry broad, task-irrelevant signals; the current paper directly addresses this limitation by learning a task-conditioned filter over such features.

### 📊 Baseline

**CLIP-Adapter: Better Vision-Language Models with Feature Adapters** (2021)
- *Authors:* Peng Gao et al.
- *Direct Connection:* CLIP-Adapter is a parameter-efficient way to adapt CLIP without full fine-tuning; the proposed method is positioned as a stronger parameter-efficient alternative that, unlike adapters, explicitly filters out task-irrelevant CLIP features.

---

## Synthesis: How Prior Work Led to This Paper

FiLM introduced a simple and effective mechanism to condition visual processing on a task or instruction by feature-wise modulation, establishing that task signals can guide what aspects of an image should be emphasized. VQ-VAE demonstrated that a learnable codebook can act as a compact, trainable bottleneck, discretizing features into a small set of prototypes that can encourage selective information flow. CLIP-Adapter showed that parameter-efficient modules attached to pre-trained vision-language models can adapt them to new tasks without full fine-tuning, but it preserves most upstream activations and does not explicitly suppress task-irrelevant content. In embodied navigation, Goal-Oriented Semantic Exploration specified the Object-Goal Navigation formulation and emphasized leveraging semantic cues to find target objects, providing the task structure and metrics. ZSON then applied multimodal foundation models like CLIP to ObjectNav, evidencing the potency of generic pre-trained features for zero-shot performance while implicitly exposing the problem that such broad representations include information irrelevant to the current goal. ManipulaTHOR extended embodied evaluation to object displacement/manipulation, offering a complementary testbed where perceptual selectivity is critical for control.
Together, these works suggest a natural opportunity: combine task conditioning (FiLM) with a compact bottleneck (VQ) to create a parameter-efficient adapter (à la CLIP-Adapter) that explicitly filters representations for embodied tasks defined by ObjectNav and manipulation benchmarks. The synthesis is a task-conditioned codebook that selectively admits goal-relevant visual signals, thereby reducing learning noise, accelerating convergence, and improving generalization across navigation and manipulation settings.

---

*Analysis generated on: 2026-01-06T06:13:47.282667*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

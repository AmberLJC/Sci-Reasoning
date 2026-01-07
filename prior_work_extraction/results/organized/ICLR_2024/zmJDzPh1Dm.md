# Prior Work Analysis Report

## Target Paper

**Title:** Nemesis: Normalizing the Soft-prompt Vectors of Vision-Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Shuai Fu, Xiequn Wang, Qiushi Huang, Yu Zhang

**Keywords:** Vision-language models; Soft-prompt tuning; Low-norm effect; Normalizing soft prompts

**Abstract:** 
> With the prevalence of large-scale pretrained vision-language models (VLMs), such as CLIP, soft-prompt tuning has become a popular method for adapting these models to various downstream tasks. However, few works delve into the inherent properties of learnable soft-prompt vectors, specifically the impact of their norms to the performance of VLMs. This motivates us to pose an unexplored research question: ``Do we need to normalize the soft prompts in VLMs?'' To fill this research gap, we first unc...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Power of Scale for Parameter-Efficient Prompt Tuning** (2021)
- *Authors:* Brian Lester et al.
- *Direct Connection:* By formalizing soft-prompt tuning as learning continuous embeddings prepended to inputs, this work provides the foundational formulation that Nemesis augments with explicit norm control of those embeddings.

### 💡 Inspiration

**P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks** (2022)
- *Authors:* Xiao Liu et al.
- *Direct Connection:* P-Tuning v2’s deep, continuous prompts highlight sensitivity to prompt parameterization and scaling, inspiring Nemesis to target the specific factor of prompt-vector magnitude through normalization.

### 🔍 Gap Identification

**Conditional Prompt Learning for Vision-Language Models** (2022)
- *Authors:* Kaiyang Zhou et al.
- *Direct Connection:* CoCoOp targets generalization to unseen classes via image-conditioned prompts yet still leaves prompt vector norms unconstrained, a limitation Nemesis identifies as a root cause of instability and addresses via normalization.

### 📊 Baseline

**MaPLe: Multi-modal Prompt Learning** (2023)
- *Authors:* Muhammad Uzair Khattak et al.
- *Direct Connection:* Nemesis is evaluated as a plug-in to MaPLe by normalizing its multi-modal prompt tokens, stabilizing their scale across layers and improving robustness without altering MaPLe’s architecture.

### 🔧 Extension

**Learning to Prompt for Vision-Language Models** (2022)
- *Authors:* Kaiyang Zhou et al.
- *Direct Connection:* Nemesis directly modifies CoOp’s learnable text context vectors by explicitly normalizing their magnitudes, addressing CoOp’s unconstrained soft-prompt norms that can drift during adaptation.

### 🔗 Related Problem

**Visual Prompt Tuning** (2022)
- *Authors:* Menglin Jia et al.
- *Direct Connection:* VPT shows that learnable visual prompt tokens injected into ViTs modulate internal activations, motivating Nemesis’s insight that controlling prompt token norms (via normalization) can systematically affect performance.

---

## Synthesis: How Prior Work Led to This Paper

Learning to Prompt for Vision-Language Models (CoOp) established that replacing hand-crafted templates with learned continuous text contexts enables effective CLIP adaptation, but it leaves prompt vectors free to grow in magnitude during training. Conditional Prompt Learning (CoCoOp) conditions prompts on image features to improve generalization to unseen classes, yet it similarly does not regulate the scale of the learned prompt embeddings. MaPLe extends prompting to multi-modal and multi-layer tokens, increasing representational power while introducing more degrees of freedom whose magnitudes can affect feature scaling across layers. Visual Prompt Tuning (VPT) shows that introducing learnable tokens on the vision side modulates transformer activations, underscoring that prompt tokens act as scale-bearing signals inside the network. In NLP, the soft-prompt formulation of Lester et al. formalized learning continuous embeddings as a compact adapter, and P-Tuning v2 showed deep prompts can match fine-tuning yet remain sensitive to prompt parameterization, implicitly pointing to the importance of prompt scale.
Together these works created a landscape where powerful but unconstrained soft prompts drive adaptation, with mounting evidence that prompt parameterization and activation scaling matter yet no direct control of prompt vector norms. This gap naturally led to investigating how the magnitude of learned prompt tokens influences VLM performance and robustness; Nemesis synthesizes these insights by explicitly normalizing soft-prompt vectors, harnessing a discovered low-norm effect and providing a simple, general plug-in that stabilizes and improves CoOp-, CoCoOp-, and MaPLe-style prompting.

---

*Analysis generated on: 2026-01-06T09:00:26.654753*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

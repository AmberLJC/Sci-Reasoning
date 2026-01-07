# Prior Work Analysis Report

## Target Paper

**Title:** Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics

**Conference:** ICLR 2024 (spotlight)

**Authors:** Christian Gumbsch, Noor Sajid, Georg Martius, Martin V. Butz

**Keywords:** world models, temporal abstraction, hierarchical learning, model-based reinforcement learning, hierarchical planning

**Abstract:** 
> Hierarchical world models can significantly improve model-based reinforcement learning (MBRL) and planning by enabling reasoning across multiple time scales. Nonetheless, the majority of state-of-the-art MBRL methods employ flat, non-hierarchical models. We propose Temporal Hierarchies from Invariant Context Kernels (THICK), an algorithm that learns a world model hierarchy via discrete latent dynamics. The lower level of THICK updates parts of its latent state sparsely in time, forming invariant...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Causal Inference using Invariant Prediction** (2016)
- *Authors:* Jonas Peters et al.
- *Direct Connection:* The invariant causal mechanisms principle in this work motivates THICK’s design of latent ‘contexts’ that remain invariant until a mechanism change, aligning its high-level discrete variable with detected distributional shifts.

### 💡 Inspiration

**Temporal Difference Variational Auto-Encoder (TD-VAE)** (2018)
- *Authors:* Karol Gregor et al.
- *Direct Connection:* TD-VAE’s jumpy latent predictions over variable time gaps directly inspired THICK’s separation of slow, categorical high-level variables from fast low-level dynamics, while THICK addresses boundary discovery by learning when high-level changes should occur.

**Recurrent Independent Mechanisms** (2019)
- *Authors:* Anirudh Goyal et al.
- *Direct Connection:* RIMs’ principle of sparsely updating independent modules underpins THICK’s invariant context kernels, where only latents associated with changing mechanisms are updated while others remain persistent.

### 📊 Baseline

**Mastering Diverse Domains through World Models (DreamerV3)** (2023)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* THICK replaces the flat dRSSM-style world model used in Dreamer with a hierarchical discrete-latent dynamics that learns adaptive temporal abstractions, and is explicitly evaluated by plugging into Dreamer-style planning to demonstrate improvements.

### 🔧 Extension

**A Hierarchical Multiscale Recurrent Neural Network** (2017)
- *Authors:* Junyoung Chung et al.
- *Direct Connection:* HM-RNN’s learned discrete boundary variables that gate multiscale updates are generalized in THICK to a probabilistic world-model setting, where subsets of the latent state update sparsely and a high-level process predicts change events.

### 🔗 Related Problem

**CompILE: Compositional Imitation Learning and Execution** (2019)
- *Authors:* Thomas Kipf et al.
- *Direct Connection:* CompILE’s variational segmentation with a categorical code per segment informed THICK’s use of discrete latents to represent invariant contexts and variable-length segments, adapted here to learn dynamics useful for model-based control rather than imitation.

---

## Synthesis: How Prior Work Led to This Paper

Dreamer-style world models demonstrated that latent dynamics trained from pixels can support planning and policy learning, but they typically rely on flat RSSM architectures that operate at a single time scale. TD-VAE introduced the idea of jumpy latent predictions, separating slower abstract latents from faster dynamics to capture long-range temporal structure. HM-RNN learned discrete boundary variables that gated updates at multiple time scales, enabling segments to persist without continuous higher-level changes. CompILE provided a variational approach to discover variable-length segments with a categorical latent per segment, showing that unsupervised boundary detection can yield compact, interpretable sequence structure. Recurrent Independent Mechanisms argued for sparsely updating modular components so that independent mechanisms remain unchanged unless driven by relevant inputs, offering a neural template for persistence and selective updates. Complementing these, invariant prediction formalized the idea that causal mechanisms remain stable across contexts, suggesting that learned representations should be constant until a genuine mechanism change occurs.
Together, these works reveal an opportunity: combine jumpy temporal abstraction with explicit boundary discovery and sparse, mechanism-aligned updates inside a predictive world model. THICK synthesizes these insights by learning invariant context kernels—subsets of the latent state that remain fixed across segments—and a high-level categorical process that predicts context changes. This yields interpretable, discrete temporal abstractions while preserving precise low-level predictions, and the resulting hierarchical world model slots directly into Dreamer-style planning to enhance model-based control.

---

*Analysis generated on: 2026-01-06T12:01:10.733267*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

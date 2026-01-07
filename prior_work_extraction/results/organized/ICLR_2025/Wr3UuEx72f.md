# Prior Work Analysis Report

## Target Paper

**Title:** LARP: Tokenizing Videos with a Learned Autoregressive Generative Prior

**Conference:** ICLR 2025 (oral)

**Authors:** Hanyu Wang, Saksham Suri, Yixuan Ren, Hao Chen, Abhinav Shrivastava

**Keywords:** Video Generation, Visual Tokenization

**Abstract:** 
> We present LARP, a novel video tokenizer designed to overcome limitations in current video tokenization methods for autoregressive (AR) generative models. Unlike traditional patchwise tokenizers that directly encode local visual patches into discrete tokens, LARP introduces a holistic tokenization scheme that gathers information from the visual content using a set of learned holistic queries. This design allows LARP to capture more global and semantic representations, rather than being limited t...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Neural Discrete Representation Learning** (2017)
- *Authors:* van den Oord et al.
- *Direct Connection:* LARP adopts discrete latent codebooks but departs by co-training with an autoregressive (AR) prior to shape the latent space for next-token prediction, directly addressing the tokenizer–prior mismatch left by VQ-VAE’s separate training.

**VideoGPT: Video Generation using VQ-VAE and Transformers** (2021)
- *Authors:* Yan et al.
- *Direct Connection:* VideoGPT formalized AR generation over patchwise VQ tokens for videos, which LARP retains while replacing patch tokens with holistic query-based discrete tokens to capture global semantics and shorten sequences.

### 💡 Inspiration

**Perceiver: General Perception with Iterative Attention** (2021)
- *Authors:* Jaegle et al.
- *Direct Connection:* LARP borrows Perceiver’s core idea of a learnable latent array that cross-attends to high-dimensional inputs to construct its holistic query set before quantization.

**TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?** (2021)
- *Authors:* Ryoo et al.
- *Direct Connection:* LARP extends TokenLearner’s adaptive spatiotemporal token selection by producing discrete, AR-aligned tokens that enable generative modeling with a variable number of tokens.

### 🔍 Gap Identification

**MAGVIT-v2** (2024)
- *Authors:* Yu et al.
- *Direct Connection:* Despite improved compression with residual quantization, MAGVIT-v2 remains patch-based with fixed token layouts, a limitation LARP explicitly overcomes by moving to learned holistic queries and AR-prior-aligned discrete latents.

### 📊 Baseline

**MAGVIT: Masked Generative Video Transformer** (2023)
- *Authors:* Yu et al.
- *Direct Connection:* MAGVIT is the primary patchwise video tokenizer baseline whose fixed grid and local code limitations LARP directly addresses via learned holistic queries and support for an arbitrary number of discrete tokens.

### 🔗 Related Problem

**Flamingo: a Visual Language Model for Few-Shot Learning** (2022)
- *Authors:* Alayrac et al.
- *Direct Connection:* Flamingo’s Perceiver Resampler shows that a small set of learned queries can summarize visual inputs for sequence models, a mechanism LARP applies inside a tokenizer and couples with a next-token AR prior.

---

## Synthesis: How Prior Work Led to This Paper

Neural Discrete Representation Learning established vector-quantized latent codes and the use of a separate autoregressive prior over them, enabling discrete generative modeling but leaving a gap between code learning and next-token prediction. VideoGPT brought this paradigm to video, modeling sequences of patchwise VQ tokens with transformers, highlighting that locality and long token streams hinder temporal coherence and semantics. MAGVIT advanced video tokenization for AR generation but still encoded fixed-grid spatiotemporal patches, and MAGVIT‑v2 improved compression via residual quantization while remaining patch-based and fixed in token count. In parallel, Perceiver introduced a learnable latent array that cross-attends to inputs, demonstrating that a small set of learned queries can absorb global information efficiently. TokenLearner showed that adaptive, learned spatiotemporal tokens can summarize videos with far fewer tokens than patches. Flamingo operationalized learned-query resampling in large sequence models, validating that such holistic queries yield compact, sequence-friendly visual representations.
Taken together, these works revealed two opportunities: replace patchwise tokens with a small, learned set of holistic queries to capture global video semantics and reduce sequence length, and align the discrete latent space with next-token prediction rather than learning it in isolation. LARP synthesizes these insights by using learned holistic queries to gather video information before quantization and by integrating a lightweight AR transformer during training so the discrete space is explicitly shaped for AR generation, while permitting an arbitrary number of tokens for adaptive efficiency.

---

*Analysis generated on: 2026-01-06T18:32:31.044371*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

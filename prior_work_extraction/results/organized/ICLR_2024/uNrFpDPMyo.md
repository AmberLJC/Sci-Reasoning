# Prior Work Analysis Report

## Target Paper

**Title:** Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs

**Conference:** ICLR 2024 (oral)

**Authors:** Suyu Ge, Yunan Zhang, Liyuan Liu, Minjia Zhang, Jiawei Han, Jianfeng Gao

**Keywords:** Large Language Model, Efficient Inference, Generative Inference, Key-Value Cache

**Abstract:** 
> In this study, we introduce adaptive KV cache compression, a plug-and-play method that reduces the memory footprint of generative inference for Large Language Models (LLMs). Different from the conventional KV cache that retains key and value vectors for all context tokens, we conduct targeted profiling to discern the intrinsic structure of attention modules. Based on the recognized structure, we then construct the KV cache in an adaptive manner: evicting long-range contexts on attention heads em...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned** (2019)
- *Authors:* Anna Voita et al.
- *Direct Connection:* This study established that attention heads specialize (e.g., positional, delimiter-focused), directly motivating this paper’s per‑head categorization (local, special‑token‑centric, global) that underpins adaptive KV caching.

**What Does BERT Look At? An Analysis of Attention** (2019)
- *Authors:* Kevin Clark et al.
- *Direct Connection:* Clark et al. showed that certain heads consistently attend to special tokens like [CLS]/[SEP], supporting the paper’s strategy to retain special tokens only on heads centered on such tokens while evicting others.

### 💡 Inspiration

**StreamingLLM: Efficient Streaming Language Modeling with Attention Sink** (2023)
- *Authors:* Xiao et al.
- *Direct Connection:* StreamingLLM revealed the 'attention sink' phenomenon and preserved a small set of special tokens while using a sliding window for others, an insight this paper adopts at head granularity by discarding non‑special tokens on special‑token heads and sliding on local heads.

### 📊 Baseline

**Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression** (2023)
- *Authors:* Sheng et al.
- *Direct Connection:* Scissorhands proposed importance‑based KV eviction without retraining but applied a uniform policy across heads, a limitation this work addresses via adaptive, head‑specific compression guided by lightweight profiling.

### 🔧 Extension

**H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models** (2023)
- *Authors:* Suyu Ge et al.
- *Direct Connection:* H2O introduced attention-driven offline profiling to identify and retain heavy-hitter tokens for KV cache eviction, which this paper directly generalizes into a head-aware oracle that chooses different eviction rules per attention head.

### 🔗 Related Problem

**Longformer: The Long-Document Transformer** (2020)
- *Authors:* Iz Beltagy et al.
- *Direct Connection:* Longformer decomposed attention into local windows plus a few global tokens, an architectural pattern that directly informs this work’s per‑head split between local-window caching and special‑token retention.

---

## Synthesis: How Prior Work Led to This Paper

H2O introduced an attention-driven profiling oracle that, from a calibration set, identifies heavy-hitter tokens to keep in the KV cache during generation, demonstrating that static precomputed signals can guide token-level eviction without retraining. StreamingLLM exposed the attention-sink phenomenon—LMs reliably attend to a tiny set of special tokens—using this to retain those sinks while sliding a local window over ordinary tokens for streaming inputs. Scissorhands posited the persistence-of-importance hypothesis to evict KV entries based on estimated token importance, but used a uniform policy that does not account for head-specific behaviors. Earlier interpretability work showed that multi-head attention is functionally diverse: Voita et al. found specialized heads (e.g., positional or delimiter-focused) that carry most of the load, and Clark et al. documented heads that consistently attend to special tokens like [CLS]/[SEP]. Longformer canonized a local-plus-global decomposition by mixing sliding-window attention with a few global tokens that broadcast information. Together these works reveal that (i) attention importance can be profiled offline, (ii) special tokens warrant different treatment, and (iii) attention structure is heterogeneous across heads. The natural next step is to make eviction head-aware: use sliding windows only on local heads, retain special tokens only on special-token heads, and leave global heads uncompressed. By coupling lightweight per-head profiling with tailored cache policies, the paper synthesizes these insights into an adaptive KV compression scheme that reduces memory without fine-tuning.

---

*Analysis generated on: 2026-01-06T09:56:24.476989*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** When Attention Sink Emerges in Language Models: An Empirical View

**Conference:** ICLR 2025 (spotlight)

**Authors:** Xiangming Gu, Tianyu Pang, Chao Du, Qian Liu, Fengzhuo Zhang, Cunxiao Du, Ye Wang, Min Lin

**Keywords:** Attention Sink, Language Models, Empirical Study

**Abstract:** 
> Auto-regressive language Models (LMs) assign significant attention to the first token, even if it is not semantically important, which is known as **attention sink**. This phenomenon has been widely adopted in applications such as streaming/long context generation, KV cache optimization, inference acceleration, model quantization, and others.  Despite its widespread use, a deep understanding of attention sink in LMs is still lacking. In this work, we first demonstrate that attention sinks exist ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**StreamingLLM: Efficient Streaming Language Models with Attention Sinks** (2023)
- *Authors:* Xiao et al.
- *Direct Connection:* This work coined and operationalized the “attention sink” phenomenon by showing that LMs consistently assign high attention to the first tokens and leveraging them to stabilize streaming generation, directly motivating a deeper investigation into why and how such sinks emerge.

### 💡 Inspiration

**Vision Transformers Need Registers** (2023)
- *Authors:* Wortsman et al.
- *Direct Connection:* By showing that adding trainable ‘register’ tokens (attention attractors) improves stability and performance in Transformers, this work suggested a general optimization-driven need for sink-like tokens and inspired probing their emergence in language model pre-training.

### 🔍 Gap Identification

**H2O: Heavy-Hitter Oracle for Efficient KV Cache** (2023)
- *Authors:* Zhang et al.
- *Direct Connection:* H2O’s observation that early tokens frequently appear as ‘heavy hitters’ for attention-based KV retention underscored a systematic bias toward first tokens that lacked a principled explanation, motivating a study into the training dynamics behind sinks.

**SnapKV: Fast and Accurate KV Cache Compression for Large Language Models** (2024)
- *Authors:* Wang et al.
- *Direct Connection:* SnapKV’s attention-magnitude–based selection often prioritizes BOS/early tokens, revealing that naive importance metrics can be dominated by sink effects and motivating a causal account of when and why sinks arise.

### 📊 Baseline

**LM-Infinite: Zero-Shot Transfer of LLMs to Infinite-Length Context** (2024)
- *Authors:* Han et al.
- *Direct Connection:* By relying on preserving a few early ‘sink’ tokens while evicting most KV states to extend context essentially without retraining, this paper highlighted the functional reliance on sink positions and exposed open questions about their origin and stability.

### 🔗 Related Problem

**Scissorhands: Efficient KV Cache Management for Large Language Model Inference** (2024)
- *Authors:* Liu et al.
- *Direct Connection:* Its token-pruning/eviction strategy implicitly protects initial tokens as anchors due to their persistent high attention, pointing to an underlying mechanism that this paper interrogates during pre-training.

---

## Synthesis: How Prior Work Led to This Paper

StreamingLLM introduced and operationalized the attention sink: the consistent tendency of autoregressive Transformers to allocate substantial attention to the initial tokens, and exploited this to stabilize streaming generation. LM-Infinite extended this idea to long and effectively unbounded contexts by retaining a small set of early tokens while evicting most key–value states, demonstrating that preserving these sink positions preserves model stability without retraining. H2O formalized heavy-hitter retention for KV caches and repeatedly found early tokens selected as ‘heavy hitters,’ implying a structural bias that was not yet explained mechanistically. Scissorhands advanced token-level KV eviction and, in practice, shielded initial tokens due to their persistent high attention, highlighting an empirical regularity rather than a principled rationale. SnapKV further showed that attention-magnitude–based importance often locks onto BOS/first tokens, suggesting that sink effects can dominate ostensibly generic selection heuristics. In parallel, Vision Transformers Need Registers showed that adding tokens acting as global attention attractors improves training stability, hinting that sink-like roles may emerge from optimization pressures broadly in Transformers.
Together these works established that sink tokens are real, useful, and ubiquitous across streaming, long-context, and KV compression—but left open why they arise, where they localize, and how training choices affect them. The present study synthesizes these clues by tracing sink emergence through pre-training, isolating the roles of optimization efficacy, data scale and distribution, loss design, and architecture, and showing that sinks appear after sufficient optimization, with their positions correlating with loss and data statistics—providing the missing causal understanding that prior engineering exploited but did not explain.

---

*Analysis generated on: 2026-01-06T16:48:31.053709*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

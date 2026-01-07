# Prior Work Analysis Report

## Target Paper
**Title:** wIPIhHd00i
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Connection:* Introduced conditional computation via input-dependent routing to a small subset of experts; Deja Vu adopts this core principle to activate only a small, input-dependent subset of attention heads and MLP neurons at inference without altering the pretrained LLM.

**Are Sixteen Heads Really Better than One?** (2019)
- *Authors:* Paul Michel et al.
- *Connection:* Demonstrated that many attention heads are redundant and can be pruned with minimal loss, directly motivating Deja Vu’s decision to target attention-head sparsity—made contextual and per-input rather than static.

**Asymmetric LSH (ALSH) for Maximum Inner Product Search** (2014)
- *Authors:* Anshumali Shrivastava et al.
- *Connection:* Provided the algorithmic basis for fast approximate selection of high inner-product neurons, a principle Deja Vu leverages to cheaply predict which FFN units matter without evaluating the full dense layer.

### 💡 Inspiration

**SLIDE: In Defense of Smart Algorithms over Hardware: Efficient Training of Deep Neural Networks using Hashing** (2020)
- *Authors:* Beidi Chen et al.
- *Connection:* Showed that input-driven, cheaply predicted neuron activation (via hashing/MIPS) can yield large wall-clock gains; Deja Vu extends this conditional activation idea to pretrained LLMs at inference and to both FFN neurons and attention heads.

### 🔍 Gap Identification

**Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned** (2019)
- *Authors:* Elena Voita et al.
- *Connection:* Showed that only a subset of heads is typically essential but relied on static pruning; Deja Vu addresses this limitation by predicting head importance on-the-fly conditioned on the current input context.

**DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference** (2020)
- *Authors:* Ji Xin et al.
- *Connection:* Pioneered dynamic inference via early exiting but at the cost of potential accuracy trade-offs and loss of in-context capabilities; Deja Vu tackles efficiency without exiting layers, preserving LLM quality and in-context learning.

### 📊 Baseline

**Movement Pruning: Adaptive Sparsity by Fine-Tuning** (2020)
- *Authors:* Victor Sanh et al.
- *Connection:* A strong structured pruning baseline that requires task-specific fine-tuning and yields static masks; Deja Vu improves upon this by avoiding retraining and using contextual (input-dependent) sparsity during inference.

---

## Synthesis

Deja Vu’s core innovation—contextual sparsity that selects a small, input-dependent subset of attention heads and FFN neurons at inference time—stands on the lineage of conditional computation and transformer sparsification. The sparsely-gated Mixture-of-Experts layer (Shazeer et al., 2017) established the foundational idea that routing tokens to a small subset of compute can preserve quality while reducing cost; Deja Vu translates this principle to pretrained dense LLMs without retraining by learning to predict which subcomponents to activate per input. Empirical work on head redundancy in Transformers (Michel et al., 2019; Voita et al., 2019) made clear that many heads are dispensable, but prior approaches largely used static masks, motivating Deja Vu’s shift to per-token, context-aware selection.
Static pruning methods such as Movement Pruning (Sanh et al., 2020) serve as strong baselines yet require fine-tuning and produce fixed sparsity patterns, which Deja Vu overcomes by predicting sparsity on the fly while preserving in-context learning. Early exiting (DeeBERT; Xin et al., 2020) introduced dynamic inference but trades off depth computation and can harm generative/in-context performance; Deja Vu instead keeps the full depth and modulates internal compute. Finally, algorithmic work on input-driven neuron activation (SLIDE; Chen et al., 2020) and fast inner-product-based selection (ALSH; Shrivastava & Li, 2014) directly informed Deja Vu’s low-cost predictors for choosing impactful FFN neurons (and analogously, attention heads), enabling actual wall-clock speedups on modern hardware.

---
*Generated: 2026-01-06T23:09:26.524602*

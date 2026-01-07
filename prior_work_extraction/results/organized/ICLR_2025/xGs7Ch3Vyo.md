# Prior Work Analysis Report

## Target Paper

**Title:** Better autoregressive regression with LLMs via regression-aware fine-tuning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Michal Lukasik, Zhao Meng, Harikrishna Narasimhan, Yin-Wen Chang, Aditya Krishna Menon, Felix Yu, Sanjiv Kumar

**Keywords:** regression, LLMs

**Abstract:** 
> Decoder-based large language models (LLMs) have proven highly versatile, with remarkable successes even on problems ostensibly removed from traditional language generation.  One such example is solving regression problems, where the targets are real numbers rather than textual tokens.  A common approach to use LLMs on such problems is to perform fine-tuning based on the cross-entropy loss, and use autoregressive sampling at inference time. Another approach relies on fine-tuning a separate predic...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer** (2020)
- *Authors:* Colin Raffel et al.
- *Direct Connection:* By casting all tasks—including scalar predictions like STS-B—into text-to-text form trained with cross-entropy, this work established the autoregressive regression formulation that RAFT critiques and makes decision-aware.

**Pix2Seq: A Language Modeling Framework for Object Detection** (2021)
- *Authors:* Ting Chen et al.
- *Direct Connection:* Pix2Seq demonstrated that continuous targets can be discretized and learned autoregressively via token-level cross-entropy, directly motivating a principled, loss-aware treatment of autoregressive regression.

**Strictly Proper Scoring Rules, Prediction, and Estimation** (2007)
- *Authors:* Tilmann Gneiting et al.
- *Direct Connection:* This paper formalizes that under squared error the Bayes-optimal action is the conditional mean, the key decision-theoretic insight RAFT operationalizes for autoregressive numeric prediction.

### 💡 Inspiration

**Minimum Risk Training for Neural Machine Translation** (2016)
- *Authors:* Shiqi Shen et al.
- *Direct Connection:* This work introduced optimizing expected task loss for sequence models, directly inspiring RAFT’s use of Bayes-risk principles for regression-aware fine-tuning.

**High Quality Neural Machine Translation by Minimum Bayes Risk Decoding** (2022)
- *Authors:* Markus Freitag et al.
- *Direct Connection:* By showing that choosing outputs to minimize expected evaluation loss outperforms likelihood-based decoding, it underpins RAFT’s decision-theoretic alignment of training/inference for regression.

### 🔍 Gap Identification

**Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation** (2020)
- *Authors:* Bryan Eikema et al.
- *Direct Connection:* By showing that MAP decoding misaligns with evaluation risk, it highlights the need for risk-aware decision rules that RAFT adapts to regression with LLMs.

### 📊 Baseline

**BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** (2019)
- *Authors:* Jacob Devlin et al.
- *Direct Connection:* BERT’s widely adopted practice of adding a separate regression head trained with squared error for scalar outputs is the contrasting baseline RAFT unifies with autoregressive approaches under a Bayes decision view.

---

## Synthesis: How Prior Work Led to This Paper

A line of work established two dominant ways to use large language models for scalar prediction. One casts numeric targets as strings and trains decoder models with cross-entropy, as in the text-to-text paradigm where even regression-style tasks (e.g., STS-B) are generated token by token. Another keeps the model as a feature extractor and attaches a separate regression head trained with squared error, a practice popularized in BERT fine-tuning for similarity scoring and other continuous outputs. Extending the former, Pix2Seq showed that even inherently continuous targets like bounding boxes can be discretized and learned autoregressively with token-level likelihood, confirming the viability of sequence modeling for regression-like outputs. In parallel, decision-theoretic advances in sequence modeling—minimum risk training and minimum Bayes risk decoding—demonstrated that optimizing or decoding with respect to expected task loss can outperform likelihood-based objectives, while analyses of MAP’s inadequacy emphasized that mode-seeking decisions often misalign with evaluation risk. The statistical foundation for these ideas is the proper scoring rules literature, which specifies Bayes-optimal actions under given losses (e.g., conditional means for squared error).
Together, these strands revealed a gap: autoregressive CE training and regression-head MSE training succeed in practice but ignore the Bayes-optimal decision for regression losses. The natural next step is to make fine-tuning and inference explicitly regression-aware: learn a predictive distribution with a decoder LLM and choose actions per the Bayes rule for the target loss, thereby unifying the two baselines and aligning training with the evaluation objective.

---

*Analysis generated on: 2026-01-06T08:28:12.773876*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

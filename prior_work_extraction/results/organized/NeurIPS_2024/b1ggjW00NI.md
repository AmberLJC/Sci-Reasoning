# Prior Work Analysis Report

## Target Paper
**Title:** b1ggjW00NI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Run-Length Tokenization (RLT) directly addresses the token explosion in video transformers crystallized by TimeSformer, where exhaustive space-time attention turns many near-duplicate patches into wasted compute. Empirical evidence from VideoMAE shows that heavy temporal masking has surprisingly small impact on learning, reinforcing the premise that video inputs contain large stretches of redundant content. Prior efficiency methods, such as DynamicViT and EViT, prune tokens using learned importance modules or attention scores, but typically require extra training, thresholds, or dataset-specific tuning; they also impose nontrivial runtime overhead. ToMe takes a content-aware route by merging similar tokens during inference, but operates inside the network and adds per-layer merging steps and hyperparameters.

RLT’s core innovation is to exploit exact temporal repetition before the model ever runs: it finds runs of identical (or near-identical) patches and collapses them into a single token, then injects the collapsed duration via a positional/length encoding. This preserves semantic content while eliminating redundant compute and memory traffic with negligible preprocessing cost and no retraining. The design of length-aware encoding resonates with ideas from ALiBi, which shows that simple, efficient positional biases can make attention aware of distance/length without larger embeddings. Finally, adaptive tokenization ideas from TokenLearner inspired the notion that content, not just position, should determine token budgets; RLT instantiates this with a deterministic, parameter-free rule tailored to temporal redundancy. Together, these works shaped RLT’s simple, robust, and fast path to accelerate video transformers without sacrificing accuracy.

---
*Generated: 2026-01-06T23:39:42.955112*

# Prior Work Analysis Report

## Target Paper

**Title:** Small-scale proxies for large-scale Transformer training instabilities

**Conference:** ICLR 2024 (oral)

**Authors:** Mitchell Wortsman, Peter J Liu, Lechao Xiao, Katie E Everett, Alexander A Alemi, Ben Adlam, John D Co-Reyes, Izzeddin Gur, Abhishek Kumar, Roman Novak, Jeffrey Pennington, Jascha Sohl-Dickstein, Kelvin Xu, Jaehoon Lee, Justin Gilmer, Simon Kornblith

**Keywords:** Small Transformers, Training, Stability

**Abstract:** 
> Teams that have trained large Transformer-based models have reported training instabilities at large scale that did not appear when training with the same hyperparameters at smaller scales. Although the causes of such instabilities are of scientific interest, the amount of resources required to reproduce them has made investigation difficult. In this work, we seek ways to reproduce and study training instability at smaller scales. First, we focus on two sources of training instability described ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Scaling Vision Transformers to 22 Billion Parameters** (2023)
- *Authors:* Mostafa Dehghani et al.
- *Direct Connection:* This work identified the large-scale instability of attention logit growth and proposed practical mitigations (e.g., QK normalization/soft-capping), which the current paper explicitly targets to reproduce at small scale and validate via high–learning-rate proxies.

**PaLM: Scaling Language Modeling with Pathways** (2022)
- *Authors:* Aakanksha Chowdhery et al.
- *Direct Connection:* PaLM documented divergence between output logits and log probabilities at scale and popularized using z-loss to stabilize training, a failure mode and mitigation the current paper reproduces and tests in small models with high learning rates.

**The Z-Loss: A Shift and Scale Invariant Classification Loss** (2016)
- *Authors:* Alexandre de Brébisson et al.
- *Direct Connection:* This paper introduced the z-loss regularizer that directly mitigates the logit–log-prob divergence phenomenon, enabling the stabilization technique the current work evaluates within its small-scale instability proxies.

### 💡 Inspiration

**Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer** (2022)
- *Authors:* Greg Yang et al.
- *Direct Connection:* μP provided the principle that certain hyperparameter behaviors (notably learning rate) transfer predictably across scale, motivating the paper’s focus on learning-rate–loss curves as a small-scale proxy for large-scale instabilities.

### 🔍 Gap Identification

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* Switch Transformers reported large-scale training instabilities and reliance on z-loss for stability, underscoring the need for resource-efficient ways to study such failures that the current paper addresses via small-scale proxies.

### 🔗 Related Problem

**NormFormer: Improved Transformer Pretraining with Extra Normalization** (2021)
- *Authors:* Benno Kroth et al.
- *Direct Connection:* NormFormer showed that additional normalization on attention (including normalizing Q/K projections) reduces attention logit magnitudes, a mitigation class the paper evaluates and finds effective in the small-scale, high–learning-rate regime.

---

## Synthesis: How Prior Work Led to This Paper

Large-scale Vision Transformer training revealed that attention logits can grow during optimization, saturating softmax and destabilizing learning; Dehghani et al. documented this failure mode and demonstrated that interventions like query–key normalization or soft-capping the logits prevent entropy collapse. In massively scaled language models, Chowdhery et al. observed another pathology: a widening gap between pre-softmax logits and their log probabilities, leading to unstable training unless an auxiliary penalty is applied. The z-loss, first introduced by de Brébisson and Vincent as a shift- and scale-invariant regularizer on the log partition function, became a practical fix for this divergence and was adopted in large-model training. Complementing these observations, NormFormer showed that injecting extra normalization around attention projections curbs logit magnitudes and improves stability. More broadly, Switch Transformers highlighted the fragility of trillion-parameter training and the pragmatic need for stabilizers like z-loss. Finally, μP established that certain hyperparameter relationships—especially learning-rate behavior—transfer across model sizes, suggesting a path to study scale phenomena with smaller models.
Together, these works suggested a clear opportunity: if instability mechanisms are tied to logit scaling and overconfidence, and if learning-rate behavior transfers across scale, then small models trained at aggressive learning rates could act as faithful stand-ins for large-scale failures. Building on the exact failure modes and fixes (attention-logit growth and z-lossable logit–prob divergence), the paper systematizes learning-rate–loss sweeps across sizes and shows that the same mitigations succeed in small-scale proxies, providing a practical, low-cost testbed for diagnosing and preventing large-model instabilities.

---

*Analysis generated on: 2026-01-06T15:00:44.641978*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

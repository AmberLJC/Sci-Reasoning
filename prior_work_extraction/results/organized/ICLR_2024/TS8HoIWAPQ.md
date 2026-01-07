# Prior Work Analysis Report

## Target Paper

**Title:** Feature-aligned N-BEATS with Sinkhorn divergence

**Conference:** ICLR 2024 (spotlight)

**Authors:** Joonhun Lee, Myeongho Jeon, Myungjoo Kang, Kyunghyun Park

**Keywords:** Time series forecasting, Deep learning, Domain generalization, Representation learning, Sinkhorn divergence

**Abstract:** 
> We propose Feature-aligned N-BEATS as a domain-generalized time series forecasting model. It is a nontrivial extension of N-BEATS with doubly residual stacking principle (Oreshkin et al. [45]) into a representation learning framework. In particular, it revolves around marginal feature probability measures induced by the intricate composition of residual and feature extracting operators of N-BEATS in each stack and aligns them stack-wise via an approximate of an optimal transport distance referre...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Interpolating between Optimal Transport and Maximum Mean Discrepancy using Sinkhorn Divergences** (2019)
- *Authors:* Jean Feydy et al.
- *Direct Connection:* The alignment loss is precisely the Sinkhorn divergence introduced here, providing a stable, unbiased OT-based distance to compare empirical feature distributions between domains at each N-BEATS stack.

**Invariant Risk Minimization** (2019)
- *Authors:* Martin Arjovsky et al.
- *Direct Connection:* IRM formalized learning predictors invariant across environments, directly informing the paper’s objective of learning invariant features across multiple source domains via explicit stack-wise distribution alignment.

### 💡 Inspiration

**Sinkhorn Distances: Lightspeed Computation of Optimal Transport** (2013)
- *Authors:* Marco Cuturi
- *Direct Connection:* Efficient entropic OT and Sinkhorn iterations from this work make differentiable, minibatch-scale distribution alignment computationally feasible for stack-wise feature matching during training.

**Optimal Transport for Domain Adaptation** (2017)
- *Authors:* Nicolas Courty et al.
- *Direct Connection:* This paper established OT-based alignment as an effective principle for learning domain-invariant representations, directly motivating the use of OT (via Sinkhorn divergence) to align feature measures across source time series domains.

### 🔍 Gap Identification

**Domain-Adversarial Training of Neural Networks** (2016)
- *Authors:* Yaroslav Ganin et al.
- *Direct Connection:* Adversarial feature alignment framed the goal of domain invariance but suffers from instability and implicit metrics, a limitation addressed here by explicit metric alignment of stack-wise features using Sinkhorn divergence.

**Learning Transferable Features with Deep Adaptation Networks** (2015)
- *Authors:* Mingsheng Long et al.
- *Direct Connection:* MMD-based alignment introduced the ERM+alignment recipe that this work adopts, while its moment-matching limitations (ignoring geometry) are overcome by OT-based Sinkhorn divergence on per-stack feature distributions.

### 🔧 Extension

**N-BEATS: Neural basis expansion analysis for interpretable time series forecasting** (2020)
- *Authors:* Boris N. Oreshkin et al.
- *Direct Connection:* The proposed model directly extends N-BEATS’ doubly residual stacking by defining per-stack feature measures from its residual/feature-extraction operators and aligning these measures across domains while preserving N-BEATS’ forecasting head.

---

## Synthesis: How Prior Work Led to This Paper

N-BEATS introduced a doubly residual stacking architecture in which each block extracts features and passes residuals downstream; this design yields interpretable decompositions and strong forecasting performance. Sinkhorn divergences provided a principled, unbiased optimal transport discrepancy for comparing empirical distributions, capturing geometry while remaining differentiable and sample efficient. The underlying entropic optimal transport and Sinkhorn iterations made large-scale, minibatch computations practical for deep learning settings. Earlier work on optimal transport for domain adaptation demonstrated that OT-based alignment can learn domain-invariant representations that respect the geometry of data distributions, offering advantages over simple moment matching. Domain-adversarial training established the goal of learning invariant features via adversarial loss but exposed instability and the lack of an explicit metric. Deep Adaptation Networks showed an effective ERM-plus-alignment template using MMD, yet moment matching can blur structure by ignoring transport geometry. Invariant Risk Minimization formulated an explicit objective to seek predictors stable across environments, sharpening the conceptual target of invariance for multi-domain learning.

Together, these works suggested a path: combine a powerful, stack-structured forecaster whose intermediate features are interpretable (N-BEATS) with a principled, efficient geometric alignment mechanism (Sinkhorn-based OT) to explicitly enforce invariance across domains. The natural next step is to treat each stack’s extracted features as empirical measures and align them across source domains during training, following the ERM-plus-alignment recipe but replacing adversarial and MMD losses with a metric-grounded Sinkhorn divergence. This synthesis addresses instability and geometry-ignorance while preserving forecasting strength, yielding stack-wise invariant representations tailored for domain-generalized time series forecasting.

---

*Analysis generated on: 2026-01-06T13:32:20.515122*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

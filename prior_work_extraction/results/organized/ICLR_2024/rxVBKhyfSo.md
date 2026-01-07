# Prior Work Analysis Report

## Target Paper

**Title:** Selective Mixup Fine-Tuning for Optimizing Non-Decomposable Objectives

**Conference:** ICLR 2024 (spotlight)

**Authors:** Shrinivas Ramasubramanian, Harsh Rangwani, Sho Takemori, Kunal Samanta, Yuhei Umeda, Venkatesh Babu Radhakrishnan

**Keywords:** Non-Decomposable Objectives, Long-Tail Learning, Semi-Supervised Learning

**Abstract:** 
> The rise in internet usage has led to the generation of massive amounts of data, resulting in the adoption of various supervised and semi-supervised machine learning algorithms, which can effectively utilize the colossal amount of data to train models. However, before deploying these models in the real world, these must be strictly evaluated on performance measures like worst-case recall and satisfy constraints such as fairness. We find that current state-of-the-art empirical techniques offer su...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Consistent Binary Classification with Generalized Performance Metrics** (2014)
- *Authors:* Oluwasanmi Koyejo et al.
- *Direct Connection:* SelMix leverages the confusion-matrix–based characterization and cost-sensitive reduction for generalized metrics from this work to derive sampling weights that align feature mixing with the target non-decomposable objective.

**A Reductions Approach to Fair Classification** (2018)
- *Authors:* Alekh Agarwal et al.
- *Direct Connection:* SelMix adopts the reductions viewpoint that fairness constraints can be mapped to cost-sensitive learning, using this mapping to compute which groups to mix and emphasize during fine-tuning to meet fairness-style objectives.

### 💡 Inspiration

**ReMix: Rebalanced Mixup for Long-Tailed Recognition** (2020)
- *Authors:* Chou et al.
- *Direct Connection:* By showing that class-aware pairing and label interpolation can mitigate long-tail imbalance, ReMix directly inspires SelMix’s idea of learning a principled, objective-derived sampling distribution for whom to mix with whom.

### 🔍 Gap Identification

**Optimizing Non-decomposable Performance Measures: A Tale of Two Classes** (2014)
- *Authors:* Harikrishna Narasimhan et al.
- *Direct Connection:* This line of work provides surrogate-based optimizers for non-decomposable measures but requires training models from scratch per objective, a limitation SelMix overcomes via inexpensive objective-aware fine-tuning.

### 📊 Baseline

**Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization** (2020)
- *Authors:* Shiori Sagawa et al.
- *Direct Connection:* Group DRO serves as a primary baseline targeting worst-group performance, which SelMix surpasses by targeting worst-group recall and related non-decomposable metrics through metric-guided selective mixup rather than uniform group reweighting.

### 🔧 Extension

**mixup: Beyond Empirical Risk Minimization** (2018)
- *Authors:* Hongyi Zhang et al.
- *Direct Connection:* SelMix directly extends mixup’s convex interpolation of examples and labels by making the pairing and sampling objective-aware, selecting which samples to mix based on the target non-decomposable metric.

**Manifold Mixup: Better Representations by Interpolating Hidden States** (2019)
- *Authors:* Vikas Verma et al.
- *Direct Connection:* SelMix builds on manifold mixup’s idea of interpolating in feature space, using hidden-state mixup but with a metric-sensitive sampling distribution over groups/classes to bias improvements on the desired objective.

---

## Synthesis: How Prior Work Led to This Paper

Mixup introduced linear interpolation between samples and labels to regularize training and transfer information across examples, while manifold mixup extended this idea into hidden representations, showing that feature-space interpolation can be especially effective. On the evaluation side, Koyejo et al. established that many non-decomposable metrics admit a confusion-matrix characterization and can be optimized via cost-sensitive reductions, grounding how importance should be distributed across classes or groups. Narasimhan and collaborators developed surrogate-based procedures to optimize such metrics directly, but these typically necessitate specialized training and often retraining per target objective. In fairness, Agarwal et al. framed constraints as reductions to cost-sensitive classification, providing a systematic way to translate fairness goals into weighted learning problems. For robustness under subpopulation shift, Group DRO emphasized worst-group performance via group reweighting, while in long-tailed learning, ReMix demonstrated that class-aware mixup can sharpen minority performance by biasing pair selection and label interpolation.
Collectively, these works revealed that (i) objective-aware cost sensitivities can dictate whom to prioritize, (ii) feature-space mixup is a powerful mechanism for transferring signal, and (iii) existing NDO optimizers are costly to retrain per objective or operate with coarse reweighting. The natural next step was to fuse reductions-derived sensitivities with feature-level interpolation: selectively mix feature pairs according to a sampling distribution induced by the target non-decomposable metric, enabling inexpensive fine-tuning of pre-trained models to optimize worst-group recall, fairness-style constraints, and other non-decomposable objectives.

---

*Analysis generated on: 2026-01-06T15:16:34.770058*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

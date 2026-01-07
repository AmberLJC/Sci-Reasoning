# Prior Work Analysis Report

## Target Paper

**Title:** LiDAR: Sensing Linear Probing Performance in Joint Embedding SSL Architectures

**Conference:** ICLR 2024 (spotlight)

**Authors:** Vimal Thilak, Chen Huang, Omid Saremi, Laurent Dinh, Hanlin Goh, Preetum Nakkiran, Joshua M. Susskind, Etai Littwin

**Keywords:** Self Supervised Learning, Joint Embedding Architectures

**Abstract:** 
> Joint embedding (JE) architectures have emerged as a promising avenue for ac-
quiring transferable data representations. A key obstacle to using JE methods,
however, is the inherent challenge of evaluating learned representations without
access to a downstream task, and an annotated dataset. Without efficient and re-
liable evaluation, it is difficult to iterate on architectural and training choices for
JE methods. In this paper, we introduce LiDAR (Linear Discriminant Analysis
Rank), a metric d...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A Simple Framework for Contrastive Learning of Visual Representations** (2020)
- *Authors:* Ting Chen et al.
- *Direct Connection:* This work formalized the joint-embedding instance-discrimination pretext task and established linear evaluation as the standard proxy, providing the surrogate class structure (instance IDs and augmentations) on which LiDAR constructs its LDA-based discriminative rank.

**Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning** (2020)
- *Authors:* Jean-Bastien Grill et al.
- *Direct Connection:* BYOL showed that joint-embedding methods can avoid collapse without negatives, motivating the need for reliable collapse/quality diagnostics across JE variants that LiDAR targets and evaluates.

**The use of multiple measurements in taxonomic problems (Fisher’s Linear Discriminant Analysis)** (1936)
- *Authors:* R. A. Fisher
- *Direct Connection:* LiDAR directly builds on LDA’s between-class vs. within-class scatter formulation, using the LDA matrix associated with the JE surrogate labels and ranking its discriminative directions as the core metric.

### 🔍 Gap Identification

**Barlow Twins: Self-Supervised Learning via Redundancy Reduction** (2021)
- *Authors:* Jure Zbontar et al.
- *Direct Connection:* By explicitly maximizing feature covariance rank via decorrelation, this paper popularized rank/covariance-based signals whose inability to distinguish informative from uninformative dimensions is precisely the shortcoming LiDAR addresses.

**VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning** (2022)
- *Authors:* Adrien Bardes et al.
- *Direct Connection:* VICReg’s variance/covariance constraints further cemented covariance-rank as a monitoring heuristic, and its limitations in predicting linear-probe performance directly motivate LiDAR’s discriminative (LDA) notion of rank.

**Whitening for Self-Supervised Representation Learning** (2021)
- *Authors:* Artur Ermolov et al.
- *Direct Connection:* This work showed that enforcing whitened, full-rank features can still yield representations whose dimensionality says little about discriminative content, highlighting why a covariance-rank metric alone is insufficient and motivating LiDAR’s LDA-based criterion.

### 🔗 Related Problem

**LogME: Practical Assessment of Pretrained Models for Transfer Learning** (2021)
- *Authors:* Kaichao You et al.
- *Direct Connection:* LogME predicts downstream performance via marginal evidence but requires labeled target data, a key limitation that LiDAR overcomes by exploiting the JE surrogate task to compute a label-free discriminative rank.

---

## Synthesis: How Prior Work Led to This Paper

Contrastive joint-embedding methods established instance discrimination as a pretext task where each image instance, under augmentations, forms the basis for representation learning, with linear probing as the standard readout to assess learned features; SimCLR crystallized this setup and evaluation practice. BYOL demonstrated that negative-free joint-embedding can avoid trivial collapse, highlighting both the diversity of JE training dynamics and the need for principled, training-time diagnostics of representation quality. Redundancy-reduction approaches like Barlow Twins promoted decorrelation and implicitly high covariance rank as desirable signals, while VICReg codified variance and covariance objectives that further elevated covariance-rank heuristics as indicators of health. Whitening-based SSL showed that enforcing full-rank, decorrelated features is feasible yet does not guarantee informative dimensions for discrimination, underscoring a mismatch between covariance rank and linear separability. In parallel, transferability estimators such as LogME predicted downstream performance via marginal evidence but relied on labeled target samples, limiting their applicability during label-free SSL pretraining. Together these works revealed a gap: prevailing rank/covariance signals are insensitive to whether dimensions are discriminative for the task at hand, and label-dependent transfer metrics are unusable during JE training. The natural synthesis is to measure rank through discriminative directions defined by between-class versus within-class scatter. By instantiating Fisher’s LDA on the surrogate labels intrinsic to JE tasks, one can quantify the number of informative dimensions relevant to solving the SSL objective, yielding a label-free, training-time metric that better tracks linear probe performance.

---

*Analysis generated on: 2026-01-06T06:53:35.906547*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

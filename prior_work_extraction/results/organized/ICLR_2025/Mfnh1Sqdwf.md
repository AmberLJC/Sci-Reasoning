# Prior Work Analysis Report

## Target Paper

**Title:** Learning to Discover Regulatory Elements for Gene Expression Prediction

**Conference:** ICLR 2025 (oral)

**Authors:** Xingyu Su, Haiyang Yu, Degui Zhi, Shuiwang Ji

**Keywords:** Gene Expression, Deep Learning, Sequence Modeling

**Abstract:** 
> We consider the problem of predicting gene expressions from DNA sequences. A key challenge of this task is to find the regulatory elements that control gene expressions. Here, we introduce Seq2Exp, a Sequence to Expression network explicitly designed to discover and extract regulatory elements that drive target gene expression, enhancing the accuracy of the gene expression prediction. Our approach captures the causal relationship between epigenomic signals, DNA sequences and their associated reg...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Activity-by-contact model of enhancer–promoter regulation from thousands of CRISPR perturbations** (2019)
- *Authors:* Charles P. Fulco et al.
- *Direct Connection:* Seq2Exp operationalizes the ABC insight that enhancer 'activity' causally drives gene expression by conditioning sequence and epigenomic decompositions on latent active regulatory elements.

**Deep Variational Information Bottleneck** (2017)
- *Authors:* Alexander A. Alemi et al.
- *Direct Connection:* Seq2Exp’s Beta-parameterized bottleneck that filters non-causal components is grounded in the VIB objective of maximizing predictive information while compressing nuisance inputs.

### 💡 Inspiration

**Learning to Explain: An Information-Theoretic Perspective on Model Interpretation** (2018)
- *Authors:* Jianbo Chen et al.
- *Direct Connection:* Seq2Exp adapts L2X’s instance-wise, IB-based feature selection by learning element-level gates that select regulatory regions most informative for target gene expression.

**Learning Sparse Neural Networks through L0 Regularization** (2018)
- *Authors:* Christos Louizos et al.
- *Direct Connection:* Seq2Exp’s differentiable gating over candidate regulatory elements parallels L0/Hard-Concrete sparsification, but replaces it with Beta-distributed mixing to achieve soft yet selective causal attribution.

### 🔍 Gap Identification

**Model-based Analysis of ChIP-Seq (MACS)** (2008)
- *Authors:* Yong Zhang et al.
- *Direct Connection:* By outperforming MACS-style peak detection at identifying influential regions, Seq2Exp directly addresses the limitation that enrichment-based peak callers do not isolate causal regulatory elements for expression.

### 📊 Baseline

**Effective gene expression prediction from sequence by integrating long-range interactions** (2021)
- *Authors:* Žiga Avsec et al.
- *Direct Connection:* This work provides the primary sequence-to-expression formulation and long-range modeling baseline that Seq2Exp builds upon, motivating explicit discovery of causal regulatory elements beyond Enformer’s implicit attention.

### 🔧 Extension

**Deep learning sequence-based ab initio prediction of variant effects on gene expression and disease risk** (2018)
- *Authors:* Jian Zhou et al.
- *Direct Connection:* Seq2Exp extends ExPecto’s two-stage sequence→epigenome→expression paradigm by jointly modeling epigenomic signals and sequence under a learned causal regulatory-element selector instead of fixed-window aggregation with a linear model.

---

## Synthesis: How Prior Work Led to This Paper

Long-range sequence-to-expression modeling established that distal regulatory DNA contributes to transcriptional output, with Enformer showing how wide receptive fields can predict gene expression from sequence while leaving the identity of causal regulatory elements implicit. ExPecto demonstrated a two-stage route, predicting epigenomic signals from sequence and then aggregating them to explain expression, but relied on fixed windows and a downstream linear model. The Activity-by-Contact framework articulated a causal view: enhancer ‘activity’ measured by epigenomic signals, coupled with regulatory linkage, drives gene expression, concretizing the notion of active regulatory elements as the mechanistic units of control. In parallel, the Deep Variational Information Bottleneck formalized how to retain only predictive information while discarding nuisances, and L2X showed that IB can be used to learn instance-wise sparse feature selectors. Complementing these, L0/Hard-Concrete regularization provided differentiable gates to sparsify contributions in neural networks. Meanwhile, practical discovery of regulatory elements often relied on MACS peak calling, which detects enrichment but not causality with respect to expression.

Together these strands expose a gap: sequence-to-expression models and peak callers do not directly learn causal regulatory elements, while IB-based selection offers a principled way to isolate informative subsets. Seq2Exp synthesizes these ideas by conditioning both sequence and epigenomic representations on latent active elements and applying an information bottleneck with Beta-distributed gates to combine their effects, filtering non-causal components. This unifies Enformer-like long-range sequence modeling with ExPecto’s epigenomic mediation under an ABC-inspired causal definition of activity, yielding an end-to-end framework that discovers influential regulatory regions beyond enrichment-based peaks.

---

*Analysis generated on: 2026-01-06T07:11:53.424825*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

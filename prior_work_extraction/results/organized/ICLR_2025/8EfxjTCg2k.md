# Prior Work Analysis Report

## Target Paper

**Title:** MoDeGPT: Modular Decomposition for Large Language Model Compression

**Conference:** ICLR 2025 (oral)

**Authors:** Chi-Heng Lin, Shangqian Gao, James Seale Smith, Abhishek Patel, Shikhar Tuli, Yilin Shen, Hongxia Jin, Yen-Chang Hsu

**Keywords:** LLM, model compression, matrix decomposition

**Abstract:** 
> Large Language Models (LLMs) have significantly advanced AI with their exceptional performance across a wide range of tasks. However, their extensive computational requirements restrict their use on devices with limited resources.
While recent compression methods based on low-rank matrices show potential
solutions, they often suffer from significant loss of accuracy or introduce substantial
overhead in parameters and inference time. In this paper, we introduce Modular De-
composition (MoDeGPT), ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**CUR Matrix Decompositions for Improved Data Analysis** (2008)
- *Authors:* Petros Drineas et al.
- *Direct Connection:* This paper provides the CR/CUR decomposition framework and relative-error bounds that MoDeGPT leverages to construct compact factors from selected columns/rows when jointly decomposing module pairs.

### 💡 Inspiration

**Linformer: Self-Attention with Linear Complexity** (2020)
- *Authors:* Sinong Wang et al.
- *Direct Connection:* Linformer showed that Transformer attention exhibits low-rank structure that can be exploited via projection, motivating MoDeGPT’s larger-scale structural decomposition and hidden-dimension reduction guided by output preservation.

**SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot** (2023)
- *Authors:* Aleksandar Frantar et al.
- *Direct Connection:* SparseGPT’s layer-output reconstruction principle for one-shot LLM pruning directly informs MoDeGPT’s use of output reconstruction to safely reduce hidden dimensions across larger module structures.

### 🔍 Gap Identification

**LoRA: Low-Rank Adaptation of Large Language Models** (2021)
- *Authors:* Edward J. Hu et al.
- *Direct Connection:* LoRA popularized low-rank structure in Transformer matrices but adds adapter parameters and inference overhead, a limitation MoDeGPT addresses by compressing native weights via joint decomposition without extra modules.

### 📊 Baseline

**Exploiting Linear Structure Within Convolutional Networks for Efficient Evaluation** (2014)
- *Authors:* Emily L. Denton et al.
- *Direct Connection:* This work established SVD-based low-rank factorization with output reconstruction for compressing linear layers, which MoDeGPT extends by jointly decomposing consecutive Transformer subcomponents and enforcing bounded reconstruction error.

### 🔧 Extension

**Nyströmformer: A Nyström-Based Algorithm for Approximating Self-Attention** (2021)
- *Authors:* Yunyang Xiong et al.
- *Direct Connection:* Nyströmformer introduced Nyström approximation with accuracy guarantees for attention, which MoDeGPT repurposes as a building block to approximate paired subcomponents with bounded error in its modular decomposition.

### 🔗 Related Problem

**ALBERT: A Lite BERT for Self-supervised Learning of Language Representations** (2019)
- *Authors:* Zhenzhong Lan et al.
- *Direct Connection:* ALBERT’s factorized parameterization and reduced hidden dimensions demonstrate that shrinking intermediate representations can preserve accuracy, an idea MoDeGPT generalizes via data-driven reconstruction across paired subcomponents.

---

## Synthesis: How Prior Work Led to This Paper

Early neural network compression via low-rank SVD showed that linear layers can be factorized while preserving outputs by minimizing reconstruction error, concretely demonstrating a practical accuracy–efficiency trade-off (Denton et al.). In Transformers, Linformer established that self-attention exhibits inherent low-rank structure and can be projected to lower dimensions with controlled degradation, while Nyströmformer introduced a Nyström-based approximation of attention with empirical and theoretical fidelity guarantees. Beyond classical SVD, CR/CUR matrix decompositions provided a principled way to approximate matrices via selected columns/rows with relative-error bounds (Drineas et al.), enriching the toolkit for structured approximations. For LLMs, SparseGPT showed that matching layer outputs via a one-shot reconstruction objective is a powerful guiding signal for accuracy-preserving compression. Meanwhile, LoRA popularized leveraging low-rank structure in Transformer weights but introduced additional adapter parameters and runtime overhead, and ALBERT demonstrated that reducing hidden dimensions through factorization can maintain quality in Transformer-based models.
Together, these works reveal that (i) output reconstruction is a reliable objective for preserving behavior during compression, (ii) Transformer substructures possess exploitable low-rank structure, and (iii) decompositions like SVD, Nyström, and CR come with error control. The natural next step is to move beyond single-layer approximations and adapter add-ons toward a joint, structured factorization of consecutive Transformer subcomponents, using output reconstruction to safely reduce hidden dimensions while invoking decomposition schemes with provable error bounds—precisely the synthesis that enables efficient, accurate LLM compression at larger structural granularity.

---

*Analysis generated on: 2026-01-06T12:30:20.812201*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Scaling Laws for Sparsely-Connected Foundation Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Elias Frantar, Carlos Riquelme Ruiz, Neil Houlsby, Dan Alistarh, Utku Evci

**Keywords:** sparsity, scaling, optimal sparsity, efficiency, foundational models, transformers, structured sparsity, pruning

**Abstract:** 
> We explore the impact of parameter sparsity on the scaling behavior of Transformers trained on massive datasets (i.e., "foundation models"), in both vision and language domains. In this setting, we identify the first scaling law describing the relationship between weight sparsity, number of non-zero parameters, and amount of training data, which we validate empirically across model and data scales; on ViT/JFT-4B and T5/C4. These results allow us to characterize the "optimal sparsity", the sparsi...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Direct Connection:* This work established the power-law framework relating loss to model size and data, which the current paper directly extends by adding sparsity (non‑zero parameter count) as an explicit variable in the scaling formulation and fitting methodology.

**Scaling Vision Transformers** (2022)
- *Authors:* Xiaohua Zhai et al.
- *Direct Connection:* Their ViT/JFT scaling setup and empirical protocols in vision serve as the foundation for validating sparsity-aware scaling laws cross-domain, which the current paper adopts to test its theory on ViT/JFT-4B.

### 💡 Inspiration

**Rigging the Lottery: Making All Tickets Winners** (2020)
- *Authors:* Utku Evci et al.
- *Direct Connection:* RigL showed sparse-from-scratch training with dynamic connectivity can match dense models, directly motivating the present study’s analysis of sparsity scaling when training sparse Transformers (as opposed to only pruning after pretraining).

### 🔍 Gap Identification

**The State of Sparsity in Deep Neural Networks** (2019)
- *Authors:* Trevor Gale et al.
- *Direct Connection:* This survey documented the strengths and limitations of pruning and sparse training—especially the lack of systematic, large-scale evaluation—highlighting the precise gap the current paper fills by deriving and validating sparsity scaling laws at foundation-model scale.

### 📊 Baseline

**SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot** (2023)
- *Authors:* Elias Frantar et al.
- *Direct Connection:* As a state-of-the-art post-training pruning approach for large Transformers, SparseGPT provides the dense-to-sparse baseline regime that the current paper explicitly evaluates when examining scaling behavior starting from a pretrained dense model.

### 🔧 Extension

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Direct Connection:* By formalizing compute-optimal trade-offs between data and parameters (Chinchilla), this paper provides the compute/data lens that the current work generalizes to include weight sparsity and from which it derives the notion of data-dependent optimal sparsity.

### 🔗 Related Problem

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* By demonstrating that activation sparsity (MoE) improves scaling under fixed compute, this work contextualizes and inspires the current paper’s complementary exploration of weight sparsity within a scaling-law framework.

---

## Synthesis: How Prior Work Led to This Paper

Kaplan et al. established that language model loss follows power-law relations with model size and dataset size, crystallizing a quantitative framework for extrapolating performance across scales. Hoffmann et al. refined this view by showing compute-optimal trade-offs between parameters and data, recasting scaling as an allocation problem along a compute budget. In vision, Zhai et al. demonstrated consistent scaling behavior for Vision Transformers on JFT, providing experimental protocols and a high-scale setting to probe such laws beyond NLP. Evci et al. (RigL) showed that sparse-from-scratch training with dynamic connectivity can match dense models, validating weight sparsity as a viable training regime rather than merely a post hoc compression step. Frantar et al. (SparseGPT) proved large Transformers can be pruned in one shot post-training with minimal loss, establishing a competitive dense-to-sparse pathway. Gale et al. catalogued pruning methods and exposed the lack of systematic, large-scale evaluations and unifying principles for sparsity. Fedus et al. (Switch Transformers) revealed that sparsity can improve scaling under fixed compute via activation sparsity, underscoring the broader promise of sparsity-aware scaling.
Synthesizing these, a gap emerges: while scaling laws rigorously capture model/data trade-offs and sparsity methods work in practice, there is no scaling law that explicitly models weight sparsity. Building on the functional forms and compute-optimal perspective, and leveraging ViT/JFT and T5/C4 protocols, the current work introduces sparsity (non-zero parameters) into the scaling relationship, compares sparse-from-scratch versus dense-to-sparse regimes, and characterizes a data-dependent optimal sparsity—thus providing the missing quantitative law governing weight sparsity at foundation-model scale.

---

*Analysis generated on: 2026-01-06T19:59:03.062881*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

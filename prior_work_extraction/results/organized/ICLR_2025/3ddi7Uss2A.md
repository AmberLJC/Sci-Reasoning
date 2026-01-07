# Prior Work Analysis Report

## Target Paper

**Title:** What Does It Mean to Be a Transformer? Insights from a Theoretical Hessian Analysis

**Conference:** ICLR 2025 (spotlight)

**Authors:** Weronika Ormaniec, Felix Dangel, Sidak Pal Singh

**Keywords:** Hessian, Transformers

**Abstract:** 
> The Transformer architecture has inarguably revolutionized deep learning, overtaking classical architectures like multi-layer perceptions (MLPs) and convolutional neural networks (CNNs). At its core, the attention block differs in form and functionality from most other architectural components in deep learning—to the extent that, in comparison to MLPs/CNNs, Transformers are more often accompanied by adaptive optimizers, layer normalization, learning rate warmup, etc. The root causes behind these...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Attention Is All You Need** (2017)
- *Authors:* Ashish Vaswani et al.
- *Direct Connection:* This paper defines the single-head self-attention computation over queries, keys, and values with softmax weights, which is exactly the module whose parameter-space Hessian this work derives and analyzes in closed form.

**Limitations of the Empirical Fisher Information for Curvature in Deep Learning** (2019)
- *Authors:* Fredrik Künstner et al.
- *Direct Connection:* Their formal decomposition of curvature into generalized Gauss–Newton versus true Hessian terms and their matrix-calculus, layer-wise recipes provide the mathematical machinery that is adapted here to obtain an exact Hessian for self-attention and to attribute its components.

### 💡 Inspiration

**An Investigation into Neural Net Hessians** (2019)
- *Authors:* Amir Ghorbani et al.
- *Direct Connection:* Their finding that network Hessians exhibit structured outliers tied to data/labels and a data-dependent bulk directly motivates the attention-layer curvature separation into data-, weight-, and attention-specific terms and the ensuing spectral interpretation.

### 🔍 Gap Identification

**On Layer Normalization in the Transformer Architecture** (2020)
- *Authors:* Ruibin Xiong et al.
- *Direct Connection:* By documenting the instability of post-LN Transformers and the reliance on warmup and adaptive optimizers, this work identifies the concrete training pathologies that the present Hessian analysis of self-attention seeks to mechanistically explain.

### 🔧 Extension

**BackPACK: Packing more into Backprop** (2020)
- *Authors:* Felix Dangel et al.
- *Direct Connection:* This modular second-order backpropagation framework for exact per-layer curvature motivates and is directly extended from linear/conv modules to the attention block, enabling the compact matrix-derivative expression of the attention Hessian used here.

### 🔗 Related Problem

**Tensor Programs V: Taming Transformers** (2021)
- *Authors:* Greg Yang
- *Direct Connection:* This study analyzes pre/post-LN Transformer stability via Jacobian/NTK dynamics at initialization, providing a theoretical backdrop that is complemented here by a Hessian-level characterization specific to self-attention.

**ReZero is All You Need: Fast Convergence at Large Depth** (2020)
- *Authors:* Johannes Bachlechner et al.
- *Direct Connection:* By showing that residual scaling can stabilize deep Transformer training without normalization, this paper supplies a key empirical phenomenon that the present curvature formulas rationalize via the attenuation of sharp Hessian modes in attention.

---

## Synthesis: How Prior Work Led to This Paper

Self-attention, as introduced in Attention Is All You Need, computes softmax-normalized interactions between queries, keys, and values, establishing the exact nonlinear layer whose internal derivatives and interactions must be handled to study curvature. Work on curvature foundations showed how deep-network Hessians can be decomposed and computed layer-wise: Künschner et al. formalized the generalized Gauss–Newton versus true Hessian split and provided matrix-calculus recipes for propagating curvature through modules, and BackPACK demonstrated a modular second-order backprop framework that yields compact, Kronecker-structured expressions for common layers. Empirically and conceptually, An Investigation into Neural Net Hessians revealed that neural Hessians have structured outliers tied to data and a bulk term, suggesting interpretable decompositions of curvature into components. Transformer-specific training studies then exposed distinctive pathologies: On Layer Normalization in the Transformer Architecture documented instability of post-LN Transformers and the need for warmup/Adam, while Tensor Programs V characterized pre/post-LN stability via Jacobian/NTK analysis at initialization. Complementing these, ReZero showed that residual scaling can stabilize deep Transformers without normalization, highlighting the role of curvature/scale.
Together, these works suggest that a precise, layer-level Hessian for self-attention—derived with modular matrix calculus—could expose how attention-specific nonlinearities induce distinct curvature components, explain spectral structure (bulk versus outliers), and clarify why normalization, warmup, and adaptive methods stabilize training. Building on the curvature machinery and guided by the documented Transformer instabilities and stabilization tricks, the present work naturally synthesizes these insights into an exact Hessian characterization that isolates data, weight, and attention terms to mechanistically account for Transformers’ unique optimization behavior.

---

*Analysis generated on: 2026-01-06T12:28:30.468262*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

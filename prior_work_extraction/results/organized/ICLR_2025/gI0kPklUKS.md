# Prior Work Analysis Report

## Target Paper

**Title:** Bilinear MLPs enable weight-based mechanistic interpretability

**Conference:** ICLR 2025 (spotlight)

**Authors:** Michael T Pearce, Thomas Dooms, Alice Rigg, Jose Oramas, Lee Sharkey

**Keywords:** interpretability, mechanistic interpretability, bilinear, feature extraction, weight-based, eigenvector, eigendecomposition, tensor network

**Abstract:** 
> A mechanistic understanding of how MLPs do computation in deep neural net-
works remains elusive. Current interpretability work can extract features from
hidden activations over an input dataset but generally cannot explain how MLP
weights construct features. One challenge is that element-wise nonlinearities
introduce higher-order interactions and make it difficult to trace computations
through the MLP layer. In this paper, we analyze bilinear MLPs, a type of
Gated Linear Unit (GLU) without any ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Language Modeling with Gated Convolutional Networks** (2017)
- *Authors:* Y. N. Dauphin et al.
- *Direct Connection:* This paper introduced the GLU gating formulation that the current work directly modifies by removing the element-wise nonlinearity to obtain a purely bilinear MLP expressible as a third-order weight tensor.

### 💡 Inspiration

**GLU Variants Improve Transformer** (2020)
- *Authors:* Noam Shazeer
- *Direct Connection:* By showing that gated two-branch MLPs (e.g., SwiGLU) outperform standard MLPs in Transformers, this work motivated retaining the GLU-style factorized structure while dropping nonlinearities to enable a bilinear, analytically tractable weight form.

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Jacob Geva et al.
- *Direct Connection:* Framing FFNs as weight-encoded key–value memories directly motivated analyzing MLP weights themselves; the present work operationalizes this by eigendecomposing the bilinear MLP weight tensor to read out weight-encoded features.

### 🔍 Gap Identification

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* By revealing entangled (superposed) features in activations, this work highlighted that activation-only methods miss how weights implement features—precisely the gap addressed here via weight-spectrum analysis of bilinear MLPs.

### 📊 Baseline

**Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 with Sparse Autoencoders** (2024)
- *Authors:* Templeton et al.
- *Direct Connection:* Large-scale SAEs are the primary activation-based feature-extraction baseline that this paper contrasts with, replacing dataset-driven activation probes by eigendecomposing the bilinear MLP weight tensor to attribute features directly to weights.

### 🔗 Related Problem

**Bilinear CNN Models for Fine-Grained Visual Recognition** (2015)
- *Authors:* Tsung-Yu Lin et al.
- *Direct Connection:* This work established that multiplicative interactions can be expressed as bilinear forms amenable to matrix/tensor decompositions, a formalism the present paper adopts to cast MLP computation as a bilinear weight tensor.

**Speeding-up Convolutional Neural Networks using CP-Decomposition** (2015)
- *Authors:* Vadim Lebedev et al.
- *Direct Connection:* By treating layer parameters as higher-order tensors and factorizing them to expose low-rank structure, this paper provided the methodological precedent for analyzing low-rank spectra of a third-order weight tensor for interpretability rather than compression.

---

## Synthesis: How Prior Work Led to This Paper

Gated nonlinearities were crystallized by the GLU formulation, which decomposes a layer into two branches whose outputs interact multiplicatively, providing a simple structure for feature construction. Subsequent work showed that such gated two-branch MLPs (e.g., SwiGLU) improve Transformer performance, underscoring that gating—not the specific nonlinearity—drives effectiveness. In parallel, the feed-forward block was reinterpreted as a key–value memory whose weights explicitly encode feature write/read operations, suggesting that decoding features directly from weights could be viable. Separately, bilinear models in vision demonstrated that multiplicative interactions can be represented as bilinear forms and analyzed using matrix/tensor decompositions, while tensor factorization methods showed that treating network parameters as higher-order tensors exposes meaningful low-rank structure. Meanwhile, mechanistic interpretability identified superposition in activations and scaled sparse autoencoders extracted large numbers of activation features, but these activation-centric methods left open how MLP weights construct those features. Together these strands point to a natural opportunity: adopt the gated factorization, drop element-wise nonlinearities to keep a purely multiplicative (bilinear) interaction, and then analyze the resulting weight tensor spectrally. By expressing the MLP as a third-order tensor, eigendecomposition can reveal low-rank, interpretable modes that align with features, directly linking weight structure to computation. This synthesis bridges the gap left by activation-based methods, enabling weight-based mechanistic interpretability while retaining strong empirical performance.

---

*Analysis generated on: 2026-01-06T14:22:01.658786*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

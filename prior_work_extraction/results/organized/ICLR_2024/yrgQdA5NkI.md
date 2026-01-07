# Prior Work Analysis Report

## Target Paper

**Title:** Equivariant Matrix Function Neural Networks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ilyes Batatia, Lars Leon Schaaf, Gabor Csanyi, Christoph Ortner, Felix Andreas Faber

**Keywords:** equivariance, graph neural networks, long range

**Abstract:** 
> Graph Neural Networks (GNNs), especially message-passing neural networks (MPNNs), have emerged as powerful architectures for learning on graphs in diverse applications. However, MPNNs face challenges when modeling non-local interactions in systems such as large conjugated molecules, metals, or amorphous materials.
Although Spectral GNNs and traditional neural networks such as recurrent neural networks and transformers mitigate these challenges, they often lack extensivity, adaptability, generali...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Invariant and Equivariant Graph Networks** (2019)
- *Authors:* Haggai Maron et al.
- *Direct Connection:* This work’s characterization of permutation-equivariant linear maps as polynomials in the adjacency matrix directly motivates MFN’s design of layers as analytic matrix functions, ensuring permutation equivariance while enabling global, non-local mixing.

### 💡 Inspiration

**CayleyNets: Graph Convolutional Neural Networks with Complex Rational Spectral Filters** (2018)
- *Authors:* Ron Levie et al.
- *Direct Connection:* By introducing rational spectral filters that approximate Green’s-function-like responses, CayleyNets provides the template MFNs generalize via analytic matrix functions and resolvent expansions to achieve efficient long-range propagation.

**Predict then Propagate: Graph Neural Networks meet Personalized PageRank (APPNP)** (2019)
- *Authors:* Johannes Klicpera et al.
- *Direct Connection:* APPNP’s use of a Neumann-series approximation to the personalized PageRank resolvent (I − αP)^{-1} directly inspires MFN’s resolvent expansion to parameterize non-local interactions with linear-time implementations.

### 🔍 Gap Identification

**On the Bottleneck of Graph Neural Networks and its Practical Implications** (2021)
- *Authors:* Uri Alon and Eran Yahav
- *Direct Connection:* This work’s formalization of oversquashing in MPNNs motivates MFN’s non-local matrix-function propagation as a principled remedy for long-range information bottlenecks.

### 📊 Baseline

**MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields** (2022)
- *Authors:* Ilyes Batatia et al.
- *Direct Connection:* MFNs take the E(3)-equivariant, size-extensive local message passing core of MACE and augment it with learned matrix-function propagation to capture non-local interactions that MACE’s strictly local design cannot represent.

### 🔧 Extension

**Graph Neural Networks with Convolutional ARMA Filters** (2021)
- *Authors:* Filippo Maria Bianchi et al.
- *Direct Connection:* ARMA filters implement resolvent-like rational graph filters through recursive layers, which MFNs extend to a principled class of analytic matrix functions (including resolvents) integrated with geometric equivariance.

### 🔗 Related Problem

**Diffusion Improves Graph Learning (GDC)** (2019)
- *Authors:* Johannes Klicpera et al.
- *Direct Connection:* GDC shows that applying diffusion-based matrix functions (e.g., PPR/heat kernels) to graphs improves long-range information flow, which MFNs internalize as learnable analytic matrix functions rather than as a preprocessing step.

---

## Synthesis: How Prior Work Led to This Paper

Permutation equivariance on graphs was rigorously characterized by showing that linear equivariant layers can be written as polynomials of the adjacency (and related) matrices, establishing matrix functions as a principled vehicle for global, structure-respecting operations. Building on spectral methods, rational graph filters such as CayleyNets and ARMA introduced resolvent-like responses that approximate Green’s functions, enabling stable long-range propagation beyond finite-hop polynomials while remaining computationally tractable. Complementarily, diffusion-based techniques like APPNP operationalized personalized PageRank via a Neumann-series expansion of a resolvent, and GDC demonstrated that applying diffusion kernels (e.g., PPR, heat) as matrix functions enhances global information mixing without heavy message passing. In atomistic machine learning, MACE provided a highly accurate, E(3)-equivariant, size-extensive local message-passing architecture, yet by design emphasized strictly local interactions, leaving non-local dependencies underrepresented. Concurrently, the oversquashing literature made explicit the limitations of finite-hop MPNNs in transmitting long-range signals.
Taken together, these works reveal a clear opportunity: marry the theoretical guarantees of matrix-function-based equivariant operators and the efficiency of resolvent/diffusion filters with the geometric fidelity and extensivity of modern E(3)-equivariant atomistic models. The present approach synthesizes these strands by learning analytic matrix functions—implemented via resolvent expansions—to parameterize non-local interactions in a way that preserves permutation and rotational equivariance and scales linearly, directly addressing oversquashing while complementing strong local equivariant representations.

---

*Analysis generated on: 2026-01-06T18:02:49.176326*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

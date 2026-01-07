# Prior Work Analysis Report

## Target Paper

**Title:** On the Benefits of Memory for Modeling Time-Dependent PDEs

**Conference:** ICLR 2025 (oral)

**Authors:** Ricardo Buitrago, Tanya Marwah, Albert Gu, Andrej Risteski

**Keywords:** State Space Models, Partial Differential Equations

**Abstract:** 
> Data-driven techniques  have emerged as a promising alternative to traditional numerical methods for solving PDEs. For time-dependent PDEs, many approaches are Markovian---the evolution of the trained system only depends on the current state, and not the past states. In this work, we investigate the benefits of using memory for modeling time-dependent PDEs: that is, when past states are explicitly used to predict the future. Motivated by the Mori-Zwanzig theory of model reduction, we theoretical...

---

## Key Prior Works (5 papers with direct influence)

### 🏗️ Foundation

**Neural Operator: Learning Maps Between Function Spaces** (2021)
- *Authors:* A. M. Stuart et al.
- *Direct Connection:* MemNO is formulated within the neural operator framework that learns discretization-invariant mappings between function spaces, augmenting this foundation with explicit temporal memory.

**Optimal prediction and the Mori–Zwanzig formalism** (2000)
- *Authors:* A. J. Chorin et al.
- *Direct Connection:* The Mori–Zwanzig theory provides the core insight that reduced dynamics generically include a convolutional memory term, which directly motivates MemNO’s non-Markovian design and its theoretical results.

### 🔍 Gap Identification

**Renormalized Mori–Zwanzig reduction for systems with memory** (2015)
- *Authors:* Panagiotis Stinis
- *Direct Connection:* This work shows that neglecting or mis-specifying memory in reduced models leads to instability and bias, highlighting the precise deficiency in Markovian surrogates that MemNO addresses by learning memory kernels.

### 🔧 Extension

**Fourier Neural Operator for Parametric Partial Differential Equations** (2021)
- *Authors:* Zongyi Li et al.
- *Direct Connection:* MemNO directly extends FNO by keeping its Fourier-based spatial operator while replacing FNO’s Markovian one-step time propagation with an explicit long-memory temporal module.

**Efficiently Modeling Long Sequences with Structured State Spaces** (2022)
- *Authors:* Albert Gu et al.
- *Direct Connection:* MemNO adopts S4’s structured state-space long-convolution kernel to implement history-dependent temporal dynamics, enabling explicit use of past PDE states for prediction.

---

## Synthesis: How Prior Work Led to This Paper

Fourier Neural Operator (FNO) demonstrated that spectral convolutions can learn discretization-invariant spatial mappings for parametric PDEs, but its practical time integration commonly proceeds via Markovian one-step updates that only use the current state. Structured State Space Models, particularly S4, introduced a provably efficient parameterization of long convolutional kernels for sequences, enabling faithful and scalable modeling of long-range temporal dependencies. The neural operator framework formalized learning maps between function spaces, providing a principled foundation for PDE surrogates that generalize across meshes and resolutions. Independently, the Mori–Zwanzig formalism established that reduced descriptions of high-dimensional dynamics inherently include a history-dependent memory integral, rather than purely Markovian evolution in the observed variables. Building on this, renormalized Mori–Zwanzig reductions made concrete how omitting or mis-specifying memory leads to instability and bias, clarifying the stakes of accurate memory modeling in coarse or noisy settings.
These threads jointly exposed a gap: mainstream neural operators excel spatially yet treat time Markovianly, contrary to theoretical guidance that memory is essential when information is unresolved or noisy. The natural synthesis is to retain FNO’s strong spatial operator while instantiating the Mori–Zwanzig memory term via an S4-based long convolution over past states. This yields a non-Markovian neural operator that explicitly aggregates history, theoretically justified by Mori–Zwanzig and practically enabled by S4’s efficient memory parameterization, improving robustness under low-resolution discretizations and observational noise.

---

*Analysis generated on: 2026-01-06T16:20:57.139983*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

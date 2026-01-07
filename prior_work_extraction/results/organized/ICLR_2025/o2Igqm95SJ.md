# Prior Work Analysis Report

## Target Paper

**Title:** CAX: Cellular Automata Accelerated in JAX

**Conference:** ICLR 2025 (oral)

**Authors:** Maxence Faldor, Antoine Cully

**Keywords:** cellular automata, emergence, self-organization, neural cellular automata

**Abstract:** 
> Cellular automata have become a cornerstone for investigating emergence and self-organization across diverse scientific disciplines. However, the absence of a hardware-accelerated cellular automata library limits the exploration of new research directions, hinders collaboration, and impedes reproducibility. In this work, we introduce CAX (Cellular Automata Accelerated in JAX), a high-performance and flexible open-source library designed to accelerate cellular automata research. CAX delivers cutt...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Lenia: Biology-Inspired Artificial Life** (2019)
- *Authors:* Bert Chan
- *Direct Connection:* Lenia’s continuous-state CA with convolution-based interactions in 2D/3D provides the precise continuous CA formalism that CAX natively supports (real-valued grids, smooth kernels, arbitrary dimensionality).

**Generalization of Conway’s Game of Life to a continuous domain (SmoothLife)** (2011)
- *Authors:* Stephan Rafler
- *Direct Connection:* SmoothLife’s stencil/integral-based continuous update rule is a direct precursor to the convolutional, differentiable CA computations that CAX generalizes and accelerates across hardware backends.

### 💡 Inspiration

**Self-Organizing Textures** (2021)
- *Authors:* Eyvind Niklasson et al.
- *Direct Connection:* By showing that texture synthesis with NCAs benefits from flexible neighborhoods, channel counts, noise injection, and custom scheduling, this work directly motivated CAX’s modular CA step and configurable API (arbitrary neighborhoods, stochastic updates, multi-field states).

### 📊 Baseline

**Growing Neural Cellular Automata** (2020)
- *Authors:* Alexander Mordvintsev et al.
- *Direct Connection:* Its differentiable, convolutional per-cell update rule and training setup for tasks like pattern growth and regeneration define the NCA workloads (stochastic firing, multi-channel states, learned neighborhood filters) that CAX implements as first-class primitives and accelerates at scale.

### 🔧 Extension

**Cellular Automata as Convolutional Neural Networks** (2019)
- *Authors:* William Gilpin
- *Direct Connection:* By formalizing CA updates as convolutional operators amenable to GPU parallelism and autodiff, this work provided the key computational template that CAX standardizes into a general-purpose, multi-dimensional CA kernel framework.

### 🔗 Related Problem

**JAX MD: A Framework for Differentiable Physics** (2020)
- *Authors:* Samuel S. Schoenholz et al.
- *Direct Connection:* Demonstrating how XLA-jitted, vectorized simulation kernels and a functional JAX API yield portable high performance directly informed CAX’s architecture (jit/vmap/pmap compilation strategy and composable simulator design).

---

## Synthesis: How Prior Work Led to This Paper

Neural cellular automata were crystallized by Growing Neural Cellular Automata, which introduced a differentiable per-cell update rule implemented as small learned convolutions with stochastic firing, enabling tasks such as pattern growth and damage-robust regeneration. Self-Organizing Textures expanded this paradigm, revealing that practical NCA applications require configurable neighborhoods, multi-channel internal states, noise injection, and flexible update scheduling to control emergent behavior. In parallel, Lenia established a continuous-state, convolution-based CA formalism, including 2D/3D variants, proving that smooth, real-valued fields and kernels can yield rich self-organizing phenomena beyond discrete rules. SmoothLife earlier showed how Life-like dynamics can be generalized to continuous domains via integral/stencil computations, anchoring the use of convolutional neighborhoods for continuous CA. Complementing these modeling advances, Cellular Automata as Convolutional Neural Networks demonstrated that CA updates can be framed as convolutional operators compatible with GPU parallelism and automatic differentiation. Finally, JAX MD showed that a functional JAX design with jit-compiled, vectorized kernels enables high-performance, portable scientific simulation libraries. Together these works exposed a clear opportunity: while NCA and continuous CA require flexible, convolutional stencil updates and benefit from differentiable, hardware-accelerated execution, implementations remained ad hoc and task-specific. Synthesizing these insights, the natural next step was to standardize convolutional CA kernels in a modular, functional JAX library that natively supports discrete and continuous CA across dimensions, jit-compiles to modern accelerators, and reproduces canonical NCA and Lenia-style workloads with state-of-the-art performance and reproducibility.

---

*Analysis generated on: 2026-01-06T11:18:32.280743*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

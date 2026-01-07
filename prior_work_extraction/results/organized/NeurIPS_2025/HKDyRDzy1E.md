# Prior Work Analysis Report

## Target Paper
**Title:** HKDyRDzy1E
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Neural Controlled Differential Equations for Irregular Time Series** (2020)
- *Authors:* Patrick Kidger et al.
- *Connection:* SLiCEs are formulated explicitly as controlled differential equations, directly building on the Neural CDE framework to cast sequence modeling as input-driven continuous-time dynamics.

**HiPPO: Recurrent Memory with Optimal Polynomial Projections** (2020)
- *Authors:* Albert Gu et al.
- *Connection:* HiPPO introduced the linear state-space perspective and memory projection tools that underpin SSM/CDE-style continuous-time sequence models that SLiCE unifies and extends.

**Efficiently Modeling Long Sequences with Structured State Spaces** (2022)
- *Authors:* Albert Gu et al.
- *Connection:* S4 established the parallel-in-time SSM pathway for long-range modeling that SLiCE retains while generalizing the form of the input-dependent state-transition beyond S4-style structures.

### 💡 Inspiration

**Learning Fast Algorithms for Linear Transforms Using Butterfly Factorizations** (2019)
- *Authors:* Tri Dao et al.
- *Connection:* Butterfly/fast transform factorisations motivate SLiCE’s Walsh–Hadamard structured transitions by showing how compositions of sparse/Hadamard-like operators can approximate dense linear maps efficiently.

**Fastfood — Approximating Kernel Expansions in Loglinear Time** (2013)
- *Authors:* Quoc V. Le et al.
- *Connection:* Fastfood’s use of Hadamard-diagonal factorizations to mimic dense projections directly inspires SLiCE’s Hadamard-based variant and its expressivity-with-efficiency guarantees.

### 🔍 Gap Identification

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2024)
- *Authors:* Albert Gu et al.
- *Connection:* Mamba’s selective SSM uses input-dependent but diagonal state-transition matrices; SLiCE explicitly targets this diagonal expressivity limitation by proving structured (block-diagonal/sparse/Hadamard) transitions match dense expressivity while staying parallel-in-time.

### 🔗 Related Problem

**Resurrecting Recurrent Neural Networks for Long Sequences** (2023)
- *Authors:* Alessio Orvieto et al.
- *Connection:* LRU demonstrated the practical value of structured linear recurrences, informing SLiCE’s design space and its unification of linear RNNs with input-structured state-transition matrices.

---

## Synthesis

SLiCE sits at the intersection of continuous-time sequence modeling and structured linear algebra. The Neural CDE formulation (Kidger et al., 2020) provides the core mathematical language: hidden states evolve via controlled dynamics driven by the input, which SLiCE keeps but specializes to linear dynamics with input-dependent, structured transition matrices. HiPPO (Gu et al., 2020) and S4 (Gu et al., 2022) established that linear state-space views can be both expressive and parallel-in-time, seeding the path for SLiCE to maintain convolution/scan-style parallelism while moving beyond standard parametrizations. Mamba (Gu et al., 2024) pinpointed a compelling direction—input-dependent (selective) SSMs—but with a diagonal state matrix that empirically works yet theoretically restricts expressivity; SLiCE’s central advance directly addresses this gap by proving block-diagonal, sparse, and Walsh–Hadamard structures recover dense-matrix expressivity. Practical evidence that structured linear recurrences can be strong sequence learners came from LRU (Orvieto et al., 2023), which informed SLiCE’s unifying perspective over linear RNN-like modules. Finally, SLiCE’s Hadamard variant and expressivity results are inspired by structured fast transforms: butterfly factorizations (Dao et al., 2019) and Fastfood (Le et al., 2013) show how compositions of diagonal and Hadamard-like operators can emulate dense linear maps at lower cost. Together, these works directly shaped SLiCE’s formulation, theory, and efficient structured designs.

---
*Generated: 2026-01-06T23:08:23.968539*

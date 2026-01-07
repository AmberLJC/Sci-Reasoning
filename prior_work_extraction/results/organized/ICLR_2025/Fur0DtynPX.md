# Prior Work Analysis Report

## Target Paper
**Title:** Fur0DtynPX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators** (2021)
- *Authors:* Lu et al.
- *Connection:* GridMix targets the core limitation of DeepONet’s branch–trunk (global) modulation—strong global modeling but weak spatially varying detail—by replacing purely global conditioning with a spatial mixture of grid modulations.

**Feature-wise Linear Modulation for Visual Reasoning (FiLM)** (2018)
- *Authors:* Perez et al.
- *Connection:* FiLM established feature-wise modulation as a conditioning mechanism; GridMix extends this paradigm from global, sample-level conditioning to explicitly spatial modulation by mixing multiple grid-based representations in neural fields for PDEs.

### 💡 Inspiration

**Semantic Image Synthesis with Spatially-Adaptive Normalization (SPADE)** (2019)
- *Authors:* Park et al.
- *Connection:* SPADE demonstrated that per-location (spatial) modulation yields sharper, locally accurate generations; GridMix adapts this spatially adaptive modulation idea to neural fields for PDEs, but crucially replaces a single spatial modulator with a learnable mixture of grid-based modulators to balance locality and global coherence.

### 🔍 Gap Identification

**Instant Neural Graphics Primitives with a Multiresolution Hash Encoding** (2022)
- *Authors:* Müller et al.
- *Connection:* Multiresolution hash grids are a canonical ‘vanilla’ grid-based spatial representation that offers strong locality yet can overfit a fixed spatial domain and lack global context; GridMix directly addresses these shortcomings by learning mixtures of grids that encode global structure while preserving local fidelity.

### 📊 Baseline

**Fourier Neural Operator for Parametric Partial Differential Equations** (2021)
- *Authors:* Li et al.
- *Connection:* FNO is a principal baseline representing global operator learning; GridMix is explicitly designed to retain FNO-like global structure while overcoming its difficulty in reconstructing fine local details via spatially mixed grid modulation.

### 🔗 Related Problem

**KiloNeRF: Speeding up Neural Radiance Fields with Thousands of Tiny MLPs** (2021)
- *Authors:* Reiser et al.
- *Connection:* KiloNeRF’s spatial mixture-of-experts shows how decomposing space into local components and blending them improves detail and scalability; GridMix adopts the same spatial mixture principle but applies it to grid-based modulators for PDE neural fields rather than to multiple radiance-field MLP experts.

---

## Synthesis

GridMix is positioned against the global-conditioning paradigm that dominates neural-field operator learning for PDEs. DeepONet formalized the branch–trunk factorization and became the archetype of global modulation—strong at capturing global structures but comparatively weak in reconstructing spatially varying details. Similarly, the Fourier Neural Operator offers a powerful global inductive bias via spectral convolutions, yet often struggles with fine-grained locality. These global methods supplied both the problem formulation and the baseline GridMix seeks to improve.
On the other side of the spectrum, spatial modulation techniques—exemplified in vision by SPADE—show that per-location modulation is a direct route to sharper local fidelity. FiLM provided the broader conditioning framework that connects global and spatial modulation conceptually. However, when naïvely importing grid-based spatial encodings from neural graphics (e.g., Instant-NGP’s multiresolution hash grids), locality is achieved at the expense of robust global modeling and generalization across spatial domains, leading to overfitting to the training domain.
The key insight behind GridMix is to combine these worlds by mixing multiple grid-based modulators so that global structure can be explored while preserving locality. This mixture idea is reinforced by spatial mixture-of-experts in neural fields such as KiloNeRF, which shows how blending local components can yield both detail and scalability. GridMix operationalizes this as a mixture of grid representations for modulation and complements it with spatial domain augmentation to strengthen robustness to domain shifts, thereby directly addressing the explicit gaps in both global and vanilla grid-based approaches.

---
*Generated: 2026-01-06T23:09:26.643606*

# Prior Work Analysis Report

## Target Paper

**Title:** Linear Mode Connectivity in Differentiable Tree Ensembles

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ryuichi Kanoh, Mahito Sugiyama

**Keywords:** Linear Mode Connectivity, Soft Tree

**Abstract:** 
> Linear Mode Connectivity (LMC) refers to the phenomenon that performance remains consistent for linearly interpolated models in the parameter space. For independently optimized model pairs from different random initializations, achieving LMC is considered crucial for understanding the stable success of the non-convex optimization in modern machine learning models and for facilitating practical parameter-based operations such as model merging. While LMC has been achieved for neural networks by co...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Linear Mode Connectivity and the Lottery Ticket Hypothesis** (2020)
- *Authors:* Jonathan Frankle et al.
- *Direct Connection:* We adopt their linear mode connectivity formulation—interpolating between independently trained models—and target achieving this phenomenon for tree ensembles rather than neural networks.

**Loss Surfaces, Mode Connectivity, and Fast Ensembling of Deep Neural Networks** (2018)
- *Authors:* Timur Garipov et al.
- *Direct Connection:* Their demonstration that distinct minima can be connected through low-loss paths frames our objective of constructing parameter-space connectors for non-neural architectures like differentiable tree ensembles.

**Deep Neural Decision Forests** (2015)
- *Authors:* Peter Kontschieder et al.
- *Direct Connection:* We build on their differentiable probabilistic-routing trees/forests as the base soft tree architecture whose inherent symmetries (e.g., child/subtree flips) we formalize and exploit to attain LMC.

### 📊 Baseline

**Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data** (2019)
- *Authors:* Sergei Popov et al.
- *Direct Connection:* NODE serves as a representative soft tree ensemble whose structure (oblivious trees) highlights split-order invariance, enabling our symmetry-aware alignment to realize LMC and support parameter-space interpolation/merging.

### 🔧 Extension

**The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks** (2022)
- *Authors:* Saeed Entezari et al.
- *Direct Connection:* This work’s core idea generalizes Entezari et al.’s permutation-based alignment for achieving LMC in neural networks to tree ensembles by adding tree-specific symmetries (subtree flips and split-order invariance) to the alignment procedure.

### 🔗 Related Problem

**Git Re-Basin: Merging Models Modulo Permutation Symmetries** (2022)
- *Authors:* Sam Ainsworth et al.
- *Direct Connection:* The re-basin framework that aligns models into a common basin via permutation matching directly motivates our symmetry-alignment approach and informs how to enable merging/linear interpolation after accounting for tree-specific invariances.

---

## Synthesis: How Prior Work Led to This Paper

Mode connectivity was first established by showing that optima in neural networks can be connected by low-loss paths, revealing that disparate solutions need not be isolated (Garipov et al.). Subsequent work sharpened this to linear mode connectivity, demonstrating that simple linear interpolation between independently trained models can preserve performance (Frankle et al.). A key mechanistic insight emerged when permutation symmetries of hidden units were explicitly aligned: by matching neurons across networks, independent solutions could be brought into a shared basin, yielding linear connectors in weight space (Entezari et al.). This symmetry perspective also enabled practical model merging via weight-space operations once permutations were resolved (Ainsworth et al.). In parallel, differentiable decision trees and forests with probabilistic routing established a trainable, gradient-based tree ensemble family (Kontschieder et al.), and modern soft tree ensembles like NODE showed strong practical value and specific structural constraints such as oblivious splits that imply ordering symmetries (Popov et al.). Together, these threads exposed a gap: LMC and symmetry alignment were well-understood for neural nets but unexplored for differentiable tree ensembles, whose architectures embody distinct invariances beyond mere permutation of components. By synthesizing permutation alignment with tree-specific symmetries—subtree flip and split-order invariance—this work extends the LMC paradigm beyond neural networks, enabling linear interpolation and parameter-based merging for soft tree ensembles and explaining when independently trained trees can be aligned into a common basin.

---

*Analysis generated on: 2026-01-06T18:50:18.798692*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

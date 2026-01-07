# Prior Work Analysis Report

## Target Paper

**Title:** Improving Convergence and Generalization Using Parameter Symmetries

**Conference:** ICLR 2024 (oral)

**Authors:** Bo Zhao, Robert M. Gower, Robin Walters, Rose Yu

**Keywords:** Symmetry, optimization, generalization

**Abstract:** 
> In many neural networks, different values of the parameters may result in the same loss value. Parameter space symmetries are loss-invariant transformations that change the model parameters. Teleportation applies such transformations to accelerate optimization. However, the exact mechanism behind this algorithm's success is not well understood. In this paper, we show that teleportation not only speeds up optimization in the short-term, but gives overall faster time to convergence. Additionally, ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks** (2022)
- *Authors:* M. Entezari et al.
- *Direct Connection:* By showing that independently trained networks become linearly connectable after aligning hidden-unit permutations, this paper formalized permutation symmetries as function-preserving moves that the current work uses as the core teleportation operators.

**On Large-Batch Training and Sharp Minima** (2017)
- *Authors:* Nitish Shirish Keskar et al.
- *Direct Connection:* By linking sharp minima with poor generalization, this work established curvature as a key generalization indicator that the current paper directly investigates by teleporting to minima with different curvatures while preserving training loss.

### 💡 Inspiration

**Path-SGD: Path-Normalized Optimization in Deep Neural Networks** (2015)
- *Authors:* Behnam Neyshabur et al.
- *Direct Connection:* Path-SGD exploited ReLU rescaling symmetries to design optimization steps invariant to neuron-wise scaling, directly inspiring the use of symmetry-induced, loss-invariant reparameterizations (rescalings) as teleportation moves to accelerate training.

### 🔍 Gap Identification

**Sharp Minima Can Generalize For Deep Nets?** (2017)
- *Authors:* Laurent Dinh et al.
- *Direct Connection:* This paper demonstrated that sharpness/curvature is not parameterization-invariant because ReLU rescalings can arbitrarily change it, motivating the present work’s symmetry-aware analysis that teleports among equivalent minima to probe curvature–generalization relations.

### 📊 Baseline

**Sharpness-Aware Minimization for Efficiently Improving Generalization** (2021)
- *Authors:* Pierre Foret et al.
- *Direct Connection:* SAM is a primary generalization-improvement baseline centered on local curvature, against which the current paper situates teleportation as a complementary, symmetry-driven approach for finding solutions with more favorable curvature.

### 🔧 Extension

**Git Re-Basin: Merging Models modulo Permutation Symmetries** (2023)
- *Authors:* Sam Ainsworth et al.
- *Direct Connection:* This work operationalized neuron-permutation symmetries via weight-matching to move between loss-equivalent parameterizations (“re-basin”), a concrete mechanism the current paper adopts and systematizes as loss-invariant teleportation steps during optimization.

---

## Synthesis: How Prior Work Led to This Paper

Ainsworth et al. introduced a practical way to exploit neuron-permutation symmetries by weight-matching, enabling networks to be moved between loss-equivalent parameterizations—re-basin moves that make function-preserving jumps in parameter space. Entezari et al. showed that independently trained solutions become linearly connected once hidden-unit permutations are aligned, formalizing permutation symmetry as an actionable, loss-invariant transformation. Neyshabur et al. leveraged ReLU rescaling invariances with Path-SGD to craft optimization steps invariant to neuron-wise scaling, revealing how symmetry-aware reparameterizations can improve optimization dynamics. Dinh et al. demonstrated that curvature-based measures like sharpness are not invariant under these very rescaling symmetries, exposing a key ambiguity in interpreting curvature and motivating symmetry-aware analyses. Keskar et al. connected sharp minima to poorer generalization, elevating curvature from a descriptive property to a target for generalization-focused training. Foret et al. operationalized this perspective with SAM, explicitly optimizing for flatter neighborhoods to improve generalization.

Together, these works expose both the ubiquity and utility of parameter symmetries (permutations and rescalings), provide algorithms to compute symmetry-aligned reparameterizations, and highlight the central yet symmetry-fragile role of curvature in generalization. Building on this, the current paper synthesizes permutation and rescaling transforms into loss-invariant teleportation steps applied during training to accelerate convergence, while using these symmetry moves to deliberately reach minima with different curvatures to study and improve generalization. This is a natural next step: once symmetry-preserving moves are computable and curvature matters yet is parameterization-dependent, integrating symmetry-driven teleportation into standard optimizers offers a principled way to reshape optimization trajectories and generalization behavior without changing the learned function.

---

*Analysis generated on: 2026-01-06T13:59:16.790188*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

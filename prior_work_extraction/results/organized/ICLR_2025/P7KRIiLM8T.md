# Prior Work Analysis Report

## Target Paper

**Title:** u-$\mu$P: The Unit-Scaled Maximal Update Parametrization

**Conference:** ICLR 2025 (spotlight)

**Authors:** Charlie Blake, Constantin Eichenberg, Josef Dean, Lukas Balles, Luke Yuri Prince, Björn Deiseroth, Andres Felipe Cruz-Salinas, Carlo Luschi, Samuel Weinbach, Douglas Orr

**Keywords:** maximal update parametrization, learning dynamics, hyperparameter transfer, efficiency, training, stability, scaling, numerics, fp8, low precision

**Abstract:** 
> The Maximal Update Parametrization ($\mu$P) aims to make the optimal hyperparameters (HPs) of a model independent of its size, allowing them to be swept using a cheap proxy model rather than the full-size target model. We present a new scheme, u-$\mu$P, which improves upon $\mu$P by combining it with Unit Scaling, a method for designing models that makes them easy to train in low-precision. The two techniques have a natural affinity: $\mu$P ensures that the scale of activations is independent of...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Unit Scaling: Training Deep Networks at Unit Scale** (2024)
- *Authors:* Luke Yuri Prince et al.
- *Direct Connection:* u-μP integrates Unit Scaling’s design—initializing and parametrizing networks so weights, activations, and gradients start at scale one—to supply the missing absolute scale in μP and enable out-of-the-box FP8 training.

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Direct Connection:* By formalizing how parametrization fixes learning dynamics in the infinite-width limit, NTK provided the theoretical backdrop μP contrasted against, motivating u-μP’s choice to stay in a feature-learning, size-stable regime while controlling absolute scales.

### 🔍 Gap Identification

**FP8 Formats for Deep Learning** (2022)
- *Authors:* Paulius Micikevicius et al.
- *Direct Connection:* This work highlighted the sensitivity of FP8 training to value scales and the need for bespoke per-tensor scaling, a limitation u-μP addresses by designing networks to operate near unit magnitude throughout so FP8 works out-of-the-box.

### 📊 Baseline

**Tensor Programs V: Tuning Large Neural Networks via Zero-shot Hyperparameter Transfer** (2022)
- *Authors:* Greg Yang et al.
- *Direct Connection:* u-μP directly builds on μP’s maximal-update parameterization to preserve width-invariant hyperparameters, then simplifies and strengthens it by fixing the absolute scale via Unit Scaling to improve sweep efficiency and stability.

### 🔗 Related Problem

**Fixup Initialization: Residual Learning Without Normalization** (2019)
- *Authors:* Hongyi Zhang et al.
- *Direct Connection:* Fixup demonstrated that carefully chosen initialization and residual scaling can control signal magnitudes without normalization, a principle u-μP adopts at unit scale and merges with μP’s update-preserving parametrization.

**DeepNet: Scaling Transformers to 1,000 Layers** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* DeepNet’s residual-branch and depth-wise scaling to stabilize activations/gradients informed the idea that architectural scalings can enforce well-behaved magnitudes, which u-μP generalizes to unit-scale signals combined with μP’s hyperparameter invariance.

---

## Synthesis: How Prior Work Led to This Paper

Maximal Update Parametrization (μP) established that choosing a specific width scaling preserves update magnitudes and makes optimal hyperparameters transferable across model sizes, enabling zero-shot hyperparameter transfer. Unit Scaling showed that careful initialization and parametrization can set weights, activations, and gradients to unit magnitude at the start of training, making low-precision numerics far more robust. The Neural Tangent Kernel framework clarified how parametrization dictates infinite-width dynamics, underscoring why standard or NTK parametrizations can either distort hyperparameter transfer or linearize learning, motivating update-preserving regimes like μP. FP8 formats documented the numerical fragility of low-precision training and the reliance on ad hoc per-tensor scaling, emphasizing that stable value ranges are essential for practicality. Fixup demonstrated that targeted initialization and residual scaling can maintain healthy signal magnitudes without normalization, while DeepNet extended this idea with residual and depth-wise scalings to stabilize very deep Transformers, reinforcing the importance of architecture-level magnitude control.

Together, these works revealed a gap: μP delivers size-invariant update dynamics but leaves absolute signal scales under-specified, while low-precision training demands tight, predictable magnitudes without heavy per-tensor heuristics. u-μP synthesizes μP’s width-invariant hyperparameter transfer with Unit Scaling’s unit-magnitude design, fixing both relative (across width) and absolute (numerical) scales. This unification yields near-default, near-optimal hyperparameters, simplifies sweeps, and makes models naturally FP8-ready—an immediate next step given the combined insights on parametrization, initialization, and precision-aware stability.

---

*Analysis generated on: 2026-01-06T17:31:09.419179*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

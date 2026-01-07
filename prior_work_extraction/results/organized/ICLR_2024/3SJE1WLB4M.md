# Prior Work Analysis Report

## Target Paper

**Title:** Generalization error of spectral algorithms

**Conference:** ICLR 2024 (spotlight)

**Authors:** Maksim Velikanov, Maxim Panov, Dmitry Yarotsky

**Keywords:** gradient descent, kernel ridge regression, optimal algorithm, generalization, asymptotic error rates, power-laws

**Abstract:** 
> The asymptotically precise estimation of the generalization of kernel methods has recently received attention due to the parallels between neural networks and their associated kernels. However, prior works derive such estimates for training by kernel ridge regression (KRR), whereas neural networks are typically trained with gradient descent (GD). In the present work, we consider the training of kernels with a family of \emph{spectral algorithms} specified by profile $h(\lambda)$, and including K...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**On regularization algorithms in learning theory** (2007)
- *Authors:* Franz Josef Bauer et al.
- *Direct Connection:* Formalized spectral-filter regularization (including Tikhonov/KRR and Landweber/gradient descent) and the qualification/saturation concepts; this paper adopts that spectral-filter view via the learning profile h(λ) and provides asymptotically precise generalization characterizations within it.

**Optimal rates for the regularized least-squares algorithm** (2007)
- *Authors:* Antonio Caponnetto et al.
- *Direct Connection:* Established power-law source/capacity conditions and optimal learning rates for KRR, providing the power-law spectral assumptions on kernels and targets that this paper uses to compute precise asymptotic errors for general spectral algorithms.

### 💡 Inspiration

**Spectral bias and task-model alignment explain generalization in kernel regression** (2021)
- *Authors:* Murat Canatar et al.
- *Direct Connection:* Introduced an eigenmode-wise decomposition of kernel regression error and analyzed power-law task/kernel spectra, which this paper leverages to derive closed-form asymptotics for general spectral filters and to prove loss localization on specific spectral scales.

### 🔍 Gap Identification

**Just Interpolate: Kernel 'Ridgeless' Regression Can Generalize** (2020)
- *Authors:* Tengyuan Liang et al.
- *Direct Connection:* Established benign overfitting and risk characterizations for ridgeless KRR under spectral/source conditions, highlighting the limitation to KRR that this work explicitly overcomes by treating a broader family of spectral algorithms and GD within a unified h(λ) framework.

### 📊 Baseline

**Generalization error of random features and kernel methods** (2021)
- *Authors:* Song Mei et al.
- *Direct Connection:* Provided asymptotically exact generalization error formulas for kernel ridge regression under high-dimensional Gaussian design, which this paper generalizes from KRR to arbitrary spectral learning profiles h(λ) (including gradient descent) and to an additional low-dimensional translation-invariant model.

### 🔧 Extension

**Early stopping and nonparametric regression: an optimal data-dependent stopping rule** (2014)
- *Authors:* Garvesh Raskutti et al.
- *Direct Connection:* Analyzed early-stopped gradient descent in RKHS as a spectral regularizer and obtained optimal-rate bounds, which this work extends by giving exact asymptotics for GD through its general h(λ)-based spectral algorithm framework.

---

## Synthesis: How Prior Work Led to This Paper

Asymptotically precise learning-curve analyses for kernel methods were first obtained for kernel ridge regression under high-dimensional Gaussian models, with Mei et al. deriving exact generalization formulas that depended on the kernel eigenvalue distribution. Liang and Rakhlin characterized benign overfitting and risk of ridgeless KRR via spectral and source conditions, clarifying when interpolation can generalize but restricting attention to the KRR filter. In parallel, Canatar, Bordelon, and Pehlevan showed that kernel learning error decomposes additively across eigenmodes and that power-law structure in target and kernel spectra governs the dominant scales, providing a mode-wise lens and empirical-theoretic evidence of spectral scale dominance. The classical learning-theory and inverse-problems literature, notably Bauer, Pereverzev, and Rosasco, formalized spectral-filter algorithms—encompassing Tikhonov (KRR) and Landweber (gradient descent)—and introduced qualification and saturation, explaining why some filters saturate while others can exploit higher smoothness. Raskutti, Wainwright, and Yu analyzed early-stopped gradient descent in RKHS as a spectral regularizer and proved optimal-rate guarantees, linking iterative methods to spectral filtering. Caponnetto and De Vito established the power-law source/capacity conditions under which rates manifest, setting the spectral assumptions used widely in kernel theory. Together, these works exposed a gap: exact-asymptotic generalization was known primarily for KRR, while the broader class of spectral filters—including gradient descent—lacked precise characterizations. By unifying the spectral-filter viewpoint with eigenmode decompositions and power-law assumptions, the present work derives exact generalization as a functional of a learning profile h(λ), covers both high-dimensional Gaussian and low-dimensional translation-invariant settings, and clarifies how loss localizes on spectral scales, offering a refined account of KRR saturation and its avoidance by alternative spectral algorithms.

---

*Analysis generated on: 2026-01-06T06:03:36.560453*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

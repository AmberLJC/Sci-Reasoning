# Prior Work Analysis Report

## Target Paper

**Title:** Adam Exploits $\ell_\infty$-geometry of Loss Landscape via Coordinate-wise Adaptivity

**Conference:** ICLR 2025 (spotlight)

**Authors:** Shuo Xie, Mohamad Amin Mohamadi, Zhiyuan Li

**Keywords:** Adam, coordinate-wise adaptivity, adaptive algorithms, infinity norm

**Abstract:** 
> Adam outperforms SGD when training language models. Yet this advantage is not well-understood theoretically --  previous convergence analysis for Adam and SGD mainly focuses on the number of steps $T$ and is already minimax-optimal in non-convex cases, which are both $\widetilde{O}(T^{-1/4})$. In this work, we argue that the exploitation of nice $\ell_\infty$-geometry is the key advantage of Adam over SGD. More specifically, we give a new convergence analysis for Adam under novel assumptions tha...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Introductory Lectures on Convex Optimization: A Basic Course** (2004)
- *Authors:* Yurii Nesterov
- *Direct Connection:* We build directly on the notion of L-smoothness with respect to a general norm from this text, instantiating it at the ℓ∞ norm to derive sharper Adam convergence bounds.

**Iteration Complexity of Randomized Block-Coordinate Descent Methods for Minimizing a Composite Function** (2014)
- *Authors:* Peter Richtárik et al.
- *Direct Connection:* Their formalization of blockwise Lipschitz/smoothness constants underpins our blockwise smoothness assumptions used to analyze blockwise Adam.

### 💡 Inspiration

**Adaptive Subgradient Methods for Online Learning and Stochastic Optimization** (2011)
- *Authors:* John Duchi et al.
- *Direct Connection:* AdaGrad’s analysis connects coordinate-wise adaptivity to exploiting problem geometry via per-coordinate preconditioning and dual norms, directly motivating our lens that Adam’s advantage arises from favorable ℓ∞-geometry.

### 🔍 Gap Identification

**On the Convergence of Adam and Beyond** (2018)
- *Authors:* Sashank J. Reddi et al.
- *Direct Connection:* Their convergence results for Adam under ℓ2-smoothness focus on step-dependent rates that essentially match SGD, a limitation our work addresses by replacing the ℓ2 assumption with ℓ∞-smoothness to reveal Adam’s distinct advantage.

### 📊 Baseline

**Adam: A Method for Stochastic Optimization** (2015)
- *Authors:* Diederik P. Kingma et al.
- *Direct Connection:* This is the optimizer whose coordinate-wise moment adaptation we analyze, and our theory reframes Adam’s updates under ℓ∞-smoothness (and extends to blockwise variants) to explain when it outperforms SGD.

### 🔗 Related Problem

**Large Batch Optimization for Deep Learning: Training BERT in 76 minutes** (2020)
- *Authors:* Yang You et al.
- *Direct Connection:* By introducing layer-wise (blockwise) Adam-style scaling in LAMB for Transformers, this work directly motivates our theoretical treatment of blockwise Adam under blockwise smoothness.

---

## Synthesis: How Prior Work Led to This Paper

Adaptive methods were first linked to problem geometry in AdaGrad, which showed that per-coordinate preconditioning exploits structure through dual norms, yielding benefits when gradients are sparse or anisotropic. Adam introduced coordinate-wise adaptivity with exponential moving averages of first and second moments, a practical and widely adopted variant whose per-coordinate scaling also embodies a geometry-aware preconditioning. Prevailing analyses of Adam, typified by work that studies convergence under ℓ2-smoothness and reports step-dependent rates similar to SGD, do not isolate why Adam can outperform SGD in practice. The optimization literature provides a broader lens: smoothness can be defined with respect to arbitrary norms, and block coordinate methods formalize blockwise Lipschitz constants that capture heterogeneous curvature across parameter groups. Meanwhile, practical optimizers such as LAMB popularized layer-wise (blockwise) scaling in large Transformer training, underscoring the importance of block-structured geometry in deep models. Together these strands suggested a missing theoretical link: Adam-like methods may be capitalizing on favorable ℓ∞ and blockwise geometries that standard ℓ2 analyses ignore. Building on general-norm smoothness, we instantiate ℓ∞-smoothness to align with coordinate-wise adaptivity and extend block-coordinate smoothness to analyze blockwise Adam. This synthesis replaces T-centric ℓ2 bounds with geometry-aware guarantees whose constants match empirical measurements on modern networks, thereby explaining when Adam surpasses SGD and predicting its sensitivity when the favorable ℓ∞ geometry is disrupted.

---

*Analysis generated on: 2026-01-06T12:34:10.831551*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Residual Deep Gaussian Processes on Manifolds

**Conference:** ICLR 2025 (oral)

**Authors:** Kacper Wyrwal, Andreas Krause, Viacheslav Borovitskiy

**Keywords:** Gaussian processes, manifolds, deep Gaussian processes, probabilistic methods, variational inference, uncertainty quantification, geometric learning

**Abstract:** 
> We propose practical deep Gaussian process models on Riemannian manifolds, similar in spirit to residual neural networks.
With manifold-to-manifold hidden layers and an arbitrary last layer, they can model manifold- and scalar-valued functions, as well as vector fields.
We target data inherently supported on manifolds, which is too complex for shallow Gaussian processes thereon.
For example, while the latter perform well on high-altitude wind data, they struggle with the more intricate, nonstati...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Deep Gaussian Processes** (2013)
- *Authors:* Andreas Damianou et al.
- *Direct Connection:* It introduced the core idea of composing GPs into multi-layer structures, which the present paper generalizes from Euclidean spaces to manifold-to-manifold layers.

**Matérn Gaussian Processes for Vector Fields on Riemannian Manifolds (tangent-bundle GPs)** (2022)
- *Authors:* Viacheslav Borovitskiy et al.
- *Direct Connection:* By constructing GP priors over tangent-vector fields on manifolds, this work provides the geometric building block the new residual layers use to add tangent updates and map back to the manifold.

### 💡 Inspiration

**Deep Residual Learning for Image Recognition** (2016)
- *Authors:* Kaiming He et al.
- *Direct Connection:* The residual connection principle directly inspires the layer design here, where small GP-predicted manifold perturbations allow deep models to remain stable and revert to near-identity (i.e., shallow) behavior when extra depth is unnecessary.

### 📊 Baseline

**Matérn Gaussian Processes on Riemannian Manifolds** (2020)
- *Authors:* Viacheslav Borovitskiy et al.
- *Direct Connection:* This work provides the practical shallow GP priors on manifolds (via Laplace–Beltrami/SPDE constructions) that the new model explicitly builds upon and surpasses, addressing their stationarity-driven limitations by stacking residual manifold-aware layers.

### 🔧 Extension

**Doubly Stochastic Variational Inference for Deep Gaussian Processes** (2017)
- *Authors:* Hugh Salimbeni et al.
- *Direct Connection:* The paper delivers the scalable variational inference machinery for DGPs that is adapted here to manifold-valued layers, enabling practical training of deep GP compositions beyond Euclidean inputs.

**A Framework for Interdomain and Inducing Variables for Gaussian Processes** (2020)
- *Authors:* Mark van der Wilk et al.
- *Direct Connection:* Its interdomain inducing-variable framework allows defining inducing features through linear operators, which is leveraged here for manifold SPDE/Laplace-Beltrami-based priors to make manifold deep layers scalable.

---

## Synthesis: How Prior Work Led to This Paper

Deep Gaussian Processes were introduced as compositions of Gaussian-process mappings, offering rich hierarchical function priors beyond shallow kernels. Doubly stochastic variational inference then made such deep models trainable at scale by sampling through layers with variationally learned inducing variables. A general framework for interdomain inducing variables further enabled inducing features defined via linear operators, crucial when kernels arise from differential operators rather than closed-form covariance functions. On the geometric side, Matérn Gaussian processes on Riemannian manifolds established practical, Laplace–Beltrami/SPDE-based priors that respect manifold geometry and work well for scalar fields on curved spaces, while making clear the stationarity-driven limits of shallow models on complex, nonstationary data. Complementarily, Matérn-type constructions for vector fields on manifolds provided GP priors on tangent bundles, yielding geometrically consistent stochastic vector fields that can drive intrinsic updates on the manifold. Meanwhile, residual networks demonstrated that additive, small-step updates stabilize deep compositions and permit identity mappings that guard against overfitting.
Taken together, these works suggest composing manifold-aware layers where each layer predicts a tangent-vector update with a Matérn manifold GP and then maps back to the manifold, i.e., an intrinsic residual step. Interdomain inducing variables and doubly stochastic VI make these manifold layers scalable, while residual design brings stability and a natural fallback to shallow behavior. Building on manifold Matérn priors for both scalar fields and vector fields yields layers that handle manifold-to-manifold mappings and support scalar or vector-field outputs, making deep GPs practical and well-calibrated for complex nonstationary phenomena on curved spaces.

---

*Analysis generated on: 2026-01-06T11:39:49.270959*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

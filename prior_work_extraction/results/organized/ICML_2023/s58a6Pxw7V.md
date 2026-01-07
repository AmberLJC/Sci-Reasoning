# Prior Work Analysis Report

## Target Paper
**Title:** s58a6Pxw7V
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Variational Learning of Inducing Variables in Sparse Gaussian Processes** (2009)
- *Authors:* Michalis Titsias et al.
- *Connection:* Provides the variational inducing-variable GP framework and ELBO that underpins both inter-domain inducing features and the decoupled/orthogonally-decoupled approximations extended by this paper.

### 💡 Inspiration

**Deep Neural Networks as Gaussian Processes** (2018)
- *Authors:* Jaehoon Lee et al.
- *Connection:* Establishes the NN–GP correspondence that motivates using NN hidden-unit activations as inducing variables; the present method operationalizes this idea within the inter-domain/orthogonal framework to enable scalable representation learning.

### 🔍 Gap Identification

**Variational Inference for Gaussian Process Models with Linear Complexity** (2017)
- *Authors:* Cheng and Boots
- *Connection:* Introduces decoupled inducing sets for mean and covariance but suffers from instability/conditioning issues; the current paper addresses these limitations by adopting an orthogonal decomposition and designing spherical inter-domain features to stabilize and scale representation learning.

**Rates of Convergence for Sparse Variational Gaussian Process Regression** (2019)
- *Authors:* James Burt et al.
- *Connection:* Shows that approximation quality hinges on the inducing-feature span and motivates data-dependent bases; the paper directly targets this by learning spherical inter-domain features to reduce projection error in both components of the decomposition.

### 📊 Baseline

**Orthogonally Decoupled Variational Gaussian Processes** (2018)
- *Authors:* Salimbeni et al.
- *Connection:* Provides the orthogonal decomposition of GP variational approximations that this paper builds on; the proposed spherical inter-domain features extend ODGP by learning flexible, data-dependent bases for both the principal and orthogonal subspaces.

### 🔧 Extension

**A Framework for Interdomain and Multioutput Gaussian Processes** (2020)
- *Authors:* Mark van der Wilk et al.
- *Connection:* Formalizes inducing variables as linear inter-domain operators; the proposed spherical inter-domain features and NN-activation inducing variables are instantiated directly within this framework.

**Variational Fourier Features for Gaussian Processes** (2017)
- *Authors:* James Hensman et al.
- *Connection:* Demonstrates a practical inter-domain inducing-feature construction (Fourier features); the present work generalizes this idea to learn data-dependent spherical features and neural activation features for both principal and orthogonal components.

---

## Synthesis

The paper’s core idea—learning data-dependent, spherical inter-domain inducing features within an orthogonally-decoupled variational GP—sits at the intersection of variational sparse GPs, inter-domain inducing constructions, and the NN–GP connection. The variational inducing-variable foundation of Titsias (2009) provides the ELBO and conditioning structure on which all subsequent extensions rely. Building on this, van der Wilk et al. (2020) formalized inter-domain inducing variables as linear operators, enabling inducing features beyond input-space points; Hensman et al. (2017) exemplified this with variational Fourier features, showing how to engineer inducing features in transformed domains. In parallel, efforts to scale variational GPs via decoupling (Cheng & Boots, 2017) exposed instability and conditioning issues, which orthogonally-decoupled variational GPs (Salimbeni et al., 2018) resolved by decomposing the function into principal and orthogonal components. The present work directly extends ODGP by designing spherical, data-dependent inter-domain features for both components, thereby stabilizing and improving flexibility. This choice is also theoretically motivated by Burt et al. (2019), who showed that approximation error is governed by the span of inducing features, motivating learned bases that minimize projection error. Finally, the use of NN hidden-unit activations as inducing variables is inspired by the NN–GP correspondence (Lee et al., 2018), enabling representation learning within a GP framework. Together, these works directly enable, motivate, and define the gaps addressed by the proposed spherical inter-domain features for orthogonally-decoupled GPs.

---
*Generated: 2026-01-06T23:09:26.539541*

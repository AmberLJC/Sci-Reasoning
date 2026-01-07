# Prior Work Analysis Report

## Target Paper
**Title:** esYrEndGsr
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh and Percy Liang
- *Connection:* This paper provides the core influence-function formalism (upweight-one-point, implicit differentiation, inverse-Hessian–vector products) that the present work generalizes from supervised losses to diffusion-model objectives and generation-probability proxies.

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Jonathan Ho et al.
- *Connection:* The DDPM training objective and sampling framework define the concrete losses and generative mechanism that this paper differentiates through to formulate influence for "probability of generating an example," supplying the core problem setting for their attribution extension.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Connection:* The score-based/SDE formulation and its connections to likelihood via probability-flow ODE inform the proxy quantities for generation probability that this paper targets with influence functions in diffusion models.

**Deep learning via Hessian-free optimization** (2010)
- *Authors:* James Martens
- *Connection:* This work popularized using the generalized Gauss–Newton (GGN) matrix as a stable, PSD curvature surrogate for deep networks—an idea the paper leverages by basing its influence Hessian approximation on GGN to make computations well-behaved and scalable.

### 📊 Baseline

**Estimating Training Data Influence by Tracing Gradient Descent** (2020)
- *Authors:* Garima Pruthi et al.
- *Connection:* TracIn is a leading scalable data attribution method; the authors position prior attribution techniques like TracIn as specific design choices within their generalized influence framework and improve on them with principled curvature (GGN/K-FAC) for diffusion models.

### 🔧 Extension

**Optimizing Neural Networks with Kronecker-factored Approximate Curvature** (2015)
- *Authors:* James Martens and Roger Grosse
- *Connection:* The paper’s scalable data attribution hinges on replacing the intractable Hessian inverse in influence functions with a K-FAC approximation; this work directly supplies the Kronecker-factored curvature machinery the authors adapt to diffusion-model GGN matrices.

---

## Synthesis

The core innovation of this paper is to bring principled, scalable influence-function–based data attribution to diffusion models by formulating appropriate generative-probability proxies and making the required second-order computations tractable. This directly builds on Koh and Liang’s influence-function framework, reusing the upweight-one-point and implicit differentiation recipe but moving beyond supervised loss changes to changes in the probability of generating a particular example. The diffusion-model foundations of Ho et al.’s DDPM and Song et al.’s score-based SDE view provide the exact training objectives and generative formalisms whose quantities the new influence definitions differentiate through, as well as motivating proxy measures tied to likelihood or probability-flow formulations. A central technical barrier—computing inverse-Hessian–vector products at diffusion scale—is overcome by adopting curvature approximations from second-order optimization: Martens’ Hessian-free perspective establishes the generalized Gauss–Newton matrix as a stable curvature surrogate, and Martens & Grosse’s K-FAC supplies the Kronecker-factored structure that makes layerwise curvature inversion feasible. Finally, TracIn serves as the primary scalable baseline for data attribution; by showing how trajectory-based attributions fit as design choices within an influence framework, the paper both clarifies prior heuristics and supersedes them with a curvature-grounded, diffusion-specific formulation. Together, these works directly enable the paper’s formulation and scalable computation of influence for data attribution in diffusion models.

---
*Generated: 2026-01-06T23:09:26.614105*

# Prior Work Analysis Report

## Target Paper
**Title:** Mfk6ZbD6eY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**End-to-End Learning of Geometry and Context for Deep Stereo Regression** (2017)
- *Authors:* Kendall et al.
- *Connection:* GC-Net introduced the discretized cost volume with soft-argmin to produce continuous disparities; Stereo Risk explicitly reinterprets this estimator as the L2 Bayes-risk solution and replaces it with a continuous L1-risk minimizer to address multi-modal disparity distributions.

**Regression Quantiles** (1978)
- *Authors:* Koenker et al.
- *Connection:* Quantile regression established that minimizing L1 risk yields the conditional median; Stereo Risk leverages this result to justify an L1 Bayes estimator of disparity that is robust to multi-modal predictive distributions.

**Strictly Proper Scoring Rules, Prediction, and Estimation** (2007)
- *Authors:* Gneiting et al.
- *Connection:* This work connects decision-theoretic risk with optimal point predictions (mean for L2, median for L1); Stereo Risk uses this framework to reinterpret soft-argmin as an L2-risk estimator and motivate switching to L1-risk for stereo.

### 💡 Inspiration

**RAFT-Stereo: Multilevel Recurrent Field Transforms for Stereo Matching** (2021)
- *Authors:* Teed et al.
- *Connection:* RAFT-Stereo’s success with continuous, iterative disparity refinement motivated Stereo Risk’s continuous modeling perspective, which the present work formalizes via a Bayes-risk estimator rather than iterative residual updates.

### 📊 Baseline

**Pyramid Stereo Matching Network** (2018)
- *Authors:* Chang et al.
- *Connection:* PSMNet is a dominant soft-argmin baseline relying on disparity discretization; Stereo Risk directly improves upon this regime by eschewing discretization and substituting expectation-based regression with an L1 risk minimization over a continuous disparity domain.

### 🔧 Extension

**Deep Declarative Networks** (2021)
- *Authors:* Gould et al.
- *Connection:* DDNs provide implicit differentiation through argmin-defined layers, including non-smooth objectives; Stereo Risk adopts this machinery to backpropagate through the non-differentiable L1-risk disparity optimizer.

**Differentiable Convex Optimization Layers** (2019)
- *Authors:* Agrawal et al.
- *Connection:* By differentiating through KKT conditions of convex programs, this work enables optimization-as-a-layer; Stereo Risk leverages the same paradigm to implement an end-to-end differentiable L1-risk minimization for disparity.

---

## Synthesis

Stereo Risk’s core idea—estimating disparity as the solution of a continuous Bayes-risk minimization—emerges at the intersection of deep stereo’s discretized cost-volume tradition and decision-theoretic estimation. GC-Net established the modern template of discretizing disparity and using soft-argmin to regress a continuous value, a formulation widely adopted by PSMNet and successors. The present work explicitly reframes soft-argmin as the L2 Bayes-risk estimator, then addresses its known brittleness under multi-modal posteriors by replacing it with an L1-risk estimator. This shift is grounded in classical results: Gneiting and Raftery formalized the link between loss functions and optimal point predictions (mean for squared loss, median for absolute loss), while Koenker and Bassett’s quantile regression establishes the median as the solution to L1 risk. In parallel, RAFT-Stereo demonstrated that dispensing with fixed disparity discretization and modeling disparity continuously can be highly effective, motivating Stereo Risk’s commitment to continuous modeling but with a principled risk-minimization lens rather than iterative updates. A practical hurdle—training through the non-differentiable L1-risk argmin—draws directly on optimization-as-a-layer advances. Deep Declarative Networks provide a general implicit differentiation framework for argmin-defined layers, including non-smooth objectives, and Differentiable Convex Optimization Layers supply KKT-based implicit gradients. Stereo Risk fuses these strands to yield a continuous, L1-risk-based estimator with end-to-end differentiability that directly overcomes the discretization and multi-modality limitations of soft-argmin stereo.

---
*Generated: 2026-01-06T23:09:26.477117*

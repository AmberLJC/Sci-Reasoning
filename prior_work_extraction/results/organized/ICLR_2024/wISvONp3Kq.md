# Prior Work Analysis Report

## Target Paper

**Title:** Learning No-Regret Sparse Generalized Linear Models with Varying Observation(s)

**Conference:** ICLR 2024 (spotlight)

**Authors:** Diyang Li, Charles Ling, zhiqiang xu, Huan Xiong, Bin Gu

**Keywords:** Generalized Linear Models, Learning with Varying Data, Differential Equations

**Abstract:** 
> Generalized Linear Models (GLMs) encompass a wide array of regression and classification models, where prediction is a function of a linear combination of the input variables. Often in real-world scenarios, a number of observations would be added into or removed from the existing training dataset, necessitating the development of learning systems that can efficiently train optimal models with varying observations in an online (sequential) manner instead of retraining from scratch. Despite the si...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Regularization Paths for Generalized Linear Models via Coordinate Descent** (2010)
- *Authors:* Jerome H. Friedman et al.
- *Direct Connection:* This work established the standard sparse-GLM formulation and exact batch solutions (via pathwise coordinate descent) that the new algorithm explicitly seeks to match while updating under data variations instead of retraining from scratch.

### 💡 Inspiration

**Least Angle Regression** (2004)
- *Authors:* Bradley Efron et al.
- *Direct Connection:* LARS’ homotopy/path-following view of l1-regularized solutions directly inspires the paper’s idea of following an exact solution path, generalized from changing regularization strength to changing datasets via a differential-equation trajectory.

### 🔍 Gap Identification

**Efficient Online and Batch Learning using Forward Backward Splitting** (2009)
- *Authors:* John C. Duchi et al.
- *Direct Connection:* FOBOS introduced proximal online updates yielding sparse solutions, but it handles only insertions and trades exact optimality for regret bounds, a limitation the new method addresses by tracking the batch-optimal sparse GLM under additions and deletions.

### 📊 Baseline

**Ad Click Prediction: a View from the Trenches** (2013)
- *Authors:* H. Brendan McMahan et al.
- *Direct Connection:* FTRL-Proximal is the canonical online sparse-GLM method the paper positions against, adopting its online learning and regret framework but overcoming its inaccuracy under dataset changes and inability to support deletions.

### 🔧 Extension

**Bregman Iterative Algorithms for l1-Minimization with Applications to Compressed Sensing** (2008)
- *Authors:* Wotao Yin et al.
- *Direct Connection:* The paper adapts the Bregman/continuous-time perspective on l1-regularization to GLM losses and time-varying data, designing an ODE-based update that preserves sparsity while remaining on (or near) the batch-optimal solution manifold.

### 🔗 Related Problem

**Incremental and Decremental Support Vector Learning** (2001)
- *Authors:* Gert Cauwenberghs et al.
- *Direct Connection:* This work demonstrated exact addition/deletion updates by maintaining KKT optimality, motivating the paper’s simultaneous handling of insertions and deletions by continuously enforcing optimality conditions for sparse GLMs.

---

## Synthesis: How Prior Work Led to This Paper

Coordinate-descent GLM solvers showed that l1-regularized generalized linear models could be fit exactly in batch, tracing solution paths over regularization levels to yield sparse, high-accuracy models. LARS provided a homotopy view of l1 solutions, revealing that optimal coefficients evolve along piecewise-smooth paths with discrete support changes as a parameter varies, a structural insight central to exact path tracking. Bregman iterative methods and their continuous-time interpretations further connected sparse solutions to differential equations/differential inclusions, where thresholding dynamics drive trajectories onto l1-optimal manifolds without sacrificing exactness. In contrast, online sparse learning methods like FOBOS and FTRL-Proximal delivered regret guarantees via proximal updates and per-step shrinkage, but they primarily support insertions, induce approximation bias relative to batch optima, and lack mechanisms to maintain exact optimality under dataset changes. Meanwhile, incremental–decremental SVM learning established that exact updates under both addition and deletion are possible by preserving optimality/KKT structure between steps. Together, these works expose a gap: exact, sparse GLMs are well understood offline, online methods provide regret but sacrifice exactness and deletions, and homotopy/ODE viewpoints suggest one can track optimal sparse solutions continuously. The present paper synthesizes these strands by formulating an ODE-driven path that maintains the batch-optimal sparse GLM as observations are added or removed, while embedding the analysis within an online learning/no-regret framework and adaptively tuning data-dependent regularization to keep the trajectory on the exact solution path.

---

*Analysis generated on: 2026-01-07T00:14:26.784907*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

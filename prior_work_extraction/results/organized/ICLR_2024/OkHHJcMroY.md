# Prior Work Analysis Report

## Target Paper

**Title:** PILOT: An $\mathcal{O}(1/K)$-Convergent Approach for Policy Evaluation with Nonlinear Function Approximation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zhuqing Liu, Xin Zhang, Jia Liu, Zhengyuan Zhu, Songtao Lu

**Keywords:** min-max optimization, adaptive batch size, policy evaluation.

**Abstract:** 
> Learning an accurate value function for a given policy is a critical step in solving reinforcement learning (RL) problems. So far, however, the convergence speed and sample complexity performances of most existing policy evaluation algorithms remain unsatisfactory, particularly with non-linear function approximation. This challenge motivates us to develop a new path-integrated primal-dual stochastic gradient (PILOT) method, that is able to achieve a fast convergence speed for RL policy evaluatio...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient** (2017)
- *Authors:* Lam M. Nguyen et al.
- *Direct Connection:* The recursive gradient tracking mechanism underlying PILOT’s estimator is directly grounded in SARAH’s stochastic recursive gradient framework that SPIDER builds upon.

**SBEED: Smoothed Bellman Error Embedding for Stochastic Control** (2018)
- *Authors:* Bo Dai et al.
- *Direct Connection:* PILOT’s primal-dual min-max policy-evaluation formulation follows SBEED’s convex-conjugate-based saddle-point embedding of Bellman error with function approximation.

### 💡 Inspiration

**SPIDER: Near-Optimal Nonconvex Optimization via Stochastic Path-Integrated Differential Estimator** (2018)
- *Authors:* Cong Fang et al.
- *Direct Connection:* PILOT borrows the SPIDER path-integrated gradient estimator idea to control stochastic gradient variance, which is key to attaining O(1/K) convergence with constant step sizes in a nonconvex setting.

**PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization** (2021)
- *Authors:* Zhize Li et al.
- *Direct Connection:* PILOT+ adopts PAGE’s core idea of replacing periodic full-gradient refreshes with probabilistic/adaptive batch updates to maintain low-variance gradients without full passes.

### 📊 Baseline

**Gradient Temporal-Difference Learning Algorithms** (2009)
- *Authors:* Richard S. Sutton et al.
- *Direct Connection:* PILOT builds on the primal-dual gradient-TD lineage (e.g., GTD2/TDC) and explicitly overcomes their two-timescale/diminishing-stepsize limitations by providing single-timescale constant-stepsize convergence guarantees.

### 🔗 Related Problem

**Near-Optimal Algorithms for Minimax Optimization** (2020)
- *Authors:* Tianyi Lin et al.
- *Direct Connection:* PILOT adapts variance-reduced single-loop techniques and O(1/K) stationarity guarantees for nonconvex–(strongly) concave minimax problems to the RL policy-evaluation saddle-point setting.

---

## Synthesis: How Prior Work Led to This Paper

Path-integrated and recursive gradient estimators emerged as powerful tools for fast nonconvex optimization. SPIDER introduced a path-integrated differential estimator that tightly controls variance, enabling constant stepsizes and near-optimal convergence in nonconvex regimes. Its roots lie in SARAH’s stochastic recursive gradient framework, which showed how incremental gradient differences along an iterate path can track true gradients accurately at low cost. PAGE refined this direction by eliminating the need for periodic full-gradient computations, using probabilistic/adaptive refreshes to retain low variance without expensive passes. In reinforcement learning, SBEED established a saddle-point embedding of Bellman error via convex conjugacy, providing a primal-dual min-max template compatible with nonlinear function approximation. Earlier, Gradient Temporal-Difference (GTD) methods pioneered a primal-dual gradient approach to policy evaluation, but typically required two-timescale updates or diminishing stepsizes for convergence. In parallel, minimax optimization advances demonstrated that single-loop, variance-reduced schemes can achieve O(1/K) stationarity in nonconvex–concave settings.
Bringing these strands together suggested a path: cast policy evaluation with nonlinear function approximation as a saddle-point problem, and endow its primal-dual updates with path-integrated variance-reduced gradients to unlock constant-stepsize O(1/K) convergence in a single timescale. The remaining bottleneck—periodic full-gradient refresh—could be removed by PAGE-style adaptive batching, preserving guarantees while reducing cost. This synthesis naturally led to PILOT’s path-integrated primal-dual design and the adaptive-batch enhancement PILOT+, directly addressing the speed, stability, and sample-efficiency gaps identified in prior GTD-style and primal-dual RL approaches.

---

*Analysis generated on: 2026-01-06T06:49:32.933841*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

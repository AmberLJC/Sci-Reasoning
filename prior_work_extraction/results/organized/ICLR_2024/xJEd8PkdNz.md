# Prior Work Analysis Report

## Target Paper

**Title:** Impact of Computation in Integral Reinforcement Learning for Continuous-Time Control

**Conference:** ICLR 2024 (spotlight)

**Authors:** Wenhan Cao, Wei Pan

**Keywords:** Integral Reinforcement Learning, Bayesian Quadrature, Newton's Method

**Abstract:** 
> Integral reinforcement learning (IntRL) demands the precise computation of the utility function's integral at its policy evaluation (PEV) stage. This is achieved through quadrature rules, which are weighted sums of utility functions evaluated from state samples obtained in discrete time. Our research reveals a critical yet underexplored phenomenon: the choice of the computational method -- in this case, the quadrature rule -- can significantly impact control performance. This impact is traced ba...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Online actor–critic algorithm to solve the continuous-time infinite-horizon optimal control problem** (2010)
- *Authors:* K. G. Vamvoudakis et al.
- *Direct Connection:* This work established the integral reinforcement learning policy-iteration framework for continuous-time HJB problems, where policy evaluation requires numerical integration of the utility along trajectories—the exact computational stage whose accuracy the current paper analyzes.

**Inexact Newton methods** (1982)
- *Authors:* R. S. Dembo et al.
- *Direct Connection:* The inexact Newton framework shows how additive evaluation errors affect Newton’s convergence, which the current paper leverages by treating policy-evaluation quadrature error in IntRL as the inexactness term and deriving proportional error bounds.

### 💡 Inspiration

**On an iterative technique for Riccati equation computations** (1968)
- *Authors:* D. L. Kleinman
- *Direct Connection:* Kleinman’s result that policy iteration for LQR is equivalent to a Newton step on the Riccati/HJB equation directly motivates framing IntRL policy iteration as Newton’s method, enabling the current paper’s analysis of how computation errors enter the Newton iteration.

**Bayes–Hermite quadrature** (1991)
- *Authors:* A. O’Hagan
- *Direct Connection:* This seminal work introduced Bayesian quadrature with principled posterior uncertainty on integrals, supplying the error-certification mechanism that the current paper uses to select and justify quadrature rules for IntRL policy evaluation.

### 🔍 Gap Identification

**Optimal control of unknown continuous-time systems using off-policy reinforcement learning** (2014)
- *Authors:* S. Modares et al.
- *Direct Connection:* By deploying off-policy IntRL with trajectory sampling and quadrature-based policy evaluation but without quantifying integration error, this paper highlighted the unaddressed impact of quadrature accuracy on policy iteration that the current work explicitly analyzes and resolves.

### 🔧 Extension

**Probabilistic Integration: A Role in Statistical Computation** (2019)
- *Authors:* F.-X. Briol et al.
- *Direct Connection:* By formalizing error bounds and convergence rates for Bayesian quadrature via Gaussian processes, this paper provides the quantitative integration-error controls that the current work plugs into its Newton-iteration analysis of IntRL.

---

## Synthesis: How Prior Work Led to This Paper

Integral reinforcement learning for continuous-time control was concretely established by Vamvoudakis et al., who formulated policy iteration around the integral form of the HJB equation and thus required numerical integration during policy evaluation. Modares et al. extended IntRL to off-policy learning with sampled trajectories, operationalizing quadrature-based policy evaluation but without assessing how the chosen quadrature rule’s error affects convergence or control. In parallel, Kleinman showed that policy iteration for LQR corresponds to a Newton step on the Riccati/HJB equation, providing a Newtonian lens on policy iteration. The numerical analysis literature on inexact Newton methods by Dembo et al. then characterized how evaluation inaccuracies enter Newton iterations as additive error terms with explicit convergence implications. From the probabilistic numerics side, O’Hagan introduced Bayesian quadrature to estimate integrals with calibrated uncertainty, while Briol et al. supplied rigorous error bounds and convergence rates for GP-based quadrature.
Together these works reveal a critical junction: IntRL’s policy evaluation hinges on numerical integration whose errors can, via the policy-iteration–as–Newton perspective, directly perturb convergence and final control performance. The synthesis is to model policy evaluation as an inexact Newton step and to control the inexactness by selecting quadrature rules with certified errors—naturally provided by Bayesian quadrature—thereby quantifying and mitigating computation-induced performance degradation in continuous-time IntRL.

---

*Analysis generated on: 2026-01-06T11:31:43.631762*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

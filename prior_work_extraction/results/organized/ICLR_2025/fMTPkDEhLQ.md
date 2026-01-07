# Prior Work Analysis Report

## Target Paper

**Title:** Tight Lower Bounds under Asymmetric High-Order Hölder Smoothness and Uniform Convexity

**Conference:** ICLR 2025 (oral)

**Authors:** Site Bai, Brian Bullins

**Keywords:** Convex Optimization, Uniform Convexity, Lower Bound, High-Order Method, Regularization, Hölder Smoothness

**Abstract:** 
> In this paper, we provide tight lower bounds for the oracle complexity of minimizing high-order Hölder smooth and uniformly convex functions. Specifically, for a function whose $p^{th}$-order derivatives are Hölder continuous with degree $\nu$ and parameter $H$, and that is uniformly convex with degree $q$ and parameter $\sigma$, we focus on two asymmetric cases: (1) $q > p + \nu$, and (2) $q < p+\nu$. Given up to $p^{th}$-order oracle access, we establish worst-case oracle complexities of $\Ome...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Problem Complexity and Method Efficiency in Optimization** (1983)
- *Authors:* A. S. Nemirovski et al.
- *Direct Connection:* The oracle-complexity framework and adversarial hard-instance methodology used to derive lower bounds here are direct extensions of the Nemirovski–Yudin information-based complexity model to higher-order oracles and mixed curvature–smoothness settings.

**Universal Gradient Methods for Convex Optimization Problems** (2015)
- *Authors:* Y. Nesterov et al.
- *Direct Connection:* The precise problem formulation—Hölder continuity of derivatives with parameters (p, ν, H) and q-uniform convexity with parameter σ—and the target dependencies on H, σ, and ε are adopted from Nesterov’s universal framework.

### 💡 Inspiration

**Tight Complexity Lower Bounds for Smooth Convex Optimization** (2016)
- *Authors:* B. Woodworth et al.
- *Direct Connection:* The Gaussian-smoothing hard-instance/resisting-oracle construction introduced here is generalized by replacing it with an ℓ∞-ball–truncated-Gaussian smoothing tailored to simultaneously control high-order Hölder constants and preserve uniform convexity.

### 🔍 Gap Identification

**Information-Theoretic Lower Bounds on the Oracle Complexity of Convex Optimization** (2009)
- *Authors:* A. Agarwal et al.
- *Direct Connection:* By revealing the distinct roles of smoothness and strong convexity (q=2) in lower bounds for first-order methods, this work highlighted the absence of tight, analogous dependencies for higher-order Hölder smoothness and general q-uniform convexity that the present results close.

### 📊 Baseline

**Implementable Tensor Methods in Unconstrained Convex Optimization** (2018)
- *Authors:* Y. Nesterov et al.
- *Direct Connection:* Upper bounds for p-th order methods under Hölder smoothness (and their restart-based behavior under uniform convexity) from implementable tensor methods serve as the primary performance benchmarks that the new lower bounds are designed to match.

### 🔧 Extension

**Oracle Complexity of Second-Order Methods for Smooth Convex Optimization** (2020)
- *Authors:* Y. Carmon et al.
- *Direct Connection:* The lower-bound template for higher-order access—via chain-like hard functions with carefully controlled derivatives—provided for p=2 is extended to arbitrary p and to the asymmetric regimes q > p+ν and q < p+ν.

---

## Synthesis: How Prior Work Led to This Paper

Nemirovski and Yudin established the information-based oracle model and the adversarial hard-instance paradigm that underpin modern lower-bound proofs in convex optimization. Nesterov’s universal gradient framework formalized Hölder-smoothness of order p with degree ν and parameters (H, ν) together with q-uniform convexity with parameter σ, and analyzed algorithms whose rates exhibit explicit dependencies on these quantities. Building on this, Nesterov’s implementable tensor methods gave practical p-th order procedures and matching upper bounds under Hölder continuity, with restart mechanisms under uniform convexity yielding characteristic accuracy dependencies. Woodworth and Srebro introduced a Gaussian-smoothing hard-instance technique for smooth convex optimization that precisely calibrates smoothness while maintaining difficulty for oracle-based methods. Carmon, Duchi, Hinder, and Sidford developed second-order oracle lower bounds via chain-style constructions that tightly control higher derivatives and track query complexity within the higher-order oracle model. Agarwal, Hazan, Kale, and Kakade provided information-theoretic lower bounds delineating how smoothness and strong convexity separately govern complexity, motivating sharper separation-of-parameter dependencies.

Together, these works revealed both the techniques and the gaps: while upper bounds existed for Hölder–tensor methods and first- or second-order lower bounds were known, there was no tight oracle complexity delineating how high-order Hölder smoothness interacts with general q-uniform convexity, especially in asymmetric regimes q ≷ p+ν. By merging chain-type adversarial constructions with a smoothing approach refined via ℓ∞-truncated Gaussian kernels, and calibrating parameters to preserve uniform convexity while controlling p-th order Hölder constants, the present work derives tight bounds that match tensor-method upper limits and expose distinct H, σ, and ε dependencies—including the log–log behavior—across the two asymmetric regimes.

---

*Analysis generated on: 2026-01-06T09:04:08.687989*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

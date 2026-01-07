# Prior Work Analysis Report

## Target Paper

**Title:** Adaptive Batch Size for Privately Finding Second-Order Stationary Points

**Conference:** ICLR 2025 (spotlight)

**Authors:** Daogao Liu, Kunal Talwar

**Keywords:** Differential privacy, non-convex optimization, adaptive batch size

**Abstract:** 
> There is a gap between finding a first-order stationary point (FOSP) and a second-order stationary point (SOSP) under differential privacy constraints, and it remains unclear whether privately finding an SOSP is more challenging than finding an FOSP. Specifically, Ganesh et al. (2023) claimed that an $\alpha$-SOSP can be found with $\alpha=\Tilde{O}(\frac{1}{n^{1/3}}+(\frac{\sqrt{d}}{n\epsilon})^{3/7})$, where $n$ is the dataset size, $d$ is the dimension, and $\epsilon$ is the differential priv...

---

## Key Prior Works (5 papers with direct influence)

### 🏗️ Foundation

**SPIDER: Near-Optimal Nonconvex Optimization via Stochastic Path-Integrated Differential Estimator** (2018)
- *Authors:* Fang et al.
- *Direct Connection:* SPIDER’s path-integrated gradient estimator underlies SpiderBoost and provides the variance-reduction backbone that the new adaptive, private estimator refines.

**How to Escape Saddle Points Efficiently** (2017)
- *Authors:* Jin et al.
- *Direct Connection:* The perturbed-gradient saddle-escape paradigm and the widely used α-SOSP notion originate here, forming the conceptual basis for the saddle-point escape procedure adapted in the private setting.

**Private and Continual Release of Statistics** (2011)
- *Authors:* Chan et al.
- *Direct Connection:* The binary tree (tree-aggregation) mechanism introduced here is incorporated to release many noisy gradient/statistics with logarithmic privacy cost, enabling the adaptive-batch SpiderBoost updates to remain DP.

### 🔍 Gap Identification

**Privately Finding Second-Order Stationary Points** (2023)
- *Authors:* Ganesh et al.
- *Direct Connection:* This work attempted a private SOSP algorithm with a saddle-escape subroutine whose flawed analysis led to weaker guarantees, directly motivating the corrected escape analysis and tighter α bound achieved here.

### 🔧 Extension

**SPIDERBoost and Momentum: Faster Variance Reduction Algorithms for Nonconvex Optimization** (2019)
- *Authors:* Wang et al.
- *Direct Connection:* The proposed method explicitly builds on the SpiderBoost framework, modifying its variance-reduced estimator with adaptive batch sizes and privatized updates to enable reliable saddle-escape under DP.

---

## Synthesis: How Prior Work Led to This Paper

Jin et al. established the perturbed-gradient paradigm for escaping strict saddle points and formalized the α-second-order stationary point condition, showing that stochastic first-order methods can provably reach local minima by injecting carefully calibrated perturbations. Fang et al. introduced SPIDER, a path-integrated variance-reduced gradient estimator that sharply lowers stochastic noise in nonconvex optimization by periodically refreshing large-batch gradients and using recursive control variates. Building on SPIDER, Wang et al. proposed SpiderBoost, a practical and faster variance-reduction scheme that keeps gradient variance small with a simple estimator structure, making it a natural platform for nonconvex optimization at scale. Chan et al. developed the binary tree mechanism for continual release, enabling many running averages or partial sums to be privately published with only logarithmic privacy cost, a key tool for maintaining differential privacy across long optimization trajectories. Ganesh et al. attempted to combine private gradient-based optimization with a saddle-escape step to privately reach SOSPs, claiming a specific α rate; however, a flaw in their escape analysis meant the privacy/noise tradeoff did not actually support the stated guarantee.

Together, these works highlighted that reliable saddle escape in a private, stochastic regime demands both low-variance gradient estimates and frugal privacy accounting across many updates. The natural synthesis is to retrofit SpiderBoost’s variance-reduction with adaptive batch sizing and tree-aggregated privatization so the estimator remains accurate enough to trigger saddle escape under DP. Correcting the escape analysis while controlling privacy loss through tree aggregation yields a tighter α bound, closing the gap exposed by the flawed prior guarantee.

---

*Analysis generated on: 2026-01-06T08:18:52.984441*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

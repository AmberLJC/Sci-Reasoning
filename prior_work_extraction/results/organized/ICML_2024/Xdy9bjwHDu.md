# Prior Work Analysis Report

## Target Paper
**Title:** Xdy9bjwHDu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Without-Replacement Sampling for Stochastic Gradient Methods** (2016)
- *Authors:* Ohad Shamir
- *Connection:* Formalized SGD without-replacement (random reshuffling) and provided core convergence analyses that this paper builds on and explicitly seeks to strengthen from average-iterate (and strong-convexity/distance metrics) to last-iterate function-value guarantees.

**Incremental Subgradient Methods for Nondifferentiable Optimization** (2001)
- *Authors:* Angelia Nedić et al.
- *Connection:* Introduced and analyzed incremental (including projected) gradient/subgradient methods—the IG component of shuffling methods—whose constrained optimization setting the current paper targets when proving last-iterate convergence in function value.

**Introductory Lectures on Convex Optimization: A Basic Course** (2004)
- *Authors:* Yurii Nesterov
- *Connection:* Established the canonical last-iterate function-value convergence framework for projected gradient methods in convex optimization, which this paper extends to the shuffling/incremental regime without assuming strong convexity.

### 💡 Inspiration

**Why Random Reshuffling Beats Stochastic Gradient Descent** (2015)
- *Authors:* A. Gürbüzbalaban et al.
- *Connection:* Established that random reshuffling can outperform with-replacement SGD and developed epoch-wise analytical tools for finite-sum shuffling that directly motivate the present last-iterate analysis for RR/SO/IG.

### 🔍 Gap Identification

**Tight Complexity Bounds for Optimizing Finite Sums** (2016)
- *Authors:* Blake Woodworth et al.
- *Connection:* Provided sharp lower bounds for finite-sum optimization methods; the present work positions its last-iterate function-value rates relative to these bounds and claims to match or nearly match the known last-iterate lower limits.

**Non-asymptotic analysis of stochastic approximation algorithms for machine learning** (2011)
- *Authors:* Eric Moulines et al.
- *Connection:* Delivered last-iterate convergence in mean-squared error for strongly convex problems (with-replacement sampling), highlighting the limitation to distance metrics and strong convexity that this paper overcomes for shuffling methods and function-value criteria.

---

## Synthesis

The core contribution—proving last-iterate convergence rates in objective value for shuffling gradient methods (RR, SO, IG) without strong convexity—rests on the finite-sum and without-replacement lineage. Shamir (2016) formalized SGD without-replacement and delivered the baseline analyses for random reshuffling, largely focused on average-iterate guarantees and settings where strong convexity or distance-based metrics were central. Gürbüzbalaban et al. (2015) showed why random reshuffling can outperform with-replacement sampling and introduced epoch-wise tools for analyzing permutation-induced bias—techniques that shape the analytical backbone for last-iterate reasoning in shuffled passes. The incremental gradient lineage originates with Nedić and Bertsekas (2001), who defined and studied IG and its projected variants in constrained convex optimization—precisely the regime where function value (not squared distance) is the appropriate performance metric and where the present paper closes a long-standing gap. On the limits side, Woodworth and Srebro (2016) provided tight lower bounds for finite-sum optimization, offering the yardstick that this paper uses when claiming its last-iterate rates match or nearly match the best possible. Classical non-asymptotic results for strongly convex problems (Moulines and Bach, 2011) emphasized last-iterate performance in squared distance under with-replacement sampling; the present work moves beyond both the metric and the strong-convexity assumption. Finally, Nesterov’s convex optimization framework (2004) sets the function-value, last-iterate benchmark for projected gradient methods that this paper extends to shuffled, incremental passes.

---
*Generated: 2026-01-06T23:09:26.457507*

# Prior Work Analysis Report

## Target Paper

**Title:** Improved Active Learning via Dependent Leverage Score Sampling

**Conference:** ICLR 2024 (oral)

**Authors:** Atsushi Shimizu, Xiaoou Cheng, Christopher Musco, Jonathan Weare

**Keywords:** leverage score sampling, active learning, polynomial regression, differential equations, pivotal sampling

**Abstract:** 
> We show how to obtain improved active learning methods in the agnostic (adversarial noise) setting by combining marginal leverage score sampling with non-independent sampling strategies that promote spatial coverage. In particular, we propose an easily implemented method based on the \emph{pivotal sampling algorithm}, which we test on problems motivated by learning-based methods for parametric PDEs and uncertainty quantification. In comparison to independent sampling, our method reduces the numb...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Fast Approximate Least Squares via Leverage Score Sampling** (2011)
- *Authors:* Petros Drineas, Michael W. Mahoney, and S. Muthukrishnan
- *Direct Connection:* This foundational result formalized leverage-score marginals as the canonical i.i.d. importance distribution for least-squares regression, providing the baseline distribution that the new method retains while introducing dependence for coverage.

**Optimal Weighted Least Squares Approximation of Functions from Random Samples** (2017)
- *Authors:* Albert Cohen and Giovanni Migliorati
- *Direct Connection:* They showed that i.i.d. Christoffel/leverage-based sampling achieves O(d log d) sample complexity for polynomial regression, a guarantee the new theory preserves under dependent leverage sampling via a one-sided l_infty independence condition.

**Matrix Chernoff Bounds for Strongly Rayleigh Distributions** (2016)
- *Authors:* Nima Anari, Shayan Oveis Gharan, and Amin Rezaei
- *Direct Connection:* Their matrix concentration results under strong negative dependence provided the template for extending Chernoff-type bounds beyond independence, which the new work generalizes to a weaker one-sided l_infty independence condition encompassing pivotal sampling.

### 💡 Inspiration

**Unequal Probability Sampling Without Replacement Through a Splitting Method** (1998)
- *Authors:* Jean-Claude Deville and Yves Tillé
- *Direct Connection:* This paper introduces the pivotal sampling algorithm, which the current work adopts and adapts to use leverage-score marginals, and it underpins the analysis by showing the dependent selection structure that the authors prove satisfies their one-sided l_infty independence condition.

**Spatially Balanced Sampling Through the Pivotal Method** (2012)
- *Authors:* Anders Grafström, Niklas Lundström, and Stefan Schelin
- *Direct Connection:* This work establishes that pivotal sampling promotes spatial coverage, directly motivating the paper’s key idea of combining leverage-score marginals with a dependent scheme to counter the poor spatial coverage of i.i.d. sampling.

### 🔗 Related Problem

**Subsampling for Ridge Regression via Regularized Volume Sampling** (2017)
- *Authors:* Michał Dereziński and Manfred K. Warmuth
- *Direct Connection:* This paper demonstrates that diversity-promoting dependent sampling (volume sampling/DPP variants) can outperform i.i.d. leverage sampling in regression, directly inspiring the search for a more practical dependent scheme that still respects leverage marginals.

---

## Synthesis: How Prior Work Led to This Paper

Pivotal sampling, introduced by Deville and Tillé, provides a dependent, without-replacement design that exactly realizes prescribed inclusion probabilities. Subsequent work by Grafström, Lundström, and Schelin showed that this algorithm naturally yields spatially balanced samples, demonstrating its ability to improve coverage in problems where the sample locations matter. In randomized numerical linear algebra, Drineas, Mahoney, and Muthukrishnan established leverage-score marginals as the canonical importance distribution for least-squares regression, yielding strong guarantees under i.i.d. sampling. In the context of polynomial approximation and parametric PDE surrogates, Cohen and Migliorati proved that i.i.d. sampling proportional to the Christoffel function (equivalently, leverage scores) achieves O(d log d) sample complexity for weighted least squares, crystallizing the modern baseline for active regression design. Meanwhile, Dereziński and Warmuth showed that diversity-promoting dependent schemes such as (regularized) volume sampling and DPPs can outperform i.i.d. leverage sampling in regression, albeit with higher implementation complexity. Complementing these algorithmic advances, Anari, Oveis Gharan, and Rezaei established matrix Chernoff-type bounds under strong negative dependence (Strongly Rayleigh), demonstrating that useful spectral concentration can survive beyond independence.
Together these works revealed a gap: i.i.d. leverage-score sampling is statistically near-optimal but can lack spatial coverage, while existing dependent diversity methods are harder to deploy and lack guarantees tied to leverage marginals. The present paper synthesizes these strands by using pivotal sampling—practical and coverage-promoting—to realize leverage-score marginals, and by extending matrix concentration theory from strongly Rayleigh to a one-sided l_infty independence condition. This preserves O(d log d) active learning guarantees while yielding substantial empirical gains from improved spatial coverage.

---

*Analysis generated on: 2026-01-06T09:54:37.206989*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

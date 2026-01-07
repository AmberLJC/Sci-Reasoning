# Prior Work Analysis Report

## Target Paper

**Title:** A General Framework for User-Guided Bayesian Optimization

**Conference:** ICLR 2024 (spotlight)

**Authors:** Carl Hvarfner, Frank Hutter, Luigi Nardi

**Keywords:** Bayesian Optimization, Hyperparameter Optimization, Gaussian Processes

**Abstract:** 
> The optimization of expensive-to-evaluate black-box functions is prevalent in various scientific disciplines. Bayesian optimization is an automatic, general and sample-efficient method to solve these problems with minimal knowledge of the the underlying function dynamics. However, the ability of Bayesian optimization to incorporate prior knowledge or beliefs about the function at hand in order to accelerate the optimization is limited, which reduces its appeal for knowledgeable practitioners wit...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Entropy Search for Information-Efficient Global Optimization** (2012)
- *Authors:* Philipp Hennig and Christian J. Schuler
- *Direct Connection:* Entropy Search formalized Bayesian optimization in terms of a posterior over the optimizer x* and mutual information about x*, which ColaBO leverages to inject user-specified priors directly over the optimizer’s location.

**The Application of Bayesian Methods for Seeking the Extremum** (1978)
- *Authors:* Jonas Mockus
- *Direct Connection:* Mockus introduced improvement-based criteria tied to beliefs about target/aspiration values, an early notion that underlies ColaBO’s Bayesian handling of user priors on the optimal value.

### 🔍 Gap Identification

**Practical Bayesian Optimization of Machine Learning Algorithms** (2012)
- *Authors:* Jasper Snoek et al.
- *Direct Connection:* Snoek et al. popularized practical GP-based BO where prior knowledge is primarily encoded via kernels and hyperpriors, a limitation ColaBO addresses by enabling priors directly about the optimizer location and optimal value.

**Multi-task Bayesian Optimization** (2013)
- *Authors:* Kevin Swersky et al.
- *Direct Connection:* Multi-task BO encodes prior knowledge through task kernels to transfer across related problems, underscoring that prevailing approaches restrict beliefs to kernel structure rather than explicit priors on x* or f*, which ColaBO remedies.

### 🔧 Extension

**Predictive Entropy Search for Efficient Global Optimization of Black-box Functions** (2014)
- *Authors:* José Miguel Hernández-Lobato et al.
- *Direct Connection:* Predictive Entropy Search provided a tractable, Monte Carlo-based mutual information objective over x* that ColaBO directly extends by replacing the implicit uniform prior on x* with user-specified beliefs in a Bayesian-principled way.

**Max-value Entropy Search for Efficient Bayesian Optimization** (2017)
- *Authors:* Zi Wang and Stefanie Jegelka
- *Direct Connection:* Max-value Entropy Search introduced an information-theoretic acquisition over the optimal value f*, which ColaBO generalizes to allow explicit user priors on f* and to propagate those beliefs across Monte Carlo acquisition functions.

---

## Synthesis: How Prior Work Led to This Paper

Entropy Search established a Bayesian view of global optimization centered on the posterior over the optimizer x* and maximizing information gain about that quantity, providing a principled handle for reasoning directly about where the minimizer lies. Predictive Entropy Search made this idea practical by introducing a Monte Carlo formulation of mutual information over x*, enabling flexible approximations that can, in principle, accommodate non-uniform beliefs over the optimizer. Complementing these, Max-value Entropy Search reframed the information objective in terms of the distribution of the optimum value f*, showing how targeting information about f* can guide sampling and paving the way for explicit modeling of beliefs over optimal values. In parallel, practical GP-based BO popularized by Snoek et al. primarily encoded prior knowledge through kernel choices and hyperpriors, while Multi-task BO transferred knowledge via task kernels—both exemplifying a prevailing restriction of priors to kernel structure. Earlier still, Mockus’s improvement-based formulations tied decisions to aspirational target values, foreshadowing the utility of explicit beliefs about the optimal value. Taken together, these works revealed two complementary information-theoretic targets—x* and f*—and a practical Monte Carlo pathway for optimizing them, yet left explicit user beliefs about these targets largely unexploited. The current paper synthesizes these threads by providing a general Bayesian framework that injects user-specified priors over x* and f* into modern Monte Carlo acquisition functions, overcoming the kernel-only bottleneck and delivering a principled route to user-guided, belief-aware Bayesian optimization.

---

*Analysis generated on: 2026-01-06T15:02:26.038459*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

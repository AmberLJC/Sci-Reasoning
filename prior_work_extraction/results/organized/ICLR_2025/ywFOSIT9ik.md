# Prior Work Analysis Report

## Target Paper

**Title:** Revisiting Zeroth-Order Optimization:  Minimum-Variance Two-Point Estimators and  Directionally Aligned Perturbations

**Conference:** ICLR 2025 (spotlight)

**Authors:** Shaocong Ma, Heng Huang

**Keywords:** zeroth-order optimization, SGD, convergence analysis

**Abstract:** 
> In this paper, we explore the two-point zeroth-order gradient estimator and identify the distribution of random perturbations that minimizes the estimator's asymptotic variance as the perturbation stepsize tends to zero. We formulate it as a constrained functional optimization problem over the space of perturbation distributions. Our findings reveal that such desired perturbations can align directionally with the true gradient, instead of maintaining a fixed length. While existing research has l...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Random gradient-free minimization of convex functions** (2017)
- *Authors:* Yurii Nesterov and Vladimir Spokoiny
- *Direct Connection:* Their Gaussian-smoothing two-point estimator and convergence analysis provide a canonical distributional choice and analytical template that we generalize by optimizing over perturbation distributions and proving variance and convergence benefits for directionally aligned perturbations.

**Online convex optimization in the bandit setting** (2005)
- *Authors:* Abraham D. Flaxman, Adam Tauman Kalai, and H. Brendan McMahan
- *Direct Connection:* This work introduced the smoothing-based random-direction gradient estimation paradigm underpinning zeroth-order methods, providing the fundamental formulation that our two-point, minimum-variance distributional design builds upon.

### 💡 Inspiration

**Multivariate stochastic approximation using a simultaneous perturbation gradient approximation** (1992)
- *Authors:* James C. Spall
- *Direct Connection:* SPSA’s two-point gradient approximation and its explicit focus on choosing a perturbation distribution (e.g., Bernoulli ±1) motivated our functional optimization over distributions and led to our result that gradient-aligned perturbations minimize asymptotic variance.

### 📊 Baseline

**An optimal algorithm for bandit and zero-order stochastic optimization with two-point feedback** (2017)
- *Authors:* Ohad Shamir
- *Direct Connection:* This work formalized the two-point random-direction estimator and achieved optimal rates with fixed-length, isotropic perturbations, which our paper directly improves by identifying the perturbation distribution that minimizes asymptotic variance and need not be fixed-length.

### 🔧 Extension

**Stochastic first- and zeroth-order methods for nonconvex stochastic programming** (2013)
- *Authors:* Saeed Ghadimi and Guanghui Lan
- *Direct Connection:* We extend their zeroth-order SGD complexity framework by establishing convergence guarantees for δ-unbiased random perturbations, which include our directionally aligned scheme and broaden the estimator class beyond those analyzed in this paper.

### 🔗 Related Problem

**Guided evolutionary strategies: Augmenting random search with surrogate gradients** (2019)
- *Authors:* Niru Maheswaranathan et al.
- *Direct Connection:* Their demonstration that aligning a search distribution with (surrogate) gradient information reduces estimator variance directly motivates our theoretically grounded result that the minimum-variance two-point perturbations align with the true gradient.

---

## Synthesis: How Prior Work Led to This Paper

Two-point zeroth-order gradient estimators were crystallized in work showing optimal rates with random directions, typically sampled isotropically on a fixed-length sphere, which established the standard estimator structure and variance behavior used in practice. Gaussian-smoothing formulations furnished an alternative distributional choice for two-point estimators and delivered clean convergence analyses, setting a baseline for how perturbation distributions affect bias/variance trade-offs in gradient-free methods. Earlier, the smoothing-based random-direction paradigm in bandit optimization introduced the foundational idea of replacing gradients by randomized directional probes of the function, anchoring the problem formulation and estimator families. Parallel to these, the SPSA literature emphasized that the perturbation distribution is a design lever—commonly using Bernoulli ±1—and studied its impact on estimator quality, implicitly raising the question of whether other distributions could systematically reduce variance. In nonconvex settings, zeroth-order SGD analyses established complexity bounds for two-point estimators under specific smoothing distributions, providing the template we can extend to broader estimator classes. Complementing these, guided evolutionary strategies empirically showed that aligning search distributions with gradient information can substantially cut estimator variance.
Taken together, these works exposed both a fixed-length bias in prior design choices and a gap: no principled characterization of the variance-minimizing perturbation distribution within the two-point framework. The current paper synthesizes these insights by posing a functional optimization over perturbation distributions, proving that the asymptotic-variance minimizer aligns with the true gradient, and by formalizing directionally aligned perturbations along with convergence guarantees under a generalized δ-unbiased framework that subsumes classical Gaussian/spherical choices.

---

*Analysis generated on: 2026-01-06T08:16:38.590617*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

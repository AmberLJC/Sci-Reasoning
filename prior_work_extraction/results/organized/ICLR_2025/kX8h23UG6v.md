# Prior Work Analysis Report

## Target Paper

**Title:** Standard Gaussian Process is All You Need for High-Dimensional Bayesian Optimization

**Conference:** ICLR 2025 (oral)

**Authors:** Zhitong Xu, Haitao Wang, Jeff M. Phillips, Shandian Zhe

**Keywords:** Gaussian Process, Bayesian Optimization, High Dimensional Bayesian Optimization

**Abstract:** 
> A long-standing belief holds that Bayesian Optimization (BO) with standard Gaussian processes (GP) --- referred to as standard BO --- underperforms in high-dimensional optimization problems. While this belief seems plausible, it lacks both robust empirical evidence and theoretical justification. To address this gap, we present a systematic investigation. First, through a comprehensive evaluation across twelve benchmarks, we found that while the popular Square Exponential (SE) kernel often leads ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Gaussian Process Optimization in the Bandit Setting: No Regret Algorithms** (2010)
- *Authors:* Srinivas et al.
- *Direct Connection:* This work provides the GP-UCB framework and kernel-dependent information gain analysis that the paper builds on to reason about how SE versus Matérn kernels interact with dimensionality in BO.

### 💡 Inspiration

**Practical Bayesian Optimization of Machine Learning Algorithms** (2012)
- *Authors:* Snoek et al.
- *Direct Connection:* Its empirical advocacy of Matérn 5/2 kernels, ARD, and careful length-scale priors directly motivates re-examining 'standard BO' kernel choices and analyzing how length-scale initialization affects training stability.

### 🔍 Gap Identification

**Bayesian Optimization in High Dimensions via Random Embeddings (REMBO)** (2013)
- *Authors:* Wang et al.
- *Direct Connection:* By asserting that naive GP BO fails in high dimensions and proposing random embeddings, this paper cemented the prevailing belief that the present work challenges and surpasses using standard GPs with appropriate kernels.

**High Dimensional Bayesian Optimization and Bandits via Additive Models** (2015)
- *Authors:* Kandasamy et al.
- *Direct Connection:* This method’s reliance on additive kernel structure to circumvent dimensionality embodies the structural assumptions the current paper shows are unnecessary when standard BO uses Matérn kernels and proper hyperparameter handling.

### 📊 Baseline

**TuRBO: Trust-Region Bayesian Optimization** (2019)
- *Authors:* Eriksson et al.
- *Direct Connection:* As a leading high-dimensional BO approach that replaces a global GP with local trust-region models to avoid surrogate pathologies, TuRBO serves as a primary comparator that the paper systematically reevaluates against standard GPs.

**Scalable Bayesian Optimization in High Dimensions via Sparse Axis-Aligned Subspace Priors (SAASBO)** (2021)
- *Authors:* Eriksson et al.
- *Direct Connection:* By imposing sparsity-inducing priors over ARD length-scales to discover low-dimensional subspaces, SAASBO represents the dominant specialized alternative that the paper shows can be matched or exceeded by standard Matérn GPs without sparsity priors.

---

## Synthesis: How Prior Work Led to This Paper

Kernel-dependent learning behavior in Gaussian process bandits was formalized by Srinivas et al., who tied regret to information gain, making explicit how kernel smoothness and hyperparameters interact with dimensionality. Snoek et al. demonstrated in practice that Matérn 5/2 kernels with ARD and informed priors on length-scales often outperform squared exponential choices, and emphasized marginal-likelihood training and initialization details that make GP BO robust. REMBO crystallized the notion that naive GP BO fails in high dimensions and proposed random low-dimensional embeddings as a remedy, catalyzing a wave of embedding-based methods. Kandasamy et al. argued that additivity assumptions are key to overcoming dimensionality, constructing GP-UCB on additive kernels with regret scaling in group sizes rather than ambient dimension. Eriksson et al.’s TuRBO sidestepped global surrogate issues by using local trust regions with GPs, establishing a powerful high-dimensional baseline. SAASBO introduced sparsity-inducing priors on ARD length-scales to automatically select a small active subspace, becoming a standard for high-dimensional problems.
Together, these works fostered a consensus that specialized structure or locality is required for high-dimensional BO, yet they also hinted—through kernel choice, hyperparameter priors, and theory—that the kernel and its training are pivotal. This paper synthesizes those cues by revisiting plain GP BO, showing empirically that Matérn kernels suffice in high dimensions and theoretically that common SE length-scale initializations induce vanishing gradients, clarifying why SE underperforms and why Matérn avoids the failure mode.

---

*Analysis generated on: 2026-01-06T09:31:26.070381*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

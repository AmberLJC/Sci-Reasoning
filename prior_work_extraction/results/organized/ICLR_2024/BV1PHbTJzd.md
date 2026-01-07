# Prior Work Analysis Report

## Target Paper

**Title:** Accelerating Distributed Stochastic Optimization via Self-Repellent Random Walks

**Conference:** ICLR 2024 (oral)

**Authors:** Jie Hu, Vishwaraj Doshi, Do Young Eun

**Keywords:** Distributed Learning, Self-Repellent Random Walk, Token Algorithm, Central Limit Theorem, Asymptotic Analysis

**Abstract:** 
> We study a family of distributed stochastic optimization algorithms where gradients are sampled by a token traversing a network of agents in random-walk fashion. Typically, these random-walks are chosen to be Markov chains that asymptotically sample from a desired target distribution, and play a critical role in the convergence of the optimization iterates. In this paper, we take a novel approach by replacing the standard *linear* Markovian token by one which follows a *non-linear* Markov chain ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**WALKMAN: A Random Walk Algorithm for Decentralized Optimization** (2020)
- *Authors:* Shi et al.
- *Direct Connection:* WALKMAN crystallized the token/random-walk paradigm for decentralized optimization with a linear Markovian walker, providing the exact algorithmic template that this paper retains while replacing the underlying walk with a self-repellent, non-linear alternative.

**Stochastic Approximation and Recursive Algorithms and Applications** (2003)
- *Authors:* Harold J. Kushner et al.
- *Direct Connection:* The SA/CLT framework in this book provides the asymptotic normality and covariance characterization for iterates with Markovian noise that the current paper leverages to quantify variance reduction under SRRW-driven token sampling.

**Central Limit Theorems for Stochastic Approximation with Controlled Markov Chain Dynamics** (2015)
- *Authors:* Gersende Fort et al.
- *Direct Connection:* Provides CLTs and asymptotic covariance formulae for stochastic approximation driven by controlled/inhomogeneous Markov chains, which underpins the paper’s asymptotic analysis for optimization iterates under the generalized SRRW token.

### 🔍 Gap Identification

**Stochastic Gradient Descent with Markovian Sampling** (2018)
- *Authors:* Chen et al.
- *Direct Connection:* By showing that Markovian dependence induces mixing-time–limited convergence and larger asymptotic variance in SGD, this paper exposes the variance bottleneck that the self-repellent token explicitly targets and overcomes.

### 🔧 Extension

**Self-Repellent Random Walks for Sampling on Graphs** (2023)
- *Authors:* Vishwaraj Doshi et al.
- *Direct Connection:* This work introduced SRRW and proved an O(1/alpha) reduction of asymptotic variance for graph-based MCMC, which the current paper generalizes and repurposes as the non-linear token dynamics to reduce gradient-sampling variance in distributed optimization.

### 🔗 Related Problem

**Lifting Markov Chains to Speed Mixing** (1999)
- *Authors:* Fan R. K. Chung et al.
- *Direct Connection:* This work established that breaking reversibility via lifted/nonreversible dynamics can reduce mixing time and variance, motivating the use of non-linear, nonreversible walk dynamics like SRRW to accelerate sampling on graphs.

---

## Synthesis: How Prior Work Led to This Paper

Self-Repellent Random Walks for Sampling on Graphs established a non-linear Markov chain on graphs whose transition probabilities are repelled by the empirical visitation profile and proved that its additive-functionals enjoy an O(1/alpha) reduction in asymptotic variance; this explicit variance control is directly relevant to any algorithm whose efficiency hinges on averaging along a trajectory. WALKMAN formalized decentralized optimization with a single traveling token that triggers local updates along a linear (memoryless) Markov walk, making the optimization accuracy and speed depend on the token’s sampling variance and mixing properties. Stochastic Gradient Descent with Markovian Sampling quantified how Markovian dependence inflates bias/variance and ties rates to mixing time, pinpointing a core limitation of linear random-walk–driven sampling. Foundational stochastic-approximation results by Kushner and Yin, and the CLTs for controlled Markovian dynamics by Fort et al., provide asymptotic normality and explicit covariance characterizations of iterates driven by Markovian noise, enabling principled variance comparisons across different token dynamics. Finally, Lifting Markov Chains to Speed Mixing demonstrated that nonreversibility can materially reduce mixing time and variance in graph walks, seeding the idea that modified dynamics can accelerate averaging-based procedures.
Taken together, these works suggest a clear opportunity: inject a self-repellent, nonreversible walker into the token framework to directly shrink the variance of gradient sampling. By grafting SRRW onto the token protocol and analyzing the resulting stochastic approximation via CLTs for Markovian noise, the current paper shows that the O(1/alpha) variance reduction from SRRW carries over to optimization iterates, addressing the mixing- and variance-limited performance of prior random-walk token methods while preserving their lightweight communication advantages.

---

*Analysis generated on: 2026-01-06T18:50:17.979585*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

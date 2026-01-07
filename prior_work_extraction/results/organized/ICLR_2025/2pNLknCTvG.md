# Prior Work Analysis Report

## Target Paper

**Title:** uniINF: Best-of-Both-Worlds Algorithm for Parameter-Free Heavy-Tailed MABs

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yu Chen, Jiatai Huang, Yan Dai, Longbo Huang

**Keywords:** Heavy Tailed, Multi-Armed Bandits, Parameter-Free, Best-of-Both-Worlds

**Abstract:** 
> In this paper, we present a novel algorithm, `uniINF`, for the Heavy-Tailed Multi-Armed Bandits (HTMAB) problem, demonstrating robustness and adaptability in both stochastic and adversarial environments. Unlike the stochastic MAB setting where loss distributions are stationary with time, our study extends to the adversarial setup, where losses are generated from heavy-tailed distributions that depend on both arms and time. Our novel algorithm `uniINF` enjoys the so-called Best-of-Both-Worlds (Bo...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Bandits with heavy tail** (2013)
- *Authors:* Sébastien Bubeck et al.
- *Direct Connection:* uniINF targets the same heavy-tailed MAB formulation and lower-bound regime introduced by Bubeck–Cesa-Bianchi–Lugosi, but removes their key requirement of knowing the moment/tail parameters (σ, α) and extends beyond the stochastic setting.

### 💡 Inspiration

**Minimax Policies for Adversarial and Stochastic Bandits** (2009)
- *Authors:* Olivier Audibert et al.
- *Direct Connection:* uniINF builds on the Implicitly Normalized Forecaster (INF) machinery—implicit normalization and mirror-descent style updates—and adapts it with robust/heavy-tail-aware estimators to handle unbounded losses while preserving adversarial optimality.

**Efficient learning by implicit exploration in bandit problems** (2014)
- *Authors:* Tamás Kocák et al.
- *Direct Connection:* uniINF robustifies the implicit-exploration loss-estimation idea to control variance under heavy tails via adaptive truncation/bias control, enabling parameter-free, high-probability stability in adversarial regimes.

### 🔍 Gap Identification

**The Best of Both Worlds: Stochastic and Adversarial Bandits** (2012)
- *Authors:* Sébastien Bubeck et al.
- *Direct Connection:* uniINF directly addresses the gap left by this BoBW line—its reliance on bounded losses—by designing a single algorithm that achieves BoBW guarantees when losses are heavy-tailed and the tail parameters are unknown.

### 📊 Baseline

**Corralling a Band of Bandit Algorithms** (2017)
- *Authors:* Alekh Agarwal et al.
- *Direct Connection:* uniINF improves over CORRAL-style meta-combination by providing a single, unified learner that attains BoBW guarantees in heavy-tailed settings without relying on specialized base algorithms or tuning of (σ, α).

### 🔧 Extension

**Tsallis-INF: An Optimal Algorithm for Stochastic and Adversarial Bandits** (2019)
- *Authors:* Julius Zimmert et al.
- *Direct Connection:* uniINF adopts the Tsallis-INF/INF-style FTRL with Tsallis regularization as its backbone and modifies the loss-estimation and analysis to remain BoBW under heavy-tailed (unbounded) losses without prior tail knowledge.

---

## Synthesis: How Prior Work Led to This Paper

Heavy-tailed stochastic bandits were formalized by Bubeck, Cesa-Bianchi, and Lugosi, who introduced robust estimators such as truncation/median-of-means and derived regret and lower bounds that depend explicitly on the unknown moment/tail parameters (σ, α). Their results established both the statistical difficulty of heavy tails and the prevailing reliance on a priori tail knowledge for optimal tuning. In parallel, the Implicitly Normalized Forecaster (INF) of Audibert and Bubeck provided an adversarially optimal mirror-descent framework whose implicit normalization underpins many best-of-both-worlds (BoBW) advances. Zimmert and Seldin’s Tsallis-INF refined this paradigm: using Tsallis-regularized FTRL and carefully designed importance-weighted estimators to achieve near-optimal stochastic and adversarial regret—but under bounded losses. Kocák and collaborators’ implicit exploration further showed how to stabilize bandit estimators by injecting bias implicitly rather than via explicit exploration parameters, yielding tighter, high-probability control of estimation variance. The broader BoBW agenda, initiated by Bubeck and Slivkins, clarified the goal of a single algorithm that adapts across regimes, while Agarwal et al.’s CORRAL pursued this via meta-combination of specialized learners, at the cost of extra overhead and tuning sensitivity. Taken together, these works revealed a clear opportunity: combine INF/Tsallis-regularized updates with an implicitly exploratory, robust loss estimator that neutralizes heavy-tail variance without knowing (σ, α). uniINF executes this synthesis, designing a parameter-free, heavy-tail-aware estimator within the INF/Tsallis framework to match stochastic and adversarial lower bounds, thereby achieving a true BoBW guarantee in heavy-tailed environments.

---

*Analysis generated on: 2026-01-06T12:13:22.204122*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper
**Title:** UBRFn7YKMe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution is a distributional training data attribution (d-TDA) framework that explicitly models how randomness in initialization and minibatching induces a distribution over model outputs, together with a theoretical result that classical influence functions (IFs) arise as the limit of unrolled differentiation—without restrictive convexity assumptions. Koh and Liang (2017) laid the foundation by introducing IFs for attributing predictions to training points, but their derivation relied on smooth convex settings. Building on the idea of differentiating through optimization, Maclaurin et al. (2015) established unrolled differentiation through full training trajectories, while Ren et al. (2018) demonstrated per-example reweighting via one-step unrolling. Pruthi et al. (2020) operationalized a trajectory-based view of influence (TracIn), accumulating gradient interactions across training, a perspective that this paper unifies by showing such unrolled views converge to IFs in the appropriate limit.

The distributional focus is motivated and supported by two complementary strands. First, Mandt et al. (2017) interpret SGD as sampling from an approximate posterior, justifying the paper’s central object: the distribution over trained models and their outputs. Second, Ilyas et al. (2022) empirically map datasets to predictions across many randomized trainings (datamodels), revealing the practical salience of attribution over training-run variability that d-TDA formalizes. Finally, data valuation work such as Data Shapley (Ghorbani & Zou, 2019) frames contribution as an expectation over algorithmic randomness; d-TDA provides a scalable, gradient-based alternative that links these expectations to IFs via the dynamics of learning, enabling improved pruning and diagnostic applications in modern deep models.

---
*Generated: 2026-01-07T00:27:38.137190*

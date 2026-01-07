# Prior Work Analysis Report

## Target Paper

**Title:** Probabilistic Neural Pruning via Sparsity Evolutionary Fokker-Planck-Kolmogorov Equation

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zhanfeng Mo, Haosen Shi, Sinno Jialin Pan

**Keywords:** Optimization for Deep Network, Probabilistic Method, Machine learning, Model compression

**Abstract:** 
> Neural pruning aims to compress and accelerate deep neural networks by identifying the optimal subnetwork within a specified sparsity budget. In this work, we study how to gradually sparsify the unpruned dense model to the target sparsity level with minimal performance drop. Specifically, we analyze the evolution of the population of optimal subnetworks under continuous sparsity increments from a thermodynamic perspective. We first reformulate neural pruning as an expected loss minimization prob...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks** (2019)
- *Authors:* Jonathan Frankle et al.
- *Direct Connection:* By framing pruning as the search for an optimal subnetwork at a given sparsity and popularizing iterative sparsification, this work establishes the problem setting that motivates modeling the evolution of the population of optimal subnetworks.

### 💡 Inspiration

**Variational Dropout Sparsifies Deep Neural Networks** (2017)
- *Authors:* Dmitry Molchanov et al.
- *Direct Connection:* By treating sparsification as learning parameters of a probabilistic distribution over weights and minimizing expected loss with a sparsity-inducing prior, this paper inspired the probabilistic, distribution-over-masks view that underpins the SFPK formulation.

**Stochastic Gradient Descent as Approximate Bayesian Inference** (2017)
- *Authors:* Stephan Mandt et al.
- *Direct Connection:* This paper’s diffusion view of SGD and its associated Fokker–Planck description of parameter-distribution dynamics directly motivate the thermodynamic/FPK machinery adapted here to derive an evolution equation for mask distributions under sparsity constraints.

### 🔍 Gap Identification

**SNIP: Single-Shot Network Pruning based on Connection Sensitivity** (2019)
- *Authors:* Namhoon Lee et al.
- *Direct Connection:* SNIP’s first-order, infinitesimal-loss-change criterion for one-shot pruning highlights the limitation of local, static saliency measures, which this paper addresses by prescribing a continuous-time, distributional evolution that minimizes expected loss under tiny sparsity increments.

### 📊 Baseline

**To prune, or not to prune: exploring the efficacy of pruning for model compression** (2017)
- *Authors:* Zhu and Gupta
- *Direct Connection:* Their gradual magnitude pruning schedule established the de facto baseline of incrementally increasing sparsity to mitigate accuracy drop, which the present work replaces with a mathematically derived FPK evolution to guide each infinitesimal sparsity increment.

**Movement Pruning: Adaptive Sparsity by Fine-Tuning** (2020)
- *Authors:* Victor Sanh et al.
- *Direct Connection:* By learning mask scores during gradual sparsification to reduce accuracy loss, this method serves as a primary baseline that the proposed FPK-guided probabilistic pruning aims to improve upon with a principled evolution of mask distributions.

### 🔧 Extension

**Learning Sparse Neural Networks through L0 Regularization** (2018)
- *Authors:* Christos Louizos et al.
- *Direct Connection:* This work formulates pruning as optimizing the expected loss under stochastic binary gates with an explicit sparsity control, which the current paper directly extends by deriving an FPK-guided infinitesimal update rule for the gate (mask) distribution as sparsity increases.

---

## Synthesis: How Prior Work Led to This Paper

L0 regularization introduced stochastic binary gates and optimized the expected loss with an explicit sparsity control, establishing a principled way to view pruning through distributions over masks rather than fixed, deterministic selections. Variational Dropout further cemented the probabilistic perspective by learning distributions over weights that induce sparsity via variational objectives, demonstrating that compression can be cast as distributional optimization. SNIP provided a sensitivity-based, first-order approximation to the expected loss change under infinitesimal parameter removal, formalizing the notion of infinitesimal pruning decisions but in a one-shot, static setting. Gradual magnitude pruning showed that increasing sparsity smoothly during training substantially reduces accuracy degradation compared to abrupt pruning, though it relies on heuristic schedules. The Lottery Ticket Hypothesis sharpened the goal to locating optimal subnetworks at prescribed sparsity and popularized iterative sparsification as a path to such subnetworks. Finally, the diffusion view of optimization from Mandt et al. connected learning dynamics to Fokker–Planck equations, offering thermodynamic tools to reason about probability flows in parameter space, while movement pruning demonstrated practical, score-based gradual sparsification as a strong baseline.
Together, these works exposed a gap: heuristics and local saliency guide either static or schedule-based pruning, but none specify how the optimal mask distribution should evolve under an infinitesimal increase in sparsity to minimize expected loss. By uniting the probabilistic gating formulations with the Fokker–Planck thermodynamic lens, the current paper naturally proposes an evolution equation for the mask distribution and realizes it via particle simulation, yielding principled, closed-form guidance for each sparsity increment.

---

*Analysis generated on: 2026-01-06T17:58:27.159874*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

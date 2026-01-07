# Prior Work Analysis Report

## Target Paper

**Title:** Implicit bias of SGD in $L_2$-regularized linear DNNs: One-way jumps from high to low rank

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zihan Wang, Arthur Jacot

**Keywords:** implicit bias, SGD, low-rank, linear networks

**Abstract:** 
> The $L_{2}$-regularized loss of Deep Linear Networks (DLNs) with
more than one hidden layers has multiple local minima, corresponding
to matrices with different ranks. In tasks such as matrix completion,
the goal is to converge to the local minimum with the smallest rank
that still fits the training data. While rank-underestimating minima
can be avoided since they do not fit the data, GD might get
stuck at rank-overestimating minima. We show that with SGD, there is always a probability to jump
f...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Exact solutions to the nonlinear dynamics of learning in deep linear neural networks** (2014)
- *Authors:* Andrew M. Saxe et al.
- *Direct Connection:* Their singular-value–mode decomposition of deep linear learning dynamics under squared loss gives the analytic scaffold for reasoning about how ranks emerge or vanish, which underlies the paper’s characterization of rank-stratified minima and mode-wise transitions.

**Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization** (2010)
- *Authors:* Benjamin Recht et al.
- *Direct Connection:* Establishing nuclear norm as a convex surrogate for rank connects Frobenius-regularized factorizations to low-rank solutions, grounding the interpretation of different local minima as competing rank choices in the regularized deep linear objective.

**Global Optimality in Tensor Factorization, Deep Learning, and Beyond** (2015)
- *Authors:* Benjamin D. Haeffele et al.
- *Direct Connection:* They show that separable factor regularization in deep factorizations induces an (atomic) low-rank–promoting penalty on the product map, providing the formal link between L2 penalties and rank strata that the absorbing sets B_r build on.

### 💡 Inspiration

**Implicit Bias of Gradient Descent on Linear Convolutional Networks** (2018)
- *Authors:* Suriya Gunasekar et al.
- *Direct Connection:* This work established that gradient dynamics in linear networks select solutions according to the parameterization-induced norm, highlighting the need to understand, in the L2-regularized case, how stochasticity (SGD) selects among multiple rank-differentiated minima.

### 🔍 Gap Identification

**Deep Learning Without Poor Local Minima** (2016)
- *Authors:* Kenji Kawaguchi
- *Direct Connection:* By proving that unregularized deep linear networks have no suboptimal local minima, this work isolates explicit regularization as the source of nontrivial rank-separated minima, directly motivating the paper’s focus on the L2-regularized setting.

### 🔗 Related Problem

**Stochastic Gradient Descent as Approximate Bayesian Inference** (2017)
- *Authors:* Stephan Mandt et al.
- *Direct Connection:* Their SDE approximation of small–step-size SGD provides the stochastic dynamical framework for analyzing transition probabilities between attraction basins, enabling the one-way (irreversible) rank-jump argument in the regularized linear setting.

**High-Dimensional Dynamics of Generalization Error in Neural Networks** (2017)
- *Authors:* Madhur Advani et al.
- *Direct Connection:* By showing that deep linear learning proceeds via SVD-mode dynamics and that weight decay shrinks lower-variance modes first, this work supplies mode-wise intuition for progressive low-rank emergence that is formalized here as absorbing rank sets under SGD.

---

## Synthesis: How Prior Work Led to This Paper

The study of deep linear networks (DLNs) has precise mode-wise dynamics: Saxe, McClelland, and Ganguli derived exact singular-value decomposed learning trajectories under squared loss, revealing how individual modes grow or shrink with depth and initialization. Kawaguchi established that, absent explicit regularization, DLNs have no suboptimal local minima, implying that any nontrivial local structure must be induced by penalties such as weight decay. Parallel developments in low-rank modeling connected factor regularization to rank: Recht, Fazel, and Parrilo formalized the nuclear norm as a convex proxy for rank, while Haeffele and Vidal showed that separable factor regularization in deep factorizations induces atomic, low-rank–promoting penalties on the product map. Implicit-bias work by Gunasekar and collaborators demonstrated that gradient dynamics in linear networks select solutions according to parameterization-defined norms, making clear that the geometry of the regularizer and parameterization dictates which solutions are preferred. On the stochastic side, Mandt, Hoffman, and Blei modeled small–step-size SGD as an SDE, enabling analysis of basin-hopping probabilities, and Advani and colleagues described how weight decay and dynamics shrink or suppress certain SVD modes, providing intuition for progressive low-rank structure. Together, these results expose an opportunity: L2-regularized DLNs possess rank-stratified minima grounded in atomic/nuclear-norm geometry, GD’s implicit bias alone cannot explain selection among them, and SGD’s stochastic dynamics near these structured basins remain under-theorized. The present work synthesizes mode-wise DLN dynamics with the induced low-rank penalty and an SDE perspective on SGD to show a directional, probabilistic selection mechanism: stochastic updates can trigger rank-decreasing transitions with positive probability, while rank-increasing moves are absorbing-barred, yielding one-way jumps to lower-rank minima.

---

*Analysis generated on: 2026-01-06T14:33:15.228095*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

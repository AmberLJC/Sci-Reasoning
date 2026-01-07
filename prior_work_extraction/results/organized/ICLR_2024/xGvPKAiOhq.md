# Prior Work Analysis Report

## Target Paper

**Title:** How Over-Parameterization Slows Down Gradient Descent in Matrix Sensing: The Curses of Symmetry and Initialization

**Conference:** ICLR 2024 (spotlight)

**Authors:** Nuoya Xiong, Lijun Ding, Simon Shaolei Du

**Keywords:** non-convex optimization, random initialization, global convergence, matrix recovery, matrix sensing

**Abstract:** 
> This paper rigorously shows how over-parameterization dramatically changes the convergence behaviors of gradient descent (GD) for the matrix sensing problem, where the goal is to recover an unknown low-rank ground-truth matrix from near-isotropic linear measurements.
First, we consider the symmetric setting with the symmetric parameterization where $M^* \in \mathbb{R}^{n \times n}$ is a positive semi-definite unknown matrix of rank $r \ll n$, and one uses a symmetric parameterization $XX^\top$ t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Global Optimality of Local Search for Low Rank Matrix Recovery** (2016)
- *Authors:* Bhojanapalli et al.
- *Direct Connection:* This work established that the nonconvex factorized formulation of matrix sensing has a benign landscape (no spurious local minima under near-isotropic/RIP measurements), which the current paper leverages to focus purely on the dynamics of GD and show that over-parameterization alone can slow convergence.

**Guaranteed minimum-rank solutions of linear matrix equations via nuclear norm minimization** (2010)
- *Authors:* Recht et al.
- *Direct Connection:* This paper formalized matrix sensing with near-isotropic linear measurements and RIP-type assumptions, which is precisely the measurement model under which the current paper proves its GD convergence lower bounds.

**A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization** (2003)
- *Authors:* Burer et al.
- *Direct Connection:* Introducing the symmetric XXᵀ factorization and its orthogonal invariance, this work underpins the rotational symmetry that the current paper identifies as a principal cause of slowed GD dynamics in the over-parameterized PSD setting.

### 💡 Inspiration

**Implicit Regularization in Matrix Factorization** (2018)
- *Authors:* Gunasekar et al.
- *Direct Connection:* Their analysis that gradient descent rapidly enforces balanced factors and respects rotational symmetries in UV/XXᵀ parameterizations directly motivates the paper’s "curse of symmetry/initialization" mechanism used to construct slow GD trajectories in over-parameterized settings.

### 📊 Baseline

**Low-rank solutions of linear matrix equations via Procrustes Flow** (2016)
- *Authors:* Tu et al.
- *Direct Connection:* Procrustes Flow established linear (exponential) convergence rates for gradient-based methods under exact parameterization with suitable initialization, providing the sharp baseline the current paper contrasts against when proving polynomial 1/T^2 rates for over-parameterized, randomly initialized GD.

### 🔗 Related Problem

**Exact solutions to the nonlinear dynamics of learning in deep linear neural networks** (2013)
- *Authors:* Saxe et al.
- *Direct Connection:* By characterizing mode-wise alignment and polynomial-time transients caused by symmetry in deep linear models, this paper provides the dynamical template the current work adapts to two-factor linear models to rigorously derive 1/T^2 lower bounds under over-parameterization.

---

## Synthesis: How Prior Work Led to This Paper

Low-rank matrix sensing was crystallized as recovering a low-rank matrix from near-isotropic linear measurements, with Recht et al. showing that such operators satisfy conditions enabling recovery via convex surrogates. Burer and Monteiro advocated factorizing PSD matrices as XXᵀ, revealing orthogonal invariances that create flat directions in the parameter space. Within this nonconvex factorized formulation, Bhojanapalli et al. proved the landscape is benign under RIP-like assumptions—local minima are global—shifting the central question from geometry to optimization dynamics. Tu et al.’s Procrustes Flow then demonstrated that, with exact parameterization and a good initialization, gradient-based methods achieve linear (exponential) convergence, highlighting the potential for very fast recovery in well-posed regimes. Orthogonal symmetries and balancing, however, strongly shape dynamics: Gunasekar et al. showed gradient methods in factorized linear models implicitly enforce balanced factors and respect rotational invariance, constraining how signal directions can grow. In deep linear networks, Saxe et al. derived exact dynamics where symmetry-induced alignment causes slow, polynomial transients, offering a dynamical mechanism tied to invariant subspaces. Together, these works implied a striking open point: despite a benign landscape and fast rates under exact parameterization, over-parameterization plus random initialization could fundamentally alter GD trajectories. The current paper synthesizes these insights by leveraging measurement isotropy, rotational invariance from XXᵀ/UVᵀ parameterizations, and balancedness to construct trajectories where signal alignment is bottlenecked, proving 1/T^2 lower bounds and contrasting them with exponential rates in the exact-parameterization case, thus pinpointing the curses of symmetry and initialization.

---

*Analysis generated on: 2026-01-06T16:09:50.097302*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

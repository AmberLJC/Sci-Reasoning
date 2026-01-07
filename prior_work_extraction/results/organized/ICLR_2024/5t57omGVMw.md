# Prior Work Analysis Report

## Target Paper

**Title:** Learning to Relax: Setting Solver Parameters Across a Sequence of Linear System Instances

**Conference:** ICLR 2024 (spotlight)

**Authors:** Mikhail Khodak, Edmond Chow, Maria Florina Balcan, Ameet Talwalkar

**Keywords:** scientific computing, data-driven algorithm design, online learning, multi-armed bandits, contextual bandits, numerical analysis, learning-augmented algorithms, algorithms with predictions

**Abstract:** 
> Solving a linear system ${\bf Ax}={\bf b}$ is a fundamental scientific computing primitive for which numerous solvers and preconditioners have been developed. 
	These come with parameters whose optimal values depend on the system being solved and are often impossible or too expensive to identify;
	thus in practice sub-optimal heuristics are used.
	We consider the common setting in which many related linear systems need to be solved, e.g. during a single numerical simulation.
	In this scenario, c...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Iterative methods for solving partial difference equations of elliptic type** (1950)
- *Authors:* D. M. Young
- *Direct Connection:* Young introduced SOR and characterized how its convergence rate depends on the relaxation parameter ω, establishing the parameter space and performance metric that the learning procedure targets.

**Data-Driven Algorithm Design** (2017)
- *Authors:* M.-F. Balcan et al.
- *Direct Connection:* Balcan et al. formalized selecting algorithm parameters from performance feedback over an instance distribution, providing the learning-theoretic framework that is instantiated for SOR parameter tuning across system sequences.

### 🔍 Gap Identification

**Matrix Iterative Analysis** (1962)
- *Authors:* R. S. Varga
- *Direct Connection:* Varga’s analysis shows that the optimal SOR parameter requires spectral information (e.g., eigenvalue bounds) that is expensive to obtain, directly motivating a no-extra-computation approach that learns ω from runtime feedback.

**Successive Overrelaxation (SOR) and related methods** (2000)
- *Authors:* A. Hadjidimos
- *Direct Connection:* This survey documents heuristic and adaptive SOR parameter rules that rely on problem-specific structure or extra matrix work, highlighting the lack of principled, black-box methods for choosing ω across varying instances.

**Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization** (2018)
- *Authors:* L. Li et al.
- *Direct Connection:* Hyperband demonstrates bandit-based parameter selection but requires multiple evaluations per task, a limitation explicitly avoided here by learning ω from a single solver run per instance without extra matrix work.

### 🔧 Extension

**The nonstochastic multiarmed bandit problem** (2002)
- *Authors:* P. Auer et al.
- *Direct Connection:* EXP3-style adversarial bandit algorithms with bandit feedback underpin the no-regret procedure that selects ω using only iteration counts and competes with the best fixed choice in hindsight.

**X-Armed Bandits** (2011)
- *Authors:* S. Bubeck et al.
- *Direct Connection:* Techniques for optimizing over continuous arm spaces motivate discretizing ω ∈ (0,2) and controlling approximation error so bandit selection can compete with the best continuous parameter.

---

## Synthesis: How Prior Work Led to This Paper

Successive over-relaxation (SOR) was introduced with an explicit dependence of convergence on the relaxation parameter ω, establishing a one-dimensional control knob whose choice can dramatically affect iteration counts (Young, 1950). Classical matrix iterative analysis made this dependence precise, tying the optimal ω to spectral properties of the iteration matrix and showing that computing or even estimating those quantities typically requires costly eigenvalue information (Varga, 1962). Surveys of SOR and its relatives catalog numerous heuristic or adaptive rules for ω that exploit problem-specific structure or extra computations, but they lack a general black-box procedure with guarantees across varying instances (Hadjidimos, 2000). In parallel, learning theory proposed selecting algorithm parameters by observing performance over instances drawn from a distribution, giving formal guarantees for data-driven algorithm design without requiring gradient information (Balcan et al., 2017). Adversarial bandit methods such as EXP3 provide no-regret selection from discrete choices using only bandit feedback, exactly the signal available when one observes iteration counts (Auer et al., 2002), while continuum-armed bandit work shows how to handle continuous parameter spaces via controlled discretization (Bubeck et al., 2011). Bandit-based hyperparameter optimization like Hyperband further underscored the viability of bandits for parameter tuning, but at the cost of multiple evaluations per task (Li et al., 2018). Taken together, these strands reveal both a ripe target—the ω-sensitive performance of SOR whose optimal choice is expensive to compute—and a toolkit: online bandits that learn from single-outcome feedback and discretization schemes to approximate continuous parameters. The natural next step is to cast ω-selection across repeated linear systems as a no-regret bandit problem, leveraging only iteration counts, discretizing ω to compete with the continuous optimum, and thereby closing the gap left by spectral-estimate-dependent or multi-evaluation heuristics.

---

*Analysis generated on: 2026-01-06T06:24:56.559971*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

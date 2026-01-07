# Prior Work Analysis Report

## Target Paper

**Title:** Computationally Efficient RL under Linear Bellman Completeness for Deterministic Dynamics

**Conference:** ICLR 2025 (oral)

**Authors:** Runzhe Wu, Ayush Sekhari, Akshay Krishnamurthy, Wen Sun

**Keywords:** reinforcement learning theory, linear function approximation

**Abstract:** 
> We study computationally and statistically efficient Reinforcement Learning algorithms for the *linear Bellman Complete* setting. This setting uses linear function approximation to capture value functions and unifies existing models like linear Markov Decision Processes (MDP) and Linear Quadratic Regulators (LQR).  While it is known from the prior works that this setting is statistically tractable, it remained open whether a computationally efficient algorithm exists. Our work provides a computa...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Contextual Decision Processes with Low Bellman Rank are PAC-Learnable** (2017)
- *Authors:* Nan Jiang et al.
- *Direct Connection:* This work formalized Bellman-structured function classes (via Bellman rank/closure), providing the theoretical footing for the linear Bellman-complete assumption that our algorithm explicitly targets.

**On the Sample Complexity of the Linear Quadratic Regulator** (2018)
- *Authors:* Stephen Tu et al.
- *Direct Connection:* Sample-efficient LQR results clarify that value functions in linear-quadratic control admit structured approximations closed under Bellman updates, justifying LQR as a canonical instance encompassed by the linear Bellman-complete framework we target.

### 💡 Inspiration

**Randomized Least-Squares Value Iteration: Efficient Reinforcement Learning with Directed Exploration** (2014)
- *Authors:* Ian Osband et al.
- *Direct Connection:* We adopt the core idea of inducing optimism by injecting noise into least-squares value regressions, but design the perturbations to act only in the empirical null space so as to guarantee optimism without corrupting well-estimated directions.

### 📊 Baseline

**Provably Efficient Reinforcement Learning with Linear Function Approximation** (2020)
- *Authors:* Chi Jin et al.
- *Direct Connection:* The least-squares value-iteration and optimism machinery of LSVI-UCB for linear MDPs is the direct computational template our method modifies—replacing explicit bonuses with structured randomized perturbations and extending beyond linear MDPs to the linear Bellman-complete class under deterministic dynamics.

### 🔗 Related Problem

**Provably Efficient Reinforcement Learning in Linear Mixture MDPs** (2021)
- *Authors:* Ayush Sekhari et al.
- *Direct Connection:* Linear mixture/linear MDP results established computationally efficient least-squares–based optimistic planning with large action spaces, which our method mirrors while relaxing the model to the broader linear Bellman-complete setting (under deterministic dynamics).

**A Policy Cover Based Approach to Reinforcement Learning in Rich Observations (PCID)** (2020)
- *Authors:* Wen Sun et al.
- *Direct Connection:* PCID showed that assuming deterministic dynamics can convert otherwise intractable rich-observation RL into a computationally tractable problem, motivating our deterministic-dynamics restriction to achieve oracle-free efficiency under linear Bellman completeness.

---

## Synthesis: How Prior Work Led to This Paper

Least-squares value iteration with optimism in linear MDPs provided a concrete and computationally efficient design for value-function-based exploration: regress Q-values on features, then add structured optimism to guide planning. Randomized least-squares value iteration proposed replacing explicit bonuses with Gaussian perturbations in the regression, a device that creates optimistic value estimates through stochasticity rather than deterministic confidence bounds. Independently, the theory of contextual decision processes introduced Bellman-structured function classes and showed that when function classes are closed under Bellman updates, learning can be statistically tractable—laying the conceptual foundation for linear Bellman completeness. In parallel, work on linear mixture/linear MDPs showed that least-squares–driven optimistic planning scales to large action spaces with polynomial computation, while policy-cover methods demonstrated that assuming deterministic dynamics can shift rich-observation RL from information-theoretically tractable but computationally daunting to practically algorithmic. Finally, sample-efficient LQR studies established that quadratic value functions under linear dynamics form a closed class under Bellman backups, situating LQR squarely within Bellman-complete frameworks.
Taken together, these strands suggested a path: exploit Bellman completeness to cover models beyond linear MDPs (including LQR), retain the computationally simple least-squares VI backbone that scales to large action spaces, and induce optimism via randomized perturbations. The remaining opportunity was to make randomization principled: by confining noise to the empirical null space, one can drive exploration only where uncertainty remains, preserving accuracy in well-estimated directions. Combining deterministic dynamics (to avoid intractable planning/oracle steps) with null-space randomized regression yields a computationally efficient algorithm in the linear Bellman-complete setting, resolving the key gap between statistical and algorithmic tractability.

---

*Analysis generated on: 2026-01-06T08:14:39.249588*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

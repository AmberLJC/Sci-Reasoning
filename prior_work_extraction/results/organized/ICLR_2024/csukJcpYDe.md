# Prior Work Analysis Report

## Target Paper

**Title:** Generalized Policy Iteration using Tensor Approximation for Hybrid Control

**Conference:** ICLR 2024 (spotlight)

**Authors:** Suhan Shetty, Teng Xue, Sylvain Calinon

**Keywords:** Optimal Control, Hybrid Actions, Robotics, Approximate Dynamic Programming, Tensor Approximation

**Abstract:** 
> Control of dynamic systems involving hybrid actions is a challenging task in robotics.  To address this, we present a novel algorithm called Generalized Policy Iteration using Tensor Train (TTPI) that belongs to the class of Approximate Dynamic Programming (ADP). We use a low-rank tensor approximation technique called Tensor Train (TT) to approximate the state-value and advantage function which enables us to efficiently handle hybrid systems. We demonstrate the superiority of our approach over p...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Neuro-Dynamic Programming** (1996)
- *Authors:* Dimitri P. Bertsekas and John N. Tsitsiklis
- *Direct Connection:* TTPI instantiates generalized policy iteration from neuro-dynamic programming but replaces generic function approximators with tensor-train representations to conduct policy evaluation and improvement over hybrid action spaces.

**Reinforcement Learning with Parameterized Actions** (2016)
- *Authors:* S. N. Masson, P. Ranchod, and G. Konidaris
- *Direct Connection:* TTPI adopts the parameterized-action MDP formulation from this work and targets its coupled discrete–continuous Bellman updates using TT-based value and advantage approximations.

**Tensor-Train Decomposition** (2011)
- *Authors:* Ivan V. Oseledets
- *Direct Connection:* TTPI relies on the TT factorization introduced here to compactly represent the state-value and advantage functions and to enable efficient Bellman backups in high-dimensional hybrid domains.

### 💡 Inspiration

**Function Train: A Continuous Analogue of the Tensor-Train Decomposition** (2015)
- *Authors:* Alex A. Gorodetsky and Youssef M. Marzouk
- *Direct Connection:* By demonstrating that low-rank separated representations can support efficient approximation and updates of high-dimensional functions, this work directly inspired TTPI’s use of TT-structured value/advantage approximation within policy iteration.

### 📊 Baseline

**Deep Reinforcement Learning in Parameterized Action Space** (2016)
- *Authors:* Timothy P. Hausknecht and Peter Stone
- *Direct Connection:* This deep RL architecture for PAMDPs serves as a primary baseline that TTPI improves upon by substituting neural Q/actor heads with structured low-rank TT value/advantage representations to better scale with hybrid action complexity.

### 🔧 Extension

**Quasioptimal TT-cross approximation for multidimensional arrays** (2011)
- *Authors:* Dmitry V. Savostyanov
- *Direct Connection:* TTPI leverages TT-cross/interpolation ideas from this work to fit TT-structured value and advantage functions from sampled rollouts during policy evaluation and improvement.

---

## Synthesis: How Prior Work Led to This Paper

Generalized policy iteration from neuro-dynamic programming established the template of alternating policy evaluation and improvement with approximate value functions, providing the procedural backbone for many ADP methods. The parameterized-action MDP formulation formalized how discrete action choices couple to continuous parameters, defining the hybrid action setting and Bellman structure that modern methods must address. Deep reinforcement learning in parameterized action spaces operationalized this formulation with neural architectures, revealing practical challenges when representing coupled discrete–continuous decisions, including instability and poor scaling as dimensionality grows. Tensor-Train decomposition introduced a scalable, low-rank factorization for high-dimensional functions, making it possible to store and manipulate value-like objects with costs that grow only linearly in dimension under low rank. TT-cross approximation supplied a sampling-based mechanism to learn TT representations from pointwise evaluations, enabling black-box function fitting without full grids. Function Trains, as a continuous analogue of TT, showed that separated low-rank formats can support efficient approximation and updates of complex high-dimensional functions, foreshadowing their utility for value and advantage approximation in control.
Together, these works reveal a gap: policy iteration for hybrid action problems needs a representation that captures discrete–continuous coupling while scaling gracefully in dimension and supporting Bellman-style updates. By marrying the PAMDP formulation and GPI loop with TT/TT-cross low-rank approximations inspired by FT/TT theory, the current work naturally emerges—performing value and advantage approximation and policy improvement in a structured format that directly addresses the instability and scalability limitations of prior neural hybrid-action baselines.

---

*Analysis generated on: 2026-01-06T06:00:52.007302*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

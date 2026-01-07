# Prior Work Analysis Report

## Target Paper

**Title:** Addressing Signal Delay in Deep Reinforcement Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Wei Wang, Dongqi Han, Xufang Luo, Dongsheng Li

**Keywords:** Deep Reinforcement Learning, Signal Delay, Robotic Control, Continuous Control

**Abstract:** 
> Despite the notable advancements in deep reinforcement learning (DRL) in recent years, a prevalent issue that is often overlooked is the impact of signal delay. Signal delay occurs when there is a lag between an agent's perception of the environment and its corresponding actions. In this paper, we first formalize delayed-observation Markov decision processes (DOMDP) by extending the standard MDP framework to incorporate signal delays. Next, we elucidate the challenges posed by the presence of si...

---

## Key Prior Works (6 papers with direct influence)

### 💡 Inspiration

**Making Deep Q-learning Methods Robust to Time Discretization** (2018)
- *Authors:* Cédric Tallec et al.
- *Direct Connection:* This work’s insight that reaction time and time discretization should be modeled explicitly informs the paper’s decision to incorporate delay into the decision process (DOMDP) and to align learning targets across delay.

**Closer control of loops with dead time (Smith Predictor)** (1957)
- *Authors:* O. J. M. Smith
- *Direct Connection:* The classical idea of predicting the current plant state from delayed measurements via a forward model inspires the paper’s strategy to reconstruct undelayed states for policy/critic updates in delayed-observation settings.

### 🔍 Gap Identification

**Deep Recurrent Q-Learning for Partially Observable MDPs** (2015)
- *Authors:* Matthew Hausknecht et al.
- *Direct Connection:* DRQN is used as the canonical recurrent baseline for partial observability, and its poor performance under fixed observation delays directly motivates the need for a delay-specific formulation and training strategy.

**DreamerV2: Mastering Atari with Discrete World Models** (2020)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* Dreamer-style latent world models provide a strong generic approach to POMDPs, but the paper shows that without delay-aware alignment these methods degrade under large, fixed observation delays, revealing a gap their method addresses.

### 📊 Baseline

**Addressing Function Approximation Error in Actor-Critic Methods (TD3)** (2018)
- *Authors:* Scott Fujimoto et al.
- *Direct Connection:* TD3 serves as a primary continuous-control baseline that the paper evaluates and improves upon by introducing delay-aware alignment that TD3 lacks.

### 🔧 Extension

**Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor** (2018)
- *Authors:* Tuomas Haarnoja et al.
- *Direct Connection:* The proposed delay-aware algorithms are implemented as modifications of SAC, re-indexing transitions and adjusting targets to align actions and values across the observation delay.

---

## Synthesis: How Prior Work Led to This Paper

Recurrent value-based agents such as DRQN aggregate histories to cope with partial observability, but they do not explicitly account for fixed observation lags and thus struggle when the agent must act on stale sensory inputs. Dreamer-style latent world models learn predictive belief states and achieve strong results in generic POMDPs, yet their training targets and rollouts assume timely observations and are not aligned to fixed delays, leading to degraded control when the signal is systematically late. Complementing these, work on time discretization shows that reaction latency should be treated as part of the state, suggesting that temporal misalignment, rather than lack of memory, is the core issue. Classical control offers a direct remedy: the Smith predictor compensates for dead time by rolling a dynamics model forward to estimate the current state from delayed measurements. Meanwhile, SAC and TD3 provide robust off-policy actor-critic frameworks for continuous control onto which algorithmic modifications can be cleanly grafted.
Taken together, these works expose a clear opportunity: generic POMDP solutions and strong actor-critics lack mechanisms to align learning signals and decisions with fixed observation delays, while control theory offers a principled compensation template. Building on this, the paper formalizes delayed-observation MDPs to pin down the misalignment, and then extends SAC-style training with delay-aware transition indexing and predictive state reconstruction, achieving non-delayed-level performance even under large lags.

---

*Analysis generated on: 2026-01-06T15:56:03.204396*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

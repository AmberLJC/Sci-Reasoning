# Prior Work Analysis Report

## Target Paper

**Title:** AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jake Grigsby, Linxi Fan, Yuke Zhu

**Keywords:** Meta-RL, Generalization, Long-Term Memory, Transformers

**Abstract:** 
> We introduce AMAGO, an in-context Reinforcement Learning (RL) agent that uses sequence models to tackle the challenges of generalization, long-term memory, and meta-learning. Recent works have shown that off-policy learning can make in-context RL with recurrent policies viable. Nonetheless, these approaches require extensive tuning and limit scalability by creating key bottlenecks in agents' memory capacity, planning horizon, and model size. AMAGO revisits and redesigns the off-policy in-context...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**RL^2: Fast Reinforcement Learning via Slow Reinforcement Learning** (2016)
- *Authors:* Yan Duan et al.
- *Direct Connection:* RL^2 introduced the in-context RL formulation—training a recurrent policy to implement a learning algorithm from experience—providing the foundational problem setup that AMAGO adopts with a sequence model instead of an RNN.

### 💡 Inspiration

**Stabilizing Transformers for Reinforcement Learning (GTrXL)** (2020)
- *Authors:* Emilio Parisotto et al.
- *Direct Connection:* GTrXL demonstrated that Transformer variants with gating can provide stable long-horizon credit assignment in RL, directly motivating AMAGO’s use of large transformer sequence models for long-term memory.

### 📊 Baseline

**PEARL: Efficient Off-Policy Meta-Reinforcement Learning** (2019)
- *Authors:* Kurtland Chua Rakelly et al.
- *Direct Connection:* PEARL is a primary off-policy meta-RL baseline whose amortized latent-context inference and scalability limitations on long horizons are explicitly targeted by AMAGO’s in-context sequence-model approach.

### 🔧 Extension

**Recurrent Experience Replay in Distributed Reinforcement Learning (R2D2)** (2019)
- *Authors:* Szymon Kapturowski et al.
- *Direct Connection:* R2D2 established how to train recurrent policies off-policy via sequence replay, burn-in, and unrolling—mechanisms that AMAGO generalizes to long-sequence Transformers and full-rollout parallel training.

**Hindsight Experience Replay** (2017)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* HER introduced multi-goal hindsight relabeling for sparse-reward, goal-conditioned RL, which AMAGO integrates with off-policy in-context learning to tackle exploration-heavy, sparse-reward tasks.

### 🔗 Related Problem

**Decision Transformer: Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Lili Chen et al.
- *Direct Connection:* Decision Transformer showed that modeling full trajectories with causal Transformers is effective for decision making, inspiring AMAGO’s design to process entire rollouts with a transformer while switching to an end-to-end RL training objective.

---

## Synthesis: How Prior Work Led to This Paper

In-context reinforcement learning was crystallized by RL^2, which framed a recurrent policy as an implicit learner that adapts online from interaction histories, establishing the core meta-RL objective of learning to learn from trajectories. R2D2 then showed that recurrent agents can be trained off-policy by replaying sequence chunks with burn-in and unrolling, making sequence-based adaptation practical at scale with experience replay. GTrXL demonstrated that Transformer-style sequence models—with gating and architectural tweaks—stabilize long-horizon credit assignment in RL, highlighting the value of long-term memory capacity beyond standard RNNs. Decision Transformer revealed the power of modeling entire trajectories with causal Transformers for control, validating full-rollout sequence modeling as an effective representation for decision making, even if trained with supervised return conditioning. PEARL advanced off-policy meta-RL with probabilistic context encoders but exposed limitations in amortized latent inference and scalability when tasks require long-horizon memory. Hindsight Experience Replay provided a principled multi-goal relabeling strategy to learn from sparse rewards in goal-conditioned settings.
Together these insights exposed a clear opportunity: combine off-policy sequence training (R2D2) with high-capacity, stable long-horizon transformers (GTrXL) and full-rollout modeling (Decision Transformer) to realize RL^2-style in-context adaptation without explicit latent inference (addressing PEARL’s bottlenecks), while leveraging HER to extend in-context learning to sparse, multi-goal exploration. The natural next step is a scalable, end-to-end RL agent that trains long-sequence transformers over entire rollouts in parallel via off-policy learning, unifying adaptation, memory, and goal conditioning in one framework.

---

*Analysis generated on: 2026-01-06T06:41:55.822007*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

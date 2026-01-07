# Prior Work Analysis Report

## Target Paper

**Title:** Learning to Search from Demonstration Sequences

**Conference:** ICLR 2025 (oral)

**Authors:** Dixant Mittal, Liwei Kang, Wee Sun Lee

**Keywords:** planning, reasoning, learning to search, reinforcement learning, large language model

**Abstract:** 
> Search and planning are essential for solving many real-world problems. However, in numerous learning scenarios, only action-observation sequences, such as demonstrations or instruction sequences, are available for learning. Relying solely on supervised learning with these sequences can lead to sub-optimal performance due to the vast, unseen search space encountered during training. In this paper, we introduce Differentiable Tree Search Network (D-TSN), a novel neural network architecture that l...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Value Iteration Networks** (2016)
- *Authors:* Aviv Tamar et al.
- *Direct Connection:* VIN established that core planning computations can be embedded as differentiable modules trained end-to-end, a principle D-TSN adopts by making best-first tree construction amenable to gradient-based learning.

### 💡 Inspiration

**Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero)** (2020)
- *Authors:* Julian Schrittwieser et al.
- *Direct Connection:* MuZero’s joint learning of an encoder, dynamics model, and value to guide tree search directly inspires D-TSN’s joint training of these submodules while additionally learning the tree expansion policy from trajectories.

### 🔍 Gap Identification

**A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger)** (2011)
- *Authors:* Stéphane Ross et al.
- *Direct Connection:* DAgger identified compounding errors and distribution shift when learning solely from demonstration sequences, a limitation D-TSN addresses by learning an explicit search procedure that explores and evaluates unseen states.

### 📊 Baseline

**Decision Transformer: Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Lili Chen et al.
- *Direct Connection:* Decision Transformer frames offline trajectories as supervised sequence modeling without explicit planning, serving as a primary baseline that D-TSN improves upon by learning a differentiable best-first search tree from the same kind of data.

### 🔧 Extension

**TreeQN and ATreeC: Differentiable Tree-Structured Models for Deep Reinforcement Learning** (2018)
- *Authors:* Gregory Farquhar et al.
- *Direct Connection:* TreeQN introduced latent dynamics, value back-ups, and differentiable lookahead trees, whose encoder–world model–value factorization D-TSN retains while extending to learning which nodes to expand in a best-first manner.

**Learning to Search with MCTSnets** (2019)
- *Authors:* Avraham Guez et al.
- *Direct Connection:* MCTSnets demonstrated end-to-end differentiable tree search by relaxing MCTS operations, which D-TSN generalizes by optimizing a stochastic best-first expansion policy from demonstrations rather than relying on soft relaxations.

---

## Synthesis: How Prior Work Led to This Paper

Value Iteration Networks showed that planning operators can be embedded as differentiable layers and trained by backpropagation, establishing that gradient-based learning can directly shape planning computations. TreeQN extended this idea to tree-structured lookahead with a learned encoder, latent dynamics, and differentiable value backups, making it possible to learn model-based planning components jointly. MCTSnets further parameterized the tree search process itself, relaxing MCTS operations so that gradients could pass through the construction and backup of the search tree. MuZero unified encoder, dynamics, and value learning to guide tree search effectively, demonstrating that learned world models and values can steer powerful best-first expansions when coupled with a search policy. DAgger revealed that naïvely imitating action sequences incurs compounding errors due to distribution shift, highlighting the need for mechanisms that deliberately explore beyond demonstrated states. Decision Transformer epitomized the supervised sequence-modeling approach to offline trajectories, yet omitted an explicit search mechanism to handle vast, unseen state spaces that arise at deployment.

Together these works suggested that end-to-end training of planning modules is feasible, that learned dynamics and values can guide search, but that purely supervised sequence imitation fails to address exploration over unseen parts of the search tree. The natural next step was to make the act of tree construction itself a learnable, optimizable component: leveraging differentiable backups and joint model–value learning while treating node expansion as a stochastic decision process. By optimizing a best-first expansion policy from demonstrations, the resulting approach marries the strengths of differentiable planning and model-based search with robustness to distribution shift inherent in learning how to search.

---

*Analysis generated on: 2026-01-06T06:20:38.187701*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Pre-Training Goal-based Models for Sample-Efficient Reinforcement Learning

**Conference:** ICLR 2024 (oral)

**Authors:** Haoqi Yuan, Zhancun Mu, Feiyang Xie, Zongqing Lu

**Keywords:** reinforcement learning, pre-training, goal-conditioned RL, open-world environments

**Abstract:** 
> Pre-training on task-agnostic large datasets is a promising approach for enhancing the sample efficiency of reinforcement learning (RL) in solving complex tasks. We present PTGM, a novel method that pre-trains goal-based models to augment RL by providing temporal abstractions and behavior regularization. PTGM involves pre-training a low-level, goal-conditioned policy and training a high-level policy to generate goals for subsequent RL tasks. To address the challenges posed by the high-dimensiona...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Universal Value Function Approximators** (2015)
- *Authors:* Tom Schaul et al.
- *Direct Connection:* UVFA introduced the formalism of goal-conditioned value/policy functions that PTGM adopts for its low-level goal-conditioned policy and high-level goal selection.

**Hindsight Experience Replay** (2017)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* HER’s goal relabeling enables learning goal-conditioned behaviors from task-agnostic datasets, a mechanism PTGM leverages to pre-train the low-level goal-conditioned policy.

### 💡 Inspiration

**Hindsight Goal Generation for Reinforcement Learning** (2019)
- *Authors:* Zhenghao Ren et al.
- *Direct Connection:* HGG’s idea of learning a goal generator to propose effective goals informs PTGM’s high-level goal policy, which is further stabilized by a learned goal prior and discretized action space.

**Behavior Regularized Offline Reinforcement Learning (BRAC)** (2019)
- *Authors:* Yifan Wu et al.
- *Direct Connection:* BRAC’s KL regularization to a learned behavior prior directly motivates PTGM’s pre-trained goal prior used to regularize the high-level policy, improving sample efficiency and stability.

### 📊 Baseline

**Data-Efficient Hierarchical Reinforcement Learning (HIRO)** (2018)
- *Authors:* Ofir Nachum et al.
- *Direct Connection:* HIRO established the subgoal-setting hierarchical structure that PTGM builds upon while directly addressing HIRO’s instability in continuous, high-dimensional goal spaces by discretizing goals via clustering and adding a goal prior.

### 🔧 Extension

**Learning to Reach Goals via Iterated Supervised Learning (GCSL)** (2021)
- *Authors:* Dibya Ghosh et al.
- *Direct Connection:* GCSL’s supervised pretraining of goal-conditioned policies from offline, relabeled data is directly extended in PTGM to pre-train the low-level goal-based policy on large task-agnostic datasets.

---

## Synthesis: How Prior Work Led to This Paper

Universal Value Function Approximators established that policies and value functions can be conditioned on explicit goals, making it natural to train components that map to and act over goal representations. Hindsight Experience Replay showed that relabeling outcomes as goals unlocks learning from sparse rewards and task-agnostic interaction data, providing a practical mechanism to train goal-conditioned policies from broad datasets. Data-Efficient Hierarchical RL (HIRO) demonstrated a powerful structure in which a high-level controller sets subgoals for a low-level goal-conditioned policy, while exposing difficulties in handling continuous, high-dimensional goal spaces and non-stationarity. Goal-Conditioned Supervised Learning (GCSL) further showed that goal-reaching policies can be pre-trained via supervised learning on relabeled offline data, enabling efficient bootstrapping of goal-conditioned skills. Hindsight Goal Generation proposed learning goal generators that propose useful goals to accelerate learning, highlighting the promise of learned goal proposal mechanisms. Behavior Regularized Offline RL (BRAC) introduced KL regularization to a learned behavior prior, evidencing that priors derived from data can stabilize and improve policy learning.

Together, these works suggested a path: pre-train robust goal-conditioned skills from broad data (HER, GCSL, UVFA), structure control hierarchically with a goal-setting high-level (HIRO, HGG), and stabilize decision-making by constraining policies toward data-driven priors (BRAC). The core opportunity was to overcome the instability of continuous subgoal spaces and the brittleness of unconstrained high-level goal selection by discretizing goals and regularizing them with a learned prior. The resulting synthesis naturally leads to pre-training goal-based models, clustering achieved goals to form a discrete, effective high-level action space, and applying a goal prior to regularize high-level decisions for more sample-efficient and stable reinforcement learning.

---

*Analysis generated on: 2026-01-06T07:23:08.679283*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

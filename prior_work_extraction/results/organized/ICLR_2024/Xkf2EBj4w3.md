# Prior Work Analysis Report

## Target Paper

**Title:** Stabilizing Contrastive RL: Techniques for Robotic Goal Reaching from Offline Data

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chongyi Zheng, Benjamin Eysenbach, Homer Rich Walke, Patrick Yin, Kuan Fang, Ruslan Salakhutdinov, Sergey Levine

**Keywords:** reinforcement learning, self-supervised learning, contrastive learning, goal-conditioned RL, offline RL, robotics

**Abstract:** 
> Robotic systems that rely primarily on self-supervised learning have the potential to decrease the amount of human annotation and engineering effort required to learn control strategies. In the same way that prior robotic systems have leveraged self-supervised techniques from computer vision (CV) and natural language processing (NLP), our work builds on prior work showing that the reinforcement learning (RL) itself can be cast as a self-supervised problem: learning to reach any goal without huma...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Hindsight Experience Replay** (2017)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* HER introduced self-supervised goal relabeling for goal-conditioned RL, providing the core data-generation and supervision paradigm that this paper leverages and adapts for offline contrastive value learning.

**Universal Value Function Approximators** (2015)
- *Authors:* Tom Schaul et al.
- *Direct Connection:* UVFA established the goal-conditioned value function formulation Q(s,a,g) that the contrastive objective estimates, providing the formal backbone for the method refined here.

### 💡 Inspiration

**Unsupervised Control through Non-Parametric Discriminative Rewards (DISCERN)** (2018)
- *Authors:* David Warde-Farley et al.
- *Direct Connection:* DISCERN’s discriminative, contrastive reward for goal reaching directly inspired using classifier-style objectives to drive goal-conditioned control, which this paper extends to multi-step value estimation and stabilizes.

### 📊 Baseline

**Goal-Conditioned Supervised Learning (GCSL)** (2019)
- *Authors:* Dibya Ghosh et al.
- *Direct Connection:* GCSL provides the primary offline goal-reaching baseline—supervised learning on relabeled future states—whose limitations on long-horizon credit assignment this paper addresses with stabilized contrastive RL.

### 🔧 Extension

**C-Learning: Learning to Achieve Goals via Contrastive Reinforcement Learning** (2022)
- *Authors:* Benjamin Eysenbach et al.
- *Direct Connection:* This work adopts the C-Learning contrastive objective for estimating goal-conditioned Q-values and directly stabilizes it with architectural and hyperparameter choices to make it robust for offline robotic deployment.

### 🔗 Related Problem

**Reinforcement Learning with Imagined Goals (RIG)** (2018)
- *Authors:* Ashvin Nair et al.
- *Direct Connection:* RIG demonstrated unsupervised robotic goal-reaching via learned latent goals, highlighting representation and stability challenges that motivate a contrastive value-learning approach made robust in this paper.

---

## Synthesis: How Prior Work Led to This Paper

Universal Value Function Approximators formalized goal conditioning by parameterizing value functions with goals, enabling policies to generalize across targets. Hindsight Experience Replay introduced self-supervised relabeling of achieved states as goals, providing an effective supervision signal for goal-conditioned learning without manual rewards. DISCERN advanced this paradigm by using a discriminative, contrastive objective that trains a classifier to reward matching between observations and goals, demonstrating that contrastive signals can drive unsupervised goal attainment. Reinforcement Learning with Imagined Goals showed on robots that learning latent goal representations and rewards can enable self-supervised goal-reaching, but also exposed brittleness and representation-dependence when scaling to real systems. Goal-Conditioned Supervised Learning simplified training from offline play data via supervised learning on relabeled trajectories, performing well but struggling with long-horizon credit assignment and generalization beyond the behavior distribution. C-Learning unified these ideas by casting goal-reaching as contrastive estimation of a goal-conditioned Q-function, leveraging negatives to learn multi-step values but exhibiting sensitivity to architecture and hyperparameters that limited practical deployment.

Taken together, these works suggested that contrastive supervision is powerful for goal-reaching, that goal-conditioned value functions are the right abstraction for long horizons, and that offline, self-supervised relabeling can supply abundant training data—yet instability and design fragility hindered real-robot use. Building directly on C-Learning’s contrastive Q formulation and the HER/UVFA problem setup, while addressing the representation and stability issues surfaced by DISCERN, RIG, and GCSL, the present paper systematically identifies architectural and hyperparameter choices that stabilize contrastive value learning, enabling practical offline, self-supervised robotic goal-reaching.

---

*Analysis generated on: 2026-01-06T08:28:57.151157*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

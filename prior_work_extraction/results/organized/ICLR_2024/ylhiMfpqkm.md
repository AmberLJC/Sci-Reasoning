# Prior Work Analysis Report

## Target Paper

**Title:** Pre-Training and Fine-Tuning Generative Flow Networks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ling Pan, Moksh Jain, Kanika Madan, Yoshua Bengio

**Keywords:** Generative Flow Network (GFlowNets), Pre-train, Goal-conditioned

**Abstract:** 
> Generative Flow Networks (GFlowNets) are amortized samplers that learn stochastic policies to sequentially generate compositional objects from a given unnormalized reward distribution.
They can generate diverse sets of high-reward objects, which is an important consideration in scientific discovery tasks. However, as they are typically trained from a given extrinsic reward function, it remains an important open challenge about how to leverage the power of pre-training and train GFlowNets in an u...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation** (2021)
- *Authors:* Emmanuel Bengio et al.
- *Direct Connection:* This paper introduced the GFlowNet framework for sampling proportional to unnormalized rewards via flow matching on compositional DAGs, whose machinery is retained while being extended to outcome-conditioned (goal-conditioned) training.

### 💡 Inspiration

**Universal Value Function Approximators** (2015)
- *Authors:* Tom Schaul et al.
- *Direct Connection:* UVFA introduced the key idea of goal-parameterized value/policy functions, directly inspiring the paper’s outcome-conditioned GFlowNet that conditions its policy and flows on desired outcomes for reward-free goal reaching.

**Hindsight Experience Replay** (2017)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* HER’s strategy of relabeling achieved outcomes as goals informs the self-supervised pretraining scheme that uses reached terminal outcomes as conditioning targets to train the goal-conditioned GFlowNet.

### 🔍 Gap Identification

**Biological Sequence Design with GFlowNets** (2023)
- *Authors:* Moksh Jain et al.
- *Direct Connection:* This application-centric work exemplifies that prior GFlowNets rely on task-specific extrinsic reward oracles, highlighting the lack of unsupervised/pretrained GFlowNets that the current paper explicitly addresses.

### 📊 Baseline

**Training GFlowNets with Trajectory Balance** (2023)
- *Authors:* Kanika Madan et al.
- *Direct Connection:* Trajectory Balance provides the primary training objective and scratch-training baseline that the proposed outcome-conditioned pretraining modifies and improves upon by conditioning the flows/policies on target outcomes.

### 🔗 Related Problem

**Learning to Reach Goals via Iterative Supervised Learning (GCSL)** (2019)
- *Authors:* Dibya Ghosh et al.
- *Direct Connection:* GCSL shows that goal-reaching policies can be learned from offline trajectories with supervised objectives absent extrinsic rewards, directly shaping the reward-free, outcome-conditioned training formulation used here.

---

## Synthesis: How Prior Work Led to This Paper

Flow Network based Generative Models established the core mechanism of Generative Flow Networks: learning flows over compositional trajectories so that terminal states are sampled in proportion to unnormalized rewards. Training GFlowNets with Trajectory Balance then provided a stable, single-trajectory objective that equates forward and backward probability products, becoming the default way to train GFlowNets from a known reward. In reinforcement learning, Universal Value Function Approximators introduced conditioning policies and value functions on explicit goals, making goal-parameterization a natural interface for reuse. Hindsight Experience Replay showed how to turn arbitrary rollouts into useful training data by relabeling achieved outcomes as the goals, enabling learning even without dense rewards. Complementing this, Goal-Conditioned Supervised Learning demonstrated that reward-free goal-reaching can be cast as supervised learning from trajectories, achieving effective coverage and adaptability. Application work such as Biological Sequence Design with GFlowNets crystallized a key limitation: prior GFlowNets are typically trained against extrinsic reward oracles, preventing the kind of unsupervised pretraining that has transformed other domains. Taken together, these works suggested a path: retain the GFlowNet and Trajectory Balance machinery but adopt a goal-conditioned parameterization, and build a self-supervised dataset of achieved outcomes—as in HER and GCSL—to pretrain a reward-free, outcome-conditioned sampler. The paper synthesizes these insights into an outcome-conditioned GFlowNet that explores and learns to reach arbitrary outcomes during pretraining, then efficiently fine-tunes on downstream extrinsic rewards, naturally extending the baseline TB-trained GFlowNets to a pretrain–finetune paradigm.

---

*Analysis generated on: 2026-01-06T17:35:07.057171*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

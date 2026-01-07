# Prior Work Analysis Report

## Target Paper

**Title:** H-GAP: Humanoid Control with a Generalist Planner

**Conference:** ICLR 2024 (spotlight)

**Authors:** zhengyao jiang, Yingchen Xu, Nolan Wagener, Yicheng Luo, Michael Janner, Edward Grefenstette, Tim Rocktäschel, Yuandong Tian

**Keywords:** Generative Modelling, Humanoid Control, Model Predictive Control, Model-based Reinforcement Learning, Offline Reinforcement Learning

**Abstract:** 
> Humanoid control is an important research challenge offering avenues for integration into human-centric infrastructures and enabling physics-driven humanoid animations.
The daunting challenges in this field stem from the difficulty of optimizing in high-dimensional action spaces and the instability introduced by the bipedal morphology of humanoids. 
However, the extensive collection of human motion-captured data and the derived datasets of humanoid trajectories, such as MoCapAct, paves the way t...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control** (2023)
- *Authors:* Yicheng Luo et al.
- *Direct Connection:* MoCapAct provided the large-scale, task-diverse humanoid state–action trajectories and benchmark tasks that H-GAP trains on and evaluates with MPC, defining the data and problem setting H-GAP directly builds upon.

**DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills** (2018)
- *Authors:* Xue Bin Peng et al.
- *Direct Connection:* DeepMimic established MoCap-driven physics-based humanoid control via RL, laying the groundwork for using motion data as a prior that H-GAP repurposes through a generalist generative model and planning.

### 💡 Inspiration

**Trajectory Transformer** (2021)
- *Authors:* Michael Janner et al.
- *Direct Connection:* Trajectory Transformer showed that sequence models of state–action trajectories can be used for planning in offline RL, inspiring H-GAP’s generalist trajectory-model-as-planner paradigm for humanoid control.

### 🔍 Gap Identification

**AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control** (2021)
- *Authors:* Xue Bin Peng et al.
- *Direct Connection:* AMP demonstrated the power of motion priors from MoCap for humanoid control but required online RL and task-specific training, a limitation H-GAP addresses by using an offline-trained generative prior with MPC to adapt to new tasks without online interaction.

### 📊 Baseline

**Decision Transformer: Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Lili Chen et al.
- *Direct Connection:* As a primary sequence-modeling baseline for offline control on diverse tasks, Decision Transformer frames generalist control from datasets that H-GAP improves upon by performing model-based MPC with a trajectory prior rather than return-conditioned action prediction.

### 🔧 Extension

**Planning with Diffusion for Control** (2022)
- *Authors:* Michael Janner et al.
- *Direct Connection:* This work established the core idea of using a learned generative trajectory prior for planning, which H-GAP extends to high-DoF humanoids by replacing diffusion with a trajectory autoencoder and embedding it within MPC for task-conditioned control.

**Learning Latent Plans from Play** (2019)
- *Authors:* Corey Lynch et al.
- *Direct Connection:* The latent-plan autoencoding framework for long-horizon behavior directly motivates H-GAP’s trajectory autoencoder and latent-space search, enabling tractable planning for 56-DoF humanoids.

---

## Synthesis: How Prior Work Led to This Paper

MoCapAct assembled human motion capture into standardized humanoid state–action trajectories across many tasks, establishing both the data modality and multi-task evaluation regime for simulated humanoid control. Planning with Diffusion for Control showed that a learned generative model over trajectories can serve as a powerful planner by sampling task-consistent rollouts, demonstrating how data-driven priors can replace explicit dynamics in planning. Trajectory Transformer further validated the notion that sequence models trained on offline trajectories can drive planning by searching in model space rather than optimizing raw actions. Learning Latent Plans from Play introduced autoencoding long-horizon behaviors into compact latent plans that can be sampled or optimized at test time, providing a way to make search tractable over complex behaviors. DeepMimic and AMP established MoCap as an effective motion prior for physics-based humanoids, with AMP in particular using an adversarial motion prior to enforce realism, but both relied on online RL and often per-task training.
Together, these works reveal a gap: motion priors from MoCap enable realism and robustness, and generative trajectory models enable data-driven planning, but high-DoF humanoids demand a tractable search space without online RL. H-GAP synthesizes these insights by training a trajectory autoencoder on MoCapAct to obtain a latent motion prior and performing MPC by optimizing over latent plans, thereby combining the realism of MoCap priors with the flexibility of generative-model planning for generalist humanoid control without online interaction.

---

*Analysis generated on: 2026-01-06T08:44:49.004702*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

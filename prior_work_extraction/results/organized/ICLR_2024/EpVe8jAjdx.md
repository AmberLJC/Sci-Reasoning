# Prior Work Analysis Report

## Target Paper

**Title:** Privileged Sensing Scaffolds Reinforcement Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Edward S. Hu, James Springer, Oleh Rybkin, Dinesh Jayaraman

**Keywords:** reinforcement learning, model-based reinforcement learning, world models, robotics, privileged information, asymmetric learning, multimodality, perception, sensing

**Abstract:** 
> We need to look at our shoelaces as we first learn to tie them but having mastered this skill, can do it from touch alone. We call this phenomenon “sensory scaffolding”: observation streams that are not needed by a master might yet aid a novice learner. We consider such sensory scaffolding setups for training artificial agents. For example, a robot arm may need to be deployed with just a low-cost, robust, general-purpose camera; yet its performance may improve by having privileged training-time-...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning Using Privileged Information: Similarity Control and Knowledge Transfer** (2009)
- *Authors:* Vladimir Vapnik et al.
- *Direct Connection:* LUPI formalized training-time-only side information, which Scaffolder instantiates in RL by treating extra sensors as privileged inputs used to aid auxiliary components while keeping the deployment policy sensor-limited.

### 💡 Inspiration

**Learning by Cheating** (2020)
- *Authors:* Mikhail Philion et al.
- *Direct Connection:* This paper demonstrated that training with privileged signals (e.g., depth/segmentation) can produce camera-only policies, motivating Scaffolder’s use of privileged sensing as a training scaffold for a deployable low-sensor policy in RL.

**End-to-End Training of Deep Visuomotor Policies** (2016)
- *Authors:* Sergey Levine et al.
- *Direct Connection:* By using full-state privileged information to supervise a vision policy that is deployed without it, this work provided a concrete precedent for train-time privileged sensing that Scaffolder adapts to modern actor-critic and world-model RL.

### 📊 Baseline

**Asymmetric Actor-Critic for Image-Based Robot Learning** (2017)
- *Authors:* Pinto et al.
- *Direct Connection:* This work established the standard asymmetric training setup where the critic receives privileged state while the actor uses deployment observations, and Scaffolder generalizes this idea beyond the critic to world models, reward estimators, and other training-only components under privileged sensing.

### 🔧 Extension

**Mastering Diverse Domains through World Models (DreamerV3)** (2023)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* Scaffolder extends Dreamer-style world-model RL by injecting privileged sensing into the training of the latent dynamics, value, and reward models while deploying a policy that operates without those privileged inputs.

### 🔗 Related Problem

**Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG)** (2017)
- *Authors:* Ryan Lowe et al.
- *Direct Connection:* MADDPG’s centralized (privileged) critic with decentralized actors established the efficacy of asymmetric training, which Scaffolder generalizes from multi-agent global-state privilege to single-agent multi-sensor privilege across multiple auxiliary modules.

---

## Synthesis: How Prior Work Led to This Paper

Asymmetric Actor-Critic showed that granting the critic access to privileged state while constraining the actor to raw observations can dramatically stabilize and accelerate learning for image-based control. Learning Using Privileged Information (LUPI) cast this as a general principle: training-time side information can guide a learner without being available at test time. DreamerV3 demonstrated that latent world models can jointly learn dynamics, value, and reward from high-dimensional observations, offering modular components whose training signals can, in principle, be enriched. Learning by Cheating proved in autonomous driving that camera-only policies can be trained effectively by exploiting privileged signals like depth or segmentation during training. End-to-End Training of Deep Visuomotor Policies used full-state supervision to train deployable vision policies, establishing a robotics precedent for “train with state, deploy with vision.” MADDPG extended asymmetric training to multi-agent settings by using a centralized critic with privileged global information, underscoring the general utility of asymmetric access in actor-critic methods.
Together, these works exposed a gap: privileged information was either confined to the critic (AAC, MADDPG) or leveraged via supervised/imitative training (GPS, LbC), while world-model RL (Dreamer) had not systematically exploited privileged sensing across its auxiliary components. The natural next step was to treat extra sensors as training-time scaffolds throughout the RL pipeline—critics, world models, and reward estimators—so the target policy benefits from richer training signals yet remains deployable with limited sensing. This synthesis yields a unified, modality-agnostic approach that broadens asymmetric learning beyond critics to all training-only modules.

---

*Analysis generated on: 2026-01-06T09:58:51.911418*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

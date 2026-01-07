# Prior Work Analysis Report

## Target Paper
**Title:** 5Akrk9Ln6N
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review** (2018)
- *Authors:* Sergey Levine
- *Connection:* RPG’s core idea of modeling an RL policy as a generative model over optimal trajectories and optimizing a variational bound directly instantiates the control-as-inference perspective formalized in this work.

### 💡 Inspiration

**Parameter-Exploring Policy Gradients** (2010)
- *Authors:* Frank Sehnke et al.
- *Connection:* RPG’s policy conditioning on an episode-level latent variable to induce coherent, multimodal exploration is a direct modern instantiation of PGPE’s parameter-based exploration concept.

**Diffuser: Diffusion Models for Offline Reinforcement Learning** (2022)
- *Authors:* Michael Janner et al.
- *Connection:* RPG is inspired by Diffuser’s demonstration that generative modeling of entire trajectories captures multimodality, but moves from offline planning to an online variational policy learning objective tied to optimality.

### 🔍 Gap Identification

**Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models** (2018)
- *Authors:* Kurtland Chua et al.
- *Connection:* RPG targets the sampling inefficiency and planner dependence of PETS/CEM-style trajectory optimization by replacing it with a learned, differentiable multimodal trajectory generator optimized via a variational bound.

### 📊 Baseline

**Dream to Control: Learning Behaviors by Latent Imagination** (2020)
- *Authors:* Danijar Hafner et al.
- *Connection:* RPG builds on Dreamer’s world-model-based data efficiency, but replaces its unimodal action policy learning with a latent-conditioned, trajectory-level generative policy and corresponding variational objective.

**Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor** (2018)
- *Authors:* Tuomas Haarnoja et al.
- *Connection:* RPG explicitly addresses SAC’s limitation of squashed-Gaussian (unimodal) policies by introducing a multimodal, latent-conditioned trajectory policy optimized with reparameterized gradients.

### 🔧 Extension

**Learning Continuous Control Policies by Stochastic Value Gradients** (2015)
- *Authors:* Nicolas Heess et al.
- *Connection:* RPG extends the pathwise (reparameterization) gradient idea of SVG by backpropagating through a learned dynamics model for trajectory-level, latent-conditioned policy optimization rather than stepwise action perturbations.

---

## Synthesis

RPG reframes policy learning as generative modeling of optimal trajectories and optimizes a variational bound to encourage exploration and data efficiency. This framing directly descends from the control-as-inference viewpoint (Levine, 2018), which interprets RL as inference over optimality and naturally yields trajectory distributions and variational objectives. To make this objective trainable end-to-end, RPG leverages pathwise derivatives through a learned dynamics model, extending the reparameterized gradient machinery of Stochastic Value Gradients (Heess et al., 2015) from stepwise action perturbations to a latent-conditioned trajectory generator. The choice to condition the policy on an episode-level latent variable for coherent, multimodal exploration traces to Parameter-Exploring Policy Gradients (Sehnke et al., 2010), which pioneered sampling global parameters to induce consistent behavior across a rollout. Empirically and conceptually, RPG draws inspiration from Diffuser (Janner et al., 2022), which validates that generative models over entire trajectories capture multimodality; RPG adapts this idea to online, model-based RL with an optimality-grounded variational bound. On the model-based side, PETS (Chua et al., 2018) highlighted the strengths of trajectory optimization but also its reliance on expensive sampling-based planners—limitations RPG avoids by learning a differentiable, multimodal trajectory policy. Finally, Dreamer (Hafner et al., 2020) provides the world-model foundation for data-efficient learning that RPG adopts while moving beyond unimodal action parameterizations typified by Soft Actor-Critic (Haarnoja et al., 2018). Together, these works form the direct intellectual lineage enabling RPG’s multimodal, reparameterized trajectory policy learning.

---
*Generated: 2026-01-06T23:09:26.580960*

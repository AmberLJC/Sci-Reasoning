# Prior Work Analysis Report

## Target Paper

**Title:** Scalable Decision-Making in Stochastic Environments through Learned Temporal Abstraction

**Conference:** ICLR 2025 (spotlight)

**Authors:** Baiting Luo, Ava Pettet, Aron Laszka, Abhishek Dubey, Ayan Mukhopadhyay

**Keywords:** Sequential Decision-Making, Monte Carlo Tree Search, Temporal Abstraction, Planning, Model-based Reinforcement Learning, Offline Reinforcement Learning

**Abstract:** 
> Sequential decision-making in high-dimensional continuous action spaces, particularly in stochastic environments, faces significant computational challenges. We explore this challenge in the traditional offline RL setting, where an agent must learn how to make decisions based on data collected through a stochastic behavior policy. We present \textit{Latent Macro Action Planner} (L-MAP), which addresses this challenge by learning a set of temporally extended macro-actions through a state-conditio...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning** (1999)
- *Authors:* Richard S. Sutton et al.
- *Direct Connection:* This work formalized temporally extended actions (“options”), providing the core abstraction that L-MAP instantiates by learning and planning over discrete macro-actions rather than primitive controls.

### 💡 Inspiration

**Learning Latent Plans from Play** (2019)
- *Authors:* Corey Lynch et al.
- *Direct Connection:* This paper introduced conditioning a VQ-VAE on state context with a learned prior over discrete plan codes to generate coherent multi-step behaviors, which L-MAP repurposes to sample plausible latent macro-actions for planning.

**Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero)** (2019)
- *Authors:* Julian Schrittwieser et al.
- *Direct Connection:* MuZero demonstrated effective MCTS over a learned latent dynamics model, directly inspiring L-MAP’s use of MCTS on a learned latent transition model to plan over discrete macro-action latents.

### 🔍 Gap Identification

**Batch-Constrained deep Q-learning** (2019)
- *Authors:* Scott Fujimoto et al.
- *Direct Connection:* BCQ showed that constraining offline decisions to the support of a learned behavior model mitigates OOD actions, motivating L-MAP’s learned prior that restricts planning to plausible macro-actions under a stochastic behavior policy.

### 📊 Baseline

**MOPO: Model-Based Offline Policy Optimization** (2020)
- *Authors:* Tianhe Yu et al.
- *Direct Connection:* As a primary model-based offline RL baseline, MOPO highlights compounding-model-error and OOD-action issues that L-MAP addresses by searching in a discretized macro-action space guided by a behavior-consistent prior.

### 🔧 Extension

**Neural Discrete Representation Learning** (2017)
- *Authors:* Aaron van den Oord et al.
- *Direct Connection:* L-MAP directly builds on VQ-VAE’s vector-quantized codebook to discretize multi-step action chunks into latent codes, adapting the framework with state conditioning to make macro-actions context-dependent.

---

## Synthesis: How Prior Work Led to This Paper

Temporal abstraction via the options framework established that multi-step behaviors can be treated as decision-making primitives, offering a route to reduce planning depth and complexity. Neural discrete representation learning with VQ-VAE introduced vector quantization and codebooks that convert continuous objects into discrete latent tokens with efficient sampling, a mechanism later adapted to sequence generation. Building on this, Learning Latent Plans from Play showed that a state- (e.g., start/goal-) conditioned VQ-VAE with a learned prior over discrete codes can produce coherent multi-step action sequences, indicating that discrete latent plans can be sampled plausibly from offline data. In offline RL, Batch-Constrained deep Q-learning demonstrated that a generative behavior model is crucial to keep action choices within the dataset’s support, directly motivating behavior-aware priors. Meanwhile, MuZero established that MCTS over a learned latent transition model enables effective planning without explicit environment models. Finally, MOPO revealed the pitfalls of model-based offline RL—namely compounding model error and out-of-distribution actions—when planning in continuous spaces.
Combining these insights, the next step was to discretize continuous control into state-conditioned macro-action tokens learned from offline trajectories, use a learned prior to sample behavior-supported latents, and plan with MCTS over a latent transition model. This synthesis reduces branching and action dimensionality, preserves plausibility under a stochastic behavior policy, and leverages tree search to handle environmental stochasticity—yielding scalable offline planning in high-dimensional stochastic domains.

---

*Analysis generated on: 2026-01-06T06:36:42.670439*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

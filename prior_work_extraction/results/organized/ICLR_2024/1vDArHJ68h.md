# Prior Work Analysis Report

## Target Paper

**Title:** Mastering Memory Tasks with World Models

**Conference:** ICLR 2024 (oral)

**Authors:** Mohammad Reza Samsami, Artem Zholus, Janarthanan Rajendran, Sarath Chandar

**Keywords:** model-based reinforcement learning, state space models, memory in reinforcement learning

**Abstract:** 
> Current model-based reinforcement learning (MBRL) agents struggle with long-term dependencies. This limits their ability to effectively solve tasks involving extended time gaps between actions and outcomes, or tasks demanding the recalling of distant observations to inform current actions. To improve temporal coherence, we integrate a new family of state space models (SSMs) in world models of MBRL agents to present a new method, Recall to Imagine (R2I). This integration aims to enhance both long...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning Latent Dynamics for Planning (PlaNet)** (2019)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* R2I builds on PlaNet’s recurrent state-space model (RSSM) formulation for latent imagination, replacing the GRU-based latent dynamics with state space models to better preserve information across long horizons.

### 💡 Inspiration

**Unsupervised Predictive Memory in a Goal-Directed Agent (MERLIN)** (2018)
- *Authors:* Greg Wayne et al.
- *Direct Connection:* MERLIN’s finding that predictive memory retrieval improves performance under partial observability directly inspires R2I’s recall-to-imagine mechanism that brings distant observations into latent rollouts.

### 🔍 Gap Identification

**RUDDER: Return Decomposition for Delayed Rewards** (2019)
- *Authors:* José A. Arjona-Medina et al.
- *Direct Connection:* By highlighting the challenge of long-horizon credit assignment with delayed rewards, RUDDER motivates R2I’s design to propagate value/gradient information to distant latent states via recall within a world model rather than return decomposition.

### 📊 Baseline

**Mastering Diverse Domains via World Models (DreamerV3)** (2023)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* R2I adopts the DreamerV3 world-model training pipeline and objectives as its main baseline and directly addresses DreamerV3’s weakness on long-term dependencies by augmenting the RSSM dynamics with an SSM-based recall mechanism.

### 🔧 Extension

**Efficiently Modeling Long Sequences with Structured State Spaces (S4)** (2022)
- *Authors:* Albert Gu et al.
- *Direct Connection:* R2I instantiates its memory-capable world-model dynamics using SSM layers derived from S4, leveraging their long-range recurrence and scan efficiency to extend the temporal context used for imagination and control.

### 🔗 Related Problem

**Stabilizing Transformers for Reinforcement Learning (GTrXL)** (2020)
- *Authors:* Emilio Parisotto et al.
- *Direct Connection:* GTrXL shows that strengthening sequence models improves long-range memory and credit assignment in RL, informing R2I’s choice to replace GRU dynamics with a stronger long-context sequence model (SSM) inside a world model.

---

## Synthesis: How Prior Work Led to This Paper

PlaNet introduced a recurrent state-space model that learns latent dynamics for imagination-based control, using GRU-augmented stochastic latents to plan in a compact space. DreamerV3 refined this world-model paradigm into a scalable, general recipe that achieves strong performance across domains, but its GRU-based dynamics remain limited on long-term dependencies. In parallel, Structured State Space models (S4) showed that linear state-space recursions with learned kernels can retain information over very long sequences while remaining training- and hardware-efficient via parallel scan. MERLIN demonstrated that predictive memory and targeted retrieval of past observations can be crucial in partially observable settings, empirically validating the importance of recall mechanisms for decision making. RUDDER squarely framed the difficulty of long-horizon credit assignment with delayed rewards and proposed return decomposition to address it, underscoring the need to propagate learning signals to events far in the past. GTrXL established that upgrading the sequence model itself can stabilize and dramatically extend temporal credit in RL.
Building on these ideas, the next step is to inject a long-memory sequence model directly into the latent dynamics of a Dreamer-style world model, and to marry it with an explicit recall mechanism so imagination can condition on distant, task-relevant observations. This synthesis addresses the observed limits of GRU-based RSSMs, leverages SSMs’ long-range memory and efficiency, and routes value information back across long gaps—thereby unifying memory and credit assignment within model-based RL.

---

*Analysis generated on: 2026-01-06T17:11:06.691975*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

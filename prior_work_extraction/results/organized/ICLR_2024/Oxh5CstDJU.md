# Prior Work Analysis Report

## Target Paper

**Title:** TD-MPC2: Scalable, Robust World Models for Continuous Control

**Conference:** ICLR 2024 (spotlight)

**Authors:** Nicklas Hansen, Hao Su, Xiaolong Wang

**Keywords:** reinforcement learning, model-based reinforcement learning, world models

**Abstract:** 
> TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model. In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm. We demonstrate that TD-MPC2 improves significantly over baselines across 104 online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single set of hyperparameters. We further show that agent capabilit...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**PlaNet: Learning Latent Dynamics for Planning from Pixels** (2019)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* TD-MPC2 builds on PlaNet’s core idea of CEM-based local trajectory optimization in a learned latent dynamics model, while replacing reconstruction-trained RSSM with value-centric, decoder-free learning.

**PETS: Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models** (2018)
- *Authors:* Kurtland Chua et al.
- *Direct Connection:* PETS pioneered uncertainty-aware model ensembles and sampling-based MPC (CEM) that inform TD-MPC2’s robust planning and ensemble design for continuous control.

### 💡 Inspiration

**Value-Aware Model Learning** (2017)
- *Authors:* Amir-massoud Farahmand et al.
- *Direct Connection:* The value-aware principle—that models should preserve value-relevant predictions rather than reconstruct observations—directly motivates TD‑MPC2’s TD-trained, decoder-free world model objective.

### 🔍 Gap Identification

**DreamerV3: Mastering Diverse Domains through World Models** (2023)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* By showing that robust, single-hyperparameter world-model agents can scale across many domains, DreamerV3 set the bar and exposed limitations of reconstruction-heavy, actor-critic pipelines that TD-MPC2 addresses with an MPC-based, decoder-free alternative.

### 📊 Baseline

**DrQ-v2: Stronger, Better, and Faster** (2021)
- *Authors:* Denis Yarats et al.
- *Direct Connection:* DrQ‑v2 serves as the principal model-free vision baseline with strong data augmentation and stable hyperparameters that TD‑MPC2 consistently benchmarks against and aims to surpass under a single configuration.

### 🔧 Extension

**TD-MPC: Temporal-Difference Learning for Model Predictive Control** (2022)
- *Authors:* Nicklas Hansen et al.
- *Direct Connection:* TD-MPC2 directly extends TD-MPC’s decoder-free latent world model and latent-space MPC, modifying the TD-driven training objectives, architecture, and scaling regimen while keeping the same planning-in-latent framework.

---

## Synthesis: How Prior Work Led to This Paper

Planning-based model-based RL from pixels crystallized with latent world models. PlaNet introduced learning a recurrent latent dynamics model and performing CEM-based local trajectory optimization entirely in latent space, showing that planning need not occur in pixel space. PETS established the effectiveness of sampling-based MPC with uncertainty-aware ensembles, providing a recipe for robust control in continuous domains that many later world-model methods inherited. DreamerV3 demonstrated that scaling latent world models and adhering to a single hyperparameter set can produce strong, general-purpose agents across diverse domains, although it achieved this with actor-critic policies and reconstruction-heavy training objectives. In parallel, value-aware model learning argued that models should be optimized for task-relevant predictive fidelity (value consistency) instead of pixel reconstruction, motivating decoder-free objectives for world models. TD‑MPC operationalized these ideas by discarding decoders, training latent dynamics via temporal-difference signals, and performing latent-space MPC, delivering strong sample efficiency and robustness on visual control. Strong model-free methods like DrQ‑v2 set competitive baselines and training practices for vision-based control, emphasizing simple, stable pipelines. Building on this, the next step was to marry PlaNet’s latent-space planning with value-aware, decoder-free training, adopt ensemble-aware robust MPC from PETS, and embrace DreamerV3’s scale and single-configuration ethos. This synthesis naturally leads to a scalable, robust, decoder-free world-model control framework that retains the planning advantages of MPC while achieving cross-domain generality with a single set of hyperparameters.

---

*Analysis generated on: 2026-01-06T23:46:12.140188*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

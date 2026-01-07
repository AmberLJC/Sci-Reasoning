# Prior Work Analysis Report

## Target Paper

**Title:** MetaPhysiCa: Improving OOD Robustness in Physics-informed Machine Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** S Chandra Mouli, Muhammad Alam, Bruno Ribeiro

**Keywords:** physics-informed machine learning, OOD robustness, meta learning, causal structure discovery

**Abstract:** 
> A fundamental challenge in physics-informed machine learning (PIML) is the design of robust PIML methods for out-of-distribution (OOD) forecasting tasks. These OOD tasks require learning-to-learn from observations of the same (ODE) dynamical system with different unknown ODE parameters, and demand accurate forecasts even under out-of-support initial conditions and out-of-support ODE parameters. In this work we propose to improve the OOD robustness of PIML via a meta-learning procedure for causal...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Causal inference using invariant prediction: identification and confidence intervals** (2016)
- *Authors:* Jonas Peters et al.
- *Direct Connection:* MetaPhysiCa treats different ODE parameterizations as environments and uses the ICP principle—recovering causal parents via invariance across environments—to guide causal structure discovery for OOD forecasting.

### 💡 Inspiration

**Invariant Risk Minimization** (2019)
- *Authors:* Martin Arjovsky et al.
- *Direct Connection:* The method’s meta-objective directly operationalizes IRM by learning structures and predictors whose mechanisms remain invariant across tasks with varying ODE parameters, thereby targeting OOD robustness.

**Learning to Generalize: Meta-Learning for Domain Generalization** (2018)
- *Authors:* Da Li et al.
- *Direct Connection:* The approach adopts an MLDG-style bilevel meta-train/meta-test scheme across environments (different ODE parameters) to explicitly pressure the learned structure to generalize to unseen conditions.

**Learning Independent Causal Mechanisms** (2018)
- *Authors:* Giambattista Parascandolo et al.
- *Direct Connection:* MetaPhysiCa leverages the ICM hypothesis by separating invariant structural relations from task-specific parameters, enabling transfer under interventions/parameter shifts in dynamical systems.

### 📊 Baseline

**Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations** (2019)
- *Authors:* Maziar Raissi et al.
- *Direct Connection:* PINNs serve as the principal PIML baseline whose brittleness to out-of-support initial conditions and parameter shifts motivates MetaPhysiCa’s meta-causal procedure for improved OOD robustness.

### 🔧 Extension

**Neural Relational Inference for Interacting Systems** (2018)
- *Authors:* Thomas Kipf et al.
- *Direct Connection:* MetaPhysiCa extends NRI’s idea of inferring an interaction (causal) graph from trajectories by meta-learning a graph that is stable across parameterized tasks to enable OOD generalization.

---

## Synthesis: How Prior Work Led to This Paper

Invariant Causal Prediction showed that causal parents can be identified by finding conditionals that remain stable across environments, establishing invariance as a criterion for structure discovery. Invariant Risk Minimization translated this into a learning objective that selects representations and predictors whose mechanisms are invariant across domains, aiming for out-of-distribution generalization. The Independent Causal Mechanisms hypothesis further argued that causal modules are modular and stable under interventions, suggesting a separation between invariant structure and environment-specific variations. Neural Relational Inference demonstrated that interaction graphs underlying physical trajectories can be inferred from data, using a learnable graph to improve predictions of dynamical systems. Meta-learning for Domain Generalization introduced a bilevel meta-train/meta-test procedure that explicitly pressures learned representations to generalize across domains by simulating domain shift during training. Physics-Informed Neural Networks injected differential-equation residuals into the loss to leverage known physics, but they often struggle when initial conditions or governing parameters move outside the training support. Bringing these strands together, the opportunity emerged to meta-learn a causal interaction structure that is invariant across tasks induced by varying ODE parameters, using a bilevel objective to enforce invariance while retaining dynamics-aware modeling. By aligning with ICP/IRM principles and ICM modularity, and operationalizing them through an NRI-style structure learner trained in an MLDG-like meta-setup, the current work naturally targets robust OOD forecasting and addresses the limitations observed in standard PIML baselines such as PINNs.

---

*Analysis generated on: 2026-01-06T14:25:39.863872*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

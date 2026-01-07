# Prior Work Analysis Report

## Target Paper

**Title:** Learning Spatiotemporal Dynamical Systems from Point Process Observations

**Conference:** ICLR 2025 (spotlight)

**Authors:** Valerii Iakovlev, Harri Lähdesmäki

**Keywords:** dynamics, spatiotemporal, neural, PDE, ODE

**Abstract:** 
> Spatiotemporal dynamics models are fundamental for various domains, from heat propagation in materials to oceanic and atmospheric flows. However, currently available neural network-based spatiotemporal modeling approaches fall short when faced with data that is collected randomly over time and space, as is often the case with sensor networks in real-world applications like crowdsourced earthquake detection or pollution monitoring. In response, we developed a new method that can effectively learn...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**An explicit link between Gaussian fields and Gaussian Markov random fields: the SPDE approach** (2011)
- *Authors:* Finn Lindgren et al.
- *Direct Connection:* This SPDE-based construction of latent spatiotemporal fields underpins Cox-process models for event data, motivating the present shift from linear-Gaussian SPDE priors to learned nonlinear neural dynamics for the intensity-driving field.

### 💡 Inspiration

**SIREN: Implicit Neural Representations with Periodic Activation Functions** (2020)
- *Authors:* Vincent Sitzmann et al.
- *Direct Connection:* The approach borrows the idea of coordinate-based implicit networks to represent continuous spatiotemporal fields and to enable querying (and differentiating) the state at arbitrary space-time points required by point-process modeling.

### 🔍 Gap Identification

**Fourier Neural Operator for Parametric Partial Differential Equations** (2021)
- *Authors:* Zongyi Li et al.
- *Direct Connection:* FNO exemplifies neural PDE solvers that assume dense, gridded supervision, a key limitation that this work addresses by learning dynamics directly from randomly sampled point events in continuous space-time.

**Learning Operators: DeepONet** (2021)
- *Authors:* Lu Lu et al.
- *Direct Connection:* DeepONet highlights operator-learning methods trained on paired input–output fields on grids, motivating the need for a framework that can infer dynamics when only stochastic point observations are available.

### 📊 Baseline

**Variational Inference for Gaussian Process Modulated Poisson Processes** (2015)
- *Authors:* James R. Lloyd et al.
- *Direct Connection:* The method adopts the Cox-process (Poisson) likelihood framework for modeling randomly located observations and replaces the GP intensity with a neural dynamical field, directly building on Lloyd et al.’s variational treatment of Poisson process data.

### 🔧 Extension

**Latent ODEs for Irregularly-Sampled Time Series** (2019)
- *Authors:* Yulia Rubanova et al.
- *Direct Connection:* The work extends the latent ODE amortized variational inference paradigm from 1D time series to a spatiotemporal latent field and swaps the usual Gaussian observation model for a point-process likelihood.

### 🔗 Related Problem

**The Neural Hawkes Process: A Neurally Self-Modulating Multivariate Point Process** (2017)
- *Authors:* Hongyuan Mei et al.
- *Direct Connection:* Neural Hawkes established neural parameterization and likelihood-based training for temporal point processes, informing how to compute and optimize the integral-plus-event-sum objective used here with a dynamics-driven intensity.

---

## Synthesis: How Prior Work Led to This Paper

Lloyd et al. introduced a practical variational framework for Cox processes by modeling the Poisson intensity as a transformed latent function, enabling inference from event locations through an integral-plus-event-sum objective. Lindgren et al.’s SPDE approach provided a principled construction for latent spatiotemporal Gaussian fields that can drive such intensities, but within a linear-Gaussian prior class. Rubanova et al. showed how amortized variational inference can be coupled with neural differential equations to learn continuous-time latent dynamics from irregular observations, replacing discrete-time models with a differentiable flow. Sitzmann et al. demonstrated that coordinate-based implicit neural representations can model continuous fields and their derivatives, allowing efficient querying at arbitrary coordinates. In parallel, Li et al.’s Fourier Neural Operator and Lu et al.’s DeepONet advanced neural PDE/operator learning but relied on supervised training with dense gridded fields, not stochastic, randomly located measurements. Mei and Eisner established neural intensity modeling and likelihood optimization techniques for point processes, clarifying how to train models that must integrate intensities over continuous time (and by extension, space).
Taken together, these works expose an opportunity: combine Cox-process likelihoods with continuous-time neural dynamics and implicit neural fields to learn spatiotemporal systems directly from randomly located events. By replacing Gaussian SPDE priors with learned neural dynamics, adopting amortized VI for latent differential equations, and leveraging implicit representations for arbitrary space-time queries, the present method naturally generalizes point-process modeling to dynamics-driven spatiotemporal fields while overcoming the dense-grid supervision assumptions of neural operator baselines.

---

*Analysis generated on: 2026-01-06T17:47:18.672867*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

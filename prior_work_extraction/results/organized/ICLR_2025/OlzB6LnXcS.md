# Prior Work Analysis Report

## Target Paper

**Title:** One Step Diffusion via Shortcut Models

**Conference:** ICLR 2025 (oral)

**Authors:** Kevin Frans, Danijar Hafner, Sergey Levine, Pieter Abbeel

**Keywords:** diffusion, flow-matching, fast inference, distillation

**Abstract:** 
> Diffusion models and flow matching models have enabled generating diverse and realistic images by learning to transfer noise to data. However, sampling from these models involves iterative denoising over many neural network passes, making generation slow and expensive. Previous approaches for speeding up sampling require complex training regimes, such as multiple training phases, multiple networks, or fragile scheduling. We introduce Shortcut Models, a family of generative models that use a sing...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Flow Matching for Generative Modeling** (2023)
- *Authors:* Yaron Lipman et al.
- *Direct Connection:* Flow Matching provides the vector-field learning framework that Shortcut Models build on, with the key modification of conditioning the learned field on a target step size to enable accurate long-step integration in one or few evaluations.

### 💡 Inspiration

**Rectified Flow** (2023)
- *Authors:* Ruiqi Gao Liu et al.
- *Direct Connection:* Rectified Flow’s insight that straightened transport paths support larger stable integration steps directly motivates Shortcut Models’ idea of training a single field to execute variable-length jumps by conditioning on the intended step size.

### 🔍 Gap Identification

**Progressive Distillation for Fast Sampling of Diffusion Models** (2022)
- *Authors:* Tim Salimans et al.
- *Direct Connection:* Progressive Distillation’s multi-phase, teacher–student halving schedule crystallized the complexity and fragility of existing speedup pipelines that Shortcut Models explicitly remove by learning a single network that handles arbitrary step sizes in one training phase.

### 📊 Baseline

**Consistency Models** (2023)
- *Authors:* Yang Song et al.
- *Direct Connection:* Consistency Models introduced time-conditioned self-consistency for one- and few-step generation, which Shortcut Models surpass by directly conditioning on the desired step size to learn skip-ahead mappings without teacher distillation or multi-phase training.

**ReFlow** (2024)
- *Authors:* X. Liu et al.
- *Direct Connection:* ReFlow aims to refit or resample the generative path to enable long-step sampling, which Shortcut Models improve upon by learning skip-ahead behavior in a single network without fragile resampling schedules or multiple training phases.

### 🔗 Related Problem

**Latent Consistency Models** (2023)
- *Authors:* Shangchen Luo et al.
- *Direct Connection:* Latent Consistency Models demonstrate practical fast sampling via consistency distillation in latent space, whose reliance on a pretrained teacher and schedule design is avoided by Shortcut Models through direct step-size conditioning learned end-to-end.

---

## Synthesis: How Prior Work Led to This Paper

Flow Matching formalized learning a time-conditioned vector field that transports noise to data, enabling deterministic ODE sampling and creating a natural interface for conditioning on continuous variables like time. Rectified Flow showed that choosing straightened transport paths stabilizes training and permits much larger integration steps without catastrophic drift, highlighting that the learned field can be shaped to support long-step moves. Consistency Models introduced the idea of enforcing time-wise self-consistency so a single network can yield one- or few-step samples, but their training typically relies on teacher trajectories or delicate objectives tied to integration schedules. Latent Consistency Models brought this idea to latent diffusion, yielding practical speedups but still depending on a pretrained teacher and tuned schedules. Progressive Distillation achieved faster sampling by repeatedly halving the number of steps through multi-stage teacher–student distillation, making speedups costly and fragile due to many phases and networks. ReFlow pursued fast sampling by reshaping or resampling the transport path to tolerate large steps, yet typically requires bespoke schedules or multi-phase procedures. Together these works reveal that long-step transport is feasible and desirable, but existing routes often hinge on teachers, multiple phases, or brittle scheduling. The natural next step is to directly learn a single time-conditioned vector field that also conditions on the desired step size, so the model itself learns to “skip ahead” across variable budgets. By marrying flow-matching’s vector-field supervision with the consistency insight—while replacing schedule/teacher dependence with explicit step-size conditioning—one network can produce high-quality samples in one or multiple steps with a single, simple training phase.

---

*Analysis generated on: 2026-01-06T19:12:10.287346*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

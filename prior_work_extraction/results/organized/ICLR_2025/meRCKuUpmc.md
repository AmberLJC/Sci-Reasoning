# Prior Work Analysis Report

## Target Paper

**Title:** Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

**Conference:** ICLR 2025 (oral)

**Authors:** Yang Tian, Sizhe Yang, Jia Zeng, Ping Wang, Dahua Lin, Hao Dong, Jiangmiao Pang

**Keywords:** Robotic Manipulation ; Pre-training ; Visual Foresight ; Inverse Dynamics ; Large-scale robot dataset

**Abstract:** 
> Current efforts to learn scalable policies in robotic manipulation primarily fall into two categories: one focuses on "action," which involves behavior cloning from extensive collections of robotic data, while the other emphasizes "vision," enhancing model generalization by pre-training representations or generative models, also referred to as world models, using large-scale visual datasets. This paper presents an end-to-end paradigm that predicts actions using inverse dynamics models conditione...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset** (2024)
- *Authors:* Caine et al.
- *Direct Connection:* PIDM’s large-scale pretraining relies on DROID as the primary dataset, enabling its end-to-end training across diverse robots and tasks.

### 💡 Inspiration

**Visual Foresight: Learning to Predict and Plan with Deep Predictive Models** (2018)
- *Authors:* Frederik Ebert et al.
- *Direct Connection:* This work established the core idea of forecasting future visual states for control, which PIDM adopts by conditioning inverse dynamics on predicted visual futures rather than planning directly in pixel space.

**Dream to Control: Learning Behaviors by Latent Imagination** (2020)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* By showing that world models can predict future latent states to guide action, this paper directly motivates PIDM’s use of predicted (visual) futures as the substrate from which actions are derived.

### 🔍 Gap Identification

**Real-World Robot Learning with Masked Visual Pre-Training (VC-1)** (2022)
- *Authors:* Ilya Radosavovic et al.
- *Direct Connection:* VC-1 demonstrates vision-side pretraining improves manipulation but leaves vision-action coupling weak; PIDM directly tackles this gap by closing the loop with an inverse dynamics head conditioned on predicted visual futures.

### 📊 Baseline

**RT-1: Robotics Transformer for Real-World Control at Scale** (2022)
- *Authors:* A. Brohan et al.
- *Direct Connection:* RT-1 is the main large-scale behavior cloning baseline focused on actions that PIDM aims to surpass by explicitly incorporating visual foresight before action prediction.

**Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** (2023)
- *Authors:* Chi et al.
- *Direct Connection:* As a strong action-focused imitation method that models action distributions given current observations, Diffusion Policy serves as a primary competitor that lacks explicit future-state prediction, which PIDM addresses.

---

## Synthesis: How Prior Work Led to This Paper

Video-prediction-based control established that anticipating future visual states can enable planning directly in image space; Visual Foresight concretized this with learned predictive models that roll out future frames for goal-directed behavior. World-model RL advanced the idea in latent space: Dream to Control showed that a compact predictive model of future states could guide action selection effectively across long horizons. In parallel, large-scale imitation learning scaled action policies from demonstrations: RT-1 introduced a transformer policy trained over diverse real-world data, proving that sequences of observations and actions can be modeled at scale, while Diffusion Policy modeled rich, multimodal action distributions conditioned on observations but remained purely reactive. On the vision side, VC-1 demonstrated that masked visual pretraining on robot data yields representations that improve manipulation, yet its vision-action interface remained decoupled during pretraining. Finally, DROID emerged as a broad, in-the-wild manipulation dataset, providing the diversity and scale needed to pretrain generalist policies. Together, these works revealed a gap: action-focused policies scale but lack explicit foresight, vision-pretrained models generalize but don’t directly produce actions, and world models often require RL or planning. The natural next step is to close the loop by predicting future visual states and then mapping those predictions to actions via supervised inverse dynamics. Leveraging DROID-scale data and transformer sequence modeling, this synthesis yields an end-to-end, scalable learner that unifies foresight with action generation.

---

*Analysis generated on: 2026-01-06T15:42:42.012749*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

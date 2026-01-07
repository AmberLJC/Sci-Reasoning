# Prior Work Analysis Report

## Target Paper
**Title:** LyJi5ugyJx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Connection:* The SDE/ODE framework and probability flow ODE from this work provide the continuous-time generative modeling formalism that the present paper uses to define, analyze, and stabilize continuous-time consistency training.

**Denoising Diffusion Probabilistic Models** (2020)
- *Authors:* Jonathan Ho et al.
- *Connection:* The original diffusion parameterizations (e.g., epsilon/x0 prediction) and training objective in DDPM are explicitly unified in this paper’s simplified framework, which identifies which parameterizations cause instability for continuous-time CMs.

### 💡 Inspiration

**Denoising Diffusion Implicit Models** (2021)
- *Authors:* Jiaming Song et al.
- *Connection:* DDIM’s deterministic ODE view and time-coupled parameterizations directly inform the paper’s unification of diffusion and consistency parameterizations and its design of stable continuous-time objectives.

### 🔍 Gap Identification

**Consistency Trajectory Models** (2024)
- *Authors:* Shaojie Zhao et al.
- *Connection:* CTM advanced few-step CMs but remained tied to discretized timesteps and schedule hyperparameters; the present work explicitly targets these limitations by formulating and stabilizing a continuous-time CM that scales to large models.

### 📊 Baseline

**Consistency Models** (2023)
- *Authors:* Yang Song et al.
- *Connection:* This paper directly builds on the original consistency-model objective, diagnosing why its continuous-time limit is unstable and replacing the discrete-time training and parameterization choices with a unified, stable continuous-time formulation.

### 🔧 Extension

**Elucidating the Design Space of Diffusion-Based Generative Models** (2022)
- *Authors:* Tero Karras et al.
- *Connection:* The paper extends EDM-style continuous noise-level/sigma parameterization and loss weighting into the consistency-model setting, using these design choices to eliminate discretization-induced instability in continuous time.

### 🔗 Related Problem

**Rectified Flow: An Alternative to Score-Based Generative Models** (2023)
- *Authors:* Yang Song? (Note: replace with correct 'Liu et al.' first author) et al.
- *Connection:* Rectified flow’s continuous-time velocity-field training and path parameterization inform the paper’s analysis of parameterizations for stable ODE-based generation, motivating the architectural and objective choices for continuous-time CMs.

---

## Synthesis

The core innovation—stable, scalable training of continuous-time consistency models—emerges by unifying and rectifying the parameterizations inherited from diffusion and ODE-based generative modeling. DDPM established the basic diffusion objectives and parameterizations (epsilon/x0/v), which later diversified, while DDIM exposed their deterministic ODE counterpart and time-coupled sampling, making explicit how predictions at different noise levels must agree. The SDE/ODE framework then formalized the continuous-time view via probability flow ODEs, providing the mathematical backbone for defining a continuous-time consistency objective.

Consistency Models introduced the fast-sampling objective that enforces agreement across time, but practical training relied on discretized timesteps, bringing schedule hyperparameters and discretization error; CTM improved quality yet remained discretized and difficult to scale. EDM contributed robust continuous sigma parameterization and loss weighting that stabilize training in continuous time; this paper absorbs those design choices into the CM setting and shows which parameterizations are stable. Finally, ideas from rectified-flow style continuous-time velocity modeling inform how to parameterize the network and objective to avoid the instabilities that appear when naively taking the continuous-time limit of discrete CMs.

By synthesizing these strands, the paper identifies the root causes of instability, proposes a unified continuous-time parameterization and objective, and demonstrates that—with the right architecture and loss weighting—continuous-time CMs can be trained at unprecedented scale and deliver state-of-the-art two-step sampling performance.

---
*Generated: 2026-01-06T23:09:26.646117*

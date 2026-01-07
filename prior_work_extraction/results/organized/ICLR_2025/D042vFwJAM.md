# Prior Work Analysis Report

## Target Paper

**Title:** Physics-aligned field reconstruction with diffusion bridge

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zeyu Li, Hongkun Dou, Shen Fang, Wang Han, Yue Deng, Lijun Yang

**Keywords:** Fluid dynamics, diffusion models, super-resolution

**Abstract:** 
> The reconstruction of physical fields from sparse measurements is pivotal in both scientific research and engineering applications. Traditional methods are increasingly supplemented by deep learning models due to their efficacy in extracting features from data. However, except for the low accuracy on complex physical systems, these models often fail to comply with essential physical constraints, such as governing equations and boundary conditions. To overcome this limitation, we introduce a nove...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Diffusion Schrödinger Bridge with Applications to Score-Based Generative Modeling** (2021)
- *Authors:* Giulia De Bortoli et al.
- *Direct Connection:* This work provides the core diffusion-bridge formulation for transporting between endpoint distributions using learned forward/reverse drifts, which PalSB adopts and tailors so that the terminal constraints encode PDE residuals and boundary conditions.

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Direct Connection:* It supplies the reverse-time SDE framework and time-indexed score networks that PalSB leverages to parameterize its local reconstruction mapping along the diffusion bridge.

### 💡 Inspiration

**Diffusion Posterior Sampling for General Noisy Inverse Problems** (2022)
- *Authors:* Hyungjin Chung et al.
- *Direct Connection:* By enforcing measurement consistency during diffusion sampling via projection/data-consistency steps, this paper motivates PalSB's boundary-aware sampling that projects bridge trajectories to satisfy physical boundary conditions.

### 🔍 Gap Identification

**Physics-Informed Neural Networks: A Deep Learning Framework for Solving Forward and Inverse Problems Involving Nonlinear Partial Differential Equations** (2019)
- *Authors:* Maziar Raissi et al.
- *Direct Connection:* PINNs established imposing PDE and boundary residuals in training but struggle on complex systems, a limitation PalSB addresses by replacing deterministic regression with a diffusion-bridge plus dual-stage physics alignment.

### 📊 Baseline

**Fourier Neural Operator for Parametric Partial Differential Equations** (2021)
- *Authors:* Zongyi Li et al.
- *Direct Connection:* As a dominant operator-learning baseline for field super-resolution/reconstruction from sparse or coarse inputs, FNO is the primary system PalSB aims to outperform while restoring physical fidelity.

### 🔧 Extension

**Physics-Informed Neural Operator for Learning Parametric Partial Differential Equations** (2022)
- *Authors:* Zongyi Li et al.
- *Direct Connection:* PINO integrates physics residual losses into operator learning; PalSB extends this principle to generative training by coupling physics-informed objectives with a diffusion-bridge to enforce global physical alignment.

---

## Synthesis: How Prior Work Led to This Paper

Diffusion Schrödinger Bridge introduced a principled way to learn stochastic bridges by estimating forward and reverse drifts so that paths connect prescribed endpoints, establishing the machinery for distribution-to-distribution transport via learned score fields. Score-Based Generative Modeling through SDEs provided the reverse-time SDE formulation and time-conditioned score networks that enable stable training and sampling of such bridges. Diffusion Posterior Sampling showed that constraints arising from measurements can be enforced during diffusion sampling through projection and data-consistency steps, demonstrating how generative trajectories can be steered to satisfy external conditions. Physics-Informed Neural Networks formalized embedding governing-equation and boundary residuals into the training objective for forward and inverse PDE problems, but also revealed difficulties on complex, multi-scale dynamics. Fourier Neural Operator established an efficient baseline for mapping from sparse/coarse information to full fields, widely used for super-resolution and reconstruction in fluids, though it generally lacks strict physics compliance. Physics-Informed Neural Operator combined operator learning with physics residual penalties to improve physical fidelity, hinting that fusing data-driven and physics-based objectives can enhance reconstruction.
Together, these works expose a gap: strong priors from diffusion models and bridges can transport distributions but need principled mechanisms to honor PDE and boundary constraints, while deterministic PINN/NO approaches encode physics yet falter on complex fields. The natural next step is to embed physics residuals and boundary conditions as endpoint/trajectory constraints within a diffusion-bridge framework, trained in a way that separates local reconstruction fidelity from global physical alignment and uses constraint-aware sampling to enforce boundaries—precisely the synthesis realized by PalSB.

---

*Analysis generated on: 2026-01-06T16:41:02.059527*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

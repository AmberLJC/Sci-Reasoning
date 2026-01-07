# Prior Work Analysis Report

## Target Paper

**Title:** Learning to Discretize Denoising Diffusion ODEs

**Conference:** ICLR 2025 (oral)

**Authors:** Vinh Tong, Dung Trung Hoang, Anji Liu, Guy Van den Broeck, Mathias Niepert

**Keywords:** Diffusion models, Efficient Sampling, Ordinary Differentiable Equations

**Abstract:** 
> Diffusion Probabilistic Models (DPMs) are generative models showing competitive performance in various domains, including image synthesis and 3D point cloud generation. Sampling from pre-trained DPMs involves multiple neural function evaluations (NFEs) to transform Gaussian noise samples into images, resulting in higher computational costs compared to single-step generative models such as GANs or VAEs. Therefore, reducing the number of NFEs while preserving generation quality is crucial. To addr...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Direct Connection:* This work introduced the probability flow ODE that turns diffusion sampling into solving an ODE, providing the exact formulation whose time grid LD3 learns to discretize.

**Denoising Diffusion Implicit Models** (2020)
- *Authors:* Jiaming Song et al.
- *Direct Connection:* DDIM showed that deterministic sampling corresponds to an ODE with a chosen timestep schedule, directly motivating LD3’s goal of learning the timestep schedule rather than hand-designing it.

### 🔍 Gap Identification

**Elucidating the Design Space of Diffusion-Based Generative Models** (2022)
- *Authors:* Tero Karras et al.
- *Direct Connection:* This paper demonstrated the outsized impact of hand-crafted noise/time discretization (e.g., the Karras ρ-schedule) on sample quality, highlighting the limitation of heuristic schedules that LD3 replaces with a learned discretization.

### 📊 Baseline

**DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Models** (2022)
- *Authors:* Cheng Lu et al.
- *Direct Connection:* DPM-Solver’s high-order ODE methods rely on fixed or heuristic timesteps, and LD3 directly plugs in by learning the timestep sequence to improve quality for a given NFE without retraining the score network.

**UniPC: A Unified Predictor-Corrector Framework for Fast Sampling of Diffusion Models** (2023)
- *Authors:* Chenyang Zhao et al.
- *Direct Connection:* UniPC’s performance is tightly coupled to the chosen discretization schedule, and LD3 provides a learned schedule that consistently boosts UniPC’s sampling efficiency across pretrained models.

### 🔧 Extension

**Pseudo Numerical Methods for Diffusion Models on Manifolds** (2022)
- *Authors:* Luping Liu et al.
- *Direct Connection:* By framing diffusion sampling as linear multistep numerical integration (PNDM), this work set up the discretization–solver interplay that LD3 extends by optimizing the time grid itself rather than only the solver coefficients.

---

## Synthesis: How Prior Work Led to This Paper

Score-based diffusion via SDEs established that sampling can be recast as integrating the probability flow ODE, making diffusion generation a numerical ODE problem whose accuracy depends on discretization. DDIM made this concrete by showing that deterministic diffusion sampling is an ODE with an explicit timestep schedule, implying that the placement of time points is a first-class design variable. Karras and colleagues then revealed that the particular choice of noise/time schedule (e.g., the ρ-parameterized sigma discretization) can dominate quality–efficiency trade-offs, but their schedules are heuristic. On the solver side, DPM-Solver introduced fast high-order ODE integrators specialized for diffusion ODEs, while UniPC unified predictor–corrector solvers; both report strong gains yet ultimately hinge on the chosen time grid. Earlier, PNDM cast diffusion sampling as a linear multistep method, illuminating how discretization and solver order interact to control error under a fixed NFE budget. Collectively, these works converged on a clear opportunity: solvers are strong and widely applicable, but their performance is bottlenecked by hand-crafted time discretizations. The natural next step is to directly learn the discretization of the diffusion ODE from pretrained models, keeping the solver and network fixed. LD3 synthesizes these insights by optimizing the timestep sequence itself—plug-and-play across DPM-Solver, UniPC, and related methods—thereby turning a key heuristic into a learned component that more efficiently allocates error across steps without retraining.

---

*Analysis generated on: 2026-01-06T11:44:11.758562*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

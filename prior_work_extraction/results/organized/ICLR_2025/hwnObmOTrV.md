# Prior Work Analysis Report

## Target Paper

**Title:** Modeling Complex System Dynamics with Flow Matching Across Time and Conditions

**Conference:** ICLR 2025 (spotlight)

**Authors:** Martin Rohbeck, Edward De Brouwer, Charlotte Bunne, Jan-Christian Huetter, Anne Biton, Kelvin Y. Chen, Aviv Regev, Romain Lopez

**Keywords:** Flow Matching, dynamical systems

**Abstract:** 
> Modeling the dynamics of complex real-world systems from temporal snapshot data is crucial for understanding phenomena such as gene regulation, climate change, and financial market fluctuations. Researchers have recently proposed a few methods based either on the Schroedinger Bridge or Flow Matching to tackle this problem, but these approaches remain limited in their ability to effectively combine data from multiple time points and different experimental settings. This integration is essential i...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Flow Matching for Generative Modeling** (2023)
- *Authors:* Lipman et al.
- *Direct Connection:* MMFM adopts the core flow-matching objective of regressing a neural vector field to the velocity of a constructed probability path, and generalizes it to simultaneously satisfy multiple time- and condition-marginal constraints.

**TrajectoryNet: A Dynamic Optimal Transport Network for Modeling Cellular Dynamics** (2020)
- *Authors:* Tong et al.
- *Direct Connection:* MMFM builds on the problem formulation of learning continuous-time dynamics from temporal snapshots introduced by TrajectoryNet, but replaces OT-based training with guided multi-marginal flow matching to integrate many time–condition marginals.

### 💡 Inspiration

**Stochastic Interpolants: Bridging the Gap Between Diffusion Models and Normalizing Flows** (2023)
- *Authors:* Albergo et al.
- *Direct Connection:* MMFM leverages the insight that one can choose smooth, user-defined interpolants and match their velocities; it instantiates this by using spline-based interpolations across time and experimental conditions.

**Classifier-Free Diffusion Guidance** (2021)
- *Authors:* Ho and Salimans
- *Direct Connection:* MMFM adopts the classifier-free guidance idea to guide conditional generation within the flow-matching framework, enabling strong conditioning without requiring an external classifier when some labels are dropped.

### 📊 Baseline

**Diffusion Schrödinger Bridge with Applications to Score-Based Models** (2021)
- *Authors:* De Bortoli et al.
- *Direct Connection:* MMFM addresses the limitations of SB-based approaches like DSB—which struggle to scalably fuse multiple time points and conditions—by replacing SB inference with multi-marginal, spline-defined flow matching.

### 🔧 Extension

**Conditional Flow Matching** (2023)
- *Authors:* Tong et al.
- *Direct Connection:* MMFM extends conditional flow matching by conditioning the vector field on both time and experimental settings and by integrating classifier-free guidance to remain robust when some time–condition pairs are missing.

---

## Synthesis: How Prior Work Led to This Paper

Flow matching established that a neural vector field can be learned by regressing the velocity of a chosen probability path, casting generative modeling as supervised learning on trajectories rather than likelihood maximization. Stochastic interpolants showed that this path can be any smooth, designer-chosen interpolant, decoupling training from a specific diffusion and enabling tailored trajectories whose velocities are easy to compute. Conditional flow matching further introduced conditioning the vector field on auxiliary variables so the learned dynamics reflect side information. In parallel, classifier-free diffusion guidance demonstrated that strong conditioning can be achieved by training with randomly dropped labels and guiding the conditional predictor at inference without an external classifier. On the snapshot-to-dynamics side, TrajectoryNet framed learning continuous-time vector fields from temporal snapshots via dynamic optimal transport, crystallizing the problem of reconstructing trajectories between marginal distributions observed at discrete times. Diffusion Schrödinger Bridge provided an alternative, SB-based route to connect given marginals by solving an entropic optimal transport inference problem through score-based diffusion processes.
Together, these works exposed a gap: SB and OT formulations struggled to scalably fuse many time points and experimental settings, while flow matching offered a flexible, supervision-style alternative if one could construct appropriate multi-marginal paths and condition robustly. The present work synthesizes these insights by defining smooth spline interpolants across time and conditions (from stochastic interpolants), training a conditional vector field with flow matching (from FM/CFM), and using classifier-free guidance to handle missing time–condition pairs, thereby delivering a practical multi-marginal flow that unifies disparate snapshots and settings.

---

*Analysis generated on: 2026-01-06T06:43:47.035831*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

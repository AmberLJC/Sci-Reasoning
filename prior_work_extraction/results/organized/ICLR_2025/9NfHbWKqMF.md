# Prior Work Analysis Report

## Target Paper

**Title:** SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yutong Chen, Marko Mihajlovic, Xiyi Chen, Yiming Wang, Sergey Prokudin, Siyu Tang

**Keywords:** Novel View Synthesis, Gaussian Splatting, Point cloud modeling

**Abstract:** 
> 3D Gaussian Splatting (3DGS) has recently transformed photorealistic reconstruction, achieving high visual fidelity and real-time performance. However, rendering quality significantly deteriorates when test views deviate from the camera angles used during training, posing a major challenge for applications in immersive free-viewpoint rendering and navigation. In this work, we conduct a comprehensive evaluation of 3DGS and related novel view synthesis methods under out-of-distribution (OOD) test ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**IBRNet: Learning Multi-View Image-Based Rendering** (2021)
- *Authors:* Qianqian Wang et al.
- *Direct Connection:* It established the generalizable NVS formulation of learning view synthesis by aggregating multi-view 3D neighborhoods, a setup the new approach recasts over explicit Gaussian primitives rather than per-ray samples.

### 💡 Inspiration

**Neural Point-Based Graphics** (2020)
- *Authors:* K. Aliev et al.
- *Direct Connection:* Showed that explicit point primitives with learned features can drive high-quality novel view synthesis, motivating an explicit, point-like representation—here Gaussians—paired with learned neighborhood reasoning.

### 🔍 Gap Identification

**RegNeRF: Regularizing Neural Radiance Fields for View Synthesis from Sparse Inputs** (2022)
- *Authors:* Michael Niemeyer et al.
- *Direct Connection:* By relying on handcrafted regularizers to cope with sparse views yet still struggling beyond the training camera distribution, it crystallized the need for a learned prior that can infer occluded content for OOD viewpoints.

### 📊 Baseline

**3D Gaussian Splatting for Real-Time Radiance Field Rendering** (2023)
- *Authors:* Bernhard Kerbl et al.
- *Direct Connection:* The method directly takes the 3DGS representation and renderer as its starting point—consuming an initial set of Gaussians optimized from limited views—and targets 3DGS’s well-known failure to extrapolate to unseen viewpoints.

### 🔧 Extension

**Point Transformer** (2021)
- *Authors:* Hengshuang Zhao et al.
- *Direct Connection:* The core network adapts Point Transformer’s vector attention and relative positional encoding to operate over Gaussian splat parameters (means, anisotropic covariances, opacities/SH), defining Gaussian-aware neighborhoods for learned aggregation.

### 🔗 Related Problem

**Point-NeRF: Point-based Neural Radiance Fields** (2022)
- *Authors:* Qiangeng Xu et al.
- *Direct Connection:* Demonstrated that point-anchored features with learned local aggregation improve view generalization, directly informing the choice to reason over explicit 3D point primitives—here specialized to Gaussian splats.

---

## Synthesis: How Prior Work Led to This Paper

Real-time novel view synthesis with explicit primitives surged with the introduction of 3D Gaussian Splatting, which optimizes anisotropic Gaussian splats and spherical harmonics and renders via differentiable splatting; yet it often leaves holes and view-dependent artifacts when extrapolating beyond the training camera manifold. IBRNet formalized generalizable view synthesis by learning to aggregate multi-view evidence in 3D, showing that learned local context can support view generalization across scenes. Point-NeRF extended this principle to explicit point anchors, where per-point features and localized aggregation improved robustness and efficiency relative to per-ray volumetric sampling. In parallel, Point Transformer introduced vector attention with relative positional encodings tailored to irregular 3D point sets, enabling powerful local-to-global reasoning over point neighborhoods. Earlier, Neural Point-Based Graphics established that explicit point primitives with learned features could achieve photorealistic rendering by conditioning on local neighborhoods, paving the way for point-centric learned renderers. Despite these advances, regularization-centric methods like RegNeRF demonstrated that hand-crafted priors for sparse inputs still falter when test views deviate substantially from training poses, underscoring the need for a stronger learned prior. Bringing these threads together, the new approach starts from a 3DGS initialization but replaces fixed regularization with a transformer that reasons directly over Gaussian splats. By adapting point-transformer attention to Gaussian-specific attributes (positions, anisotropic covariances, and appearance parameters), it learns to aggregate neighborhood evidence to refine or augment splats, filling unseen regions and stabilizing view extrapolation—an expected next step given prior successes of learned neighborhood aggregation and explicit point representations.

---

*Analysis generated on: 2026-01-06T19:58:49.598661*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

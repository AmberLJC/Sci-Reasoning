# Prior Work Analysis Report

## Target Paper

**Title:** DyST: Towards Dynamic Neural Scene Representations on Real-World Videos

**Conference:** ICLR 2024 (spotlight)

**Authors:** Maximilian Seitzer, Sjoerd van Steenkiste, Thomas Kipf, Klaus Greff, Mehdi S. M. Sajjadi

**Keywords:** neural scene representations, scene representations, representation learning, novel view synthesis

**Abstract:** 
> Visual understanding of the world goes beyond the semantics and flat structure of individual images. In this work, we aim to capture both the 3D structure and dynamics of real-world scenes from monocular real-world videos. Our Dynamic Scene Transformer (DyST) model leverages recent work in neural scene representation to learn a latent decomposition of monocular real-world videos into scene content, per-view scene dynamics, and camera pose. This separation is achieved through a novel co-training ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Neural Scene Representation and Rendering (GQN)** (2018)
- *Authors:* S. M. Ali Eslami et al.
- *Direct Connection:* DyST adopts the GQN-style context-to-query training objective and latent scene representation paradigm as the basis for learning to render novel views from observations.

**BARF: Bundle-Adjusting Neural Radiance Fields** (2021)
- *Authors:* Chen-Hsuan Lin et al.
- *Direct Connection:* DyST leverages BARF’s insight that camera poses can be learned jointly with neural rendering, but encodes pose as an explicit latent disentangled from content and dynamics to enable controllable generation.

### 💡 Inspiration

**D-NeRF: Neural Radiance Fields for Dynamic Scenes** (2021)
- *Authors:* Alberto Pumarola et al.
- *Direct Connection:* DyST generalizes D-NeRF’s key idea of separating canonical scene content from time-varying dynamics by replacing explicit deformation fields with a learned per-view dynamics latent that modulates rendering independently of content.

**NeRF in the Wild: Neural Radiance Fields for Unconstrained Photo Collections** (2021)
- *Authors:* Ricardo Martin-Brualla et al.
- *Direct Connection:* DyST adapts NeRF-W’s per-image latent concept—used to explain view-specific appearance/transients—into a per-view dynamics code that captures transient motion and view-dependent factors while keeping scene content stable.

### 🔍 Gap Identification

**Nerfies: Deformable Neural Radiance Fields** (2021)
- *Authors:* Keunhong Park et al.
- *Direct Connection:* DyST addresses Nerfies’ reliance on calibrated multi-view captures and explicit deformation modeling by learning camera and dynamics jointly from monocular real-world videos within a latent, transformer-based scene model.

### 📊 Baseline

**DynIBaR: Neural Dynamic Image-Based Rendering** (2023)
- *Authors:* Zhengqi Li et al.
- *Direct Connection:* Targeting dynamic novel view synthesis from casual monocular videos like DynIBaR, DyST replaces feature aggregation/warping with a learned latent scene representation that affords separate control over camera and scene dynamics.

### 🔧 Extension

**Scene Representation Transformer: Geometry-Free Novel View Synthesis through Set-Latent Scene Representations** (2022)
- *Authors:* Mehdi S. M. Sajjadi et al.
- *Direct Connection:* DyST directly extends SRT’s set-latent, transformer-based scene encoder–renderer by adding temporal conditioning and a factorized latent split into scene content, per-view dynamics, and camera pose to handle real-world dynamic videos.

---

## Synthesis: How Prior Work Led to This Paper

Transformer-based scene representation learning matured with the Scene Representation Transformer (SRT), which encodes a set of context views into a geometry-free latent and renders target views via attention, establishing a powerful encoder–renderer for generalizable view synthesis. Earlier, the Generative Query Network (GQN) introduced the context-to-query formulation and latent scene representations trained purely by novel-view supervision, laying the conceptual basis for learning to render from observations without explicit geometry. For dynamic scenes, D-NeRF proposed factoring a canonical content field from time-dependent deformation, while Nerfies operationalized deformable radiance fields but assumed calibrated multiview captures and explicit warping. NeRF in the Wild (NeRF-W) demonstrated that per-image latent codes can soak up view-specific effects and transients, suggesting a path to factor view-dependent phenomena from persistent scene content. BARF showed that camera parameters can be optimized jointly with neural rendering, revealing that pose can be treated as learnable variables within the rendering objective. Concurrently, DynIBaR tackled dynamic novel view synthesis from casual videos via feature aggregation and warping rather than an explicit latent scene model. Together, these works suggest combining a generalizable transformer-based scene encoder–renderer with principled factorization: persistent content separated from per-view dynamics and learnable camera. The limitations of deformable NeRFs (calibration dependence, explicit warps) and image-based renderers (lack of disentangled control) motivate a latent, factorized dynamic scene representation trained with a GQN/SRT-style objective and pose learning, naturally leading to DyST’s design and co-training strategy for real-world monocular videos.

---

*Analysis generated on: 2026-01-06T11:23:22.849419*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** ResFields: Residual Neural Fields for Spatiotemporal Signals

**Conference:** ICLR 2024 (spotlight)

**Authors:** Marko Mihajlovic, Sergey Prokudin, Marc Pollefeys, Siyu Tang

**Keywords:** neural fields, NeRF, reconstruction

**Abstract:** 
> Neural fields, a category of neural networks trained to represent high-frequency signals, have gained significant attention in recent years due to their impressive performance in modeling complex 3D data, such as signed distance (SDFs) or radiance fields (NeRFs), via a single multi-layer perceptron (MLP). However, despite the power and simplicity of representing signals with an MLP, these methods still face challenges when modeling large and complex temporal signals due to the limited capacity o...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis** (2020)
- *Authors:* Ben Mildenhall et al.
- *Direct Connection:* ResFields plugs its temporal residual layers into the NeRF-style coordinate-based MLP, inheriting NeRF’s field formulation to model time-varying radiance.

**DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation** (2019)
- *Authors:* Jeong Joon Park et al.
- *Direct Connection:* ResFields applies the same residual adaptation mechanism to SDF-based neural fields defined by DeepSDF, demonstrating seamless generalization beyond radiance fields.

### 💡 Inspiration

**Learning Multiple Visual Domains with Residual Adapters** (2017)
- *Authors:* Sylvestre-Alvise Rebuffi et al.
- *Direct Connection:* The idea of inserting small residual adapter modules to specialize a shared backbone across domains inspires ResFields’ per-time residual layers that adapt a shared field across timesteps.

### 🔍 Gap Identification

**Nerfies: Deformable Neural Radiance Fields** (2021)
- *Authors:* Keunhong Park et al.
- *Direct Connection:* Nerfies relies on a large shared deformation network and per-frame latents, whose escalating parameter demands motivate ResFields’ parameter-efficient temporal adapters.

**HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields** (2021)
- *Authors:* Keunhong Park et al.
- *Direct Connection:* HyperNeRF’s higher-dimensional representation highlights the growing complexity required for dynamic scenes, which ResFields mitigates with lightweight temporal residual layers.

### 📊 Baseline

**D-NeRF: Neural Radiance Fields for Dynamic Scenes** (2021)
- *Authors:* Albert Pumarola et al.
- *Direct Connection:* D-NeRF conditions a single MLP on time to model dynamics, and ResFields directly addresses this capacity bottleneck by replacing a monolithic time-conditioned MLP with a shared base plus time-specific residual layers.

### 🔧 Extension

**LoRA: Low-Rank Adaptation of Large Language Models** (2021)
- *Authors:* Edward J. Hu et al.
- *Direct Connection:* ResFields’ matrix factorization of temporal residual weights directly adapts LoRA’s low-rank update parameterization to neural field layers for parameter efficiency and generalization.

---

## Synthesis: How Prior Work Led to This Paper

Coordinate-based neural fields use a compact MLP to map spatial inputs to continuous signals, with NeRF demonstrating this for radiance and DeepSDF for signed distance functions. To capture dynamics, D-NeRF extends this paradigm by conditioning the MLP on time, while Nerfies introduces a deformation network and per-frame latents to canonicalize motion, and HyperNeRF further enlarges representational capacity via a higher-dimensional embedding to handle topology changes. These dynamic-field approaches show that modeling complex temporal variation with a single shared MLP often strains capacity and inflates parameters or architectural complexity. In parallel, residual adapters insert small residual modules into backbones to specialize them to new domains with minimal overhead, and LoRA shows that weight updates can be parameterized as low-rank matrices, retaining performance while dramatically reducing trainable parameters. Together, these lines suggest a path: preserve a shared neural field for spatiotemporal structure, while adding lightweight, per-time specialization in a parameter-efficient form. Building on this, ResFields introduces temporal residual layers that adapt a shared base neural field across timesteps, directly addressing the capacity limitations seen in time-conditioned or deformation-heavy dynamic fields. By factorizing these residual weights in a LoRA-style low-rank manner, the method controls parameter growth and improves generalization, and because it is formulated at the network-layer level, it integrates seamlessly with both NeRF and DeepSDF formulations.

---

*Analysis generated on: 2026-01-06T23:44:30.618955*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

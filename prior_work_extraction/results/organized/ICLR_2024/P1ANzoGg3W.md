# Prior Work Analysis Report

## Target Paper

**Title:** H2O-SDF: Two-phase Learning for 3D Indoor Reconstruction using Object Surface Fields

**Conference:** ICLR 2024 (spotlight)

**Authors:** Minyoung Park, Mirae Do, Yeon Jae Shin, Jaeseok Yoo, Jongkwang Hong, Joongrock Kim, Chul Lee

**Keywords:** 3D reconstruction, Neural implicit surface learning

**Abstract:** 
> Advanced techniques using Neural Radiance Fields (NeRF), Signed Distance Fields (SDF), and Occupancy Fields have recently emerged as solutions for 3D indoor scene reconstruction. We introduce a novel two-phase learning approach, H2O-SDF,  that discriminates between object and non-object regions within indoor environments. This method achieves a nuanced balance, carefully preserving the geometric integrity of room layouts while also capturing intricate surface details of specific objects. A corne...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**VolSDF: Volume Rendering of Signed Distance Functions for Surface Reconstruction** (2021)
- *Authors:* Ronen Yariv et al.
- *Direct Connection:* H2O-SDF adopts the SDF-to-density mapping and differentiable volume rendering formulation of VolSDF as the underlying surface-learning framework that its two-phase scheme and OSF are built upon.

**Implicit Geometric Regularization for Learning Shapes** (2020)
- *Authors:* Amos Gropp et al.
- *Direct Connection:* H2O-SDF uses the IGR eikonal regularization to maintain SDF properties while augmenting training with OSF to concentrate gradients near object surfaces.

### 💡 Inspiration

**Object-NeRF: Towards Object-Compositional Neural Radiance Fields** (2021)
- *Authors:* Guangyang Yang et al.
- *Direct Connection:* By decomposing scenes into object and background components, Object-NeRF provided the conceptual cue for H2O-SDF’s explicit separation of object vs. non-object regions realized through a two-phase SDF learning scheme.

### 🔍 Gap Identification

**MonoSDF: Exploring Monocular Geometric Cues for Neural Implicit Surface Reconstruction** (2023)
- *Authors:* Zehao Yu et al.
- *Direct Connection:* MonoSDF shows that even with extra geometric cues, SDF-based reconstructions struggle with fine object details in indoor scenes, a limitation H2O-SDF addresses through OSF-driven gradient concentration and object-focused training.

**Neuralangelo: High-Fidelity Neural Implicit Surfaces from Video** (2023)
- *Authors:* Zhengqi Li et al.
- *Direct Connection:* Neuralangelo highlights the need for mechanisms that preserve high-frequency surface detail, which H2O-SDF pursues in indoor scenes via an Object Surface Field that counteracts vanishing gradients near fine object geometry.

### 🔧 Extension

**NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction** (2021)
- *Authors:* Weihao Zhang et al.
- *Direct Connection:* H2O-SDF directly builds on NeuS-style SDF rendering and explicitly tackles the vanishing gradient/over-smoothing behavior observed in NeuS by introducing an Object Surface Field and a two-phase training schedule.

### 🔗 Related Problem

**UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction** (2021)
- *Authors:* Michael Oechsle et al.
- *Direct Connection:* UNISURF’s analysis of occupancy- versus SDF-based supervision and its surface-focused rendering motivates H2O-SDF’s choice of an SDF framework and the need to sharpen gradients to recover high-frequency geometry.

---

## Synthesis: How Prior Work Led to This Paper

VolSDF established a principled way to map signed distance values to volumetric densities, enabling surface-accurate rendering and supervision within an SDF framework. NeuS refined SDF volume rendering and exposed a practical training recipe, while also revealing a tendency toward vanishing gradients and over-smoothed geometry away from the zero level set. IGR introduced eikonal regularization to enforce valid signed distance geometry and popularized near-surface sampling to stabilize SDF learning. UNISURF analyzed the trade-offs between occupancy- and SDF-based formulations and advocated surface-focused rendering to better localize geometry. MonoSDF injected monocular depth/normal cues into SDF learning, improving indoor reconstructions but still leaving high-frequency object details under-recovered. Complementarily, Object-NeRF demonstrated that decomposing scenes into object and background components can disentangle geometry and appearance, suggesting architectural and training strategies that treat object regions differently for finer reconstructions. Neuralangelo, targeting high-fidelity geometry, further underscored the broader challenge of retaining high-frequency detail in neural implicit surfaces. Together these works crystalized a gap: SDF-based renderers excel at clean surfaces and global structure but struggle to balance large, planar room layouts with intricate object detail due to gradient sparsity near fine-scale geometry. H2O-SDF synthesizes these insights by retaining SDF rendering and eikonal regularization, explicitly separating object and non-object regions as inspired by object-compositional fields, and introducing an Object Surface Field with a two-phase training schedule to concentrate learning signals where objects require high-frequency detail while preserving the integrity of room layouts.

---

*Analysis generated on: 2026-01-06T13:52:21.084703*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

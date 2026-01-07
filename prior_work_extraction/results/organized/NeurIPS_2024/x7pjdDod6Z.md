# Prior Work Analysis Report

## Target Paper
**Title:** x7pjdDod6Z
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MeshFormer’s core innovation—high-quality mesh reconstruction from sparse views via an explicitly 3D-guided model—emerges by unifying advances across representation, supervision, and priors. Early generalizable reconstruction methods (pixelNeRF) established the sparse-view, open-world setting but suffered from weak 3D inductive bias. MVSNeRF demonstrated that building and processing 3D volumes with projective geometry cues yields stronger generalization, while NSVF showed that sparse voxel representations can efficiently capture 3D structure. MeshFormer synthesizes these ideas by storing learnable features in sparse 3D voxels and processing them with 3D convolutions augmented by transformers, explicitly injecting 3D and projective bias. In parallel, SDF-based surface rendering (NeuS) revealed that coupling SDF learning with differentiable surface rendering yields cleaner, watertight meshes—guiding MeshFormer’s choice to supervise SDFs while rendering surfaces directly. To overcome the ill-posedness of sparse-view geometry, MonoSDF showed that monocular depth/normal priors provide powerful constraints for SDF optimization; MeshFormer operationalizes this further by requiring normal maps as inputs and outputs. Finally, the practicality of obtaining high-quality normal maps from 2D diffusion models (as enabled by ControlNet-like conditioning) makes normal-guided reconstruction scalable and robust. The combination of an explicitly 3D voxel backbone, surface-oriented SDF rendering, and diffusion-predicted normal guidance thus directly addresses the training cost, generalization, and mesh quality limitations of triplane-based and purely volumetric predecessors (e.g., EG3D), culminating in MeshFormer.

---
*Generated: 2026-01-06T23:39:42.971609*

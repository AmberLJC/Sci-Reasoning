# Prior Work Analysis Report

## Target Paper
**Title:** xZxXNhndXU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

4DGF sits at the confluence of high-speed explicit rasterization, dynamic 4D modeling, large-scale scene decomposition, and robust appearance handling. The shift from volumetric ray marching to rasterization with Gaussian primitives in 3D Gaussian Splatting established the core efficiency and quality envelope that 4DGF inherits for interactive rendering. Extending Gaussians into time, 4D Gaussian Splatting demonstrated that dynamic content can be captured by temporally varying or deformable primitives; 4DGF generalizes this to the urban regime by replacing per-primitive motion with a scene-graph that organizes static infrastructure and dynamic actors at global scale.
Work on scaling NeRFs to cities—Block-NeRF and Mega-NeRF—showed that partitioning, composition, and large-batch training strategies are essential for thousands of frames and unbounded extents. 4DGF integrates these lessons operationally via a global scene graph and an efficient Gaussian scaffold that keeps memory and rendering costs tractable.
Heterogeneous imagery across weather, season, and lighting is addressed by decoupling geometry from appearance. NeRF in the Wild introduced appearance embeddings and transient components to model such variability; K-Planes further showed that compact, factorized neural fields can represent space–time–appearance efficiently. 4DGF synthesizes these ideas by storing geometry in Gaussians while predicting appearance from a lightweight neural field conditioned on view and scene factors. Finally, deformation-based dynamic NeRFs (D-NeRF) motivate the general 4D formulation that 4DGF achieves more scalably with a scene-graph-driven dynamic integration suited to complex urban environments.

---
*Generated: 2026-01-06T23:33:35.582015*

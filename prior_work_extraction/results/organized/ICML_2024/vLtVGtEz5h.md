# Prior Work Analysis Report

## Target Paper
**Title:** vLtVGtEz5h
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Sliced and Radon Wasserstein Barycenters of Measures** (2015)
- *Authors:* Bonneel et al.
- *Connection:* Established the sliced/Radon-Wasserstein paradigm—reducing high-dimensional OT to 1D projections via (generalized) Radon transforms—which S3W ports to spherical data through stereographic projection.

**The Radon Cumulative Distribution Transform and its Inverse** (2018)
- *Authors:* Park et al.
- *Connection:* Provided the distribution-transform viewpoint grounded in Radon geometry for probability measures, a key mathematical toolset S3W leverages when formulating spherical slicing via stereographic projection and correcting projection-induced distortions.

### 💡 Inspiration

**Max-Sliced Wasserstein Distance** (2019)
- *Authors:* Deshpande et al.
- *Connection:* Optimizing over projection directions to induce invariances/robustness in sliced OT inspired S3W’s rotationally invariant variant, which optimizes over rotations to remove orientation dependence on the sphere.

### 🔍 Gap Identification

**A Newton Algorithm for Semi-Discrete Optimal Transport** (2019)
- *Authors:* Kitagawa et al.
- *Connection:* Represents state-of-the-art but computationally heavy OT on manifolds (including spherical settings); S3W is explicitly motivated as a fast, highly parallelizable alternative to such semi-discrete spherical OT solvers.

### 📊 Baseline

**Manifold Sliced Wasserstein Distance** (2022)
- *Authors:* Nguyen et al.
- *Connection:* Formulated sliced OT directly on Riemannian manifolds; S3W targets the sphere specifically and improves computational efficiency by flattening via stereographic projection and analytically correcting distortion.

### 🔧 Extension

**Generalized Sliced Wasserstein Distances** (2019)
- *Authors:* Kolouri et al.
- *Connection:* Introduced the use of generalized Radon transforms and non-linear projections to define sliced OT variants; S3W adopts this generalized slicing framework and adapts it to spherical measures through a stereographic map.

---

## Synthesis

S3W’s core innovation—fast, parallelizable sliced Wasserstein distances for spherical distributions via stereographic projection with explicit distortion correction—sits squarely on the intellectual lineage of sliced optimal transport and Radon-based formulations. Bonneel et al. (2015) provided the foundational blueprint: approximate high-dimensional OT by integrating 1D Wasserstein distances over projected views, tightly linked to the Radon transform. Kolouri et al. (2019) generalized this paradigm to non-linear and generalized Radon transforms, a crucial step S3W builds upon to define spherical slicing after mapping the sphere to Euclidean space. Park et al. (2018) further grounded the use of Radon-style transforms for probability measures, informing S3W’s transform-driven perspective and facilitating principled distortion handling.

On the application side, existing spherical OT solvers—typified by semi-discrete Newton methods (Kitagawa et al., 2019)—deliver accurate geodesic-cost OT but remain computationally heavy; S3W explicitly addresses this gap with a highly parallel slicing pipeline. Moreover, ideas from max-sliced Wasserstein (Deshpande et al., 2019)—optimizing over directions to induce invariances—directly inspire S3W’s rotationally invariant variant, which minimizes dependence on a chosen orientation. Finally, manifold sliced Wasserstein (Nguyen et al., 2022) offers a direct baseline for doing sliced OT on manifolds; S3W specializes to spheres and achieves speed by stereographically flattening the geometry and analytically compensating for the conformal distortion. Together, these works directly enabled S3W’s formulation and motivated its efficiency and invariance properties.

---
*Generated: 2026-01-06T23:09:26.446609*

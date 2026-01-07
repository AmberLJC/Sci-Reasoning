# Prior Work Analysis Report

## Target Paper

**Title:** Ghost on the Shell: An Expressive Representation of General 3D Shapes

**Conference:** ICLR 2024 (oral)

**Authors:** Zhen Liu, Yao Feng, Yuliang Xiu, Weiyang Liu, Liam Paull, Michael J. Black, Bernhard Schölkopf

**Keywords:** Non-watertight mesh; generative model; 3D geometry; differentiable rendering

**Abstract:** 
> The creation of photorealistic virtual worlds requires the accurate modeling of 3D surface geometry for a wide range of objects. For this, meshes are appealing since they enable 1) fast physics-based rendering with realistic material and lighting, 2) physical simulation, and 3) are memory-efficient for modern graphics pipelines. Recent work on reconstructing and statistically modeling 3D shape, however, has critiqued meshes as being topologically inflexible. To capture a wide range of object sha...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation** (2019)
- *Authors:* Jeong Joon Park et al.
- *Direct Connection:* The use of signed distance fields as a continuous shape representation is adopted and reinterpreted by moving the SDF domain to a surface manifold, enabling the SDF machinery to model non-watertight, thin structures.

**Occupancy Networks: Learning 3D Reconstruction in Function Space** (2019)
- *Authors:* Lars Mescheder et al.
- *Direct Connection:* This work established neural implicit functions for generative 3D modeling but inherently produced watertight surfaces, a formulation that the new method keeps (function-space modeling) while removing the watertightness constraint via manifold parameterization.

### 💡 Inspiration

**AtlasNet: A Papier-Mâché Approach to Learning 3D Surface Generation** (2018)
- *Authors:* Thibault Groueix et al.
- *Direct Connection:* The idea of parameterizing complex surfaces via learnable manifolds directly inspired defining a scalar field on a watertight manifold so that open-surface “islands” can be generated while remaining compatible with mesh rendering.

### 🔍 Gap Identification

**Neural Unsigned Distance Fields for Implicit Surface Reconstruction** (2020)
- *Authors:* Julian Chibane et al.
- *Direct Connection:* By showing that unsigned distance fields can capture open, thin surfaces yet are hard to integrate with material-aware mesh rendering or unconditional generation, this work exposes the gap the manifold-SDF addresses.

### 📊 Baseline

**GET3D: A Generative Model of High Quality 3D Textured Shapes Learned from Images** (2022)
- *Authors:* Jun Gao et al.
- *Direct Connection:* As a leading generative model that outputs textured, renderable meshes but only watertight topology, it serves as the main baseline the new representation aims to generalize to non-watertight, open surfaces.

### 🔗 Related Problem

**PolyGen: An Autoregressive Generative Model of 3D Meshes** (2020)
- *Authors:* Charlie Nash et al.
- *Direct Connection:* This mesh-autoregressive approach demonstrated generation of non-watertight polygonal geometry, motivating a representation that preserves mesh compatibility while offering a learnable, geometry-regularized field on a manifold.

---

## Synthesis: How Prior Work Led to This Paper

DeepSDF formalized signed distance fields as continuous, learnable shape representations whose isosurfaces yield clean geometry, while Occupancy Networks popularized function-space modeling for 3D reconstruction and unconditional shape generation; both, however, intrinsically favored watertight surfaces. AtlasNet showed that complex shapes can be parameterized via learnable surface manifolds (atlases), demonstrating that mapping from low-dimensional, surface-aligned coordinates to 3D geometry can flexibly realize open structures. In contrast, Neural Unsigned Distance Fields established that unsigned distances capture thin and open surfaces from image/point inputs, but their volumetric formulations and extraction procedures complicate material-aware mesh rendering and unconditional generative modeling. GET3D advanced generative modeling of textured, physically renderable meshes at high quality, yet its outputs remain watertight and thus struggle with thin, open geometries. PolyGen provided a route to non-watertight meshes through autoregressive polygon generation, but lacked the geometric regularity and rendering-friendly structure afforded by field-based representations anchored to surfaces.
Taken together, these works revealed a clear opportunity: retain the renderability and generative strengths of mesh- and field-based methods while breaking the watertight constraint to express open surfaces. The natural synthesis is to transplant the SDF concept onto a learned watertight manifold, borrowing AtlasNet’s surface-parameterization insight and UDF’s open-surface capability, and to integrate it into a mesh-compatible pipeline as exemplified by GET3D’s material-aware rendering. This manifold SDF yields open-surface “islands” anchored to a shell, unifying expressive geometry with fast, differentiable rendering and enabling unconditional generative modeling of general 3D shapes.

---

*Analysis generated on: 2026-01-06T14:05:31.330612*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

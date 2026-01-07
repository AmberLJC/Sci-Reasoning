# Prior Work Analysis Report

## Target Paper

**Title:** TetSphere Splatting: Representing High-Quality Geometry with Lagrangian Volumetric Meshes

**Conference:** ICLR 2025 (oral)

**Authors:** Minghao Guo, Bohan Wang, Kaiming He, Wojciech Matusik

**Keywords:** geometry representation, 3D modeling

**Abstract:** 
> We introduce TetSphere Splatting, a Lagrangian geometry representation designed for high-quality 3D shape modeling. TetSphere splatting leverages an underused yet powerful geometric primitive -- volumetric tetrahedral meshes. It represents 3D shapes by deforming a collection of tetrahedral spheres, with geometric regularizations and constraints that effectively resolve common mesh issues such as irregular triangles, non-manifoldness, and floating artifacts. Experimental results on multi-view and...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction** (2021)
- *Authors:* Wang et al.
- *Direct Connection:* NeuS formalized surface-consistent volume rendering for multi-view reconstruction, providing the reconstruction objective that TetSphere adopts while addressing NeuS’s common mesh extraction issues (floaters, non-manifoldness) via explicit tetrahedral volumetric meshes.

### 💡 Inspiration

**3D Gaussian Splatting for Real-Time Radiance Field Rendering** (2023)
- *Authors:* Kerbl et al.
- *Direct Connection:* The paper’s core idea of optimizing a set of deformable, local primitives via differentiable splatting is directly inspired by 3D Gaussian Splatting, which established the efficiency and stability of Lagrangian primitive-based optimization and rendering.

### 🔍 Gap Identification

**SDF-GS: 3D Gaussian Splatting for High-Quality Surface Reconstruction via Signed Distance Fields** (2024)
- *Authors:* Zhang et al.
- *Direct Connection:* By attaching SDFs to Gaussian primitives, SDF-GS explicitly sought better surfaces but still struggled with manifoldness and floating artifacts, motivating TetSphere’s move to tetrahedral volumetric primitives with built-in geometric constraints.

### 📊 Baseline

**nvdiffrec: Neural 3D Reconstruction with Differentiable Rendering** (2022)
- *Authors:* Munkberg et al.
- *Direct Connection:* As a leading mesh-based inverse rendering baseline, nvdiffrec’s use of mesh regularizers and photometric objectives frames the reconstruction setting that TetSphere targets while improving mesh manifoldness and eliminating floaters through a volumetric Lagrangian parameterization.

**DreamGaussian: Generative 3D Using Gaussian Splatting** (2023)
- *Authors:* Tang et al.
- *Direct Connection:* DreamGaussian showed how splatting primitives can drive text/image-to-3D generation but produces weak or post-hoc meshing, which TetSphere directly improves by using tetrahedral volumetric primitives that enforce high-quality, watertight meshes in generative settings.

### 🔧 Extension

**DMTet: Deformable Meshes using Tetrahedral Grids** (2021)
- *Authors:* Shen et al.
- *Direct Connection:* TetSphere extends the DMTet insight that volumetric tetrahedral parameterizations yield high-quality meshes by replacing fixed grids with deformable tetrahedral ‘spheres’ and adding geometric constraints to overcome grid bias, irregular triangles, and non-manifold artifacts.

---

## Synthesis: How Prior Work Led to This Paper

3D Gaussian Splatting demonstrated that optimizing a set of localized primitives with differentiable splatting yields fast, stable inverse rendering and opened a path to primitive-centric scene representations. DMTet showed that parameterizing geometry volumetrically with tetrahedral elements enables robust, high-quality mesh extraction and differentiable optimization, but its fixed grid introduces bias and occasional irregular or non-manifold output. nvdiffrec established mesh-based inverse rendering as a practical baseline, coupling photometric objectives with mesh regularizers, yet relied on triangle parameterizations that can tangle or spawn floaters. NeuS introduced a surface-consistent volume rendering formulation for multi-view reconstruction, producing accurate surfaces but still suffering from floaters and non-manifold artifacts at extraction time. DreamGaussian transferred splatting primitives into text/image-to-3D pipelines, proving scalability for generative modeling but relying on post-hoc meshing or producing weak geometry. SDF-GS fused SDF estimation with Gaussian primitives to improve surface fidelity, yet its surfel-like primitives made manifoldness and floating artifacts difficult to control. Together, these works suggested that splatting-based Lagrangian optimization is powerful, volumetric tetrahedra produce cleaner meshes, and current primitive choices or implicit-to-mesh conversions limit manifoldness and regularity. The natural next step is to combine splatting’s optimization and rendering pipeline with an explicitly volumetric, deformable primitive: tetrahedralized spheres. By adopting Lagrangian volumetric meshes and adding geometric regularizations and constraints, the current work integrates the strengths of splatting and tetrahedra while directly addressing grid bias, irregular triangles, non-manifoldness, and floaters, and it slots cleanly into both reconstruction and generative modeling pipelines.

---

*Analysis generated on: 2026-01-06T14:08:01.379982*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

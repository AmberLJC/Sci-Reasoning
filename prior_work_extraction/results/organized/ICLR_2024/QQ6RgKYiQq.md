# Prior Work Analysis Report

## Target Paper

**Title:** MovingParts: Motion-based 3D Part Discovery in Dynamic Radiance Field

**Conference:** ICLR 2024 (spotlight)

**Authors:** Kaizhi Yang, Xiaoshuai Zhang, Zhiao Huang, Xuejin Chen, Zexiang Xu, Hao Su

**Keywords:** NeRF, Dynamic, Motion, Part discovery

**Abstract:** 
> We present MovingParts, a NeRF-based method for dynamic scene reconstruction and part discovery. We consider motion as an important cue for identifying parts, that all particles on the same part share the common motion pattern. From the perspective of fluid simulation, existing deformation-based methods for dynamic NeRF can be seen as parameterizing the scene motion under the Eulerian view, i.e., focusing on specific locations in space through which the fluid flows as time passes. However, it is...

---

## Key Prior Works (7 papers with direct influence)

### 💡 Inspiration

**Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes** (2021)
- *Authors:* Zhengqi Li et al.
- *Direct Connection:* NSFF introduces 3D scene flow with forward–backward consistency for dynamic view synthesis, inspiring our motion-centric formulation and cycle constraints to recover coherent trajectories that can be grouped into parts.

**SE3-NETS: Learning Rigid Body Motion using Deep Neural Networks** (2017)
- *Authors:* Arun M. Byravan et al.
- *Direct Connection:* SE3-Nets showed that grouping points by shared SE(3) motion yields unsupervised rigid part segmentation, directly motivating our factorization of dynamic radiance fields into part-level rigid motions.

### 🔍 Gap Identification

**D-NeRF: Neural Radiance Fields for Dynamic Scenes** (2021)
- *Authors:* Albert Pumarola et al.
- *Direct Connection:* D-NeRF frames motion as a deformation field indexed by spatial locations (Eulerian), whose inability to expose object- or part-level motions is the explicit limitation we address with a Lagrangian parameterization of trajectories.

**HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields** (2021)
- *Authors:* Keunhong Park et al.
- *Direct Connection:* HyperNeRF remains an Eulerian deformation formulation even while handling topology changes, underscoring the difficulty of extracting rigid parts from per-location warps and motivating our alternative Lagrangian view.

### 📊 Baseline

**Nerfies: Deformable Neural Radiance Fields** (2021)
- *Authors:* Keunhong Park et al.
- *Direct Connection:* As a main baseline, Nerfies models dynamics via an Eulerian warp from a canonical template, which our method contrasts by adding a Lagrangian particle-tracking view and enforcing Eulerian–Lagrangian cycle consistency to enable part discovery.

### 🔗 Related Problem

**A-NeRF: Articulated Neural Radiance Fields for Learning Human Shape, Appearance, and Pose** (2021)
- *Authors:* Shih-Yang Su (Peng) et al.
- *Direct Connection:* A-NeRF demonstrates that part-wise SE(3)/LBS warps enable controllable articulated NeRFs when skeletal parts are known, a supervised prerequisite our method removes by discovering those parts from motion cues alone.

**BANMo: Building Animatable 3D Neural Models from Many Casual Videos** (2022)
- *Authors:* Jiaru Zhang et al.
- *Direct Connection:* BANMo builds animatable neural models by tracking correspondences across time (a Lagrangian intuition), which we bring into dynamic NeRFs via particle trajectories and Eulerian–Lagrangian cycle consistency for part discovery.

---

## Synthesis: How Prior Work Led to This Paper

Deformable NeRF methods such as Nerfies parameterize dynamics by learning a warp from a canonical template to each frame, embedding motion in an Eulerian field tied to spatial locations; D-NeRF similarly models non-rigid motion as a per-voxel deformation, reinforcing the view that dynamics are best captured as canonical-to-observation warps. HyperNeRF extends this paradigm to topological changes by lifting into higher dimensions yet still retains an Eulerian, per-location representation. In contrast, Neural Scene Flow Fields explicitly estimates 3D scene flow with forward–backward consistency, showing that accurate motion cues and cycle constraints can stabilize dynamic view synthesis. Beyond radiance fields, SE3-Nets demonstrated that grouping points by consistent SE(3) transforms yields unsupervised rigid part segmentation, establishing the principle that “shared motion defines parts.” Articulated NeRFs such as A-NeRF validated the power of part-wise rigid warps for controllability, albeit requiring known skeletal structure. BANMo further emphasized a Lagrangian perspective by tracking correspondences across time to build animatable models from casual videos.
Taken together, these works reveal a gap: Eulerian deformation fields excel at novel view synthesis but obscure object- and part-level motion, while motion-centric and articulated methods suggest that tracking trajectories and factoring rigid motions are key to discovering parts. The natural next step is to fuse these insights by introducing a Lagrangian particle-tracking view alongside the Eulerian warp and enforcing cycle consistency between them, then factorizing motion into per-part rigid components to obtain interpretable, motion-driven part discovery within a dynamic NeRF.

---

*Analysis generated on: 2026-01-06T17:59:57.923729*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

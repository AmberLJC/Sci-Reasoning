# Prior Work Analysis Report

## Target Paper

**Title:** EmbodiedSAM: Online Segment Any 3D Thing in Real Time

**Conference:** ICLR 2025 (oral)

**Authors:** Xiuwei Xu, Huangxing Chen, Linqing Zhao, Ziwei Wang, Jie Zhou, Jiwen Lu

**Keywords:** 3d instance segmentation; online 3d scene segmentation

**Abstract:** 
> Embodied tasks require the agent to fully understand 3D scenes simultaneously with its exploration, so an online, real-time, fine-grained and highly-generalized 3D perception model is desperately needed. Since high-quality 3D data is limited, directly training such a model in 3D is infeasible. Meanwhile, vision foundation models (VFM) has revolutionized the field of 2D computer vision with superior performance, which makes the use of VFM to assist embodied 3D perception a promising direction. Ho...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Fusion++: Volumetric Object-Level SLAM** (2018)
- *Authors:* McCormac et al.
- *Direct Connection:* Introduces the online object-level map representation and per-instance TSDF fusion pipeline that the method adopts while replacing category-specific detectors with SAM masks and adding fast streaming association.

**MaskFusion: Real-Time Recognition, Tracking and Reconstruction of Multiple Moving Objects** (2018)
- *Authors:* Rünz et al.
- *Direct Connection:* Demonstrates real-time RGB-D instance-aware SLAM by fusing per-frame 2D instance masks into 3D and highlights the need for robust mask-to-object association that the new work redesigns for streaming with SAM.

### 💡 Inspiration

**Segment Anything** (2023)
- *Authors:* Kirillov et al.
- *Direct Connection:* Provides the promptable, high-quality 2D mask generator that is leveraged per RGB frame to obtain category-agnostic instance masks without 3D supervision, enabling the core lift-to-3D pipeline.

### 🔍 Gap Identification

**OpenScene: 3D Scene Understanding with Open Vocabularies** (2023)
- *Authors:* Peng et al.
- *Direct Connection:* Shows that lifting 2D vision-language/foundation model features into 3D yields open-vocabulary segmentation but operates offline and slowly, motivating an online, real-time VFM-to-3D alternative.

### 📊 Baseline

**OpenMask3D: Open-Vocabulary 3D Instance Segmentation** (2023)
- *Authors:* Schult et al.
- *Direct Connection:* Aggregates 2D masks across views to form 3D instances with open-vocabulary labels, establishing a primary baseline whose multi-view batch processing and latency the new method addresses with streaming fusion.

### 🔧 Extension

**Point-Anything: Segment Anything You Want in 3D Point Clouds** (2023)
- *Authors:* Li et al.
- *Direct Connection:* Back-projects SAM masks to point clouds and enforces multi-view consistency for 3D instance formation, a technique that is adapted to incremental RGB-D streaming with efficient inter-frame matching.

---

## Synthesis: How Prior Work Led to This Paper

Promptable mask generation with category-agnostic generalization emerged with Segment Anything, which delivers high-quality 2D instance masks from single images via flexible prompts. In parallel, online object-centric mapping advanced through Fusion++, which established per-instance TSDF volumes and maintained an object-level map while ingesting frame-by-frame detector outputs. MaskFusion further proved that fusing 2D instance masks into a real-time RGB-D SLAM pipeline is feasible, underscoring the central difficulty of associating transient 2D masks with persistent 3D objects across frames. As vision foundation models matured, OpenScene demonstrated that lifting 2D VLM/VFM features into 3D enables open-vocabulary recognition, but its offline, multi-view processing limited applicability to embodied, time-critical settings. OpenMask3D extended this theme to 3D instance segmentation by aggregating 2D masks across views for open-vocabulary 3D instances, yet relied on batch multi-view inputs and incurred high latency. Point-Anything showed a practical recipe to back-project SAM masks to point clouds and fuse multi-view evidence to form 3D instances, illustrating how SAM can be exploited in 3D via geometric consistency.
Building on these insights, a natural gap appears: object-level, online mapping pipelines rely on task-specific detectors, while VFM-based 3D methods are offline and slow. The synthesis is to combine SAM’s promptable 2D masks with Fusion++/MaskFusion-style incremental fusion, adopting Point-Anything’s back-projection and multi-view consistency but redesigning association to operate causally per frame. This resolves the tension between generalization and latency by performing efficient mask-to-object matching and real-time 3D integration without future frames.

---

*Analysis generated on: 2026-01-06T19:02:42.801595*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

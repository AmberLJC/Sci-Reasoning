# Prior Work Analysis Report

## Target Paper
**Title:** 7ieZWCc7rB
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

OpenBox’s core innovation—a two-stage, open-vocabulary 3D box annotation pipeline without iterative self-training—stands on three converging threads of prior work. First, open-vocabulary 2D foundations such as Grounding DINO and SAM provide robust, category-flexible instance cues from images. These models enable OpenBox to retrieve instance masks and text-conditioned detections at scale, seeding reliable proposals and labels without task-specific retraining. Second, recent 2D-to-3D transfer methods like OpenScene demonstrate how to project and fuse multi-view 2D vision-language signals into 3D. OpenBox leverages this paradigm in Stage 1, performing context-aware association of 2D instances to point clouds and refining them with scene consistency rather than the multi-round pseudo-labeling typical in self-training pipelines like ST3D. Third, classical 2D-driven 3D detection and temporal reasoning inform OpenBox’s Stage 2. Frustum PointNets established lifting 2D detections into 3D search regions and employing class-wise size priors; OpenBox generalizes this with open-vocabulary class-specific size statistics and adaptive box shapes. Complementarily, motion modeling from 3D tracking (e.g., AB3DMOT) motivates categorizing instances by rigidity and motion state, allowing OpenBox to tailor box generation to dynamic versus static objects. Together, these strands yield a single-pass, foundation-model-guided pipeline that produces high-quality, open-vocabulary 3D bounding boxes while avoiding the computational overhead and error accumulation of iterative self-training.

---
*Generated: 2026-01-06T23:42:48.154672*

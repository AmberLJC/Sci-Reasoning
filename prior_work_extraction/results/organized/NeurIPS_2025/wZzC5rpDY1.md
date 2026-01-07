# Prior Work Analysis Report

## Target Paper
**Title:** wZzC5rpDY1
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

MonoLift’s core idea—training a monocular RGB policy to perform 3D-aware manipulation by distilling knowledge from a depth-guided teacher—sits at the intersection of distillation, privileged-information RL, and 3D manipulation. At the action level, MonoLift inherits the principle of transferring behavior from a competent teacher to a compact student from Policy Distillation, ensuring the RGB student replicates the teacher’s control decisions. The general teacher–student framework and the use of softened supervision are rooted in classic Knowledge Distillation, which MonoLift extends to robotics with additional spatial and temporal alignment. Critically, its spatial distillation directly follows Cross-Modal Distillation: depth encodes geometry that is difficult to infer from RGB, and transferring depth-informed features into RGB backbones provides 3D inductive bias without test-time depth. The training-time use of extra modalities echoes Asymmetric Actor–Critic approaches to privileged information, but MonoLift operationalizes this via an explicit tri-level KD objective so the student needs only monocular input at deployment. Finally, advances in depth-guided 3D manipulation policies, such as PerAct’s voxelized RGB-D perception and 3D Diffusion Policy’s spatiotemporal structure, motivate MonoLift’s choice of a depth-aware teacher: these works demonstrate the performance benefits of explicit 3D reasoning, which MonoLift captures through spatial, temporal, and policy distillation while avoiding the runtime cost of depth estimation or additional sensors.

---
*Generated: 2026-01-07T00:21:32.235815*

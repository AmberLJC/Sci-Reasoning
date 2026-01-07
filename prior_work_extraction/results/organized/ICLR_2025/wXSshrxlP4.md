# Prior Work Analysis Report

## Target Paper
**Title:** wXSshrxlP4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

GrabS’s core innovation—segmenting 3D point clouds without scene-level supervision by querying pretrained generative object priors with an embodied agent—emerges from converging threads in object-centric generative modeling, implicit shape priors, and active vision. DeepSDF demonstrates how continuous, optimizable generative shape priors can explain observed geometry through latent codes; this directly underpins GrabS’s stage-1 objective of learning object-centric generative and discriminative priors from object datasets. MONet and Slot Attention supply the object-centric decomposition and slot-based competition mechanisms that inform how multiple object hypotheses are represented and refined, enabling GrabS to maintain coherent, multi-object priors suitable for scene querying.
At the algorithmic level, DreamFusion’s use of a powerful pretrained generator as an optimization oracle crystallizes GrabS’s central idea: rather than relying on weak external cues, use a learned generative prior to guide inference in unlabelled scenes. The second stage’s embodied agent builds on active vision principles from Learning to Look Around, recasting segmentation as sequential evidence acquisition—choosing viewpoints or interactions that most reduce ambiguity when matching scene fragments to generative priors. This stands in contrast to prior unsupervised 3D segmentation that leans on motion grouping and heuristic cues, exemplified by Co-Fusion, and to pipelines that depend on 2D self-supervised features like DINO with limited 3D objectness. By integrating these strands, GrabS establishes a two-stage pipeline where rich object-centric generative priors and an active querying policy jointly deliver robust, label-free 3D instance segmentation in complex scenes.

---
*Generated: 2026-01-06T23:42:48.093434*

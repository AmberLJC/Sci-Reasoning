# Prior Work Analysis Report

## Target Paper
**Title:** T9qNDtvAJX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DeltaFlow’s core innovation is an efficient multi-frame scene flow estimator that scales in temporal length with minimal added computation via a Δ-based temporal feature scheme, complemented by losses that address long-tail categories and enforce instance-level motion coherence. This directly builds on two-frame point-cloud scene flow foundations such as FlowNet3D and FLOT, which established end-to-end learning and robust correspondences but left temporal redundancy across multiple frames untapped. The iterative refinement ethos of RAFT inspired efficient correlation aggregation and recurrent updates, which DeltaFlow adapts to 3D by updating only temporal deltas rather than recomputing heavy features per frame. Crucially, efficiency lessons from video recognition—Temporal Shift Module and Deep Feature Flow—demonstrated that simple temporal operators and feature propagation of changes can capture motion cues at negligible cost; DeltaFlow translates these ideas to point-cloud scene flow, making multi-frame reasoning practical without exploding compute. Beyond architecture, DeltaFlow tackles dataset imbalance with a Category-Balanced Loss rooted in the effective-number-of-samples principle, improving learning for underrepresented object classes common in driving datasets. Finally, its Instance Consistency Loss draws on classic piecewise rigid scene flow priors, promoting coherent, near-rigid motion within object instances to stabilize estimates under occlusions and sparse observations. Together, these influences converge to a lightweight, scalable 3D scene flow framework that leverages long temporal context while remaining computationally efficient.

---
*Generated: 2026-01-06T23:42:48.109586*

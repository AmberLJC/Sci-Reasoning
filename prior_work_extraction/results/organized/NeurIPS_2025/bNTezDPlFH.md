# Prior Work Analysis Report

## Target Paper
**Title:** bNTezDPlFH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Rectified Point Flow (RPF) fuses two trajectories of prior work: continuous-time generative transport and learning-based 3D registration/assembly. On the generative side, Neural ODEs established representing dynamics with learned velocity fields, and FFJORD showed how to train such flows as practical generative models. Score-based SDEs then connected diffusion to deterministic probability flow ODEs, crystallizing the principle of learning a velocity field that transports simple noise to data. RPF adapts this transport paradigm to a conditional setting on point clouds, learning a point-wise velocity field that moves unposed points to their target positions, from which rigid part poses can be recovered.
On the geometric side, FlowNet3D validated learning per-point motion vectors directly on unordered point sets, foreshadowing RPF’s point-wise velocity parameterization. Deep Closest Point and RPM-Net reframed registration as learned feature matching and robust pose estimation, revealing the importance of overlap/contact cues; RPF retains this insight via an overlap-aware encoder but sidesteps brittle correspondence/pose regression by using generative transport to implicitly align parts. Finally, NOCS demonstrated that mapping observations to a canonical target enables pose recovery while exposing symmetry ambiguities. RPF generalizes this idea: its learned transport intrinsically captures symmetric assemblies without explicit symmetry labels. Together, these works enabled RPF’s unified conditional generative formulation that spans pairwise registration and multi-part assembly and benefits from joint training across heterogeneous datasets.

---
*Generated: 2026-01-07T00:29:41.032541*

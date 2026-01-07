# Prior Work Analysis Report

## Target Paper
**Title:** te2RsWcyQp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Mesh-RFT’s core contribution—fine-grained reinforcement fine-tuning with Masked DPO guided by topology-aware metrics—builds on two converging lines of work: preference-based policy optimization and mesh-generation/processing. Direct Preference Optimization (Rafailov et al., 2023) provides the backbone for aligning generators with preference signals without learning an explicit reward model; Mesh-RFT adapts this to a masked, localized regime so updates target only problematic regions. This directly counters the known limitation of global, sequence-level RL (e.g., SCST; Rennie et al., 2017), where object-level rewards obscure where errors arise and hinder credit assignment.

On the 3D side, early and modern mesh generators such as AtlasNet (Groueix et al., 2018), PolyGen (Nash et al., 2020), and GET3D (Gao et al., 2022) demonstrate strong generative capabilities but struggle with topology, manifoldness, and local geometric regularity—precisely the failure modes Mesh-RFT seeks to correct post hoc. MeshCNN (Hanocka et al., 2019) crystallizes the value of operating directly at edge/face granularity, informing Mesh-RFT’s quality-aware face masking and localized optimization. Finally, the idea of injecting topological reasoning into learning pipelines (Clough et al., 2019) underpins Mesh-RFT’s objective metrics—Boundary Edge Ratio and Topology Score—which provide actionable, topology-sensitive signals at both object and face levels. By marrying DPO-style preference learning with face-level masking and topology-aware scoring, Mesh-RFT becomes the first to align mesh generators at per-face granularity, repairing local errors while preserving global coherence.

---
*Generated: 2026-01-07T00:29:41.033140*

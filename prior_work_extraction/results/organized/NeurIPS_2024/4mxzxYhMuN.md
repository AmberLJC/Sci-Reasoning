# Prior Work Analysis Report

## Target Paper
**Title:** 4mxzxYhMuN
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

RealMotion’s core contribution—casting motion forecasting as a continuous, streaming task that accumulates scene context across successive driving scenes—stands on two pillars: efficient scene representations and temporally aligned memory. VectorNet and LaneGCN established compact, structured encodings of agents and HD maps and the importance of explicit agent–map interactions; RealMotion inherits these representational advantages to store and propagate interaction structure over time. On the modeling side, Scene Transformer and Wayformer showed that attention-based, scene-level reasoning scales well for per-snapshot multi-agent prediction; RealMotion extends this capability from isolated scenes to a continuous drive by coupling a strong per-scene backbone with an additional stream that fuses historical context.
A key enabler of continuous accumulation is spatial consistency under ego motion. BEVFormer’s ego-motion–aligned temporal BEV memory in perception directly inspires RealMotion’s progressive scene-context memory, ensuring that information from previous viewpoints remains usable as the vehicle moves. Complementing this, Trajectron++ demonstrated the value of carrying temporal latent state for interactive agents; RealMotion elevates this notion from per-agent recurrence to a scene-level memory that preserves interaction patterns across time. Finally, Occupancy Flow showed that aggregating temporal evidence benefits scene-wide motion prediction, reinforcing RealMotion’s design choice to maintain a persistent, interaction-aware scene context that improves accuracy and efficiency in real, continuous driving.

---
*Generated: 2026-01-06T23:39:42.949335*

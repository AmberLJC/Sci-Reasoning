# Prior Work Analysis Report

## Target Paper
**Title:** kFsWpSxkFz
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MetaUrban’s core contribution is a compositional, at-scale simulation platform tailored to urban micromobility, capable of generating effectively infinite, interactive scenes populated by diverse agents. Its design directly builds on procedural composition pioneered by PGDrive, extending parameterized road and scenario generation to include sidewalks, plazas, and vulnerable road users, thus shifting the focus from car-only driving to shared public spaces. From CARLA, MetaUrban inherits the impetus for high-fidelity perception, rich actuation/sensor modeling, and interactive urban assets, while explicitly re-scoping those capabilities to the sidewalk regime. The scalability, speed, and generalization-centric ethos of Habitat inform MetaUrban’s emphasis on large-scale training and evaluation, enabling robust assessment of policy generalization across procedurally varied cities. Gibson’s focus on perceptual realism further motivates MetaUrban’s attention to visual and physical plausibility, ensuring procedurally composed scenes remain credible for embodied agents. To model the complex multi-agent dynamics characteristic of urban public spaces, MetaUrban draws on SUMO’s microsimulation principles for heterogeneous flows, and adopts classic interaction models—ORCA for reciprocal, real-time collision avoidance and the Social Force model for pedestrian dynamics—to populate environments with realistic human and VRU behaviors. Together, these strands converge in MetaUrban: a platform that unifies scalable, compositional scene generation with credible multi-agent interactions and embodied sensing, purpose-built to evaluate safety and generalization of AI-driven micromobility.

---
*Generated: 2026-01-06T23:42:48.082350*

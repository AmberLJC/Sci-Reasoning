# Prior Work Analysis Report

## Target Paper
**Title:** fCirUh6FRb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

FSDrive’s core contribution—replacing textual chains-of-thought with a spatio-temporal visual CoT—emerges from combining three lines of prior work. First, Chain-of-Thought prompting and its multimodal extensions established the power of explicit intermediate reasoning but largely relied on text. These approaches are ill-suited for driving because symbolic summaries obscure metric geometry and fine appearance cues. FSDrive directly addresses this by making the intermediate chain an image that encodes the scene’s spatial layout and temporal evolution.
Second, world-model research (e.g., Dreamer) showed that predicting future observations enables stronger decision making. FSDrive adopts this principle to generate a physically plausible future frame, then augments it with lanes and 3D boxes to make the imagined future explicitly structure-aware. This design resonates with driving-centric spatio-temporal modeling such as BEVFormer and the unification ethos of UniAD, which demonstrated that tightly coupling perception, prediction, and planning with structured representations benefits control.
Third, the Vision-Language-Action paradigm (RT-2) illustrated that a single foundation model can map high-dimensional perception to actions. FSDrive leverages a similar VLA backbone in a dual role: (1) as a world model that imagines a future visual CoT, and (2) as an inverse-dynamics planner that conditions on this visual CoT to output trajectories—conceptually related to conditioning in diffusion-based planners (Diffuser). By unifying imagination and control inside one VLA and by making the intermediate explicitly visual and temporally grounded, FSDrive bridges the perception–planning gap while preserving the model’s language-grounded understanding.

---
*Generated: 2026-01-07T00:21:32.347988*

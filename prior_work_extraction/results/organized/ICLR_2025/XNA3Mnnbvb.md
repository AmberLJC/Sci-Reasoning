# Prior Work Analysis Report

## Target Paper
**Title:** XNA3Mnnbvb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DartControl’s core innovation—real-time, text-driven control of long, continuous human motion with spatial constraints—emerges from three converging lines of work. First, diffusion-based motion generation (MDM; MotionDiffuse) provided the high-fidelity denoising backbone and practical text-conditioning pipelines that DART adopts as its per-primitive generator. Second, research on long-horizon and tokenized motion modeling (T2M-GPT) demonstrated that decomposing sequences into reusable units and generating them autoregressively improves scalability and temporal coherence. DART blends these by treating short motion primitives as the autoregressive units, but samples each primitive via diffusion to retain fine-grained realism absent in discrete token decoders.
A second pillar is controllability. MCDiff showed diffusion models can be steered with kinematic controls (e.g., trajectories, contacts), while Diffuser framed sequential control and planning as conditional diffusion. DART extends this to multi-modal, online control, aligning free-form text semantics with explicit spatial goals and 3D scene geometry to guide each primitive in a closed loop. Finally, achieving real-time responsiveness draws on efficiency advances from latent-space diffusion for motion (MLD), suggesting compact representations and short denoising schedules, which DART combines with short-horizon primitives to meet latency constraints. Semantic alignment techniques from MotionCLIP ensure streaming language commands remain faithfully reflected in the generated motion. Together, these works directly shape DART’s diffusion-based autoregressive design, enabling responsive, goal-aware, and semantically accurate long-form motion control.

---
*Generated: 2026-01-07T00:02:04.907312*

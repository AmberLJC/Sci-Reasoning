# Prior Work Analysis Report

## Target Paper
**Title:** vhACnRfuYh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Diffuser: Diffusion Models for Planning** (2022)
- *Authors:* Michael Janner et al.
- *Connection:* LDP adopts Diffuser’s core idea of using denoising diffusion to generate full trajectories for planning and extends it by operating in a learned latent state space and decoupling action prediction from planning.

**Behavioral Cloning from Observation** (2018)
- *Authors:* Arash Torabi et al.
- *Connection:* LDP’s design of a separate inverse dynamics module is grounded in BCO’s insight that state-only demonstrations can be leveraged by learning inverse dynamics, enabling action-free learning.

**PlaNet: Learning Latent Dynamics for Planning from Pixels** (2019)
- *Authors:* Danijar Hafner et al.
- *Connection:* LDP follows PlaNet’s principle of planning in a learned latent state space from pixels, but replaces explicit dynamics+CEM with a diffusion-based planner and a learned inverse-dynamics stage.

### 💡 Inspiration

**High-Resolution Image Synthesis with Latent Diffusion Models** (2022)
- *Authors:* Robin Rombach et al.
- *Connection:* LDP directly borrows the latent-diffusion paradigm—first learning a VAE and then running diffusion in the compact latent—to make trajectory generation from high-dimensional images efficient and stable.

**Learning Latent Plans from Play** (2019)
- *Authors:* Corey Lynch et al.
- *Connection:* LDP’s ability to leverage broad, suboptimal interaction data for control echoes Play-LMP’s finding that diverse play can train control primitives; LDP extends this by restricting suboptimality to inverse dynamics while planning from action-free data.

### 📊 Baseline

**Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** (2023)
- *Authors:* Chi et al.
- *Connection:* LDP targets Diffusion Policy’s limitation of requiring large expert, action-labeled datasets by separating planning (trainable from action-free demos) from action prediction, yielding stronger performance on visual manipulation.

---

## Synthesis

Latent Diffusion Planning (LDP) sits at the intersection of three lines of work that directly enabled its core innovation: diffusion-based planning, latent-space planning from pixels, and learning from action-free or suboptimal data. Diffuser established that denoising diffusion can synthesize expert-like trajectories for decision making; LDP builds on this by moving planning into a compact latent space and by decoupling plan generation from action prediction. The latent-space move is inspired by Latent Diffusion Models, which showed that VAE-backed latent diffusion delivers efficient and scalable generation from high-dimensional inputs—critical for image-based robotics. On the planning side, PlaNet provided the blueprint for learning from pixels by planning in a learned latent state space; LDP follows this decomposition but substitutes classical dynamics+CEM with a diffusion trajectory generator and executes plans via a learned inverse-dynamics head. The inverse-dynamics component and the use of action-free demonstrations are grounded in Behavioral Cloning from Observation, which formalized how to leverage state-only demos via inverse dynamics. LDP refines this by training the planner purely from action-free data while using abundant, possibly suboptimal interaction data to learn inverse dynamics. Finally, Diffusion Policy serves as the primary baseline whose limitations—dependence on large action-labeled expert datasets and entangling action generation with planning—are explicitly addressed. Together with Play-LMP’s insight that diverse, suboptimal play data suffices for control learning, these works directly shaped LDP’s modular latent-diffusion planning framework.

---
*Generated: 2026-01-06T23:07:19.564126*

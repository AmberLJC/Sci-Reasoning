# Prior Work Analysis Report

## Target Paper
**Title:** ph1V6n7BSv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EDELINE’s core contribution—unifying diffusion-based observation modeling with linear-time state-space sequence modeling to unlock long-horizon memory—emerges at the intersection of three lines of work. First, PlaNet and DreamerV2 established recurrent state-space world models that jointly model latent dynamics, rewards, and terminations for sample-efficient RL. While these models excel in compact sequence modeling, their discrete or heavily compressed latents can sacrifice visual fidelity, motivating a higher-capacity observation generator.
Second, diffusion models advanced visual fidelity. Latent Diffusion made high-resolution generation efficient, and Video Diffusion Models demonstrated next-frame prediction conditioned on a short context. However, such diffusion approaches typically rely on fixed windows, limiting memory and making it natural to bolt on separate RNN heads for rewards/terminations—fragmenting the world model. Diffuser further showed diffusion’s suitability for sequential decision-making, reinforcing the premise that diffusion can model temporally structured processes.
Third, modern State Space Models such as S4 and Mamba provide linear-time sequence modeling with strong long-range dependency capture, offering an attractive alternative to quadratic-cost attention for memory. EDELINE synthesizes these threads by conditioning a diffusion-based observation decoder on an SSM state that summarizes arbitrarily long histories, while using the same SSM backbone to model rewards and terminations. This replaces fixed-window conditioning with scalable, unified memory, addressing visual fidelity and long-horizon credit simultaneously and yielding improved performance on Atari 100k, Crafter, and ViZDoom.

---
*Generated: 2026-01-07T00:29:42.065568*

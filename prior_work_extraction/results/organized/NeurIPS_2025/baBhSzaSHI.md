# Prior Work Analysis Report

## Target Paper
**Title:** baBhSzaSHI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DEXTER fuses three influential threads into a single, data-free explanatory pipeline. First, activation maximization and feature visualization originated by DeepDream and advanced by Nguyen et al. established that one can synthesize inputs to expose a model’s internal preferences. DEXTER inherits this probing philosophy but replaces pixel-space or GAN-based synthesis with state-of-the-art diffusion priors to yield high-fidelity, semantically coherent samples that robustly activate a target classifier.
Second, the diffusion modeling advances that enable this swap are twofold: classifier guidance (Dhariwal & Nichol) provides a principled gradient signal to steer generation toward target classes, while latent diffusion (Rombach et al.) supplies an efficient, text-conditioned backbone capable of large-scale, controllable image synthesis. Building on Textual Inversion’s insight that learned, continuous token embeddings can precisely steer diffusion, DEXTER directly optimizes prompts so that the generated images maximally elicit the classifier’s decision rules—without any access to the original training data.
Third, for global, human-understandable analysis, DEXTER draws on concept-based and natural-language explanation paradigms. TCAV framed explanations at the concept level for model auditing and bias probing; Hendricks et al. demonstrated that natural language can faithfully describe visual decision evidence. DEXTER unifies these ideas by using an LLM to convert synthetic, class-activating cohorts into global textual reports of discriminative patterns, spurious cues, and dataset biases, enabling activation maximization, slice discovery/debiasing, and bias explanation in a single, data-free framework.

---
*Generated: 2026-01-07T00:21:32.260685*

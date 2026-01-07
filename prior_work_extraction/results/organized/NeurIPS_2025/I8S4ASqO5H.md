# Prior Work Analysis Report

## Target Paper
**Title:** I8S4ASqO5H
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Chain-of-Zoom (CoZ) fuses three lines of prior work into a single framework: multiscale autoregression, diffusion SR backbones, and preference-aligned language guidance. From LAPGAN and LapSRN, CoZ inherits the core insight that high-resolution synthesis is easier when decomposed across scales; it recasts that principle as a model-agnostic, inference-time chain that repeatedly reuses a single pretrained SR module to traverse intermediate scale states. ZSSR contributes the training-free ethos: instead of retraining for larger magnifications, CoZ attains extreme upscaling by procedural factorization and reuse—trading new parameters for a smarter inference schedule.
Diffusion-based SR, exemplified by SR3, supplies the robust 4× building block. Rather than redesigning architecture, CoZ wraps such a backbone and composes it autoregressively, preserving SR3’s fidelity while pushing far beyond its native scale.
Finally, CoZ addresses the diminishing visual evidence at large magnifications with multi-scale-aware textual prompts. BLIP-2–style VLMs make per-step, fine-grained descriptions feasible, and the alignment of these prompts with human preference draws directly from RLHF. By training the prompt extractor with GRPO against a critic VLM—an application of RLAIF—CoZ ensures textual guidance is not merely descriptive but preference-aligned. Together, these influences yield a practical recipe: decompose scaling into tractable steps, reuse a strong SR backbone, and inject preference-aligned language cues at each hop, enabling stable super-resolution to extreme factors without additional SR model training.

---
*Generated: 2026-01-07T00:27:38.141597*

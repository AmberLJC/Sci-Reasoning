# Prior Work Analysis Report

## Target Paper
**Title:** QwXpn5IPKk
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

RepLDM’s core contribution—training-free reprogramming of pretrained latent diffusion models to produce high-quality, structurally consistent images at resolutions beyond training—emerges from two converging lines of prior work. First, the latent diffusion framework of Rombach et al. established the U-Net-with-attention backbone RepLDM reuses, while attention-manipulation methods such as Prompt-to-Prompt and Attend-and-Excite demonstrated that inference-time control of internal attention maps can enforce semantic and structural fidelity without parameter updates. RepLDM extends these attention-centric ideas to a novel, parameter-free self-attention guidance stage, using the model’s own attention to distill a higher-quality latent at the training resolution that preserves global structure before any upscaling.

Second, the progressive, coarse-to-fine generation paradigm exemplified by Cascaded Diffusion Models and diffusion-based super-resolution (SR3) motivates RepLDM’s progressive upsampling in pixel space. Rather than train separate super-resolution models, RepLDM couples SDEdit-style noise reintroduction with the pretrained LDM to iteratively upscale and refine, achieving cascaded benefits using a single model. In contrast to tiled fusion approaches like MultiDiffusion—which suffer from seams and high compute—RepLDM’s global attention-guided base generation plus pixel-space progressive refinement yields better structural coherence and efficiency. Together, these works directly inform RepLDM’s two-stage design: attention-guided latent consolidation at base scale followed by training-free, progressive pixel upsampling that preserves structure while scaling resolution and reducing runtime.

---
*Generated: 2026-01-07T00:21:32.239662*

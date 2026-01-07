# Prior Work Analysis Report

## Target Paper
**Title:** mSiN7i0BYH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Self Forcing targets the core weakness of teacher-forced video diffusion—exposure bias—by training under the same autoregressive conditions faced at inference. This on-policy orientation directly traces to three seminal strands: Scheduled Sampling introduced mixing model outputs into training inputs; DAgger formalized training on states induced by the model’s own policy to counter covariate shift; and Professor Forcing advocated sequence-level alignment of train and test dynamics. Building on these, Self Forcing fully rolls out self-generated context during training and evaluates with a video-level objective, echoing the sequence-level emphasis of Ranzato et al. (MIXER) but in a diffusion setting.

Realizing on-policy training for video diffusion demands efficiency mechanisms. Transformer-XL’s memory-based segment recurrence provides the conceptual and practical foundation for the paper’s rolling KV cache and stochastic gradient truncation, enabling long-horizon rollouts with manageable backpropagation. To keep rollouts affordable within diffusion, the work leverages advances in few-step diffusion, with progressive distillation furnishing a concrete pathway to reduce sampling steps while preserving fidelity. All of this builds upon the DDPM framework, whose denoising objective underlies the model’s per-step predictions while Self Forcing reshapes the conditioning regime and supervision granularity from frame-wise to video-level. Together, these prior works directly enable Self Forcing’s central contribution: efficient, on-policy, video-level training for autoregressive video diffusion that bridges the train–test gap.

---
*Generated: 2026-01-07T00:21:32.354461*

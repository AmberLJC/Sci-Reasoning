# Prior Work Analysis Report

## Target Paper
**Title:** VsDsRqaMJv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Post Hoc Registers (PH-Reg) addresses a practical gap: existing large ViTs often exhibit artifact tokens that harm localization and structure, yet fully retraining at scale to add register tokens is infeasible. The foundational ViT formulation by Dosovitskiy et al. established the tokenized image representation and special-token interface that PH-Reg modifies by introducing registers. Prior evidence that distillation can supervise special tokens in ViTs comes from DeiT, where a dedicated distillation token is trained via a teacher, suggesting a path to supervise newly added tokens without architectural upheaval. DINO demonstrated that ViTs can be distilled without labels using a teacher–student framework, providing the label-free training recipe PH-Reg adopts to learn registers from a frozen teacher. Crucially, DINOv2 introduced register tokens in ViTs and argued they absorb nuisance and artifact content, directly motivating PH-Reg’s central idea to retrofit registers into already-trained models. Conceptually, Set Transformer’s inducing points established that learned latent tokens can mediate attention and act as memory, a perspective that underpins the role of registers as information sinks. Finally, the adapter literature on parameter-efficient transfer (Houlsby et al.) and self-distillation via Born-Again Networks inform PH-Reg’s practical recipe: minimally augment a large pretrained model, keep most weights fixed, and transfer behavior from the original to the augmented model. Together, these works crystallize PH-Reg’s contribution: a label-free self-distillation procedure that post hoc equips pretrained ViTs with register tokens to suppress artifacts without full retraining.

---
*Generated: 2026-01-07T00:21:32.285757*

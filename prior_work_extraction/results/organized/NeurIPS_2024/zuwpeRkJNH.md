# Prior Work Analysis Report

## Target Paper
**Title:** zuwpeRkJNH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PeskaVLP fuses three strands of prior art to address surgical video–language pretraining: contrastive language supervision, learning from noisy instructional narrations, and explicit temporal alignment. CLIP established the modern contrastive objective with in-batch negatives, providing the base training signal that PeskaVLP adapts to video and the surgical domain. The instructional-video line—HowTo100M and MIL-NCE—demonstrated that ASR transcripts from narrated procedures are scalable yet noisy, motivating PeskaVLP’s use of lecture narrations and the need for robustness to misalignment. Rather than treating alignment implicitly (as in MIL-NCE), PeskaVLP embraces explicit procedure-aware alignment, drawing on ideas from weakly supervised step alignment in narrated instructional videos and operationalizing them with a differentiable dynamic time warping loss grounded in soft-DTW. This makes the model sensitive to the ordered, variable-rate nature of surgical workflows.
Complementing alignment, PeskaVLP improves the language side via hierarchical knowledge augmentation, inspired by BLIP’s caption bootstrapping and filtering, but specialized for surgical terminology and multi-level concepts to reduce textual sparsity and overfitting. Finally, the framework sharpens cross-modal discrimination by constructing procedure- and step-level hard negatives, following the VSE++ insight that focusing on the most confusable negatives boosts retrieval and alignment quality. Together, these works directly inform PeskaVLP’s key contributions: LLM-driven hierarchical text enrichment, procedure-aware DTW-based video–text alignment, and a contrastive training scheme with hard negatives tailored to surgical instructional data.

---
*Generated: 2026-01-06T23:42:49.039162*

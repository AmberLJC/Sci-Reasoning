# Prior Work Analysis Report

## Target Paper
**Title:** s4LnWgjacg
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core innovation—framing LoRA performance as primarily governed by the magnitude of weight updates and unifying learning rate, scaling (α), and initialization as mechanisms for regulating this magnitude—builds directly on several strands of prior work. LoRA (Hu et al., 2022) created the low-rank update pathway and introduced the α/r scaling and standard initialization practices that define the knobs whose effects this paper seeks to demystify. QLoRA (Dettmers et al., 2023) provided large-scale empirical evidence that LoRA’s outcomes are highly sensitive to α, rank, and learning rate, hinting that a single underlying quantity—update magnitude—might be the common currency.
A complementary line showed that shaping either the spectrum or the norm of updates improves LoRA. Spectral-initialization methods such as PiSSA align LoRA with principal singular subspaces of pretrained weights and consistently boost convergence; the present work argues these benefits are largely magnitude amplification rather than privileged spectral knowledge. DoRA’s weight-decomposed formulation isolates magnitude from direction and reports gains by explicitly learning norms, directly reinforcing the idea that magnitudes are primary drivers. AdaLoRA’s adaptive budget allocation further supports the view that low-rank structure constrains and redistributes update norms across layers.
Situated against this backdrop, the paper formalizes how low-rank parameterization intrinsically bounds update magnitudes and shows that hyperparameters chiefly modulate these bounds. This leads to LoRAM, a magnitude-driven “Basis & Basis” initialization that matches spectral methods’ benefits without their SVD cost—operationalizing the magnitude primacy hypothesis into a practical, efficient initializer.

---
*Generated: 2026-01-07T00:21:32.332827*

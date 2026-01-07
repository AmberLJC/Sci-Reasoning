# Prior Work Analysis Report

## Target Paper
**Title:** UTGjik64IK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central insight—that distilling an unlearned model into a freshly initialized, noised student yields robust unlearning—sits at the intersection of two mature literatures: distillation and machine unlearning. Hinton et al. (2015) established distillation as a practical mechanism to transfer behavior via soft targets, while Papernot et al. (2016) demonstrated that distillation can enhance robustness, suggesting that the training signal itself can inoculate models against certain perturbations. Building on Furlanello et al. (2018), the authors leverage the fact that a student trained from random initialization can inherit teacher behavior without preserving the teacher’s internal representations, a property crucial for leaving latent capabilities behind after unlearning. Xie et al. (2020) further inform the UNDO method by showing that injecting noise into the student during distillation improves robustness and offers a knob to trade compute for performance—precisely the adjustable frontier UNDO targets.
In parallel, Cao and Yang (2015) and Bourtoule et al. (2021) define the machine unlearning goal and scalable system designs (e.g., SISA), clarifying the efficiency–effectiveness frontier that current methods struggle to advance. Finally, ROME (Meng et al., 2022) reveals that edits and finetuning can change outputs while leaving knowledge intact, directly motivating the paper’s premise: naïve unlearning is fragile because capabilities persist. UNDO reconciles these strands by using noisy, from-scratch distillation to transfer only desired behavior from an unlearned teacher, thereby robustifying unlearning against subsequent finetuning and establishing a stronger Pareto frontier.

---
*Generated: 2026-01-07T00:02:04.979581*

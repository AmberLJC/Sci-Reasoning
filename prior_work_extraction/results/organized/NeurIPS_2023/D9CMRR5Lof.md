# Prior Work Analysis Report

## Target Paper
**Title:** D9CMRR5Lof
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MGDD responds to the core limitations of iterative dataset distillation by reframing the synthesis process as generation conditioned on learner initialization, plus closed-form label computation. The original Dataset Distillation formulation defined the bilevel objective of optimizing synthetic data to mimic real training, which subsequent methods operationalized through gradient-centric criteria. Gradient Matching and its DSA-enhanced variant established effective, widely adopted objectives but required many forward–backward passes to adjust pixel-level parameters, making them slow and inflexible when target set sizes change. Matching Training Trajectories further improved fidelity by aligning entire learning trajectories, yet accentuated the computational burden. This line of work collectively motivates MGDD’s pursuit of drastically higher time efficiency.

MGDD adopts a meta-learning perspective, inspired by MAML’s conditioning on learner initialization, to train a generator that outputs synthetic samples tailored to a given network init. This removes the need to re-run heavy inner-loop optimization when requesting different synthetic dataset sizes and supports fast, flexible distillation. For labels, MGDD leverages kernel-inspired reasoning: the NTK view connects network training to kernel regression, justifying MGDD’s least-squares solution in a feature space and underpinning its theoretical error analysis between original and feature domains. Finally, distribution matching ideas guide the goal of aligning synthetic and real data statistics, which MGDD attains implicitly through its generator rather than explicit iterative optimization. Together, these works directly shape MGDD’s generator-based, meta-conditioned, and closed-form labeling pipeline that achieves fast, scalable dataset distillation.

---
*Generated: 2026-01-06T23:42:49.110449*

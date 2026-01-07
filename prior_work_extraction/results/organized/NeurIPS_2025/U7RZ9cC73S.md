# Prior Work Analysis Report

## Target Paper
**Title:** U7RZ9cC73S
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

RobustMerge targets a rising practical need: combining many task-specific, parameter-efficient experts into a single, multi-task MLLM without extra training. The core idea is that PEFT merging fails when the low-rank update directions misalign across tasks, and that stabilizing these directions requires compensating for singular-value disparities. This view is rooted in LoRA’s low-rank parameterization, which makes singular vectors and values central to how updates shape model behavior. Earlier training-free weight-space approaches, like Model Soups and Fisher-weighted merging, show that simple averaging or importance-weighted interpolation can succeed for full fine-tunes; however, RobustMerge explains why such strategies are brittle for adapters, where directional consistency is the bottleneck rather than just global scaling or curvature. Conflict-aware methods such as TIES-Merging highlight that interference must be explicitly controlled; RobustMerge adapts this principle to the PEFT regime via pruning and complementary parameter scaling to guard update directions. On the PEFT mechanics side, DoRA’s emphasis on decoupling magnitude from direction and PiSSA’s SVD-based alignment both elevate the role of spectral structure, directly motivating RobustMerge’s compensation for uneven singular spectra to preserve direction robustness. Together, these threads crystallize into a training-free, parameter-efficient merging algorithm that prunes, scales, and complements adapter parameters to maintain stable low-rank directions across tasks.

---
*Generated: 2026-01-07T00:21:32.345590*

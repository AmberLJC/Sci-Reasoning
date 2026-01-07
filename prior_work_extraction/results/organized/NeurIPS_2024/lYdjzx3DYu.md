# Prior Work Analysis Report

## Target Paper
**Title:** lYdjzx3DYu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EMR-Merging emerges at the intersection of weight-space model composition and parameter-efficient multi-tasking. Early demonstrations that models can be combined without extra training—via uniform/greedy weight averaging in Model Soups and two-way interpolation in WiSE-FT—established that merging can yield robustness and multi-task benefits. However, Fisher-weighted averaging highlighted a key limitation of naive averages: parameters contribute unequally across tasks, and a single averaged model may inadequately capture all task optima.

Concurrently, task arithmetic reframed fine-tuning as displacement vectors in weight space, where both direction and magnitude matter for composition. This viewpoint directly motivates EMR’s Elect–Mask–Rescale design: elect a unified base and then align each task’s direction (mask) and magnitude (rescale) relative to that base. From the multi-task systems side, Piggyback and AdapterFusion showed that adding lightweight, task-specific modules atop a shared backbone can preserve task performance while avoiding interference; LoRA generalized this efficiency principle to modern large models. EMR synthesizes these strands but removes the need for any additional data or training: its task-specific masks and rescalers are computed directly from existing fine-tuned checkpoints. The result is a tuning-free, high-performance merger that preserves per-task fidelity by explicitly correcting directional conflicts and magnitude mismatches, surpassing what a single unmodulated average can simulate while keeping inference overhead minimal.

---
*Generated: 2026-01-06T23:33:35.573275*

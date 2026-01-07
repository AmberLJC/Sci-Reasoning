# Prior Work Analysis Report

## Target Paper
**Title:** glLqTK9En3
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central contribution—demonstrating that functional alignment via model stitching can be highly misleading about informational similarity—emerges from two converging lines of prior work. First, methodological and empirical precedents for stitching: Lenc and Vedaldi’s linear mappings to test representation equivalence and Yosinski et al.’s layer-swapping studies established that subnetworks can be grafted across models with minimal adaptation. Li et al. extended this with evidence that independently trained networks can be aligned via simple transformations, reinforcing the intuition that functional compatibility implies similar internal content. Second, the representational similarity literature (SVCCA; CKA) normalized the practice of comparing internal spaces and fostered a community prior that alignment signals shared information. Against this backdrop, Geirhos et al. showed that equally accurate models can embody starkly different inductive biases (texture vs. shape), and Zhang et al. revealed that deep nets can memorize arbitrary noise. The present paper synthesizes these threads: it adopts the stitching mechanism to align systems that, by design, should encode different information (different biases, tasks, modalities, and even clustered noise) and shows that functional alignment can still succeed. This directly undermines the prevalent inference—from both geometric and functional alignment—that similar performance under simple adapters implies informational equivalence, and it motivates evaluation tools that track information content rather than mere alignability.

---
*Generated: 2026-01-07T00:21:32.383159*

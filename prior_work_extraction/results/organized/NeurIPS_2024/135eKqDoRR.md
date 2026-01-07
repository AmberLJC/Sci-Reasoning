# Prior Work Analysis Report

## Target Paper
**Title:** 135eKqDoRR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Bayesian-guided Label Mapping (BLM) advances visual reprogramming by replacing brittle one-to-one label assignments with a probabilistic, iteratively updated mapping between pretrained and downstream label spaces. This shift is rooted in the original adversarial/visual reprogramming paradigm—repurposing fixed networks via input/output interfaces—where early methods enforced hard permutations between label sets. Such one-to-one strategies, often formalized through Hungarian matching, overlook real-world many-to-many correspondences. BLM draws methodological traction from probabilistic label modeling traditions. Label-shift estimation with black-box predictors uses confusion matrices to infer relationships between source and target label distributions, aligning closely with BLM’s need to quantify cross-space label affinities. Likewise, deep learning with noisy labels introduced the notion of a label-noise transition matrix; BLM adapts this idea to represent uncertainty and overlap between pretrained and downstream labels instead of noise. Noise adaptation layers and EM-style estimation further inspire BLM’s iterative Bayesian updates, allowing the mapping matrix to be refined jointly with model evidence. Finally, optimal transport for domain adaptation motivates the use of soft couplings rather than hard permutations, conceptually aligning with BLM’s probabilistic mapping while BLM grounds the coupling in Bayesian guidance rather than cost-based transport. Together, these strands directly shape BLM’s core contribution: a Bayesian, soft, and iteratively learned label alignment that better captures complex pretrained–downstream label relationships than prior one-to-one mappings.

---
*Generated: 2026-01-06T23:33:36.274145*

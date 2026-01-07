# Prior Work Analysis Report

## Target Paper
**Title:** rk2L9YGDi2
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Sequoia’s core innovation—scalable, temperature-robust speculative decoding with an optimally chosen token tree—sits at the intersection of two key trajectories in prior work. First, early predict-and-verify methods such as Blockwise Parallel Decoding established the idea of proposing multiple next steps and validating them efficiently. This concept was instantiated for modern LLMs by Speculative Decoding (Leviathan et al.), which formalized draft-and-verify using a small draft model and a larger verifier. Second, a subsequent wave of systems and algorithmic work sought to scale speculative decoding by proposing multiple candidates in tree or graph form and verifying them in batch. Medusa explored multi-branch draft structures via auxiliary heads, while EAGLE generalized to multi-draft proposals with heuristic branching/acceptance. SpecInfer pushed the systems side, introducing token graphs and batched verification for high-throughput serving. These efforts revealed two pain points that Sequoia directly addresses: (1) performance depends heavily on the choice of tree structure and speculation budget, and (2) speedups can degrade under higher temperatures or different decoding hyperparameters. Sequoia contributes a dynamic-programming algorithm that computes an optimal speculation tree under compute and memory constraints, subsuming prior fixed or heuristic trees, and a sampling/verification procedure that sustains high acceptance and quality across temperatures. Together, these advances unlock larger effective speculation budgets and stable gains, extending and unifying the ideas introduced across the above prior works.

---
*Generated: 2026-01-06T23:33:36.292127*

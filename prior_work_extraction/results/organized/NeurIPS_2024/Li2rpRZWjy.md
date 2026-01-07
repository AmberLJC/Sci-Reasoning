# Prior Work Analysis Report

## Target Paper
**Title:** Li2rpRZWjy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This work’s core contribution—defining rule extrapolation as a compositional OOD scenario where prompts violate one or more governing rules of a formal language, and evaluating it across architectures—sits at the intersection of three research threads. First, compositional generalization benchmarks such as SCAN and CFQ crystallized the need to test models on novel compositions of learned primitives and provided methodologies to factor tasks into rules and combinations. The present paper extends this paradigm by moving from recombining rules to explicitly violating them within formal languages whose structure is cleanly specified as intersections of rules, enabling unambiguous OOD definitions.
Second, the architecture-centric literature on formal language expressivity shaped the cross-model evaluation. Analyses of RNNs’ practical expressive power and Transformers’ theoretical limitations on formal languages provide expectations about which dependencies each architecture should capture or fail to extrapolate. The inclusion of structured state space models (S4) broadens this comparison to a modern recurrent alternative designed for long-range dependencies, allowing the authors to disentangle architectural inductive biases in rule extrapolation.
Third, the observed OOD capabilities of large language models through in-context learning motivate the focus on OOD prompts, while Solomonoff’s universal prior offers a normative lens: simplicity-based inductive biases can predict which rule-violating continuations are preferred. By combining these strands, the paper introduces a principled, architecture-aware framework for studying OOD compositional generalization and initiates a theory-grounded account of when and why language models extrapolate rules.

---
*Generated: 2026-01-06T23:42:49.025339*

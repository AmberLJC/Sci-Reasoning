# Prior Work Analysis Report

## Target Paper
**Title:** nfK0ZXFFSn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

HaloScope’s core innovation is to detect hallucinations by harnessing unlabeled LLM generations encountered in the wild, using an automated scoring function to separate truthful from untruthful responses and then training a binary classifier. This builds directly on two strands of prior work. First, consistency-based evaluation of LLM outputs—exemplified by SelfCheckGPT and the self-consistency paradigm—shows that one can assess reliability by aggregating multiple samples from the model itself. HaloScope generalizes this idea into a formal, scalable scoring function for truthfulness on unlabeled mixtures. Second, the weak-supervision and semi-supervised literature (Snorkel, Noisy Student, and PU learning) demonstrates how noisy or heuristic signals over unlabeled data can be converted into effective supervisory signals. HaloScope adopts this blueprint: it programmatically transforms its automated truthfulness scores into pseudo-labels for training, without human annotation or curated references.
In shaping the final detector, HaloScope is aligned with classifier-based factuality approaches like FactCC, but replaces expensive labeled data with its automated scoring pipeline. Conceptually, it also echoes the Li group’s work on training detectors without explicit negatives (VOS), using generated or derived signals to inform decision boundaries. Together, these works converge into HaloScope’s design: use multi-sample agreement signals to score truthfulness, convert those scores into weak labels, and train a discriminative classifier that scales to real-world unlabeled LLM outputs while avoiding additional data collection and human labeling.

---
*Generated: 2026-01-06T23:33:35.575127*

# Prior Work Analysis Report

## Target Paper
**Title:** TyW1V1KukG
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution—an information-theoretic attacker that is transferable across both models and prompts in LVLMs—stands on two converging lines of prior work. First, the transferability literature in vision established that perturbations can generalize beyond a single model through careful objective design and optimization. Universal Adversarial Perturbations and Adversarial Patch showed that model- and input-agnostic perturbations exist, inspiring the present work’s aim for agnostic behavior with respect to both model architecture and prompt semantics. Successive advances like MI-FGSM, DI^2-FGSM, and TI-FGSM demonstrated concrete mechanisms—momentum stabilization, input diversity, and translation-invariant smoothing—to reduce overfitting to a source model and align perturbations with broadly shared features, directly motivating a search for a more principled criterion for generalization.
Second, the conceptual reframing by Ilyas et al. that adversarial examples exploit non-robust yet predictive features provided the semantic lens for the paper’s disentanglement of benign versus adversarial patterns. Rather than implicitly encouraging transfer via heuristics, the authors explicitly modulate a model’s dependency on these patterns. This is enabled technically by mutual information optimization, for which MINE supplies a tractable estimator, allowing the attack to increase output dependence on adversarial patterns while suppressing dependence on benign ones. By marrying universal/transferable attack principles with an MI-based dependency control grounded in the non-robust features perspective, the paper advances from image-only CNN settings to LVLMs, achieving both model-transferability and prompt-transferability—two dimensions previously handled only implicitly or separately.

---
*Generated: 2026-01-07T00:21:32.306006*

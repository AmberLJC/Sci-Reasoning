# Prior Work Analysis Report

## Target Paper
**Title:** tTPHgb0EtV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Booster’s core contribution—attenuating the reduction in harmful loss under simulated weight perturbations during alignment—sits at the intersection of adversarial robustness, weight-space optimization, and LLM safety alignment. Conceptually, SAM (Foret et al., 2021) established that optimizing against worst-case weight perturbations can induce flat minima and robustness; Booster repurposes this idea for safety by constructing weight perturbations that simulate downstream harmful fine-tuning and then discouraging any harmful-loss improvement post-perturbation. This mirrors the minimax structure popularized by Madry et al. (2018), but the inner maximization is carried out in parameter space and the outer objective focuses on harmlessness rather than classification accuracy.
Operationally, Booster augments standard alignment training, exemplified by RLHF (Ouyang et al., 2022), with a perturbation-aware regularizer. Its definition of harmful loss and its goal of preserving refusal behavior build directly on harmlessness-centric alignment, as in Constitutional AI (Bai et al., 2022). The motivation to model attacks as weight perturbations is reinforced by model-editing results like ROME (Meng et al., 2022), which show how small, directed weight changes can predictably alter model behavior—precisely what malicious fine-tuning seeks to achieve. Finally, LoRA (Hu et al., 2022) makes such fine-tuning cheap and practical, broadening the real-world attack surface that Booster aims to defend against. Together, these works inform Booster’s key insight: proactively shaping the alignment landscape to be insensitive, in the harmful direction, to plausible post-deployment parameter updates.

---
*Generated: 2026-01-06T23:42:48.095319*

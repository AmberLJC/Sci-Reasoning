# Prior Work Analysis Report

## Target Paper
**Title:** qZFshkbWDo
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—exposing the superficial nature of many backdoor purification defenses and formalizing post-purification robustness—builds on two converging lines of prior work. First, BadNets codified the modern backdoor threat and ASR evaluation, which defenses like Fine-Pruning, Spectral Signatures, and Neural Cleanse were designed to defeat by driving ASR down on held-out tests. More recent unlearning approaches such as Neural Attention Distillation advanced this defensive paradigm by refining model-centric mitigation via fine-tuning and knowledge transfer. These methods collectively form the class of “safety purification” techniques scrutinized in the paper. Second, attack-side insights foreshadowed that backdoor features can be stubborn and sample-efficient: Latent Backdoor Attacks showed that poisoned features may persist and re-emerge under transfer or further training, while Label-Consistent/Clean-label attacks demonstrated that only a handful of poisoned examples can install a backdoor. Integrating these observations, the paper argues that low ASR after purification does not mean the backdoor representation is eliminated; rather, a vulnerable subspace often remains, enabling rapid re-learning with very small poisoned fine-tuning sets. By systematically evaluating leading purification defenses under this few-shot re-poisoning regime and providing an explanation rooted in lingering backdoor-sensitive features, the authors motivate a stronger criterion—post-purification robustness—and propose a practical mitigation aimed at reducing the model’s susceptibility to reactivation, moving the field beyond ASR-centric notions of safety.

---
*Generated: 2026-01-06T23:33:36.271115*

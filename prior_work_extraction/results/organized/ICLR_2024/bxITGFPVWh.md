# Prior Work Analysis Report

## Target Paper

**Title:** Sharpness-Aware Data Poisoning Attack

**Conference:** ICLR 2024 (spotlight)

**Authors:** Pengfei He, Han Xu, Jie Ren, Yingqian Cui, Shenglai Zeng, Hui Liu, Charu C. Aggarwal, Jiliang Tang

**Keywords:** Data poisoning attack; generalization; deep learning

**Abstract:** 
> Recent research has highlighted the vulnerability of Deep Neural Networks (DNNs) against data poisoning attacks. These attacks aim to inject poisoning samples into the models' training dataset such that the trained models have inference failures. While previous studies have executed different types of attacks, one major challenge that greatly limits their effectiveness is the 
uncertainty of the re-training process after the injection of poisoning samples. It includes the uncertainty of training...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima** (2017)
- *Authors:* Nitish Shirish Keskar et al.
- *Direct Connection:* This work established loss-landscape sharpness as a proxy for generalization and sensitivity to training, providing the conceptual basis for modeling retraining uncertainty via sharpness in the poisoning objective.

### 💡 Inspiration

**Bullseye Polytope: A Scalable Clean-Label Poisoning Attack with Improved Transferability** (2021)
- *Authors:* Omid Aghakhani et al.
- *Direct Connection:* By targeting poisons that transfer across initializations and architectures, this work directly motivates SAPA’s goal of training-agnostic poisoning, which SAPA generalizes via a sharpness-based worst-case formulation.

### 🔍 Gap Identification

**MetaPoison: Practical General-purpose Clean-label Data Poisoning** (2020)
- *Authors:* Yuxin Huang et al.
- *Direct Connection:* MetaPoison’s bilevel, expectation-over-randomness approach to retraining uncertainty highlights the challenge of variability across seeds/augmentations, which SAPA addresses by replacing expectations with a sharpness-based worst-case surrogate.

### 📊 Baseline

**Witches’ Brew: Industrial Scale Data Poisoning via Gradient Matching** (2021)
- *Authors:* Jonas Geiping et al.
- *Direct Connection:* SAPA is instantiated on top of gradient-matching poisons to make them robust to retraining by optimizing their effect under worst-case weight perturbations, directly improving this primary baseline.

### 🔧 Extension

**Sharpness-Aware Minimization for Efficiently Improving Generalization** (2021)
- *Authors:* Pierre Foret et al.
- *Direct Connection:* SAPA extends SAM’s inner maximization over adversarial weight perturbations to the poisoning setting, directly using SAM’s sharpness surrogate to approximate the worst-case retrained model when optimizing poison data.

### 🔗 Related Problem

**Adversarial Weight Perturbation Helps Robust Generalization** (2020)
- *Authors:* Dongxian Wu et al.
- *Direct Connection:* By showing that maximizing loss over small weight perturbations captures worst-case behavior around a solution, this work motivates SAPA’s use of weight-space adversarial perturbations to represent retraining variability.

---

## Synthesis: How Prior Work Led to This Paper

Sharpness in loss landscapes was identified as a key indicator of generalization and sensitivity to training by Keskar et al., who connected sharp minima to instability with respect to initialization and training choices. Building on this insight, Foret et al. operationalized sharpness through sharpness-aware minimization (SAM), introducing an efficient inner maximization over small weight perturbations to approximate worst-case loss in a neighborhood. Wu et al. further validated the weight-perturbation perspective by showing that adversarial weight perturbations capture worst-case behavior and improve robust generalization, providing practical mechanisms for weight-space maximization. In parallel, Huang et al.’s MetaPoison framed neural network poisoning as a bilevel problem and attempted to handle retraining randomness via expectation over augmentations and training variations, exposing both the centrality of retraining uncertainty and the computational cost of expectation-based approaches. Geiping et al. introduced gradient matching, an efficient and strong poisoning objective widely used in practice but known to be brittle to victim training details. Aghakhani et al. explicitly pursued transferability across seeds and architectures in clean-label poisoning via geometric constraints, emphasizing the need for retraining-agnostic poisons. Taken together, these works suggest a gap: strong poisoning objectives lack principled robustness to retraining variability, while expectation-based defenses are costly and incomplete. The natural synthesis is to replace expectations with a worst-case surrogate grounded in sharpness: use weight-space adversarial perturbations (as in SAM/AWP) to model the hardest plausible retrained model and then optimize poisons against that surrogate. By embedding this sharpness-aware inner maximization into existing poisoning objectives like gradient matching, one obtains a general, training-agnostic poisoning strategy.

---

*Analysis generated on: 2026-01-06T10:49:10.389543*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

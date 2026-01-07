# Prior Work Analysis Report

## Target Paper
**Title:** gNiT81iag0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

TokenSwap’s core contribution—a post-hoc defense that mixes token probabilities from a large, capable but memorization-prone LM with those from a smaller, less-memorizing LM—emerges at the intersection of three lines of prior work. First, memorization risk was concretely characterized by Carlini et al. (2021) and later quantified across scales (Carlini et al., 2023), establishing that larger models regurgitate more and providing the exposure-style metrics used to assess defenses. Second, common mitigation baselines such as DP-SGD (Abadi et al., 2016) and unlearning frameworks like SISA (Bourtoule et al., 2021) require retraining and access to internal weights, making them impractical for typical model consumers—thus motivating a purely output-level, post-hoc intervention. Third, a stream of decoding-control methods demonstrated that multiple models’ probability signals can be combined at inference to steer generation without retraining: GeDi reweights logits using an auxiliary discriminator/LM, while Contrastive Decoding leverages a weaker reference model to shape token choices. TokenSwap repurposes this two-model decoding paradigm specifically for privacy/memorization: it selectively delegates function-word (and similarly common) token probabilities to a compact model that is fluent yet less prone to memorization. Distillation results (Sanh et al., 2019) underpin the feasibility of using small LMs to provide high-quality probabilities on such tokens, preserving grammaticality while disrupting memorized rare sequences. Together, these works directly inform TokenSwap’s design constraints, mechanism (probability-level composition), and evaluation against regurgitation.

---
*Generated: 2026-01-06T23:42:48.143259*

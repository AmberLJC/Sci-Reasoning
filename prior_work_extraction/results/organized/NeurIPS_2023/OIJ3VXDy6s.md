# Prior Work Analysis Report

## Target Paper
**Title:** OIJ3VXDy6s
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

RePo’s key contribution—a latent representation that is both maximally predictive of dynamics and reward while constraining observational information—sits at the confluence of information bottleneck theory and latent world-model RL. The Information Bottleneck (Tishby et al.) provides the conceptual grounding: compress observations to preserve only task-relevant predictive content. Deep VIB (Alemi et al.) translates this principle into a variational objective with a stochastic encoder and KL regularization, while β-VAE (Higgins et al.) demonstrates the practical power of capacity control via KL weighting to discard nuisance variation.

On the RL side, PlaNet and Dreamer establish the variational latent dynamics framework—RSSM with posterior–prior KL and learning control from imagined rollouts—upon which RePo is directly implemented. However, standard world-model training can over-encode visually salient but task-irrelevant factors. RePo modifies the regularization to prioritize posterior predictability, thereby selecting features that are predictable under the learned dynamics and informative for reward, which improves resilience to distractors.

This predictiveness criterion aligns tightly with the DeepMDP view of sufficient representations: latents should preserve exactly what is needed to model transitions and rewards. The bisimulation metrics literature (Ferns et al.) supplies the theoretical ideal—grouping states that are indistinguishable for control—clarifying why enforcing predictability and an information bottleneck jointly promotes invariance to spurious visual changes while maintaining control performance.

---
*Generated: 2026-01-06T23:42:49.062219*

# Prior Work Analysis Report

## Target Paper
**Title:** zk5k2NQcEA
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Score-of-Mixture Training (SMT) sits at the intersection of divergence-minimization and score-based learning. Lin’s formulation of Jensen–Shannon divergence (and its skewed variant) establishes the precise objective SMT targets. GANs subsequently operationalized JS minimization for generative modeling, while f-GAN framed a broader variational treatment over f-divergences (capturing α-skew JS), thereby motivating principled divergence choices in generative training. SMT departs from adversarial estimation by importing the score-based toolkit: Vincent’s denoising score matching showed that scores of smoothed distributions are learnable from corrupted samples, and Song & Ermon’s noise-conditional score networks extended this to multi-scale training, a blueprint SMT adopts when estimating scores of noise-corrupted mixtures of real and model samples across noise levels.

For fast generation, SMT is directly informed by the surge of one-step methods. Consistency Models demonstrated that a single forward pass can be trained either from scratch or via distillation from diffusion models, establishing both the training paradigm and the distillation template that SMT/SMD echo. Progressive Distillation further evidenced the feasibility of compressing diffusion samplers into few/one steps, which SMD adapts but replaces trajectory-focused objectives with an α-JS-driven mixture-score objective. Collectively, these works converge in SMT’s key contribution: a simple, stable, and principled one-step training framework that minimizes α-skew JS by learning the score of real–fake mixtures across noise scales, unifying divergence minimization with score estimation and supporting efficient distillation.

---
*Generated: 2026-01-07T00:21:32.385448*

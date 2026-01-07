# Prior Work Analysis Report

## Target Paper
**Title:** Vota6rFhBQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MeZO’s core idea—fine-tuning large language models using only forward passes—stands on the classic zeroth-order optimization paradigm developed for high-dimensional problems. Spall’s SPSA introduced the two-point simultaneous perturbation estimator, a minimal-query mechanism to approximate gradients from paired function evaluations; Ghadimi and Lan formalized stochastic zeroth-order methods via Gaussian smoothing and ZO-SGD templates; and Nesterov–Spokoiny clarified the variance and dimensional dependence of random-direction estimators. Together, these works provide the estimator, update rule, and theoretical caveats that MeZO adapts.

A second lineage demonstrated that such estimators can be practical for deep nets. OpenAI’s Evolution Strategies showed parameter-space perturbations scaling to millions of parameters, while ZOO established that query-based gradient estimates can effectively steer neural network objectives. These results directly motivate MeZO’s claim that forward-only, parameter-space optimization can work even for modern LMs, provided the implementation is efficient.

Finally, recent memory-efficient fine-tuning techniques for LMs—LoRA and QLoRA—shaped the problem focus: enabling strong downstream adaptation under tight GPU memory budgets. Whereas these approaches reduce memory by restricting trainable subspaces or quantizing weights while still relying on backprop, MeZO attacks the bottleneck at its source by eliminating backprop and optimizer state, executing ZO-SGD in-place so that training’s memory footprint matches inference. The synthesis of classical ZO estimators with LM-scale engineering yields a surprisingly competitive and highly memory-frugal fine-tuning method.

---
*Generated: 2026-01-07T00:02:04.799309*

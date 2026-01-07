# Prior Work Analysis Report

## Target Paper
**Title:** N8YbGX98vc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

TFG’s core contribution—an algorithm-agnostic, theoretically grounded framework that unifies training-free guidance for diffusion models—builds on two pillars: the score-based theory of conditional generation and a diverse set of practical, inference-time guidance mechanisms. The SDE formulation of score-based generative modeling formalized that conditioning is achieved by augmenting the prior score with the gradient of the conditional likelihood, directly motivating TFG’s view of guidance as adding a predictor-driven gradient term. Dhariwal and Nichol’s classifier guidance instantiated this idea with ∇ log p(y|x_t) from a noisy-image classifier, revealing practical knobs such as noise-dependent strength; Ho and Salimans’ classifier-free guidance crystallized the notion of a tunable guidance scale and schedules that trade off fidelity and diversity.

Subsequent training-free conditioning methods exposed the breadth and brittleness of these knobs. GLIDE’s CLIP-guided sampling showed that external predictors can steer diffusion without retraining, but require delicate, task-specific tuning. Inverse-problem methods like DDRM and DPS demonstrated training-free conditioning via projection or data-consistency gradients, further diversifying where and how guidance can be injected in the sampling trajectory. TFG identifies the common structure across these approaches—predictor choice, normalization, timing, and strength scheduling—and provides theoretical analysis and a robust hyperparameter search strategy that applies uniformly across models and tasks. By encompassing classifier-guided, CLIP-guided, and inverse-problem guidance as special cases, TFG converts a fragmented set of heuristics into a unified design space, delivering consistent performance gains across a wide benchmark.

---
*Generated: 2026-01-06T23:33:35.560006*

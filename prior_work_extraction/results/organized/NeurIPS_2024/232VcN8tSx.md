# Prior Work Analysis Report

## Target Paper
**Title:** 232VcN8tSx
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

GREATS sits at the intersection of online subset selection, gradient/Taylor-based utility estimation, and greedy optimization. Its most direct antecedent is GLISTER, which formalized data selection as maximizing a first-order (Taylor) surrogate of generalization performance and solved it greedily each iteration; GREATS adopts the same core machinery but pivots the objective to the immediate training-loss decrease induced by an SGD step, a choice that removes reliance on validation surrogates and scales more naturally to LLM training. GradMatch likewise established that gradients provide a faithful target for subset construction by matching the full-batch gradient; GREATS retains the gradient-centric view but replaces gradient matching with a Taylor approximation of loss reduction, which is more directly aligned with per-step optimization and computationally lighter.
Active learning advances such as BADGE demonstrated that gradient embeddings encode both informativeness and diversity, often optimized via greedy selection; GREATS echoes this but grounds selection in an explicit loss-decrease objective, letting diversity emerge through diminishing returns in the greedy process. The theoretical legitimacy for using Taylor expansions to quantify data influence traces to influence functions, which approximate loss changes from small parameter updates; GREATS applies a similar first-order perspective without expensive Hessian computations. Earlier efficiency-oriented selection methods, including importance sampling and online batch selection based on losses or gradient norms, motivated the need for principled scoring but were heuristic or variance-focused; GREATS unifies these signals into a single Taylor-based criterion. Finally, Taylor saliency from network pruning provided a template for estimating loss impact via first-order terms, which GREATS repurposes from pruning parameters to selecting training examples in every iteration.

---
*Generated: 2026-01-07T00:02:04.733609*

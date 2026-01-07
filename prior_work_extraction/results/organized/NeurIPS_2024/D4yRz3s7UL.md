# Prior Work Analysis Report

## Target Paper
**Title:** D4yRz3s7UL
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

DeSparsify emerges at the intersection of adaptive vision transformer design and resource-focused adversarial ML. The ViT formulation by Dosovitskiy et al. established both the tokenization interface and the quadratic cost scaling that make token count a critical lever. Efficiency methods such as DynamicViT and TokenLearner then introduced differentiable, input-dependent token selection, while ToMe generalized token reduction via similarity-driven merging. Collectively, these sparsification mechanisms rely on average-case behavior: most inputs permit aggressive token reduction without harming accuracy.

Resource-centric attacks disrupted this assumption. Sponge Examples showed that models can be manipulated to maximize energy and latency consumption, and DeepSloth revealed that adaptive inference policies (e.g., early exits) can be adversarially coerced into worst-case execution paths. DeSparsify fuses these two lines: it recasts token sparsification as a vulnerable adaptive policy and optimizes inputs—via gradients over token-importance/selectors or token-similarity structures—to suppress pruning/merging at each stage. This forces a cascade of maximal token retention, turning the quadratic cost into a denial-of-availability vector that exhausts OS resources. Crucially, by leveraging the differentiable nature of modern sparsifiers (DynamicViT, TokenLearner) and the structural properties of merging (ToMe), DeSparsify remains broadly applicable while preserving task semantics for stealth. In short, DeSparsify translates slowdown/energy-attack principles into the specific mechanics of token sparsification in ViTs, weaponizing adaptivity against itself.

---
*Generated: 2026-01-06T23:33:36.291174*

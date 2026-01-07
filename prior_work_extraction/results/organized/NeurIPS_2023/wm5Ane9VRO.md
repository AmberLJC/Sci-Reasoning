# Prior Work Analysis Report

## Target Paper
**Title:** wm5Ane9VRO
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—jointly maximizing Average Precision (AP) while enforcing adversarial ranking robustness—sits at the confluence of two lines of work: direct optimization of non-decomposable ranking metrics and adversarial robustness via consistency regularization. On the ranking side, Joachims (2005) introduced structural optimization for non-decomposable measures, and Yue et al. (2007) specialized this to AP, demonstrating that AP can be targeted directly through appropriate surrogates. Taylor et al. (2008) further enabled practical optimization by smoothing inherently non-differentiable rank-based objectives, paving the way for differentiable AP surrogates compatible with deep networks. On the robustness side, Madry et al. (2018) established the min–max adversarial training framework, while Miyato et al. (2018) and Zhang et al. (2019, TRADES) showed the efficacy of enforcing prediction consistency between clean and adversarially perturbed inputs through regularization. This paper synthesizes these strands by (i) adopting an AP-focused surrogate to train models explicitly for ranking quality under class imbalance, and (ii) introducing a ranking-consistency regularizer that, in the spirit of VAT/TRADES, penalizes disagreements between clean and adversarial orderings rather than only mismatched class probabilities. The result is a principled objective that preserves the ranking structure crucial to AP in the presence of adversarial perturbations, bridging the gap between accuracy-oriented robustness and ranking-aware performance optimization.

---
*Generated: 2026-01-06T23:42:49.069168*

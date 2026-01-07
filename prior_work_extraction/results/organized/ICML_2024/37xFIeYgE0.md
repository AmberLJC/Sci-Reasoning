# Prior Work Analysis Report

## Target Paper
**Title:** 37xFIeYgE0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core idea—replacing scalar, expectation-based payoffs with random-variable “distributional values” to explain probabilistic models—stands on the axle of cooperative game theory and its adaptation to ML. Shapley’s axioms (1953) provide the allocation blueprint that virtually all attribution methods, including SHAP (Lundberg & Lee, 2017), follow. Early practical instantiations (Štrumbelj & Kononenko, 2014) operationalized Shapley via conditional/marginal expectations, cementing the convention that the value operator is an expectation of a scalar output. Subsequent work (Aas et al., 2021) showed that the choice of operator—marginal vs conditional expectation—materially changes explanations when features are dependent, underscoring that the operator must align with the explanandum. Parallel to this, Shapley Effects (Owen & Prieur, 2017) demonstrated that Shapley principles can attribute distributional properties like variance, not just means, hinting at a broader class of distribution-aware values. Finally, counterfactual explanations (Wachter et al., 2017) shifted attention from probabilities to decisions, emphasizing outcome flips as the target of explanation. Synthesizing these strands, the present paper generalizes the game and value operator so that the payoff itself is a random variable capturing distributional events (e.g., class flips) and derives analytic forms for Gaussian, Bernoulli, and Categorical payoffs. This resolves the mismatch between what practitioners want to explain (decisions and distributional behavior) and what classic Shapley-style methods quantify (scalar averages), while preserving desirable axiomatic properties.

---
*Generated: 2026-01-06T23:42:48.053525*

# Prior Work Analysis Report

## Target Paper
**Title:** U4BC0GrFAz
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core hypothesis scrutinized in this paper—that predictors built on causal features generalize better across domains—emerges from the invariance perspective crystallized by Peters, Bühlmann, and Meinshausen’s invariant causal prediction and extended by causal transfer works such as Rojas-Carulla et al. and Magliacane et al. These works argue that causal parents induce invariant conditionals across environments, suggesting that restricting models to such variables should enhance out-of-domain reliability. Arjovsky et al.’s Invariant Risk Minimization operationalized this idea algorithmically, aiming to learn representations whose predictive relations are stable across environments. Complementing these, Subbaswamy, Schulam, and Saria advanced causality-guided adjustment and feature selection to build transportable predictors, while Pearl and Bareinboim’s transportability framework provided the theoretical foundation that causal relations can be moved across populations under specified conditions. At the same time, critiques such as Rosenfeld et al. highlighted that IRM’s invariance objective can be brittle, raising doubts about practical gains.

Building on and directly testing these claims, the present study constructs a broad empirical evaluation across 16 tabular tasks with multiple domains and carefully identified causal features. Contrary to the invariance-based expectation, models limited to causal features did not outperform models using all available features either in-domain or out-of-domain, nor did they exhibit smaller accuracy drops across domains. The findings therefore challenge a central practical implication of causal-invariance theory: in realistic tabular settings, excluding non-causal but predictive variables offers no observed OOD advantage and often harms overall accuracy, calling for a reassessment of when and how causal constraints translate into tangible generalization benefits.

---
*Generated: 2026-01-06T23:33:35.536364*

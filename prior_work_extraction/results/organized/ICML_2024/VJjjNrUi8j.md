# Prior Work Analysis Report

## Target Paper
**Title:** VJjjNrUi8j
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core innovation of the ICML 2024 paper is an axiomatized, distance-based framework for quantifying predictive uncertainty when predictions are second-order distributions (distributions over class-probability vectors), with a concrete instantiation via the Wasserstein distance. This advances—and corrects—prior second-order approaches that relied on Dirichlet-based models and entropy/mutual-information functionals. Sensoy et al. (2018) and Malinin & Gales (2018) established the practical template of predicting a distribution over the simplex (e.g., a Dirichlet) and quantifying aleatoric/epistemic uncertainty via entropy and mutual information; however, these measures exhibit pathological behaviors that recent work has surfaced. The mutual-information lens itself stems from the BALD principle (Houlsby et al., 2011), whose adoption in second-order classification motivated a careful re-examination of whether MI satisfies desirable properties in this context.
Grounding the remedy, the paper draws on the axiomatic viewpoint of Gneiting & Raftery (2007) to articulate formal criteria for uncertainty functionals, aligning with the broader taxonomy and desiderata synthesized in Hüllermeier & Waegeman (2021). Conceptually, Murphy’s (1973) Brier-score decomposition provides a distance-based prototype for separating components of uncertainty, inspiring the move from entropy/MI to metric-based constructions that admit clean decompositions and monotonicity guarantees. Finally, Peyré & Cuturi (2019) supply the optimal-transport machinery that makes Wasserstein distances on the simplex—and their lifting to distributions over distributions—both principled and practical. Together, these works directly shaped a framework that is axiomatic in spirit, second-order in scope, and Wasserstein in implementation.

---
*Generated: 2026-01-06T23:42:48.064528*

# Prior Work Analysis Report

## Target Paper
**Title:** gGl0n7Onug
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The NeurIPS 2023 paper re-evaluates influence functions (IF) in the context of modern deep networks by interrogating the precise assumptions needed for IF to predict leave-one-out effects. Its starting point is the classical statistical notion of influence (Hampel), and its most direct antecedent is Koh and Liang’s adaptation of IF to deep learning, which operationalized IF via H^{-1}v computations to attribute predictions to training points. This operationalization depends on efficient curvature primitives—Pearlmutter’s Hessian–vector products and stochastic inverse-Hessian estimators like LiSSA—that made IF scalable but also introduced numerical stability and damping choices that the paper shows can critically affect accuracy.
At the modeling level, the paper contrasts IF’s local, single-iterate linearization with trajectory-aware perspectives such as TracIn, which empirically demonstrated that SGD path information can dominate attribution quality in non-convex regimes. Complementarily, Representer Point Selection crystallized how strong convexity and L2 regularization enable clean data-to-prediction decompositions, highlighting assumptions that often fail in contemporary deep models.
Synthesizing these strands, the paper systematically identifies five problematic assumptions—centered on convexity, numerical conditioning, training trajectory, and especially parameter divergence—and delineates which can be mitigated and which constitute fundamental roadblocks. Insights from curvature-rich optimization (e.g., Martens) help explain why local second-order approximations can be unstable or misleading when retraining moves parameters across different basins. The result is a clarified theoretical and practical scope for IF: some limitations are addressable, but parameter divergence poses a principled barrier to reliably predicting retraining effects in modern deep networks.

---
*Generated: 2026-01-07T00:02:04.783581*

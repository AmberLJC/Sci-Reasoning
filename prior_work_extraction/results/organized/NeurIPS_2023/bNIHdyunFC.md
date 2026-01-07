# Prior Work Analysis Report

## Target Paper
**Title:** bNIHdyunFC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core idea—learning the amount of equivariance in each layer via gradients and marginal likelihood—sits at the intersection of equivariant architectures and Bayesian evidence optimization. Group Equivariant CNNs established the benefits of encoding symmetry via hard constraints, while Equivariance Through Parameter-Sharing clarified that such symmetries arise from weight-tying/connectivity patterns. Steerable CNN frameworks generalized these constructions with flexible filter bases for Euclidean groups, informing how layer-wise equivariances can be parameterized. However, these approaches fix symmetries a priori.

Augerino shifted the paradigm by learning symmetries directly from data through differentiable objectives, demonstrating that invariances need not be prescribed. In probabilistic modeling, Learning Invariances Using the Marginal Likelihood showed that the evidence can balance data fit and model complexity to infer invariances automatically. Bringing this insight to deep networks requires scalable, differentiable approximations to the marginal likelihood; Laplace Redux provided exactly this tool, while earlier scalable Laplace methods (e.g., K-FAC-based Laplace) made evidence estimation practical for large networks.

Combining these strands, the paper introduces improved soft parameterizations of layer-wise equivariance (informed by steerable/parameter-sharing views) and learns their strength via differentiable Laplace-approximated marginal likelihood. This unifies symmetry discovery with Bayesian model selection, enabling data-driven, layer-specific equivariance that adapts beyond fixed group assumptions while preserving computational tractability.

---
*Generated: 2026-01-07T00:02:04.782180*

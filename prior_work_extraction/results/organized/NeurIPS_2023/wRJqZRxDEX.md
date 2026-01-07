# Prior Work Analysis Report

## Target Paper
**Title:** wRJqZRxDEX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Doshi, He, and Gromov build on the mean-field and infinite-width program that connects initialization to trainability. The Gaussian-process perspective (Lee et al., 2018) grounds their use of layerwise statistics in the wide-limit, while edge-of-chaos analyses (Poole et al., 2016; Schoenholz et al., 2017) supply the conceptual link between criticality and stable information flow. Earlier work stabilized training via variance tuning (Sussillo & Abbott, 2015) and revealed how normalization and residual connections reshape signal propagation (Pennington et al., 2017). Complementarily, spectral studies of the input–output Jacobian (Pennington et al., 2018) formalized dynamical isometry as a target for robust gradient flow. 

The key advance here is to shift from global or purely forward-propagation metrics to partial Jacobians—derivatives from preactivations at layer l0 to those at layer l—which directly probe the stability of gradients and signals between arbitrary depths. The authors derive recurrence relations for norms of these partial Jacobians and turn them into a simple numerical test for criticality. This unifies and extends prior criteria by (i) providing a local-in-depth diagnostic tighter than input–output Jacobian analyses, (ii) encompassing architectures with residual connections and LayerNorm within the same framework, and (iii) using the recurrences to select weight and bias variances and learning rates in practice. In short, the work operationalizes the edge-of-chaos/dynamical-isometry intuition at a finer granularity and for modern architectures, delivering a practical and theoretically grounded initialization procedure.

---
*Generated: 2026-01-06T23:42:49.114240*

# Prior Work Analysis Report

## Target Paper
**Title:** t7euV5dl5M
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Approximation-Aware Bayesian Optimization (AABO) fuses two historically separate threads: scalable Gaussian process approximation and decision-theoretic acquisition design. The inducing-point lineage—beginning with pseudo-input sparse GPs (Snelson & Ghahramani, 2006) and formalized via variational inducing variables (Titsias, 2009)—made GPs computationally viable for large or high-dimensional BO, but at the cost of approximation bias. Hensman et al. (2013) further enabled stochastic variational inference for GPs (SVGP), cementing a practical training objective (ELBO) and optimization pipeline. However, standard SVGP training optimizes global posterior fidelity rather than the quality of BO decisions derived from that posterior. The decision-theoretic perspective in BO, epitomized by Expected Improvement (Jones et al., 1998), defines an explicit utility for data acquisition; yet typical pipelines treat acquisition optimization and model approximation as decoupled. AABO’s central step is to adopt utility-calibrated variational inference (Lacoste-Julien et al., 2011), replacing a pure evidence objective with one that explicitly optimizes the approximate posterior for the downstream acquisition utility. This yields a joint objective that differentiates the acquisition (e.g., EI) through the GP approximation, aligning limited computational resources with decision quality rather than global fit. Finally, high-dimensional trust-region BO such as TuRBO (Eriksson et al., 2019) motivates AABO’s design constraints and illustrates its plug-in compatibility: the acquisition-calibrated SVGP can be dropped into TuRBO to improve query selection under tight budgets. Together, these works directly scaffold AABO’s idea of approximation-aware, decision-aligned GP training for BO.

---
*Generated: 2026-01-06T23:33:35.545202*

# Prior Work Analysis Report

## Target Paper
**Title:** mKYBMf1hHG
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The core contribution of "Rethinking Data Shapley for Data Selection Tasks" is a principled characterization of when Data Shapley (DS) helps or misleads in data selection. This work directly builds on Ghorbani and Zou’s introduction of DS, which positioned Shapley-based data valuation as a general tool and showcased data selection use cases, and on Jia et al.’s efficient DS estimation, which broadened applicability while revealing mixed empirical performance. The paper leverages Shapley’s axioms to analyze how value assignments relate to marginal contributions under structured utilities, making the link between axiomatic properties and selection optimality explicit.

Crucially, the authors situate data selection within the modular/submodular framework popularized by Wei, Iyer, and Bilmes and underpinned by Nemhauser–Wolsey–Fisher. By aligning DS with additive (modular) utilities and showing that monotone transformations preserve the relevant ordering for selection, they identify a class in which DS is optimal. This structural view explains prior empirical inconsistencies: DS excels when the task utility is effectively modular, but can be unreliable otherwise.

Finally, echoing the spirit of Wolpert and Macready’s No Free Lunch results, the authors formalize that without constraints on the utility function, DS cannot be guaranteed to outperform random selection. This motivates their hypothesis-testing framework and predictive heuristic for DS effectiveness, providing a unifying theory that reconciles earlier positive and negative findings about DS in data selection.

---
*Generated: 2026-01-07T00:02:04.896881*

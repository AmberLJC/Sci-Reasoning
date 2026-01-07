# Prior Work Analysis Report

## Target Paper
**Title:** xWI0MKwJSS
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The ICML 2024 paper targets a widely overlooked mismatch: practitioners typically implement DP-SGD with shuffled, fixed-size minibatches (sampling without replacement) yet analyze privacy using Poisson-subsampled accountants. The intellectual pathway to this finding begins with Abadi et al. (2016), which introduced DP-SGD and the moments accountant, setting the canonical mechanism and practice of subsampling-based analysis. Mironov’s Rényi Differential Privacy (2017) then provided a powerful composition framework that enabled tight, scalable accounting. Building on RDP, Wang, Balle, and Kasiviswanathan (2019) delivered tight bounds for the subsampled Gaussian mechanism and the analytical moments accountant, cementing Poisson subsampling as the default analysis path and powering modern open-source accountants.

However, the training-time reality often uses shuffled, without-replacement minibatching. Balle and Wang (2018) gave tight amplification results that separate Poisson and without-replacement sampling, highlighting that the sampling rule fundamentally changes privacy. Feldman et al. (2018) further developed privacy amplification by iteration, offering tools to reason about iterative procedures like DP-SGD under shuffling. Finally, Dong, Roth, and Su (2019) introduced Gaussian Differential Privacy, a unifying metric that normalizes comparisons across analyses.

Together, these works enabled precise Poisson-based accounting while revealing conceptual gaps for shuffling-based implementations. The ICML 2024 paper leverages this foundation to formalize DP-SGD as post-processing of adaptive batch linear queries and to demonstrate that shuffling and Poisson subsampling can yield substantially different privacy guarantees—showing that prevalent practice can materially misestimate privacy.

---
*Generated: 2026-01-06T23:42:48.071756*

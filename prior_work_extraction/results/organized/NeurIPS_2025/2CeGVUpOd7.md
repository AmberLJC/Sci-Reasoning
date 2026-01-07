# Prior Work Analysis Report

## Target Paper
**Title:** 2CeGVUpOd7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—recovering the eigenvalue distribution of a large, impalpable matrix from only tiny masked submatrices—stands on three converging lines of prior work. First, free probability provides the conceptual and analytic backbone. Results summarized in Anderson–Guionnet–Zeitouni and refined in Benaych-Georges establish how spectral laws transform under projection/rectangular operations (free compression), via Stieltjes/Blue transforms and subordination. The present method inverts that map: given the spectrum of compressed (masked) principal blocks, it performs a free decompression to estimate the original global spectrum.

Second, practical deconvolution of spectral laws has precedents in high-dimensional covariance estimation. Ledoit–Wolf’s QuEST shows how to invert Marčenko–Pastur to estimate population spectra from sample eigenvalues, while Dobriban develops stable numerical solvers for the associated fixed-point/subordination equations. This work adapts those numerical ideas to the compression-induced transforms, yielding a robust pipeline for decompression from limited, blockwise access.

Third, the access model and evaluation targets connect to scalable spectral approximation in ML. Nyström methods demonstrate that small submatrices can retain essential spectral information of kernels, inspiring the use of restricted sub-blocks. Meanwhile, matvec-based estimators like Stochastic Lanczos Quadrature motivate the need for an alternative when even implicit operators are unavailable, while still aiming to compute quantities such as log-determinants and traces of matrix functions. Together, these works directly shape the paper’s theory, algorithms, and problem framing.

---
*Generated: 2026-01-06T23:42:48.163666*

# Prior Work Analysis Report

## Target Paper
**Title:** kePsKwxvaV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s key contribution—purifying Shampoo by decoupling its preconditioner into eigenvalues and eigenbasis, then replacing learning-rate grafting with direct eigenvalue correction and adaptively scheduling eigenbasis updates—sits at the intersection of Kronecker-factorized preconditioning and adaptive methods. Shampoo (Gupta et al., 2018) provided the core Kronecker-factored preconditioner that this work dissects, while subsequent scalable implementations (Anil et al., 2020) introduced the very heuristics—learning-rate grafting to Adam and stale/periodic preconditioning—that the authors analyze and aim to replace. Adam (Kingma & Ba, 2015) is central because its magnitude is the object of grafting; the authors reinterpret this magnitude transfer as implicitly correcting mis-scaled eigenvalues and formalize a Frobenius-norm approximation to full-matrix Adam to perform that correction directly.
K-FAC (Martens & Grosse, 2015) established Kronecker factorization and routine staleness in curvature updates, shaping the notion that eigenbases can be recomputed infrequently. EKFAC (George et al., 2018) is a particularly direct antecedent: it decouples eigenbasis and eigenvalues and performs Frobenius-optimal eigenvalue correction in a fixed basis, mirroring the present work’s decomposition and correction strategy but applied to Shampoo’s adaptive preconditioner and to full-matrix Adam. Finally, Adafactor (Shazeer & Stern, 2018) demonstrated factored second-moment estimation and step-magnitude heuristics that informed Shampoo-at-scale practice; this paper replaces such scale-dependent heuristics with principled eigenvalue corrections and an adaptive criterion for when to refresh the eigenbasis.

---
*Generated: 2026-01-06T23:42:48.128356*

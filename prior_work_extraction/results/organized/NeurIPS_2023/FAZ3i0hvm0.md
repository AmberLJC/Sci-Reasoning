# Prior Work Analysis Report

## Target Paper
**Title:** FAZ3i0hvm0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The key contribution of “A Privacy-Friendly Approach to Data Valuation” is to redesign a practical Shapley-based data valuation method—KNN-Shapley—so that it admits principled differential privacy guarantees with strong utility. This work is rooted in the data-Shapley line inaugurated by Ghorbani and Zou, which formalized per-example valuation via Shapley values, and in the scalability-focused advances by Jia et al., which made Shapley-style valuation practical and motivated specialized estimators like KNN-based valuation. KNN-Shapley itself is the immediate methodological predecessor: it delivers efficient, accurate valuations by exploiting the structure of k-nearest neighbor prediction, but its dependence on many records creates high and data-dependent sensitivity, exposing privacy risks.
To overcome these obstacles, the paper draws on core DP principles from Dwork et al., using sensitivity-calibrated noise to protect individuals, and on smooth-sensitivity ideas from Nissim et al., which motivate structurally bounding contributions so that useful noise magnitudes become feasible. The proposed truncation/refinement in TKNN-Shapley effectively localizes influence to a bounded neighborhood, taming sensitivity and enabling straightforward privatization. Gaussian DP (Dong, Roth, Su) provides tight accounting for the added noise, clarifying the privacy–utility frontier and demonstrating superiority over naive privatization of KNN-Shapley. Finally, membership-inference work by Shokri et al. underscores the real-world risks of releasing non-private data valuations, strengthening the case for DP-TKNN-Shapley as a safer default. Collectively, these prior works shape both the valuation objective and the privacy-aware algorithmic design that defines the paper’s contribution.

---
*Generated: 2026-01-06T23:33:35.593188*

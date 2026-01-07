# Prior Work Analysis Report

## Target Paper
**Title:** HN05DQxyLl
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—approximating mutual information for very high-dimensional variables by estimating MI on learned low-dimensional representations—sits at the intersection of MI estimation and multiview representation learning. Classical nonparametric estimators like KSG established a reliable way to compute MI but break under high dimensionality; LMI preserves their strengths by first compressing the data, then applying KSG where it is accurate. Neural MI estimators (MINE) and contrastive bounds (InfoNCE/CPC) motivated the need for a different route: while they scale to large models, they suffer from bias, variance, and calibration issues that make numeric MI unreliable in high dimensions. LMI avoids these pitfalls by not estimating MI directly in the original space.

Information Bottleneck theory provides the conceptual backbone: learn compressed representations that retain the information relevant to the other variable. Variational IB supplies practical stochastic encoders and regularization to enforce compactness while preserving dependence. Deep CCA demonstrates that two-tower networks can concentrate cross-view dependence into a small number of shared components; the probabilistic view of CCA further clarifies that, in Gaussian settings, MI is governed by a few canonical factors—precisely the structure LMI seeks to uncover nonlinearly. By combining IB-inspired two-view encoders with nonparametric MI estimation on the resulting latents, LMI overcomes the curse of dimensionality and yields accurate MI approximations for variables with thousands of dimensions.

---
*Generated: 2026-01-07T00:02:04.761913*

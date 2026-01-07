# Prior Work Analysis Report

## Target Paper
**Title:** KFm2lZiI7n
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MeCo emerges at the intersection of zero-shot NAS practice and spectral theory of over-parameterized training. On the theory side, NTK analysis (Jacot et al., 2018) and over-parameterization convergence results (Allen-Zhu et al., 2019) show that optimization speed and stability hinge on the spectrum—especially the minimum eigenvalue—of data- or feature-induced Gram matrices. Deep Information Propagation (Schoenholz et al., 2017) further links activation correlations to effective signal flow, suggesting that correlation structure is diagnostic of trainability and generalization.

On the NAS side, NASWOT (Mellor et al., 2021) proved that forward-pass activation correlations can reliably rank architectures without training, while the Zero-Cost Proxies benchmark (Abdelfattah et al., 2021) established the landscape of training-free metrics—many relying on backprop, labels, or sizable data batches (e.g., SNIP). These works motivate MeCo’s design goals: eliminate backprop and labels, minimize data needs, and retain high correlation with true performance.

MeCo synthesizes these threads by operationalizing a theoretically grounded spectral statistic—the minimum eigenvalue of the Pearson correlation matrix of feature maps—as a one-sample, single-forward-pass proxy for both convergence rate and generalization capacity. It departs from prior forward-only methods by collapsing the requirement of a batch to just one input and by focusing on a sharper spectral indicator (minimum eigenvalue) rather than determinants or heuristic scores. In doing so, MeCo directly addresses the computational and data dependencies highlighted by earlier proxies, while aligning closely with spectral theory that predicts how and why architectures train effectively.

---
*Generated: 2026-01-06T23:42:49.097319*

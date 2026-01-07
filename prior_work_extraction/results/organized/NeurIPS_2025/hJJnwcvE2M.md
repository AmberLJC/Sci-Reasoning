# Prior Work Analysis Report

## Target Paper
**Title:** hJJnwcvE2M
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

SPAGD sits at the intersection of reconstruction-based TS anomaly detection, graph-based dependency modeling, and data imbalance mitigation through auxiliary signals. Variational autoencoders (Kingma & Welling) underpin SPAGD’s reconstruction stage, whose residuals become a first-class signal. OmniAnomaly demonstrated the efficacy and limits of reconstruction-centered multivariate TSAD: it captures normal dynamics but can overfit and miss subtle deviations. SPAGD tackles this by converting reconstruction residuals into two mechanisms—self-perturbations that generate pseudo-anomalies to relieve class imbalance, and anomaly-aware cues that adapt the dependency graph. The graph component traces to GAT, enabling learnable, time-varying inter-variable weights; MTAD-GAT brought this idea to TSAD, showing that modeling sensor relations boosts detection. SPAGD pushes further by making the graph explicitly responsive to residuals from self-perturbed data, steering edges toward correlations most informative for anomalies rather than purely normal dynamics. Complementing this, Outlier Exposure’s principle—training with auxiliary atypical samples to improve boundary awareness—motivates SPAGD’s internal pseudo-anomaly generation without requiring external outliers. Finally, Anomaly Transformer’s association-discrepancy perspective highlights that subtle anomalies often manifest as shifts in relational structure; SPAGD embraces this by using residuals to drive dynamic, anomaly-aware graph reweighting. Together, these strands yield a framework that balances scarce anomalies, adapts to evolving inter-variable correlations, and resists overfitting to normal reconstructions.

---
*Generated: 2026-01-07T00:21:32.304984*

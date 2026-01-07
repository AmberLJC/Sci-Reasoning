# Prior Work Analysis Report

## Target Paper
**Title:** HZQZli6amV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Teney et al.’s core contribution—showing that ID and OOD performance can be inversely correlated on real-world datasets and explaining why prior studies often miss this—emerges from reconciling two influential but seemingly conflicting lines of work. On one side, corruption and natural shift benchmarks such as ImageNet-C (Hendrycks & Dietterich, 2019) and ImageNet-based evaluations (Taori et al., 2020; Recht et al., 2019) repeatedly reported strong positive associations between ID accuracy and performance under shift, encouraging the community to treat ID gains as a proxy for OOD gains. On the other side, theory and group-shift studies indicated inherent tensions: Tsipras et al. (2019) formalized accuracy–robustness trade-offs, while Sagawa et al. (2020) demonstrated that ERM can excel on average yet fail on minority groups due to spurious correlations. Teney et al. synthesize these perspectives by arguing that the prevailing empirical evidence of positive correlations stems from methodological biases—evaluating along narrow model families or selection criteria that favor monotonic ID improvements—thereby masking regimes where robust and spurious features compete and induce inverse ID–OOD trends. Methodological frameworks emphasizing careful, standardized evaluation (Gulrajani & Lopez-Paz, 2021) and real-world shift testbeds (Koh et al., 2021) provide the tools and datasets enabling Teney et al. to surface these inverse patterns beyond synthetic or worst-case constructions. The result is a reframing: while positive correlations can occur, they are not universal; in some realistic settings, optimizing ID performance can harm OOD generalization, necessitating evaluation and model selection practices that explicitly account for distribution shift.

---
*Generated: 2026-01-07T00:02:04.840912*

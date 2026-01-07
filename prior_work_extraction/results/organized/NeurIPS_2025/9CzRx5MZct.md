# Prior Work Analysis Report

## Target Paper
**Title:** 9CzRx5MZct
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Asymmetric Duos build on a decade of evidence that combining models substantially improves both accuracy and uncertainty quality, while rethinking how to do so under modern compute and fine-tuning constraints. Deep Ensembles established the gold standard for calibrated uncertainty and selective prediction, and follow-up work highlighted that ensembles remain the strongest practical baseline. However, their cost scales with the number and size of members, clashing with today’s large models and rapid fine-tuning workflows. A line of efficient alternatives—Snapshot Ensembles, SWAG, and BatchEnsemble—pursued lower-overhead ensembling through trajectory sampling, posterior approximation, or parameter sharing, demonstrating that much of the ensemble benefit can be retained with less computation. In parallel, Model Soups showed that simple averaging can be surprisingly effective in weight space during fine-tuning. Asymmetric Duos synthesize these insights: retain the core ensemble principle (diversity boosts uncertainty and accuracy) but make it compute-friendly by pairing a high-performing large model with a much smaller, cheaper “sidekick,” then fusing their predictions via a learned weighted combiner rooted in stacked generalization. The key leap is embracing architectural asymmetry and heterogeneity as a source of complementary errors while using an extremely simple, data-driven aggregation rule. This yields ensemble-like gains in calibration and selective classification at a fraction of the traditional cost, fitting real-world fine-tuning practice.

---
*Generated: 2026-01-07T00:05:12.527714*

# Prior Work Analysis Report

## Target Paper
**Title:** xOJUmwwlJc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core innovation of Proximity-Informed Calibration is to expose and correct a systematic, sample-dependent failure mode of modern calibrators: proximity bias—overconfidence that grows in sparse, low-density regions of the data distribution. This builds on two strands of prior art. First, calibration foundations (Guo et al.) and evaluations under shift (Ovadia et al.) establish both the centrality of post-hoc calibration and its degradation when test inputs diverge from training data. The paper reframes this as a within-distribution heterogeneity problem, where low-proximity samples locally resemble shifted data. Second, proximity-sensitive reliability signals from representation space—Trust Score (Jiang et al.), Deep kNN (Papernot & McDaniel), Mahalanobis distance (Lee et al.), and energy scores (Liu et al.)—demonstrate that nearness to the training manifold is a strong predictor of correctness and uncertainty. These works provide concrete, scalable proxies (kNN density, class-conditional Gaussian distance, energy) that the paper can directly adopt to quantify proximity. Finally, advanced multiclass calibrators like Dirichlet calibration (Kull et al.) underscore that strong global post-hoc schemes still ignore sample-specific structure. The present paper synthesizes these insights: it diagnoses miscalibration stratified by proximity, shows the persistence of the issue across architectures and after standard calibrators, and proposes a proximity-informed calibration procedure that conditions the mapping from logits to probabilities on a representation-space proximity measure, thereby delivering more consistent calibration across dense and sparse regions.

---
*Generated: 2026-01-06T23:42:49.111322*

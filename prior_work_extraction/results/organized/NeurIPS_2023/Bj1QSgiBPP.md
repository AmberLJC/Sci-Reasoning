# Prior Work Analysis Report

## Target Paper
**Title:** Bj1QSgiBPP
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central innovation is a model-agnostic, prediction-time mechanism that lets individuals opt into revealing a sensitive group attribute only when it yields demonstrable benefit—thereby operationalizing consent while improving accuracy and privacy. Two streams of prior work directly converge to enable this idea. First, fairness research established that using protected attributes at decision time can be necessary to achieve desirable properties. Equality of Opportunity (Hardt et al., 2016) and On Fairness and Calibration (Pleiss et al., 2017) formalized group-dependent thresholds and trade-offs, providing the normative and technical basis for personalization with group attributes. Second, selective and deferred decision-making provided the algorithmic blueprint for when to engage personalization. Learning to Defer (Madras et al., 2018) learns a gate based on predicted error differences between experts, which maps cleanly onto deciding between a non-personalized model and a group-personalized one; SelectiveNet (Geifman & El-Yaniv, 2019) reinforces the accuracy–coverage framing that underlies optional engagement. The test-time feature acquisition literature (Nan et al., 2017) contributes the notion of treating group membership as a costly/sensitive feature whose acquisition is a decision variable, aligning with the paper’s opt-in mechanism. Finally, uplift/heterogeneous treatment effect estimation (Künzel et al., 2019) supplies model-agnostic techniques to estimate the individual benefit from personalization, which the system exposes to facilitate informed consent, while work on fairness without observed demographics (Kallus et al., 2020) grounds the comparisons to imputation/proxy-based alternatives when users decline disclosure.

---
*Generated: 2026-01-06T23:42:49.068139*

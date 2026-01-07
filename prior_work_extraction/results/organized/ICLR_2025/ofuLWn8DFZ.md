# Prior Work Analysis Report

## Target Paper

**Title:** Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yan Scholten, Stephan Günnemann

**Keywords:** Conformal prediction, Certifiable robustness, Adversarial robustness

**Abstract:** 
> Conformal prediction provides model-agnostic and distribution-free uncertainty quantification through prediction sets that are guaranteed to include the ground truth with any user-specified probability. Yet, conformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, which can significantly alter prediction sets in practice. As a solution, we propose reliable prediction sets (RPS): the first efficient method for constructing confo...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Algorithmic Learning in a Random World** (2005)
- *Authors:* Vladimir Vovk et al.
- *Direct Connection:* This book introduced conformal prediction’s nonconformity-score-and-calibration paradigm and exchangeability-based finite-sample guarantees, which the current work preserves while altering scoring and calibration aggregation to be reliable under poisoning.

### 💡 Inspiration

**Cross-Conformal Predictors** (2015)
- *Authors:* Vladimir Vovk et al.
- *Direct Connection:* Cross-conformal prediction’s idea of constructing multiple conformal predictors on disjoint calibration folds and aggregating their evidence directly motivates building multiple calibration-based prediction sets and combining them, here via a majority rule to tolerate corrupted calibration subsets.

**Certified Adversarial Robustness via Randomized Smoothing** (2019)
- *Authors:* Jeremy M. Cohen et al.
- *Direct Connection:* The smoothing-for-certification principle—averaging predictions to obtain robustness certificates—inspires the current work’s smoothed score functions that aggregate predictions from models trained on distinct partitions to certify reliability under training-data poisoning.

### 🔍 Gap Identification

**Certified Defenses for Data Poisoning Attacks** (2017)
- *Authors:* Jacob Steinhardt et al.
- *Direct Connection:* This paper formalized bounded-fraction poisoning threat models and certified guarantees for learning, highlighting the lack of analogous, efficient certificates for conformal prediction that the current work addresses for both training and calibration corruption.

### 📊 Baseline

**Classification with Valid and Adaptive Coverage** (2020)
- *Authors:* Y. Romano et al.
- *Direct Connection:* The APS/RAPS framework provides the standard score-based conformal prediction sets for classification that the current method directly modifies by replacing per-model scores with smoothed scores aggregated across partition-trained models to withstand training-set poisoning.

### 🔗 Related Problem

**Predictive Inference with the Jackknife+** (2021)
- *Authors:* Rina Foygel Barber et al.
- *Direct Connection:* Jackknife+ shows how multi-split conformalization aggregates fold-wise calibrations to retain finite-sample validity, informing the current paper’s strategy of split-based construction and aggregation while adapting the aggregation rule to be robust to adversarially corrupted folds.

---

## Synthesis: How Prior Work Led to This Paper

Conformal prediction’s modern form arises from the nonconformity-score and calibration blueprint of Vovk, Gammerman, and Shafer, which delivers finite-sample guarantees under exchangeability. Building on that foundation for classification, Romano, Sesia, and Candès proposed APS/RAPS, which turn softmax-derived scores into compact, valid prediction sets—implicitly assuming uncorrupted training and calibration data. Cross-conformal prediction introduced the use of multiple, disjoint calibration folds and aggregation of their evidence, while Jackknife+ generalized multi-split conformalization to aggregate fold-wise calibrations and preserve validity. Separately, Cohen, Rosenfeld, and Kolter’s randomized smoothing established that averaging predictions across randomized or structured variations can yield certifiable robustness guarantees. In robust learning under poisoning, Steinhardt, Koh, and Liang provided formal bounded-fraction threat models and certification techniques, crystallizing the need for defenses that reason about worst-case contamination rather than benign sampling fluctuations.
Together, these works reveal a path: conformal prediction offers distribution-free coverage but lacks guarantees under poisoning; multi-split aggregation suggests constructing multiple, independent calibration views; and smoothing provides a mechanism to certify robustness via aggregation. The present paper synthesizes these ideas by (i) smoothing score functions through ensembles of models trained on disjoint data partitions to neutralize training-set poison and (ii) constructing multiple calibration-based prediction sets and aggregating them via a majority rule to ensure reliability even when an adversary corrupts a bounded fraction of calibration data, yielding the first efficient conformal sets with provable reliability under poisoning.

---

*Analysis generated on: 2026-01-06T11:08:36.211365*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

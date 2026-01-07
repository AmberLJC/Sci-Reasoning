# Prior Work Analysis Report

## Target Paper

**Title:** Soft Contrastive Learning for Time Series

**Conference:** ICLR 2024 (spotlight)

**Authors:** Seunghan Lee, Taeyoung Park, Kibok Lee

**Keywords:** Soft Contrastive Learning, Time Series Analysis, Self-supervised Learning

**Abstract:** 
> Contrastive learning has shown to be effective to learn representations from time series in a self-supervised way.
However, contrasting similar time series instances or values from adjacent timestamps within a time series leads to ignore their inherent correlations, which results in deteriorating the quality of learned representations.
To address this issue, we propose \textit{SoftCLT}, a simple yet effective soft contrastive learning strategy for time series.
This is achieved by introducing ins...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Dynamic programming algorithm optimization for spoken word recognition** (1978)
- *Authors:* Hiroaki Sakoe et al.
- *Direct Connection:* SoftCLT uses the DTW distance from Sakoe–Chiba to quantify inter-series similarity under temporal misalignment, which directly defines the instance-wise soft assignment weights.

### 💡 Inspiration

**Debiased Contrastive Learning** (2020)
- *Authors:* Ching-Yao Chuang et al.
- *Direct Connection:* SoftCLT is motivated by the false-negative issue highlighted in Debiased CL and mitigates it by down-weighting likely-colliding pairs using input-space similarity (DTW) and timestamp distance.

**Supervised Contrastive Learning** (2020)
- *Authors:* Prannay Khosla et al.
- *Direct Connection:* SoftCLT adapts the multi-positive weighting idea of supervised contrastive learning to the unsupervised time-series setting by replacing label-based positives with similarity-driven soft assignments.

### 🔍 Gap Identification

**Time Series Representation Learning via Temporal and Contextual Contrasting** (2021)
- *Authors:* Mahmoud Eldele et al.
- *Direct Connection:* By relying on binary positives/negatives for temporal and contextual contrasting, TS-TCC exposes the limitation that SoftCLT addresses via soft assignments that respect inter-series similarity and temporal proximity.

### 📊 Baseline

**TS2Vec: Towards Universal Representation of Time Series** (2022)
- *Authors:* Zhenda Yue et al.
- *Direct Connection:* SoftCLT plugs into the TS2Vec-style instance-wise and temporal contrastive framework and replaces its hard positive/negative assignments with similarity-based soft weights to avoid penalizing correlated series or adjacent timestamps.

### 🔧 Extension

**Unsupervised Scalable Representation Learning for Multivariate Time Series** (2019)
- *Authors:* Jean-Yves Franceschi et al.
- *Direct Connection:* SoftCLT generalizes Franceschi et al.’s use of DTW-based instance similarity—originally used to select hard triplet positives/negatives—into continuous, DTW-driven soft weights applied across all instance pairs in the contrastive loss.

**Unsupervised Representation Learning for Time Series with Temporal Neighborhood Coding** (2021)
- *Authors:* Nima Tonekaboni et al.
- *Direct Connection:* SoftCLT extends TNC’s hard temporal-neighborhood notion (local positives vs distant negatives) by introducing a soft temporal contrast where pair contributions decay smoothly with timestamp separation.

---

## Synthesis: How Prior Work Led to This Paper

Franceschi et al. established that dynamic time warping (DTW) is a principled way to measure similarity between time series and used it to choose hard positives and negatives in a triplet loss, demonstrating the value of warping-aware instance relationships. Temporal Neighborhood Coding (TNC) codified temporal locality by treating segments within a temporal window as positives and those far away as negatives, operationalizing a hard neighborhood around timestamps. TS2Vec unified instance-wise and temporal contrastive learning in a simple, strong framework, but still relied on binary assignments that ignored graded similarities across series and time. TS-TCC further emphasized temporal and contextual contrasting for time series, yet its binary positive/negative design left correlated instances and adjacent timestamps vulnerable to being treated as hard negatives. Debiased Contrastive Learning identified the false-negative phenomenon in contrastive learning and proposed adjusting losses to reduce penalties on semantically similar negatives. The classic Sakoe–Chiba DTW made it possible to compute alignment-robust distances between sequences, while Supervised Contrastive Learning showed that weighting multiple positives within a contrastive loss can improve representations by reflecting graded similarity.
Together, these works revealed a gap: time-series contrastive objectives capture temporal structure and inter-series similarity but with hard pair labels that cause false negatives, especially under misalignment and temporal proximity. SoftCLT naturally synthesizes these insights by injecting DTW-based instance similarity and timestamp-difference-based temporal proximity as soft weights into TS2Vec/TS-TCC-style objectives, thereby reducing false negatives and better respecting inherent correlations without changing the overall contrastive framework.

---

*Analysis generated on: 2026-01-06T13:10:25.792055*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

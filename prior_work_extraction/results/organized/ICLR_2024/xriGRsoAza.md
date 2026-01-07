# Prior Work Analysis Report

## Target Paper

**Title:** Inherently Interpretable Time Series Classification via Multiple Instance Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Joseph Early, Gavin Cheung, Kurt Cutajar, Hanting Xie, Jas Kandola, Niall Twomey

**Keywords:** Multiple Instance Learning, Time Series Classification, Interpretability

**Abstract:** 
> Conventional Time Series Classification (TSC) methods are often black boxes that obscure inherent interpretation of their decision-making processes. In this work, we leverage Multiple Instance Learning (MIL) to overcome this issue, and propose a new framework called MILLET: Multiple Instance Learning for Locally Explainable Time series classification. We apply MILLET to existing deep learning TSC models and show how they become inherently interpretable without compromising (and in some cases, ev...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**A Framework for Multiple-Instance Learning** (1998)
- *Authors:* Oded Maron et al.
- *Direct Connection:* MILLET adopts the classic MIL assumption from this work—that a positive bag contains at least one positive instance—and instantiates it over temporal windows to ground its interpretable aggregation of subsequence evidence.

### 💡 Inspiration

**Learning Time-Series Shapelets** (2014)
- *Authors:* Josif Grabocka et al.
- *Direct Connection:* MILLET generalizes the shapelet insight that decisions hinge on discriminative subsequences by replacing explicit shapelet learning with MIL over sliding windows to learn which subsequences support each class.

### 🔍 Gap Identification

**Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization** (2017)
- *Authors:* Ramprasaath R. Selvaraju et al.
- *Direct Connection:* MILLET explicitly addresses the instability and post-hoc nature of Grad-CAM-style saliency used on time series by making the explanation an inherent, sparse instance-weighting learned during training.

### 🔧 Extension

**Attention-based Deep Multiple Instance Learning** (2018)
- *Authors:* Maximilian Ilse et al.
- *Direct Connection:* MILLET directly adapts attention-based MIL pooling so that instance weights become temporally localized, inherently interpretable contributions that are trained end-to-end with the sequence classifier.

### 🔗 Related Problem

**Audio Set Classification with Attention Model** (2017)
- *Authors:* Qiuqiang Kong et al.
- *Direct Connection:* This work showed that attention-based MIL can localize informative moments within weakly labeled audio clips, a mechanism MILLET reuses to highlight salient time windows in generic time series.

**W-TALC: Weakly-supervised Temporal Activity Localization and Classification** (2018)
- *Authors:* Sujoy Paul et al.
- *Direct Connection:* By formulating temporal localization with MIL and soft pooling to aggregate segment scores, W-TALC informed MILLET’s design of pooling over time windows to retain local evidence while producing a global label.

---

## Synthesis: How Prior Work Led to This Paper

Multiple-instance learning (MIL) was formalized by Maron and Lozano-Pérez, introducing the bag–instance assumption that a positive bag contains at least one positive instance; this principle enables learning with only coarse labels while implicitly localizing evidence. Ilse et al. extended MIL with a trainable attention mechanism, producing instance weights that both aggregate to a bag prediction and serve as natural importance scores. In time series classification, Grabocka et al. demonstrated that decisions can be driven by short, discriminative subsequences (“shapelets”), establishing subsequence-level interpretability as a desirable property. In weakly labeled temporal domains, Kong et al. showed that attention-based MIL can localize salient moments in audio clips, while W-TALC operationalized MIL and soft pooling to aggregate segment evidence for video activities, retaining temporal scores that reflect local support. Meanwhile, Grad-CAM became a standard post-hoc explanation for deep models, but its gradient-based saliency often yields diffuse, unstable attributions when applied to sequences.
Synthesizing these threads suggested a clear opportunity: combine the subsequence-centric view from shapelets with the principled, label-efficient aggregation of MIL and the interpretable instance weights of attention pooling to obtain faithful, localized explanations without post-hoc surrogates. By casting sliding windows as instances and training with attention-style MIL pooling, the approach naturally pools window evidence into a sequence label while exposing sparse, time-local contributions, directly addressing the shortcomings of Grad-CAM and extending MIL’s successes in audio/video to general time series.

---

*Analysis generated on: 2026-01-06T15:31:46.312933*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

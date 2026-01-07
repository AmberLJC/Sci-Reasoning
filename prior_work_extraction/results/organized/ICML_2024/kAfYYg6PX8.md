# Prior Work Analysis Report

## Target Paper
**Title:** kAfYYg6PX8
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Interpretable Explanations of Black Boxes by Meaningful Perturbation** (2017)
- *Authors:* Ruth Fong et al.
- *Connection:* L-MAC adopts the core mask-optimization paradigm introduced by Meaningful Perturbations—learning a mask that preserves the classifier’s decision—while adapting it to audio with a trainable decoder and binary, listenable masks.

**Rationalizing Neural Predictions** (2016)
- *Authors:* Tao Lei et al.
- *Connection:* L-MAC’s binary time-mask can be seen as an audio rationale that is sufficient for the classifier’s decision, mirroring the generator–predictor framework for selecting minimal, discrete evidence introduced in this work.

### 🔍 Gap Identification

**ERASER: A Benchmark to Evaluate Rationalized NLP Models** (2020)
- *Authors:* Jay DeYoung et al.
- *Connection:* L-MAC operationalizes ERASER’s sufficiency and comprehensiveness notions by explicitly maximizing confidence on masked-in audio while minimizing it on masked-out audio to yield faithful rationales.

### 📊 Baseline

**RISE: Randomized Input Sampling for Explanation of Black-box Models** (2018)
- *Authors:* Vitali Petsiuk et al.
- *Connection:* As a leading masking-based baseline, RISE motivates L-MAC’s learned decoder approach by highlighting the limitations of random masks and non-listenable perturbations that L-MAC replaces with deterministic, faithful audio masks.

**Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization** (2017)
- *Authors:* Ramprasaath R. Selvaraju et al.
- *Connection:* L-MAC improves over gradient-based localization (often adapted to audio spectrograms) by producing directly listenable, time-domain masks with higher faithfulness.

**Axiomatic Attribution for Deep Networks (Integrated Gradients)** (2017)
- *Authors:* Mukund Sundararajan et al.
- *Connection:* L-MAC addresses the noise and non-causal artifacts of gradient-based attributions like Integrated Gradients by learning binary masks that causally affect the classifier and can be listened to.

### 🔧 Extension

**Understanding Deep Networks via Extremal Perturbations and Smooth Masks** (2019)
- *Authors:* Ruth Fong et al.
- *Connection:* L-MAC directly builds on extremal-perturbation style objectives by learning compact, high-confidence regions, extending them to a decoder that outputs discrete time masks and adding an explicit penalty on the masked-out portion.

---

## Synthesis

L-MAC’s core innovation—learning a decoder that produces binary, listenable masks which both preserve and contrast a classifier’s decision—emerges from two intersecting lines of work. From the vision XAI literature, Meaningful Perturbations and its extremal-perturbation successor established mask optimization as a principled way to extract minimal, decision-preserving evidence. L-MAC inherits this optimization view but adapts it to audio by training a decoder that outputs discrete time masks and by explicitly combining a ‘keep’ objective (maximize confidence on masked-in audio) with a complementary ‘remove’ objective (minimize confidence on masked-out audio). This dual objective resonates with the rationale literature in NLP: Rationalizing Neural Predictions framed explanations as selecting a sparse, discrete subset sufficient for prediction, and ERASER formalized sufficiency and comprehensiveness, a gap L-MAC closes in audio by baking both criteria into its loss.

At the same time, L-MAC positions itself against prevalent baselines. RISE shows the promise of mask-based, black-box explanations but relies on random masks and often yields non-listenable perturbations; L-MAC replaces randomness with a learned, deterministic decoder and enforces listenability by operating directly as binary time masks on the signal. Gradient-based methods like Grad-CAM and Integrated Gradients, commonly adapted to audio, suffer from noisy, non-causal attributions; L-MAC’s causal keep/remove training yields more faithful, human-auditable explanations. Together, these works directly shape L-MAC’s formulation and the specific limitations it overcomes.

---
*Generated: 2026-01-06T23:09:26.402753*

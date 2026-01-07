# Prior Work Analysis Report

## Target Paper

**Title:** Entropy is not Enough for Test-Time Adaptation: From the Perspective of Disentangled Factors

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jonghyun Lee, Dahuin Jung, Saehyung Lee, Junsung Park, Juhyeon Shin, Uiwon Hwang, Sungroh Yoon

**Keywords:** Test-time adaptation, Roustness

**Abstract:** 
> Test-time adaptation (TTA) fine-tunes pre-trained deep neural networks for unseen test data. The primary challenge of TTA is limited access to the entire test dataset during online updates, causing error accumulation. To mitigate it, TTA methods have utilized the model output's entropy as a confidence metric that aims to determine which samples have a lower likelihood of causing error. Through experimental studies, however, we observed the unreliability of entropy as a confidence metric for TTA ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Tent: Fully Test-Time Adaptation by Entropy Minimization** (2021)
- *Authors:* Dequan Wang et al.
- *Direct Connection:* Established the modern TTA formulation and the practice of using prediction entropy as a surrogate confidence/objective, which DeYO directly reexamines and replaces with PLPD for reliable sample selection.

### 💡 Inspiration

**MEMO: Test-Time Robustness via Multi-View Entropy Minimization** (2022)
- *Authors:* Zhang et al.
- *Direct Connection:* Shows that disagreement across augmented views is informative of prediction reliability, inspiring DeYO’s use of a targeted transformation and prediction-difference (PLPD) to probe factor-specific influence.

**ImageNet-trained CNNs are biased towards texture; increasing shape-bias improves accuracy and robustness** (2019)
- *Authors:* Robert Geirhos et al.
- *Direct Connection:* Demonstrates that shape and texture act as disentangled factors driving CNN decisions, directly motivating DeYO’s design of an object-shape–destroying transformation to quantify shape influence via PLPD.

### 🔍 Gap Identification

**EATA: Efficient Test-Time Adaptation** (2022)
- *Authors:* Niu et al.
- *Direct Connection:* Uses entropy-based sample selection to curb error accumulation in online TTA, whose brittleness under bias is the explicit limitation DeYO addresses by substituting entropy with PLPD.

### 📊 Baseline

**CoTTA: Continual Test-Time Adaptation** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* Relies on augmentation-averaged pseudo-labels and confidence heuristics for stable continual TTA, providing a primary baseline into which DeYO’s PLPD can be plugged as a more robust confidence metric.

**SAR: Sharpness-Aware Minimization for Test-Time Adaptation (Towards Stable TTA in Dynamic Environments)** (2023)
- *Authors:* Niu et al.
- *Direct Connection:* Employs entropy-based selective updating with sharpness-aware optimization, serving as a main competitor whose entropy-centric gating DeYO replaces with a factor-aware PLPD criterion.

---

## Synthesis: How Prior Work Led to This Paper

Test-time adaptation (TTA) matured around the idea that a model can self-improve at inference by minimizing its output uncertainty. Tent crystallized this formulation and made prediction entropy the de facto signal for both objective and confidence. EATA pushed this further into the online setting, mitigating error accumulation by selectively updating on low-entropy samples and anchoring the model to reduce drift, thereby entrenching entropy as the central gating heuristic. CoTTA improved stability under continual shifts through augmentation-averaged pseudo labels and EMA regularization, still relying on confidence/consistency proxies to decide when to trust updates. MEMO highlighted that multi-view disagreement under test-time augmentations correlates with unreliability, suggesting that carefully chosen transformations can expose fragile predictions. Complementing these methodological advances, Geirhos et al. showed that CNN decisions often hinge on disentangled factors like texture and shape, and that perturbing one factor can radically change predictions, implying that confidence measures oblivious to factor influence can be misleading. Together, these works created a robust but entropy-centric TTA pipeline while revealing that latent factors drive failures under biased scenarios. The current paper synthesizes these threads by replacing generic entropy confidence with PLPD, a targeted prediction-difference probe that destroys object shape to quantify its influence. By plugging PLPD into selective-update pipelines (e.g., EATA/CoTTA/SAR), DeYO curbs error accumulation precisely where entropy is unreliable—biased, factor-driven shifts—making factor-aware confidence the natural next step for stable online TTA.

---

*Analysis generated on: 2026-01-06T22:50:40.311100*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

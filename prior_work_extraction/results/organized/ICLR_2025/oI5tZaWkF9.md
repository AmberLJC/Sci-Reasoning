# Prior Work Analysis Report

## Target Paper

**Title:** Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification

**Conference:** ICLR 2025 (spotlight)

**Authors:** Hsun-Yu Kuo, Yin-Hsiang Liao, Yu-Chieh Chao, Wei-Yun Ma, Pu-Jen Cheng

**Keywords:** data weighing, data augmentation, distillation, data-efficient training, NLP in resource-constrained settings, fine-tuning, weighted loss

**Abstract:** 
> Synthetic data augmentation via Large Language Models (LLMs) allows researchers to leverage additional training data, thus enhancing the performance of downstream tasks, especially when real-world data is scarce. However, the generated data can deviate from the real-world data, and this misalignment can bring about deficient results while applying the trained model to applications. Therefore, we proposed efficient weighted-loss approaches to align synthetic data with real-world distribution by e...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Improving predictive inference under covariate shift by weighting the log-likelihood function** (2000)
- *Authors:* Hidetoshi Shimodaira
- *Direct Connection:* The paper’s core idea—importance-weighting synthetic examples to approximate the real-data risk—rests on Shimodaira’s covariate-shift principle of correcting distribution mismatch by sample weighting.

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* By establishing the practical pipeline of using LLM-generated data to supervise downstream models, Self-Instruct supplies the generation paradigm whose uneven quality the present paper addresses via principled weighting.

### 💡 Inspiration

**Active Learning for Convolutional Neural Networks: A Core-Set Approach** (2018)
- *Authors:* Ozan Sener et al.
- *Direct Connection:* The diversity/coverage insight from core-set selection informs the new method’s explicit weighting toward diversified synthetic samples rather than redundant generations.

### 📊 Baseline

**Learning to Reweight Examples for Robust Deep Learning** (2018)
- *Authors:* Mengye Ren et al.
- *Direct Connection:* This work’s meta-reweighting with a tiny clean set directly motivates the paper’s use of a small real subset to assign per-example weights, but the new method tailors the weighting to LLM-generated synthetic data and adds a diversity-aware component for distribution alignment.

**Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels** (2018)
- *Authors:* Zhilu Zhang et al.
- *Direct Connection:* GCE is a primary robust-loss baseline that the new approach surpasses by moving from loss-shape robustness to explicit, real-data-informed importance weighting of LLM-generated samples.

### 🔗 Related Problem

**Noisy Student Training: Improving ImageNet Classification with Self-Training** (2020)
- *Authors:* Qizhe Xie et al.
- *Direct Connection:* Confidence-based filtering from Noisy Student highlights the common practice of gating pseudo-labeled data quality, which the new work replaces with real-data-guided loss weighting better suited to LLM-generated text.

**MentorNet: Learning Data-Driven Curriculum for Very Deep Neural Networks on Corrupted Labels** (2018)
- *Authors:* Lu Jiang et al.
- *Direct Connection:* MentorNet’s learned curriculum/sample-weighting for noisy labels frames the idea of per-example weights, while the current paper addresses its limitation by calibrating weights using a tiny real set to align synthetic data to the target distribution.

---

## Synthesis: How Prior Work Led to This Paper

Sample weighting to correct distribution mismatch is a long-standing idea: Shimodaira showed that importance-weighted likelihood corrects covariate shift by rebalancing training risk toward the target distribution. Building on this, Ren et al. introduced meta-learning of per-example weights using a small clean set, directly demonstrating that a tiny amount of ground-truth data can calibrate training under noisy supervision. MentorNet further operationalized data-driven curricula by learning weight schedules to downweight corrupted labels. In parallel, Sener and Savarese emphasized that diversity and coverage in selected examples matter, proposing core-set selection to avoid redundancy and improve generalization. As large language models began generating supervision, Self-Instruct established the now-standard paradigm of using LLM-synthesized data for downstream tasks, surfacing variability in data quality. Confidence-thresholding from Noisy Student popularized filtering pseudo-labels but left open whether confidence aligns with real-data distributions in NLP settings.
Together, these works reveal a gap: LLM-generated examples can be both misaligned with the real distribution and redundant, and existing robust losses or confidence filters do not explicitly reconcile these issues using the small amount of real data available. The current paper takes the natural next step by combining covariate-shift-inspired importance weighting with meta-reweighting calibrated on a tiny real set while incorporating diversity-aware weighting akin to core-set coverage. This synthesis yields an efficient weighted-loss framework that prioritizes synthetic samples both closest to the real distribution and most complementary in coverage, enabling BERT-level models to reliably leverage LLM-generated data across text classification tasks.

---

*Analysis generated on: 2026-01-06T13:55:19.334682*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

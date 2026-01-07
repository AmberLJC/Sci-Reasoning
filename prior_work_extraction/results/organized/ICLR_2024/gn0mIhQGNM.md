# Prior Work Analysis Report

## Target Paper

**Title:** SalUn: Empowering Machine Unlearning via Gradient-based Weight Saliency in Both Image Classification and Generation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chongyu Fan, Jiancheng Liu, Yihua Zhang, Eric Wong, Dennis Wei, Sijia Liu

**Keywords:** Machine unlearning, generative model, diffusion model, weight saliency

**Abstract:** 
> With evolving data regulations, machine unlearning (MU) has become an important tool for fostering trust and safety in today's AI models. However, existing MU methods focusing on data and/or weight perspectives often suffer limitations in unlearning accuracy, stability, and cross-domain applicability. To address these challenges, we introduce the concept of 'weight saliency' for MU, drawing parallels with input saliency in model explanation. This innovation directs MU's attention toward specific...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Machine Unlearning** (2021)
- *Authors:* Adrien Bourtoule et al.
- *Direct Connection:* SISA formalizes the unlearning problem and establishes retraining-after-removal as the gold standard that SalUn explicitly aims to approximate efficiently and uses for evaluation.

### 💡 Inspiration

**Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps** (2013)
- *Authors:* Karen Simonyan et al.
- *Direct Connection:* The use of gradients as saliency signals for attribution directly inspires SalUn’s core idea of gradient-based weight saliency to target parameters most responsible for the forget data.

### 🔍 Gap Identification

**Eternal Sunshine of the Spotless Net: Selective Forgetting in Deep Networks** (2020)
- *Authors:* Agastya Golatkar et al.
- *Direct Connection:* This Fisher/noise-based weight-space unlearning shows selective forgetting is possible but suffers accuracy and stability issues that SalUn addresses by concentrating updates on salient weights rather than perturbing the full parameter space.

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Direct Connection:* Influence-function–based unlearning quantifies training-point effects but is computationally heavy and unstable at scale, motivating SalUn’s tractable gradient-based weight saliency as a practical alternative for localizing forgetting.

### 📊 Baseline

**Ablating Concepts in Text-to-Image Diffusion Models** (2023)
- *Authors:* Kumari et al.
- *Direct Connection:* This concept-erasure baseline for diffusion models fine-tunes against target concepts but often over-forgets and harms unrelated content, a failure SalUn mitigates by updating only salient parameters tied to the forget set.

**Erasing Concepts from Diffusion Models** (2023)
- *Authors:* Gandikota et al.
- *Direct Connection:* As a primary generative unlearning baseline, this method erases concepts via targeted fine-tuning yet lacks stability and generality, directly motivating SalUn’s saliency-guided, principled procedure that scales across classification and generation.

### 🔧 Extension

**SNIP: Single-shot Network Pruning based on Connection Sensitivity** (2019)
- *Authors:* Namhoon Lee et al.
- *Direct Connection:* SalUn repurposes SNIP’s gradient-based connection sensitivity into a per-weight saliency score computed on the forget set, and then limits unlearning updates to these high-saliency parameters.

---

## Synthesis: How Prior Work Led to This Paper

Gradient signals have long been used as attribution measures: Simonyan et al. showed that taking gradients of class scores with respect to inputs yields saliency maps that pinpoint responsible features, establishing gradients as a practical saliency proxy. In parallel, SNIP demonstrated that gradients can quantify connection sensitivity, enabling single-shot identification of critical weights via a gradient-based score, a parameter-centric saliency concept closely tied to training loss. The unlearning problem was formalized by Bourtoule et al. with SISA, which defined efficient unlearning protocols and positioned retraining-after-removal as the gold standard target for approximate unlearning methods. Golatkar et al. then pursued selective forgetting directly in weight space using Fisher information and noise injection, showing feasibility but exposing accuracy and stability weaknesses when perturbing the full parameter set. On the data-influence side, Koh and Liang’s influence functions quantified how specific training examples affect parameters and predictions, but incurred computational and stability burdens in deep networks. In generative models, Kumari et al. and Gandikota et al. erased concepts from diffusion models via fine-tuning, but these methods frequently over-forgot and degraded unrelated content.
Taken together, these works suggested a gap: practical, stable unlearning needed a way to localize updates to just the parameters most tied to the forget data, while matching the retrain-from-scratch ideal across both classifiers and diffusion generators. SalUn synthesizes gradient-based saliency from attribution and pruning with the unlearning objective, computing weight saliency on the forget set and restricting updates to salient parameters, thereby improving accuracy, stability, and cross-domain applicability toward the SISA ideal.

---

*Analysis generated on: 2026-01-06T19:39:49.015565*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

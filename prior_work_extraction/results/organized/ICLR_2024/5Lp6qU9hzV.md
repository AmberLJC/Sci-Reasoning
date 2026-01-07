# Prior Work Analysis Report

## Target Paper

**Title:** Multiscale Positive-Unlabeled Detection of AI-Generated Texts

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yuchuan Tian, Hanting Chen, Xutao Wang, Zheyuan Bai, QINGHUA ZHANG, Ruifeng Li, Chao Xu, Yunhe Wang

**Keywords:** Large Language Models, AI-Generated Texts, Positive-Unlabeled Learning

**Abstract:** 
> Recent releases of Large Language Models (LLMs), e.g. ChatGPT, are astonishing at generating human-like texts, but they may impact the authenticity of texts. Previous works proposed methods to detect these AI-generated texts, including simple ML classifiers, pretrained-model-based zero-shot methods, and finetuned language classification models. However, mainstream detectors always fail on short texts, like SMSes, Tweets, and reviews. In this paper, a Multiscale Positive-Unlabeled (MPU) training ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning Classifiers from Only Positive and Unlabeled Data** (2008)
- *Authors:* Charles Elkan et al.
- *Direct Connection:* The paper adopts Elkan & Noto’s PU formulation—using a positive prior to correct risk under missing labels—to reframe AI-text detection so that ambiguous short machine texts can be treated as unlabeled rather than confidently labeled negatives.

**Defending Against Neural Fake News** (2019)
- *Authors:* Rowan Zellers et al.
- *Direct Connection:* This work established supervised discriminators for human vs. machine text detection, which the paper retains but retools with a PU objective to cope with label ambiguity that is especially acute for short, human-like generations.

### 💡 Inspiration

**Estimating the Class Prior in Positive and Unlabeled Data through Decision Tree Induction** (2018)
- *Authors:* Jesse Davis et al.
- *Direct Connection:* Building on the necessity of class-prior estimation emphasized by TIcE, the paper replaces a single global prior with a learned, multiscale (length-dependent) prior estimated by a recurrent model to match scale-variant corpora.

### 🔍 Gap Identification

**A Watermark for Large Language Models** (2023)
- *Authors:* Jacob Kirchenbauer et al.
- *Direct Connection:* By showing detection power grows with sample length and is weak on short outputs, this work crystallizes the length-driven detectability gap that the paper addresses via a multiscale, length-sensitive PU prior and loss.

### 📊 Baseline

**DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (2023)
- *Authors:* Eric Mitchell et al.
- *Direct Connection:* DetectGPT serves as a primary zero-shot baseline whose performance degrades on short passages, directly motivating a supervised, length-aware PU training scheme to recover power on short texts without sacrificing long-text accuracy.

### 🔧 Extension

**Positive-Unlabeled Learning with Non-Negative Risk Estimator** (2017)
- *Authors:* Masashi Kiryo et al.
- *Direct Connection:* The proposed Multiscale PU Loss directly extends the nnPU risk estimator by incorporating length-conditioned positive priors, preventing negative risk overfitting while making the PU objective sensitive to text length.

---

## Synthesis: How Prior Work Led to This Paper

Supervised detection of machine-generated text was popularized by Grover, which demonstrated that discriminators trained on human vs. generator outputs can be effective but implicitly assume clean labels across examples. Zero-shot detection advanced with DetectGPT, which exploits probability curvature but exhibits a marked drop on short inputs. Watermarking further quantified the statistical reality that detection power scales with sample length, making very short texts intrinsically hard to flag. In parallel, Elkan and Noto formalized learning from positive and unlabeled data by correcting risk with a positive prior under missing labels, while Kiryo et al. stabilized PU training via the non-negative risk estimator to avoid negative risk overfitting. Davis and colleagues (TIcE) emphasized that estimating the class prior is central in PU settings, motivating methods that infer priors from structure in the data rather than assuming a fixed constant. Together, these lines showed that short texts are both label-ambiguous and statistically underpowered for detection, and that PU learning with careful prior estimation can handle missing or unreliable labels. The current paper synthesizes these insights by recasting short machine outputs as unlabeled within a PU framework and generalizing nnPU with a length-sensitive, multiscale loss. By learning length-conditioned positive priors—rather than assuming a global prior—it aligns the PU objective with detectability that varies by text length, closing the short-text gap while preserving long-text performance.

---

*Analysis generated on: 2026-01-06T13:16:22.365134*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

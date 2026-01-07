# Prior Work Analysis Report

## Target Paper

**Title:** Influencer Backdoor Attack on Semantic Segmentation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Haoheng Lan, Jindong Gu, Philip Torr, Hengshuang Zhao

**Keywords:** Semantic Segmentation, Backdoor Attack

**Abstract:** 
> When a small number of poisoned samples are injected into the training dataset of a deep neural network, the network can be induced to exhibit malicious behavior during inferences, which poses potential threats to real-world applications. While they have been intensively studied in classification, backdoor attacks on semantic segmentation have been largely overlooked. Unlike classification, semantic segmentation aims to classify every pixel within a given image. In this work, we explore backdoor...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain** (2017)
- *Authors:* Tianyu Gu et al.
- *Direct Connection:* IBA adopts the core trigger-based data poisoning framework introduced by BadNets and adapts it from classification to the dense pixel-wise setting of semantic segmentation.

**Pyramid Scene Parsing Network** (2017)
- *Authors:* Hengshuang Zhao et al.
- *Direct Connection:* PSPNet established that segmentation relies on global multi-scale context aggregation, which IBA explicitly exploits by placing triggers on contextual (non‑victim) regions to influence victim-class pixels.

**Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation (DeepLabv3+)** (2018)
- *Authors:* Liang-Chieh Chen et al.
- *Direct Connection:* DeepLabv3+ demonstrates strong multi-scale context modeling via ASPP, a property IBA leverages so that a non‑local trigger can systematically sway predictions of all victim-class pixels.

### 💡 Inspiration

**Hidden Trigger Backdoor Attacks** (2020)
- *Authors:* Aniruddha Saha et al.
- *Direct Connection:* The idea of learning a stealthy, robust trigger that generalizes across inputs directly inspires IBA’s design of a compact trigger, but IBA relocates it onto non‑victim (context) pixels to drive class-wide misclassification.

**Non-local Neural Networks** (2018)
- *Authors:* Xiaolong Wang et al.
- *Direct Connection:* By formalizing long-range pixel interactions, Non-local Networks provide the key insight that distant context can drive a pixel’s label, enabling IBA’s strategy of triggering misclassification from non‑victim regions.

### 🔗 Related Problem

**BadDet: Backdoor Attacks on Object Detection** (2022)
- *Authors:* Xiang Li et al.
- *Direct Connection:* BadDet extends backdoors to dense prediction and exposes task-specific challenges, directly motivating IBA to formulate a segmentation-specific backdoor that flips all victim-class pixels while preserving non‑victim accuracy.

---

## Synthesis: How Prior Work Led to This Paper

Trigger-based poisoning was crystallized by BadNets, which showed that stamping a learned pattern during training can cause consistent misclassification when the trigger reappears at test time. Hidden Trigger Backdoor Attacks advanced the stealth and robustness of such patterns, demonstrating that compact, inconspicuous triggers can generalize across inputs while remaining hard to detect. In semantic segmentation, PSPNet revealed that per-pixel predictions are not purely local but depend critically on global, multi-scale context via pyramid pooling, while DeepLabv3+ further strengthened this paradigm with atrous spatial pyramid pooling that integrates broad contextual cues into each pixel’s decision. Non-local Neural Networks formalized the idea that distant pixels can strongly influence each other’s responses, grounding the notion that modifying seemingly unrelated regions can sway target predictions. In dense prediction security, BadDet pushed backdoors beyond classification to object detection, underscoring that task structure matters and that backdoors must be designed to exploit how dense models aggregate information. Together these works suggest a latent opportunity: if segmentation models rely on non-local context, a trigger placed on non-victim (context) regions could systematically bias predictions of victim-class pixels. Building on the poisoning framework and stealthy trigger design while explicitly exploiting long-range, multi-scale context, the current work unifies these insights into an influencer backdoor that flips all victim-class pixels per inference yet preserves non-victim accuracy.

---

*Analysis generated on: 2026-01-07T00:11:16.427501*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

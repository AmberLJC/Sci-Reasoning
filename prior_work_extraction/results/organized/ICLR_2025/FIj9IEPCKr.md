# Prior Work Analysis Report

## Target Paper

**Title:** Proxy Denoising for Source-Free Domain Adaptation

**Conference:** ICLR 2025 (oral)

**Authors:** Song Tang, Wenxin Su, Yan Gan, Mao Ye, Jianwei Dr. Zhang, Xiatian Zhu

**Keywords:** Domain adaptation, source-free, multimodal proxy space, proxy confidence theory

**Abstract:** 
> Source-Free Domain Adaptation (SFDA) aims to adapt a pre-trained source model to an unlabeled target domain with no access to the source data. Inspired by the success of large Vision-Language (ViL) models in many applications, the latest research has validated ViL's benefit for SFDA by using their predictions as pseudo supervision. However, we observe that ViL's supervision could be noisy and inaccurate at an unknown rate, potentially introducing additional negative effects during adaption. To a...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Do We Really Need to Access the Source Data? Source Hypothesis Transfer for Unsupervised Domain Adaptation (SHOT)** (2020)
- *Authors:* Jian Liang et al.
- *Direct Connection:* SHOT formalized the SFDA setting and introduced a self-training/Information Maximization backbone that ProDe uses as the adaptation substrate while replacing self-generated pseudo-labels with denoised vision–language proxy supervision.

**Learning Transferable Visual Models From Natural Language Supervision (CLIP)** (2021)
- *Authors:* Alec Radford et al.
- *Direct Connection:* CLIP’s zero-shot image–text alignment provides the concrete vision–language proxy whose predictions ProDe explicitly corrects and leverages to guide adaptation toward a domain-invariant space.

### 💡 Inspiration

**Learning to Prompt for Vision-Language Models (CoOp)** (2022)
- *Authors:* Kaiyang Zhou et al.
- *Direct Connection:* CoOp established a controllable multimodal proxy space via learnable prompts, which ProDe exploits conceptually to define and measure proxy divergence against a latent domain-invariant space during adaptation.

**Confident Learning: Estimating Uncertainty in Dataset Labels** (2021)
- *Authors:* Curtis G. Northcutt et al.
- *Direct Connection:* ProDe’s proxy confidence theory borrows the key idea of estimating unknown noise rates from model confidences to identify and correct erroneous supervision, extending it from label noise to vision–language proxy noise.

### 🔍 Gap Identification

**Test-time Prompt Tuning for Zero-shot Generalization in Vision-Language Models (TPT)** (2022)
- *Authors:* Zhang et al.
- *Direct Connection:* TPT showed that CLIP’s own predictions can drive unsupervised adaptation but are unstable under domain shift, directly motivating ProDe’s need to denoise vision–language pseudo supervision with principled confidence modeling.

### 🔗 Related Problem

**DivideMix: Learning with Noisy Labels as Semi-supervised Learning** (2020)
- *Authors:* Junnan Li et al.
- *Direct Connection:* ProDe generalizes DivideMix’s principle of separating clean versus noisy supervision by confidence into a multimodal, dynamically evolving proxy setting rather than a fixed single-label noise scenario.

---

## Synthesis: How Prior Work Led to This Paper

Source-free domain adaptation was crystallized by SHOT, which showed that a source-trained model can be adapted in a target-only regime by self-training and information maximization, establishing the optimization backbone used broadly in SFDA. CLIP demonstrated that large vision–language models produce zero-shot class predictions via image–text alignment, making their outputs a natural external teacher or proxy without accessing source data. Test-time Prompt Tuning (TPT) further evidenced that CLIP’s own predictions can steer unsupervised adaptation on target data, but also revealed brittleness: proxy predictions fluctuate and degrade under domain shift, introducing noisy supervision. CoOp introduced learnable prompts to control CLIP’s multimodal embedding space, highlighting that the proxy space is not fixed but can be shaped, and offering a handle to characterize alignment or divergence. Beyond adaptation, Confident Learning provided a principled way to estimate unknown label noise rates from classifier confidences and prune or correct mislabeled data. DivideMix treated label noise as a semi-supervised problem, separating clean from noisy samples using confidence-driven mixture modeling to stabilize training.
Bringing these insights together exposes a clear opportunity: vision–language proxies are powerful for SFDA but their noise is unmodeled and dynamically varies as adaptation proceeds. The natural next step is to keep the SHOT-style target adaptation backbone while explicitly modeling a confidence-driven, multimodal proxy space derived from CLIP/CoOp, diagnosing proxy divergence, and denoising proxy predictions as they evolve. By instantiating a confidence theory tailored to proxy supervision and by operationalizing it to correct proxy labels before they guide updates, the current work synthesizes robust noisy-label principles (Confident Learning/DivideMix) with ViL-driven SFDA (CLIP/TPT) into a unified proxy denoising framework that targets the latent domain-invariant space.

---

*Analysis generated on: 2026-01-06T19:25:48.926561*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

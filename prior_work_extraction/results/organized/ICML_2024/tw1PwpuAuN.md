# Prior Work Analysis Report

## Target Paper
**Title:** tw1PwpuAuN
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Understanding Neural Networks through Representation Erasure** (2016)
- *Authors:* Jiwei Li et al.
- *Connection:* Introduced token-level erasure (mask/delete and measure performance drop) as a direct operationalization of faithfulness that this paper keeps but makes reliable by bringing masked inputs in-distribution.

**ERASER: A Benchmark to Evaluate Rationalized NLP Models** (2020)
- *Authors:* Jay DeYoung et al.
- *Connection:* Established comprehensiveness and sufficiency—masking-based faithfulness metrics widely used in NLP—which the current work preserves while removing their out-of-distribution pitfalls via masking-aware fine-tuning.

### 💡 Inspiration

**Rationalizing Neural Predictions** (2016)
- *Authors:* Tao Lei et al.
- *Connection:* Showed that incorporating masking into training (selector–predictor with rationales) can make explanations measurable; this inspired the paper’s train-time masking to render post-hoc masking tests faithful without changing the model class.

**Interpretable Neural Predictions with Differentiable Masking** (2019)
- *Authors:* Yova Kementchedjhieva Bastings et al.
- *Connection:* Demonstrated train-time, differentiable masking (HardKuma) to ensure predictions depend on selected tokens; the present work adapts the same principle—bake masking into training—to standard masked LMs for faithfulness measurement.

### 🔍 Gap Identification

**Pathologies of Neural Models Make Interpretations Difficult** (2018)
- *Authors:* Shi Feng et al.
- *Connection:* Demonstrated that deletion/masking causes out-of-distribution inputs and counterintuitive ‘input reduction,’ directly motivating the paper’s core idea of training models so that masking becomes in-distribution by design.

**Attention is not Explanation** (2019)
- *Authors:* Sarthak Jain et al.
- *Connection:* Provided strong evidence that popular importance measures can be persuasive yet unfaithful, underscoring the need for faithful, perturbation-based evaluation that this paper makes practical and robust.

### 📊 Baseline

**A Benchmark for Interpretability Methods in Deep Neural Networks (ROAR)** (2019)
- *Authors:* Sarah Hooker et al.
- *Connection:* Proposed Remove-And-Retrain to mitigate OOD effects of feature removal, but at high computational cost; the new method achieves ROAR’s goal inherently during fine-tuning, avoiding repeated retraining and proxy models.

---

## Synthesis

The core of this paper is to make masking-based faithfulness testing valid and scalable by ensuring masks are in-distribution through a masking-aware fine-tuning procedure for masked language models. This builds directly on the erasure paradigm introduced by Li et al., and on ERASER’s comprehensiveness/sufficiency metrics, which formalize faithfulness as the performance impact of masking important tokens. However, prior work has shown that naive masking creates out-of-distribution artifacts: Feng et al. documented input-reduction pathologies, and the community’s trust in post-hoc importance scores was further eroded by Jain and Wallace’s demonstrations that persuasive explanations can be unfaithful. One influential workaround, ROAR (Hooker et al.), addresses OOD by removing features and retraining models, but its computational burden and reliance on retrained proxies limit practical use. The present work’s key insight is to import a lesson from rationalization methods—such as Lei et al.’s selector–predictor framework and Bastings et al.’s differentiable masking—that train with masking so the model’s decision truly depends on the revealed tokens. By integrating masking during fine-tuning of standard masked LMs, the paper preserves the simplicity and generality of erasure/ERASER-style tests while eliminating OOD shift and the need for remove-and-retrain. The result is an inherently faithfulness-measurable model family that makes deletion-based evaluation both principled and practical across many NLP tasks.

---
*Generated: 2026-01-06T23:09:26.460007*

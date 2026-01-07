# Prior Work Analysis Report

## Target Paper
**Title:** 7arAADUK6D
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DeePEn’s core technical advance—training-free, step-wise fusion of heterogeneous LLMs’ next-token distributions via a universal relative space—builds directly on the tradition of probability-space ensembling in sequence generation. Shallow and deep fusion in neural machine translation established that combining a model’s decoder with an external LM at each decoding step can improve outputs, and Cold Fusion further underscored the value of leveraging internal probabilistic signals rather than just final texts. The WMT16 Edinburgh systems popularized per-step ensemble averaging in NMT, but these methods presuppose shared vocabularies; DeePEn tackles the missing piece: vocabulary/tokenizer heterogeneity that otherwise blocks direct logit fusion.
Knowledge Distillation provided the conceptual basis for treating soft probability distributions as rich, transferable carriers of knowledge. Products of Experts offered a principled lens for combining multiple expert distributions to yield sharper predictions, a perspective reflected in DeePEn’s fusion rule. In contrast to text-only ensemble strategies such as self-consistency, which vote over final responses and can overfit to seen distributions, DeePEn aggregates information at the distributional level during decoding, mitigating generalization issues.
Finally, while Switch Transformers demonstrate the power of expert collaboration within a single sparse model through routing, DeePEn operationalizes a parallel, training-free collaboration across independent LLMs. Its key novelty is resolving tokenizer mismatches by mapping each model’s probability space into a universal relative representation, enabling deep, step-wise collaboration without retraining or additional reward/fusion models.

---
*Generated: 2026-01-06T23:33:36.261046*

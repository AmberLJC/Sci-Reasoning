# Prior Work Analysis Report

## Target Paper
**Title:** wJv4AIt4sK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—a first formal proof that sparsity and quantization are non-orthogonal and order-dependent—emerges from two converging lines of work. On the sparsity side, magnitude pruning and its second-order successors laid the sensitivity-theoretic groundwork. Han et al.’s magnitude pruning provided the ubiquitous sparsity mechanism used in modern pipelines, while Optimal Brain Surgeon introduced a curvature-aware view of weight perturbations. On the quantization side, Jacob et al.’s integer-only quantization established the operator and error model widely assumed in practice, and more recent Hessian-aware methods such as GPTQ characterized quantization as curvature-weighted perturbations, linking quantization noise to model sensitivity.
Historically, Deep Compression popularized a sequential composition of pruning and quantization, implicitly treating them as orthogonal. However, emerging LLM-centric methods—SparseGPT for pruning and SpQR’s hybrid sparse–quantized representation—showed empirically that co-design matters. These works supplied both the practical regimes (large transformers, post-training settings) and the algorithmic primitives (sensitivity-aware pruning/quantization) that the present paper leverages to derive and validate a general non-orthogonality result. By unifying quantization noise models with sensitivity-based views of pruning, the paper explains why the two perturbations couple through curvature and masking, making the application order consequential. It then substantiates this with experiments on OPT/LLaMA, ViT, and ResNet, converting prior empirical hints into a principled ordering guideline for combined compression.

---
*Generated: 2026-01-06T23:42:48.092502*

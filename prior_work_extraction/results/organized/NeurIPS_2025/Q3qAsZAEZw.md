# Prior Work Analysis Report

## Target Paper
**Title:** Q3qAsZAEZw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—diagnosing and mitigating numerically induced nondeterminism in LLM inference—rests on unifying classic floating‑point analysis with GPU-level reproducibility research and transformer-specific numerical design. Goldberg’s account of non‑associativity and rounding provides the fundamental lens through which changes in GPU count, kernel choice, and batch size are shown to reorder reductions and thus perturb logits. Collange et al. and Demmel & Nguyen translate this theory into the GPU setting, demonstrating how parallel reductions become non‑reproducible and offering deterministic or order‑robust summation schemes; these directly inspire the paper’s deterministic reduction strategies for softmax, attention, and layer normalization.
Complementing reduction order, precision policy is central: Micikevicius et al. establish that higher‑precision accumulators temper rounding amplification, and Wang & Kanwar’s characterization of bfloat16 explains why reasoning‑oriented LLMs are especially sensitive under BF16. Building on these, the paper prescribes selective upcasting and accumulation in FP32 at numerically sensitive points of the inference pipeline.
At the algorithmic level, FlashAttention’s online, numerically stable softmax/attention shows how restructured normalization reduces susceptibility to chunking and parallelization artifacts; the paper adapts such patterns to enhance determinism across hardware and batching. Finally, the observed cascading divergence in generated reasoning traces to exposure bias as articulated by scheduled sampling: small early perturbations compound across decoding steps. Together, these works shape a principled toolbox—deterministic reductions, stable normalizers, and precision-aware accumulators—for reproducible LLM inference across heterogeneous systems.

---
*Generated: 2026-01-06T23:42:48.160143*

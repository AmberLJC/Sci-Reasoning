# Prior Work Analysis Report

## Target Paper
**Title:** dGVZwyq5tV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

TEAL’s core idea—training-free, magnitude-based activation sparsity across all layers of modern LLMs—emerges from two converging threads of prior work. First, post-training modification at LLM scale has proven both effective and practical: SparseGPT demonstrated that large models can be sparsified without retraining by relying on simple saliency criteria and efficient sparse kernels. Parallel advances in post-training quantization (LLM.int8, SmoothQuant, AWQ) revealed that activations in Transformers are heavy-tailed with prominent outliers, and that preserving high-magnitude channels is crucial for quality. These works established that activation statistics can be exploited post hoc to deliver efficiency while maintaining accuracy—directly motivating TEAL’s choice of magnitude-based activation pruning and its seamless compatibility with quantization.

Second, the efficiency of sparse activation has a conceptual precedent in Mixture-of-Experts: Switch Transformers use top-k gating to activate only selected experts, yielding sparse computation pathways at inference. TEAL internalizes this principle at a finer granularity by selecting the top-magnitude elements of hidden states within each feedforward block, requiring no learned router or additional training. Finally, because modern LLMs rely on gated MLPs (GLU/SwiGLU), TEAL’s activation selection aligns naturally with the gating-induced activation structure these layers produce. In sum, TEAL synthesizes training-free sparsity (SparseGPT), activation-aware calibration (LLM.int8, SmoothQuant, AWQ), and top-k sparse activation routing (Switch) into a single, practical method that pairs with optimized sparse kernels to yield real wall-clock speedups.

---
*Generated: 2026-01-06T23:42:48.090478*

# Prior Work Analysis Report

## Target Paper
**Title:** gsP05g8IeK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Optimal Brain Compression: A Unified Framework for Model Compression** (2022)
- *Authors:* Elias Frantar et al.
- *Connection:* SparseGPT instantiates the OBC second-order reconstruction objective layerwise, using activation-derived curvature to select and compensate pruned weights, exactly following OBC’s theoretical formulation for post-training compression.

**Second-Order Derivatives for Network Pruning: Optimal Brain Surgeon** (1993)
- *Authors:* Babak Hassibi et al.
- *Connection:* The core idea of pruning with minimal loss increase via inverse-Hessian–based compensation of remaining weights comes from OBS, which SparseGPT approximates efficiently at GPT scale with blockwise curvature.

**Optimal Brain Damage** (1990)
- *Authors:* Yann LeCun et al.
- *Connection:* OBD introduced the seminal second-order saliency view of pruning, which SparseGPT refines beyond diagonal approximations by using richer (blockwise) curvature information from real activations.

### 🔍 Gap Identification

**Movement Pruning: Adaptive Sparsity by Fine-Tuning** (2020)
- *Authors:* Victor Sanh et al.
- *Connection:* Movement Pruning achieves strong sparsity on transformers but requires task-specific fine-tuning; SparseGPT explicitly addresses this limitation by delivering high-sparsity pruning without any retraining.

### 📊 Baseline

**Learning Both Weights and Connections for Efficient Neural Networks** (2015)
- *Authors:* Song Han et al.
- *Connection:* Magnitude pruning is the canonical unstructured sparsification baseline that SparseGPT consistently outperforms by replacing magnitude scores with second-order, compensation-aware one-shot pruning.

### 🔧 Extension

**GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers** (2022)
- *Authors:* Elias Frantar et al.
- *Connection:* SparseGPT directly adapts GPTQ’s blockwise, Hessian-informed, sequential reconstruction-and-compensation procedure from quantization to pruning, enabling post-training compression of GPT-scale models without retraining.

### 🔗 Related Problem

**SNIP: Single-Shot Network Pruning Based on Connection Sensitivity** (2019)
- *Authors:* Namhoon Lee et al.
- *Connection:* SNIP demonstrated the feasibility of one-shot pruning, and SparseGPT realizes this paradigm for fully-trained GPT models by using activation-driven second-order reconstruction rather than first-order initialization-time saliency.

---

## Synthesis

SparseGPT’s key insight—accurate, one-shot pruning of GPT-scale models without retraining—emerges from a lineage of second-order pruning and modern post-training compression. Optimal Brain Damage and Optimal Brain Surgeon established the foundational view that pruning should minimize loss increase using curvature information, with OBS introducing compensation of remaining weights via (approximate) inverse Hessian updates. Optimal Brain Compression modernized this principle into a practical, unified post-training framework: reconstruct each layer’s outputs under a quadratic approximation built from activation-derived curvature and compensate surviving parameters accordingly. GPTQ operationalized OBC for LLMs by processing weights in blocks, computing a local curvature (from activations), and applying fast sequential updates via blockwise solves; SparseGPT directly extends this machinery from quantization to pruning by selecting zeros under the same reconstruction objective and performing the same compensation to preserve layer outputs. Against prevalent baselines, magnitude pruning represents the standard unstructured approach that SparseGPT replaces with curvature-aware selection and updates, yielding far lower perplexity at 50–60% sparsity. In NLP-specific pruning, Movement Pruning demonstrated strong sparsity but hinges on fine-tuning, which is impractical for 100B+ parameter models; SparseGPT explicitly targets this gap by requiring no retraining. Finally, SNIP’s one-shot paradigm foreshadowed zero-training pruning, but SparseGPT achieves it on fully trained GPTs through second-order, activation-driven reconstruction rather than first-order initialization heuristics.

---
*Generated: 2026-01-06T23:09:26.537137*

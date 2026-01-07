# Prior Work Analysis Report

## Target Paper

**Title:** OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Wenqi Shao, Mengzhao Chen, Zhaoyang Zhang, Peng Xu, Lirui Zhao, Zhiqian Li, Kaipeng Zhang, Peng Gao, Yu Qiao, Ping Luo

**Keywords:** Large Language Model Compression, Differentiable Quantization

**Abstract:** 
> Large language models (LLMs) have revolutionized natural language processing tasks. However, their practical deployment is hindered by their immense memory and computation requirements. Although recent post-training quantization (PTQ) methods are effective in reducing memory footprint and improving the computational efficiency of LLM, they hand-craft quantization parameters, leading to low performance, especially in extremely low-bit quantization. To tackle this issue, we introduce an Omnidirect...

---

## Key Prior Works (7 papers with direct influence)

### 💡 Inspiration

**Up or Down? Adaptive Rounding for Post-Training Quantization** (2020)
- *Authors:* Nagel et al.
- *Direct Connection:* OmniQuant adopts AdaRound’s calibration-based reconstruction paradigm to differentiably optimize quantization parameters, but targets clipping thresholds and equivalent transforms rather than rounding offsets.

### 🔍 Gap Identification

**ACIQ: Analytical Clipping for Integer Quantization of Neural Networks** (2019)
- *Authors:* Banner et al.
- *Direct Connection:* OmniQuant replaces ACIQ’s closed-form clipping under distributional assumptions with data-driven, learnable clipping thresholds (LWC) and extends clipping to weights for robust low-bit PTQ.

### 📊 Baseline

**GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers** (2022)
- *Authors:* Frantar et al.
- *Direct Connection:* OmniQuant adopts GPTQ’s PTQ setting for LLMs but replaces GPTQ’s fixed per-group scales/rounding with learnable clipping thresholds and equivalent transformations to recover 3–4-bit accuracy.

**AWQ: Activation-aware Weight Quantization for LLMs** (2023)
- *Authors:* Lin et al.
- *Direct Connection:* OmniQuant addresses AWQ’s heuristic, activation-aware weight scaling by learning the weight clipping thresholds and activation re-scaling factors from calibration data to improve extreme low-bit settings.

### 🔧 Extension

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models** (2023)
- *Authors:* Xiao et al.
- *Direct Connection:* OmniQuant generalizes SmoothQuant’s invertible per-channel rebalancing into a learnable equivalent transformation (LET) that is optimized jointly with quantization to suppress activation outliers while preserving function equivalence.

**PACT: Parameterized Clipping Activation for Quantized Neural Networks** (2018)
- *Authors:* Choi et al.
- *Direct Connection:* OmniQuant extends PACT’s idea of learning clipping thresholds by making clipping learnable within PTQ and applying it to weight distributions via LWC rather than only to activations during QAT.

### 🔗 Related Problem

**8-bit Matrix Multiplication for Transformers at Scale (LLM.int8())** (2022)
- *Authors:* Dettmers et al.
- *Direct Connection:* OmniQuant tackles the activation outlier problem highlighted by LLM.int8 without resorting to mixed precision by learning equivalent transformations (LET) that smooth activations while keeping layers functionally equivalent.

---

## Synthesis: How Prior Work Led to This Paper

GPTQ established efficient post-training quantization for large transformers by approximating second-order effects to quantize weights, but it relied on fixed per-group scales and rounding that degrade at 3–4 bits. AWQ introduced activation-aware weight quantization, scaling weights based on activation importance and clipping heuristics, yet still depended on hand-tuned rules that struggle under extreme compression. SmoothQuant proposed an invertible per-channel rescaling that transfers magnitude between activations and weights to tame activation outliers for INT8, demonstrating the power of function-preserving equivalent transformations. ACIQ analytically derived clipping thresholds under assumed distributions to reduce quantization error, offering simple PTQ calibration but limited by modeling assumptions and fixed parameters. AdaRound showed that optimizing quantization parameters via calibration-set reconstruction—without full training—can substantially improve PTQ accuracy by differentiably adjusting rounding. PACT introduced learnable activation clipping thresholds optimized via gradients, revealing that trainable clipping can control outliers more effectively than static ranges. LLM.int8 identified activation outliers in LLMs and addressed them with mixed precision, underscoring the centrality of outlier handling for accuracy.
Combining these insights revealed a gap: extreme low-bit PTQ needs both function-preserving activation shaping and data-driven learnable quantization parameters, but without costly fine-tuning. OmniQuant naturally synthesizes this by learning weight clipping thresholds (inspired by PACT/ACIQ but done in PTQ) and by generalizing SmoothQuant’s invertible rescaling into a learnable equivalent transformation, optimized with AdaRound-style calibration, thereby overcoming GPTQ/AWQ’s fixed heuristics and avoiding LLM.int8’s mixed precision.

---

*Analysis generated on: 2026-01-06T19:36:04.811003*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

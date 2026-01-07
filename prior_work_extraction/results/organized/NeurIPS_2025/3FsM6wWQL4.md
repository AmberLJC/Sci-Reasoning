# Prior Work Analysis Report

## Target Paper
**Title:** 3FsM6wWQL4
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers** (2022)
- *Authors:* Frantar et al.
- *Connection:* HBLLM inherits the GPTQ-style PTQ formulation and block/group treatment of weights, extending it to 1‑bit with frequency-aware intra-row grouping and band-wise statistics to minimize quantization error.

### 💡 Inspiration

**QuaRot: Outlier-Free LLM Quantization via Rotation** (2023)
- *Authors:* First author et al.
- *Connection:* HBLLM is inspired by QuaRot’s core idea that an orthonormal change of basis can make weights more quantization-friendly; it specializes this with a Haar wavelet transform and couples it with frequency-aware grouping for 1‑bit PTQ.

### 🔍 Gap Identification

**BitNet b1.58: 1.58-bit Large Language Models** (2024)
- *Authors:* First author et al.
- *Connection:* By showing ultra-low-bit representations are viable only with training-time changes, BitNet b1.58 highlights the gap HBLLM fills: high-fidelity, post-training near-binary (≈1‑bit) compression of LLM weights.

### 📊 Baseline

**BiLLM: Pushing the Limit of Post-Training 1-Bit LLM Quantization** (2024)
- *Authors:* First author et al.
- *Connection:* HBLLM directly targets the same 1‑bit PTQ setting as BiLLM and overcomes BiLLM’s loss from sign-only expressiveness by introducing a Haar-wavelet basis and frequency-aware grouping to markedly improve fidelity and storage.

### 🔧 Extension

**AWQ: Activation-Aware Weight Quantization for LLMs** (2023)
- *Authors:* Lin et al.
- *Connection:* HBLLM’s ℓ2-norm-based saliency-driven column selection is a direct adaptation of AWQ’s channel saliency idea, but applied within wavelet frequency bands and pushed to the extreme 1‑bit regime.

**SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression** (2024)
- *Authors:* Frantar et al.
- *Connection:* HBLLM builds on SpQR’s insight of selectively treating salient weights differently by retaining band-wise flexibility for salient columns and using a shared mean for non-salient groups to cut storage while preserving accuracy.

### 🔗 Related Problem

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models** (2022)
- *Authors:* Xiao et al.
- *Connection:* HBLLM echoes SmoothQuant’s strategy of redistributing magnitude before quantization, but does so via frequency decomposition of weights (Haar) and saliency-aware grouping to enable high-fidelity 1‑bit quantization.

---

## Synthesis

HBLLM sits at the intersection of three lines of work that directly shaped its core idea. First, GPTQ established the practical post‑training quantization framework and grouping paradigm for LLM weights, which HBLLM keeps while redesigning the basis and grouping to suit the 1‑bit extreme. Second, low‑bit fidelity hinges on handling saliency and outliers: SmoothQuant demonstrated the value of redistributing magnitude to ease quantization, while AWQ formalized channel saliency (often via ℓ2 norms) to protect important columns. SpQR went further by selectively treating salient weights differently to retain accuracy under tight storage budgets. HBLLM directly extends these saliency notions into the wavelet domain, using ℓ2‑based column selection within frequency bands and assigning a shared mean to non‑salient groups for storage efficiency. Third, the key spark for HBLLM’s wavelet-enhanced design comes from orthonormal‑basis methods like QuaRot, which showed that rotating to a better basis can dramatically reduce quantization error. HBLLM specializes this idea with a structured Haar wavelet transform to decompose weights by frequency, then performs frequency‑aware intra‑row grouping that boosts the expressiveness of 1‑bit representations. Against the immediate 1‑bit PTQ baseline BiLLM—whose sign‑only capacity limits fidelity—HBLLM’s wavelet basis plus saliency‑aware grouping closes the accuracy gap while keeping overhead near 1 bit, addressing the broader ultra‑low‑bit challenge framed by BitNet b1.58 without retraining.

---
*Generated: 2026-01-06T23:08:23.952797*

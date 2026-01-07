# Prior Work Analysis Report

## Target Paper

**Title:** CBQ: Cross-Block Quantization for Large Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Xin Ding, Xiaoyu Liu, Zhijun Tu, Yun Zhang, Wei Li, Jie Hu, Hanting Chen, Yehui Tang, Zhiwei Xiong, Baoqun Yin, Yunhe Wang

**Keywords:** Large Language Model Compression, ultra-low bits precision

**Abstract:** 
> Post-training quantization (PTQ) has played a pivotal role in compressing large language models (LLMs) at ultra-low costs. Although current PTQ methods have achieved promising results by addressing outliers and employing layer- or block-wise loss optimization techniques, they still suffer from significant performance degradation at ultra-low bits precision. To dissect this issue, we conducted an in-depth analysis of quantization errors specific to LLMs and surprisingly discovered that, unlike tr...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Up or Down? Adaptive Rounding for Post-Training Quantization** (2020)
- *Authors:* Markus Nagel et al.
- *Direct Connection:* CBQ adopts the reconstruction-based rounding framework pioneered by AdaRound but optimizes rounding jointly across blocks to respect cross-block dependencies that AdaRound treats as independent.

**LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale** (2022)
- *Authors:* Tim Dettmers et al.
- *Direct Connection:* CBQ moves beyond the outlier-centric view established by LLM.int8() by demonstrating that ultra-low-bit failures stem from cross-layer dependencies and by designing reconstruction that directly models those dependencies.

### 🔍 Gap Identification

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models** (2023)
- *Authors:* Xiao et al.
- *Direct Connection:* CBQ targets the residual accuracy loss that persists after SmoothQuant’s outlier migration by modeling inter- and intra-layer dependencies that SmoothQuant ignores when scaling layers independently.

**AWQ: Activation-aware Weight Quantization for LLMs** (2023)
- *Authors:* Lin et al.
- *Direct Connection:* CBQ addresses AWQ’s layer-local saliency focus by reconstructing across blocks so weight rounding accounts for downstream activation interactions that dominate at ultra-low precision.

### 📊 Baseline

**GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers** (2022)
- *Authors:* Jacob Frantar et al.
- *Direct Connection:* CBQ identifies GPTQ’s limitation of independently quantizing layers and replaces the per-layer reconstruction with a cross-block reconstruction objective that couples multiple transformer blocks to capture long-range error dependencies at ultra-low bits.

**OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models** (2023)
- *Authors:* Shao et al.
- *Direct Connection:* CBQ builds upon OmniQuant’s calibration-driven PTQ setup but augments it with a cross-block reconstruction term that links multiple blocks, overcoming OmniQuant’s largely local optimization.

### 🔧 Extension

**BRECQ: Pushing the Limit of Post-Training Quantization by Block Reconstruction** (2021)
- *Authors:* Y. Li et al.
- *Direct Connection:* CBQ generalizes BRECQ’s block-reconstruction idea from a single residual block to multi-block coupling, explicitly controlling inter-layer error propagation via a cross-block loss during PTQ.

---

## Synthesis: How Prior Work Led to This Paper

GPTQ introduced a highly effective PTQ procedure for transformers that greedily reconstructs each weight matrix using second-order information, but it treats layers independently and accumulates errors across depth. BRECQ advanced reconstruction-based PTQ by optimizing groups of layers as a block to suppress inter-layer error propagation, showing that coupling adjacent layers reduces quantization damage. AdaRound provided the core technique of optimizing rounding decisions with an output-reconstruction loss, establishing the reconstruction-based PTQ paradigm that many later LLM methods inherit. SmoothQuant attacked the LLM activation outlier problem by shifting activation magnitude into weights via per-channel scaling, enabling lower precisions but leaving cross-layer interactions untouched. AWQ further mitigated outlier harms by preserving activation-sensitive weight channels through activation-aware saliency, yet its optimization remained layer-local. OmniQuant broadened calibration to both weights and activations with an omnidirectional objective, improving robustness but still optimizing primarily within layers or short blocks. LLM.int8() crystallized the outlier phenomenon in LLMs and popularized mixed-precision pathways, catalyzing outlier-centric PTQ. Taken together, these works revealed two threads: reconstruction-based PTQ is crucial, and outlier handling helps—but at ultra-low bits, locally optimized or outlier-only strategies leave significant residual error that grows with depth. A natural next step is to marry reconstruction-based rounding with an explicit mechanism that ties multiple blocks together, so optimization captures long-range inter- and intra-layer dependencies. By extending block reconstruction beyond single blocks and embedding cross-block dependency modeling into the PTQ objective, the new approach preserves accuracy in ultra-low-bit regimes where prior per-layer or outlier-centric methods falter.

---

*Analysis generated on: 2026-01-06T12:06:56.061404*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

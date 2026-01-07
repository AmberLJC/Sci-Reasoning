# Prior Work Analysis Report

## Target Paper
**Title:** E1EHO0imOb
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**PaLM: Scaling Language Modeling with Pathways** (2022)
- *Authors:* Chowdhery et al.
- *Connection:* Established SwiGLU-based Transformer MLPs as a de facto large-scale LLM architecture; the present work targets FP8 training stability precisely in this PaLM-style setting and modifies the SwiGLU component.

### 💡 Inspiration

**LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale** (2022)
- *Authors:* Dettmers et al.
- *Connection:* Identified activation outliers in transformer MLPs that break naive low-precision quantization; this insight directly motivates the paper’s analysis that outlier amplification (specifically via SwiGLU) drives FP8 training instability over long horizons.

### 📊 Baseline

**FP8 Formats for Deep Learning** (2022)
- *Authors:* Micikevicius et al.
- *Connection:* Established the E4M3/E5M2 FP8 formats and scaling recipe used for transformer training; the present work directly builds on this FP8 training paradigm and exposes its long-run instabilities when scaled to trillion-token regimes.

### 🔧 Extension

**GLU Variants Improve Transformer** (2020)
- *Authors:* Shazeer
- *Connection:* Introduced SwiGLU, the MLP activation used in modern LLMs; this paper pinpoints SwiGLU as the source of FP8 instability over long training and proposes Smooth-SwiGLU as a targeted modification of that activation.

**8-bit Optimizers via Block-wise Quantization** (2022)
- *Authors:* Dettmers et al.
- *Connection:* Demonstrated quantization of Adam’s moments to 8-bit integers to reduce memory; this work extends that line by showing, for the first time, stable FP8 quantization of both Adam moments within end-to-end FP8 LLM training.

### 🔗 Related Problem

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models** (2023)
- *Authors:* Xiao et al.
- *Connection:* Proposed smoothing/scale redistribution to handle activation outliers for INT8 inference; the current paper adopts a closely related outlier-suppression philosophy but implements it by modifying SwiGLU itself to stabilize FP8 training.

---

## Synthesis

The paper’s core innovations—stable trillion-token FP8 training, diagnosing long-horizon instabilities to SwiGLU outlier amplification, introducing Smooth-SwiGLU, and FP8-quantized Adam moments—grow directly from two lines of prior work. First, Micikevicius et al. defined the modern FP8 training paradigm (E4M3/E5M2 formats and scaling), which this work adopts as its baseline and then stress-tests far beyond prior training lengths; the discovered failure modes are a direct consequence of pushing that exact FP8 recipe to trillion-token scales. Second, the activation/outlier literature around LLM quantization (LLM.int8 and SmoothQuant) specifically identified and mitigated transformer MLP outliers in low-precision settings. Those findings catalyze the present paper’s central diagnosis: in FP8 training, outliers are progressively amplified by SwiGLU over long durations due to weight alignment dynamics. Because SwiGLU itself (from Shazeer) is now standard in PaLM-style LLMs, modifying the activation (Smooth-SwiGLU) becomes the most surgical fix that preserves model behavior while ensuring FP8 stability. Finally, the memory- and bandwidth-saving thread from 8-bit Adam optimizers is extended from integer quantization to FP8: the paper is the first to FP8-quantize both Adam moments in a full FP8 training pipeline. Together, these works directly shape the problem setting, reveal the outlier mechanism, and provide the FP8 and optimizer quantization frameworks that the paper extends.

---
*Generated: 2026-01-06T23:09:26.608900*

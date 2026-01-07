# Prior Work Analysis Report

## Target Paper

**Title:** Scaling Laws for Precision

**Conference:** ICLR 2025 (oral)

**Authors:** Tanishq Kumar, Zachary Ankner, Benjamin Frederick Spector, Blake Bordelon, Niklas Muennighoff, Mansheej Paul, Cengiz Pehlevan, Christopher Re, Aditi Raghunathan

**Keywords:** quantization, scaling laws, precision, language models

**Abstract:** 
> Low precision training and inference affect both the quality and cost of language models, but current scaling laws do not account for this. In this work, we devise "precision-aware" scaling laws for both training and inference. We propose that training in lower precision reduces the model's "effective parameter count," allowing us to predict the additional loss incurred from training in low precision and post-train quantization. For inference, we find that the degradation introduced by post-trai...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Direct Connection:* This work established the param/data power-law loss scaling that the present paper directly extends by introducing precision as a new axis via an "effective parameter count" that predicts additional loss under low precision.

**FP8 Formats for Deep Learning** (2022)
- *Authors:* Paulius Micikevicius et al.
- *Direct Connection:* By demonstrating practical low-precision (FP8) training and detailing dynamic-range/rounding effects, this work defines the training regime whose loss impact the present paper models as a precision-dependent effective capacity.

### 💡 Inspiration

**Explaining Neural Scaling Laws** (2021)
- *Authors:* Yasaman Bahri et al.
- *Direct Connection:* This theory links performance to an effective model dimension under noise, directly motivating the present paper’s key idea that finite precision acts like noise that reduces an "effective parameter count" governing loss scaling.

### 🔍 Gap Identification

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models** (2023)
- *Authors:* Xiao Xiao et al.
- *Direct Connection:* SmoothQuant documents that activation outliers and model scale make PTQ harder and proposes empirical fixes, highlighting the absence of a predictive law that the current paper fills with a quantization-aware scaling framework.

### 📊 Baseline

**GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers** (2022)
- *Authors:* Tim Dettmers Frantar et al.
- *Direct Connection:* As a primary PTQ baseline whose quantization-induced loss is well characterized, GPTQ provides the empirical target that the new precision-aware scaling law is designed to predict across model and data scales.

**AWQ: Activation-aware Weight Quantization for LLMs** (2023)
- *Authors:* Shuming Lin et al.
- *Direct Connection:* AWQ’s finding that preserving salient (outlier) channels is crucial for 4-bit LLM inference pinpoints the mechanisms of quantization degradation that the present paper abstracts into a precision-driven reduction of effective parameters.

### 🔧 Extension

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Direct Connection:* By formalizing compute-optimal tradeoffs between model size and data, this paper provides the functional form and optimization lens that the current work augments to incorporate precision, yielding new compute-optimal recommendations (e.g., larger models at lower precision).

---

## Synthesis: How Prior Work Led to This Paper

Power-law loss scaling with parameters and data was established for language models by work showing that cross-entropy decreases predictably as model size and dataset grow, providing a quantitative backbone for extrapolation. Subsequent analysis of compute-optimality unified parameters and data into a single budgeting lens, giving a functional form and optimization criterion for deciding how to allocate compute between width and data. Theoretical accounts of scaling then linked performance to an effective model dimension in the presence of noise, indicating that capacity relevant to generalization can be smaller than the raw parameter count. On the inference side, accurate post-training quantization methods such as GPTQ characterized how weight rounding errors translate into generative loss, while AWQ revealed that preserving a small set of outlier channels is critical to avoid sharp degradation at 4-bit precision. SmoothQuant further showed that activation outliers and model scale exacerbate PTQ difficulty, motivating a need to predict when and how quantization harms performance rather than only mitigate it empirically. In parallel, FP8 training established that low-precision arithmetic is feasible for pretraining, but with accuracy-sensitive tradeoffs tied to dynamic range and rounding.
Together, these works expose a gap: existing scaling laws ignore precision, while PTQ and low-precision training papers lack predictive laws for loss as precision varies. The present paper synthesizes the effective-dimension perspective with compute-optimal scaling, modeling finite precision as a reduction in effective parameter count and unifying pre- and post-training quantization into a single predictive form that explains when quantization harm grows with data and when larger, lower-precision models are compute optimal.

---

*Analysis generated on: 2026-01-06T07:29:18.446821*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

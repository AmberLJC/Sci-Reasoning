# Prior Work Analysis Report

## Target Paper
**Title:** jKUWlgra9b
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**ZeroQ: A Novel Zero Shot Quantization Framework** (2020)
- *Authors:* Li et al.
- *Connection:* ZeroQ established the calibration/reconstruction-based PTQ setting without training data that ERQ operates within, providing the foundational reconstruction formulation onto which ERQ’s sequential activation-then-weight error reduction is layered.

### 💡 Inspiration

**Data-Free Quantization Through Weight Equalization and Bias Correction** (2019)
- *Authors:* Nagel et al.
- *Connection:* This work established that modifying weights can systematically reduce activation quantization error (via equalization/bias-correction), a weight–activation interplay that ERQ formalizes and strengthens through an explicit ridge-regression objective for activation error reduction.

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models** (2023)
- *Authors:* Xiao et al.
- *Connection:* SmoothQuant shifts activation magnitude into weights to ease activation quantization without retraining; ERQ’s Aqer generalizes this principle to ViTs by learning full-precision weight updates via ridge regression specifically to minimize activation quantization error.

### 📊 Baseline

**BRECQ: Pushing the Limit of Post-Training Quantization by Block Reconstruction** (2021)
- *Authors:* Li et al.
- *Connection:* ERQ builds on the reconstruction-driven PTQ paradigm popularized by BRECQ and addresses its limitation of treating weights/activations insufficiently coupled by first minimizing activation quantization error (via ridge regression) before iteratively optimizing weight rounding.

### 🔧 Extension

**Up or Down? Adaptive Rounding for Post-Training Quantization** (2020)
- *Authors:* Nagel et al.
- *Connection:* ERQ’s Wqer explicitly refines weight rounding directions via an efficient proxy objective, directly extending AdaRound’s core idea that rounding decisions should be optimized (not fixed R2N) using a differentiable surrogate tied to reconstruction error.

### 🔗 Related Problem

**GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers** (2022)
- *Authors:* Frantar et al.
- *Connection:* GPTQ introduced importance-aware rounding for transformer weights; ERQ’s Wqer pursues the same goal for ViT layers but replaces expensive second-order machinery with an empirically efficient proxy to iteratively refine rounding directions.

---

## Synthesis

ERQ sits squarely in the reconstruction-based, training-free PTQ lineage and crystallizes two strands of prior insight into a unified, ViT-tailored procedure. First, the weight–activation coupling recognized by early PTQ works—through weight equalization and bias correction—showed that adjusting weights can alleviate activation quantization error. SmoothQuant later made this explicit in transformers by shifting activation magnitude into weights to stabilize activation quantization. ERQ’s Aqer formalizes and strengthens this idea: instead of heuristic rescaling, it solves a ridge-regression problem to update full-precision weights so that activation quantization error is directly minimized in ViT layers. Second, the shift from fixed round-to-nearest to optimized rounding, inaugurated by AdaRound and further explored in transformer PTQ such as GPTQ, established that rounding directions are learnable decisions tied to reconstruction fidelity. ERQ’s Wqer embraces this principle but avoids second-order cost by using an efficient proxy to iteratively refine rounding directions. BRECQ provided the immediate baseline—block reconstruction PTQ—upon which ERQ improves by explicitly decoupling and sequencing activation-error reduction before weight rounding. Operating within the data/calibration-efficient PTQ framework typified by ZeroQ, ERQ’s two-step design surfaces the interdependence between activations and weights as the core lever, yielding a targeted, sequential error-reduction pipeline for ViTs.

---
*Generated: 2026-01-06T23:09:26.503986*

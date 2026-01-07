# Prior Work Analysis Report

## Target Paper

**Title:** On Quantizing Neural Representation for Variable-Rate Video Coding

**Conference:** ICLR 2025 (spotlight)

**Authors:** Junqi Shi, Zhujia Chen, Hanfei Li, Qi Zhao, Ming Lu, Tong Chen, Zhan Ma

**Keywords:** Variable Rate, Video Coding, Quantization, Neural Representation

**Abstract:** 
> This work introduces NeuroQuant, a novel post-training quantization (PTQ) approach tailored to non-generalized Implicit Neural Representations for variable-rate Video Coding (INR-VC). Unlike existing methods that require extensive weight retraining for each target bitrate, we hypothesize that variable-rate coding can be achieved by adjusting quantization parameters (QPs) of pre-trained weights. Our study reveals that traditional quantization methods, which assume inter-layer independence, are in...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference** (2018)
- *Authors:* Jacob et al.
- *Direct Connection:* This paper introduced per-channel weight quantization and practical calibration procedures, which are directly adapted here as channel-wise QP control to achieve fine-grained, representation-preserving rate adjustment in INR-VC.

### 💡 Inspiration

**BRECQ: Pushing the Limit of Post-Training Quantization by Block Reconstruction** (2021)
- *Authors:* Li et al.
- *Direct Connection:* BRECQ showed that layer-independent PTQ is suboptimal and proposed block-level reconstruction to capture cross-layer dependencies, inspiring the network-wise calibration that mitigates inter-layer coupling in INR-VC.

### 🔍 Gap Identification

**GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers** (2022)
- *Authors:* Frantar et al.
- *Direct Connection:* GPTQ models cross-channel dependencies with efficient second-order PTQ, but it neither targets INR-VC nor couples sensitivity to rate, motivating this work’s task-specific sensitivity theory and rate-aware mixed-precision formulation.

### 📊 Baseline

**NeRV: Neural Representations for Videos** (2021)
- *Authors:* Chen et al.
- *Direct Connection:* NeRV established INR-based video coding by storing a per-video network’s quantized weights for compression—typically retraining per target bitrate—providing the baseline formulation that this work replaces with PTQ-driven QP adjustment for variable rate without retraining.

### 🔧 Extension

**HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision** (2019)
- *Authors:* Dong et al.
- *Direct Connection:* HAWQ’s mixed-precision bit-allocation via Hessian-based sensitivity directly motivates redefining variable-rate INR-VC as a mixed-precision quantization problem and informs the sensitivity criteria used for rate control.

### 🔗 Related Problem

**Up or Down? Adaptive Rounding for Post-Training Quantization** (2020)
- *Authors:* Nagel et al.
- *Direct Connection:* AdaRound’s idea of optimizing weight rounding via a reconstruction objective is leveraged here to formulate a representation-oriented PTQ calibration that minimizes quantization-induced distortion on decoded video signals.

---

## Synthesis: How Prior Work Led to This Paper

Neural representations for video established that a single per-video network could store a sequence’s content and be compressed by quantizing and entropy coding its weights, but this practice typically required retraining separate models for different bitrates. Practical quantization foundations showed that per-channel weight quantization and simple calibration substantially reduce quant error by addressing channel imbalance, while Hessian-aware mixed-precision quantization framed bit allocation as sensitivity-guided optimization under a bit budget. Subsequent PTQ advances demonstrated that independent layerwise treatment is inadequate: block reconstruction exposed strong cross-layer coupling that must be accounted for during calibration, and adaptive rounding optimized the discrete rounding decision itself by minimizing a reconstruction loss on calibration data. Efficient second-order PTQ for large generative models further highlighted that inter-channel dependencies matter and can be handled analytically, though without an explicit linkage between sensitivity and compression rate.

Taken together, these works revealed a clear opportunity: treat bitrate control in INR-based video coding as a mixed-precision quantization problem, use sensitivity to guide bit allocation, and calibrate at the network level to respect inter-layer dependencies—while adopting channel-wise granularity for finer control. By unifying sensitivity-driven bitwidth assignment with representation-oriented calibration and channel-wise quantization, the present work provides variable-rate INR-VC without retraining, naturally extending PTQ theory to a rate-distortion setting tailored to implicit video representations.

---

*Analysis generated on: 2026-01-06T11:29:36.867292*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

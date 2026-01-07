# Prior Work Analysis Report

## Target Paper

**Title:** Surprising Effectiveness of pretraining Ternary  Language Model at Scale

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ayush Kaushal, Tejas Vaidhya, Arnab Kumar Mondal, Tejas Pandey, Aaryan Bhagat, Irina Rish

**Keywords:** Large Language Models, low-bit language models, quantization-aware training, pretraining of large language models, and scaling laws

**Abstract:** 
> Rapid advancements in GPU computational power has outpaced memory capacity and bandwidth growth, creating bottlenecks in Large Language Model (LLM) inference. Post-training quantization is the leading method for addressing memory-related bottlenecks in LLM inference, but it suffers from significant performance degradation below 4-bit precision. This paper addresses these challenges by investigating the pretraining of low-bitwidth models specifically Ternary Language Models (TriLMs) as an alterna...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Kaplan et al.
- *Direct Connection:* Its power-law characterization of loss versus model/data/compute supplies the framework extended here to analyze scaling in terms of total model size measured in bits.

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Hoffmann et al.
- *Direct Connection:* The Chinchilla compute–data optimality results guide token budgets and comparative scaling methodology that underpin the bit-level scaling analysis of low-precision models.

### 💡 Inspiration

**BitNet b1.58: 1.58-bit Large Language Models** (2024)
- *Authors:* Wang et al.
- *Direct Connection:* By demonstrating that end-to-end training of ternary-weight Transformers (≈1.58-bit) can approach floating-point quality, this work directly inspired scaling up pretraining of ternary LMs and systematically comparing their scaling behavior against post-training quantized models.

### 📊 Baseline

**GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers** (2022)
- *Authors:* Frantar et al.
- *Direct Connection:* As a leading PTQ baseline for 3–4-bit LLMs whose quality degrades below 4-bit, it is the primary competitor that the ternary-pretrained models are designed to outperform at ultra-low precision.

**AWQ: Activation-aware Weight Quantization for LLMs** (2023)
- *Authors:* Lin et al.
- *Direct Connection:* This activation-aware PTQ method preserves 4-bit accuracy but still struggles in sub-4-bit regimes, motivating the shift to pretraining ternary weights as an alternative path to ultra-low-bit quality.

### 🔧 Extension

**Trained Ternary Quantization** (2017)
- *Authors:* Chenzhuo Zhu et al.
- *Direct Connection:* The paper’s learned positive/negative scaling for ternary weights and straight-through estimation provide the concrete quantizer and training recipe that are extended to Transformer weight matrices for large-scale ternary LM pretraining.

### 🔗 Related Problem

**TernaryBERT: Distillation-aware Ultra-low Bit BERT** (2020)
- *Authors:* Zhang et al.
- *Direct Connection:* By showing Transformer-based language models can retain accuracy under ternary weights via task-aware training, it established feasibility in NLP and informed design choices for moving from finetuning to full autoregressive pretraining at scale.

---

## Synthesis: How Prior Work Led to This Paper

Early work on ternary quantization established both the mechanism and feasibility of extreme weight discretization. Trained Ternary Quantization introduced a learned ternary quantizer with positive/negative scales and straight‑through estimation, providing a practical recipe for training networks with 2‑bit weight representations. In the Transformer/NLP setting, TernaryBERT showed that language models can sustain ternary weights when training is task‑aware, signaling that low‑bit transformers are viable beyond vision. More recently, BitNet b1.58 demonstrated that end‑to‑end training of ternary‑weight Transformers can achieve competitive perplexity, bringing ternary LMs from niche feasibility to a realistic path for large‑scale models. In parallel, post‑training quantization advanced with GPTQ and AWQ, which preserve strong 4‑bit accuracy but empirically degrade below 4 bits, especially on generative tasks. Finally, the scaling-law literature, from Kaplan’s power laws to Hoffmann’s compute‑optimal Chinchilla prescriptions, defined how to evaluate model quality as a function of parameters, data, and compute, setting standards for rigorous scaling analyses. Together, these works expose a clear opportunity: PTQ struggles at sub‑4‑bit precision, while learned ternary training appears promising but lacked systematic, large‑scale validation and a principled scaling treatment. Building on TTQ’s quantizer mechanics and BitNet’s proof of viability, and using GPTQ/AWQ as strong PTQ baselines within a Kaplan–Chinchilla scaling framework, the present study pretrains ternary LMs across sizes and data budgets, enabling a direct, bit‑normalized scaling comparison that reveals the advantages of ternary pretraining at billion‑parameter scales.

---

*Analysis generated on: 2026-01-06T09:20:27.786919*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

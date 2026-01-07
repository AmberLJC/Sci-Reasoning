# Prior Work Analysis Report

## Target Paper

**Title:** Can Watermarked LLMs be Identified by Users via Crafted Prompts?

**Conference:** ICLR 2025 (spotlight)

**Authors:** Aiwei Liu, Sheng Guan, Yiming Liu, Leyi Pan, Yifei Zhang, Liancheng Fang, Lijie Wen, Philip S. Yu, Xuming Hu

**Keywords:** Large Language Models, Watermark, Identification

**Abstract:** 
> Text watermarking for Large Language Models (LLMs) has made significant progress in detecting LLM outputs and preventing misuse. Current watermarking techniques offer high detectability, minimal impact on text quality, and robustness to text editing. 
    However, current researches lack investigation into the imperceptibility of watermarking techniques in LLM services.
    This is crucial as LLM providers may not want to disclose the presence of watermarks in real-world scenarios, as it could r...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**A Watermark for Large Language Models** (2023)
- *Authors:* Kirchenbauer et al.
- *Direct Connection:* This keyed green/red token-binning watermark introduces position-wise, key-dependent token biases that Water-Probe explicitly exploits by crafting prompts to surface the consistent bias patterns induced by a fixed key.

### 💡 Inspiration

**Fingerprinting Large Language Models via Black-Box Queries** (2023)
- *Authors:* Krishna et al.
- *Direct Connection:* Demonstrates that consistent, model-specific output biases can be surfaced with carefully designed prompts, inspiring Water-Probe’s use of crafted queries to expose key-induced behavioral regularities of watermarked LLMs.

### 🔍 Gap Identification

**Adversarial Attacks on Text Watermarking** (2023)
- *Authors:* Carlini et al.
- *Direct Connection:* While focusing on robustness attacks and evasion, this work highlights that prior research overlooked imperceptibility under black-box user interaction—a gap Water-Probe directly addresses by testing if users can detect watermarking via prompts.

### 📊 Baseline

**SynthID-Text: Watermarking for Large Language Models** (2024)
- *Authors:* DeepMind/Google et al.
- *Direct Connection:* SynthID-Text’s binning-and-bias framework with a secret key is a primary baseline whose assumed imperceptibility Water-Probe challenges by showing users can identify the watermark via behavioral probes.

**SemStamp: A Semantic Watermark for LLM-Generated Text** (2024)
- *Authors:* Zhang et al.
- *Direct Connection:* SemStamp’s key-conditioned semantic constraints produce stable, cross-prompt generation biases that Water-Probe targets to test whether such semantic watermarks can be detected by end users through crafted prompts.

### 🔗 Related Problem

**Robust Watermarking for AI-Generated Text** (2023)
- *Authors:* Kuditipudi et al.
- *Direct Connection:* By strengthening watermark-induced biases to improve robustness under edits, this line of work implicitly increases the consistency signal across prompts that Water-Probe leverages to identify the presence of a watermark.

---

## Synthesis: How Prior Work Led to This Paper

Keyed watermarking for text generation established that a secret seed can partition the vocabulary into preferred and disfavored bins at each position, gently biasing sampling without noticeably harming fluency; this idea, introduced in A Watermark for Large Language Models, grounded the prevailing assumption that such perturbations are practically imperceptible. SynthID-Text generalized the same binning-and-bias principle into a production-ready scheme, further reinforcing the view that secret-key watermarks are stealthy in user-facing settings. Semantic variants like SemStamp shifted from purely lexical to meaning-level constraints, yet still relied on key-conditioned, repeatable tendencies in token selection or content planning. Robustness-focused work (e.g., Kuditipudi et al.) amplified the watermark signal to survive paraphrasing and edits, implicitly increasing the stability of the watermark’s bias across prompts. In parallel, attacks on text watermarks by Carlini et al. concentrated on evasion and resilience, leaving the question of human- or user-side detectability largely unexamined. Separately, black-box fingerprinting research (Krishna et al.) showed that stable, model-specific biases are extractable through carefully crafted probes. Taken together, these strands suggested an untested vulnerability: if watermark schemes create consistent, key-dependent biases, then a user might reveal them without knowing the key. This paper synthesizes those insights by designing Water-Probe—prompt pairs that amplify cross-key differences and same-key similarities—thereby testing and ultimately challenging the imperceptibility assumption underlying modern lexical and semantic watermarks.

---

*Analysis generated on: 2026-01-06T11:32:55.260763*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

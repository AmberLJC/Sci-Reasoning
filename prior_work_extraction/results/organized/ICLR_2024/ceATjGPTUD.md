# Prior Work Analysis Report

## Target Paper

**Title:** Large Language Models are Efficient Learners of Noise-Robust Speech Recognition

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yuchen Hu, CHEN CHEN, Chao-Han Huck Yang, Ruizhe Li, Chao Zhang, Pin-Yu Chen, EngSiong Chng

**Keywords:** Large language models, automatic speech recognition, generative error correction, noise-robustness

**Abstract:** 
> Recent advances in large language models (LLMs) have promoted generative error correction (GER) for automatic speech recognition (ASR), which leverages the rich linguistic knowledge and powerful reasoning ability of LLMs to improve recognition results. The latest work proposes a GER benchmark with "HyPoradise" dataset to learn the mapping from ASR N-best hypotheses to ground-truth transcription by efficient LLM finetuning, which shows great effectiveness but lacks specificity on noise-robust ASR...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**HyPoradise: Benchmarking Generative Error Correction for ASR with LLMs** (2023)
- *Authors:* Yuchen Hu et al.
- *Direct Connection:* This work introduced the GER task and dataset that finetunes LLMs to map ASR N-best hypotheses to ground-truth transcripts, which the current paper directly extends to noisy conditions and uses as its primary methodological and data foundation.

**Recognizer Output Voting Error Reduction (ROVER)** (1997)
- *Authors:* Jonathan G. Fiscus
- *Direct Connection:* ROVER established that aggregating multiple hypotheses yields robust signals for error reduction, motivating the current paper’s use of the N-best list itself as a source to derive a robust language-space noise embedding.

**Finding consensus in speech recognition: Word error minimization and other applications of confusion networks** (2000)
- *Authors:* Lidia Mangu et al.
- *Direct Connection:* By converting N-best lists into posterior-bearing confusion networks, this work shows how hypothesis distributions encode uncertainty—an insight the current paper leverages to extract noise-condition cues from N-best statistics in language space.

**The 4th CHiME Speech Separation and Recognition Challenge** (2017)
- *Authors:* Emmanuel Vincent et al.
- *Direct Connection:* CHiME-4 codified evaluation under real and simulated noisy conditions, highlighting the specific robustness gap that the current paper addresses by bringing GER explicitly into the noise-robust ASR setting.

### 💡 Inspiration

**An Investigation of Deep Neural Networks for Noise Robust Speech Recognition** (2013)
- *Authors:* Martin L. Seltzer et al.
- *Direct Connection:* This paper’s noise-aware training concept—conditioning recognition models on explicit noise representations—directly inspires the current work’s core idea of conditioning GER with a noise embedding, adapted here into language space to avoid cross-modality mismatch.

### 🔗 Related Problem

**Deliberation Networks: Sequence to Sequence Learning by Learning to Deliberate** (2017)
- *Authors:* Yingce Xia et al.
- *Direct Connection:* The deliberation paradigm—feeding first-pass hypotheses into a second-pass generator to refine outputs—directly informs the GER framing of consuming N-best hypotheses to produce corrected transcripts.

---

## Synthesis: How Prior Work Led to This Paper

HyPoradise established the generative error correction (GER) formulation for ASR by finetuning large language models to transform an N-best list into the ground-truth transcript, concretely defining the N-best-to-reference mapping and providing a benchmark to study it. Noise-aware training showed that explicitly conditioning recognition models on noise representations can materially improve robustness, introducing the principle of noise conditioning that later methods could adapt. ROVER demonstrated that aggregating multiple hypotheses exposes complementary evidence useful for error reduction, while the confusion network framework made this concrete by turning N-best lists into posteriors whose dispersion encodes uncertainty—signals often correlated with acoustic difficulty. Deliberation networks contributed the second-pass paradigm that consumes first-pass hypotheses to generate improved sequences, validating the general mechanism of hypothesis-informed generation. The CHiME-4 challenge crystallized the community’s focus on realistic noisy environments, standardizing noise conditions and clarifying robustness targets.
Together, these works revealed a natural opportunity: combine GER’s hypothesis-to-transcript mapping with noise-aware conditioning, but do so without injecting raw audio features that cause cross-modality mismatch for LLMs. The current paper synthesizes this by extracting a language-space noise embedding directly from N-best statistics—akin to confusion-network uncertainty—thereby preserving the textual modality while capturing noise conditions and extending HyPoradise to evaluate GER under explicit noisy scenarios.

---

*Analysis generated on: 2026-01-06T13:49:36.324318*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

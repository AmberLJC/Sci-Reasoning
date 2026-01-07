# Prior Work Analysis Report

## Target Paper

**Title:** Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision

**Conference:** ICLR 2024 (spotlight)

**Authors:** Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Chunyi Li, Wenxiu Sun, Qiong Yan, Guangtao Zhai, Weisi Lin

**Keywords:** Benchmark, Vision-Language, Large Language Models, Low-level Vision, Image Quality Assessment

**Abstract:** 
> The rapid evolution of Multi-modality Large Language Models (MLLMs) has catalyzed a shift in computer vision from specialized models to general-purpose foundation models. Nevertheless, there is still an inadequacy in assessing the abilities of MLLMs on **low-level visual perception and understanding**. To address this gap, we present **Q-Bench**, a holistic benchmark crafted to systematically evaluate potential abilities of MLLMs on three realms: low-level visual perception, low-level visual des...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Visual Instruction Tuning** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* Q-Bench targets and probes the very class of general-purpose MLLMs instantiated by LLaVA’s visual instruction–tuned QA interface, adopting this QA-style interaction to evaluate low-level perception and description.

**PIPAL: A Large-Scale Image Quality Assessment Dataset for Perceptual Image Restoration** (2020)
- *Authors:* Jinjin Gu et al.
- *Direct Connection:* Q-Bench’s overall visual quality assessment component draws on PIPAL’s formulation of human-perceived quality for restoration artifacts to define stimuli and assessment criteria for MLLMs.

**KonIQ-10k: An Ecologically Valid Database for Deep Learning of Blind Image Quality Assessment** (2018)
- *Authors:* Ionut Hosu et al.
- *Direct Connection:* Q-Bench leverages KonIQ-10k’s in-the-wild MOS-based IQA paradigm to ground its evaluation of MLLMs on authentic distortions and human quality judgments.

**LIVE In the Wild Image Quality Challenge Database** (2016)
- *Authors:* Kede Ma et al.
- *Direct Connection:* Q-Bench adopts LIVE Challenge’s authentic-distortion, MOS-driven problem setup as the basis for testing whether MLLMs can assess overall visual quality beyond synthetic degradations.

### 🔍 Gap Identification

**MMBench: A Holistic Evaluation of Multimodal Large Language Models** (2023)
- *Authors:* Anonymous et al.
- *Direct Connection:* Q-Bench explicitly addresses MMBench’s lack of dedicated low-level visual perception and quality assessment coverage by introducing purpose-built tasks and datasets for these abilities.

**SEED-Bench: Benchmarking Multimodal Large Language Models** (2023)
- *Authors:* Anonymous et al.
- *Direct Connection:* Q-Bench fills SEED-Bench’s identified gap where recognition and reasoning dominate while fine-grained degradation perception and visual quality understanding are largely absent.

**MME: A Comprehensive Evaluation of Multimodal Large Language Models** (2023)
- *Authors:* Anonymous et al.
- *Direct Connection:* Q-Bench is designed to complement MME by adding systematic evaluation dimensions specifically for low-level perception, detailed low-level descriptions, and overall image quality—areas MME does not directly test.

---

## Synthesis: How Prior Work Led to This Paper

Visual instruction–tuned MLLMs were crystallized by Visual Instruction Tuning (LLaVA), which established a QA-style interface enabling general-purpose vision-language agents to be probed through natural language. Parallelly, multimodal benchmarks such as MMBench, SEED-Bench, and MME organized comprehensive test suites for recognition, reasoning, and grounding, but their task inventories largely emphasized high-level semantics and commonsense while providing little direct coverage of low-level perception of degradations or visual quality judgment. On the image quality side, PIPAL introduced large-scale human judgments targeting perceptual artifacts from restoration algorithms, emphasizing perceptual fidelity beyond simple distortion metrics. KonIQ-10k contributed an ecologically valid, in-the-wild MOS framework for no-reference IQA, highlighting authentic distortions. The LIVE In the Wild Challenge similarly framed IQA with authentic degradations and MOS, becoming a cornerstone for evaluating subjective visual quality in the wild.

These lines of work collectively suggested an opportunity: MLLMs, already queried via instruction-tuned QA, lacked targeted evaluation on low-level perception and human-aligned quality understanding that IQA datasets rigorously define. Building on LLaVA’s interaction paradigm while addressing the gaps in existing MLLM benchmarks, and grounding tasks in the MOS- and artifact-centric formulations from PIPAL, KonIQ-10k, and LIVE Challenge, Q-Bench naturally emerges as a benchmark that systematizes three complementary dimensions—low-level perception, descriptive articulation of low-level attributes, and overall visual quality assessment—to holistically test whether general-purpose MLLMs possess low-level visual competence.

---

*Analysis generated on: 2026-01-07T00:16:55.625927*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

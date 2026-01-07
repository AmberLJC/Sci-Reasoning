# Prior Work Analysis Report

## Target Paper

**Title:** Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors

**Conference:** ICLR 2024 (oral)

**Authors:** Ido Amos, Jonathan Berant, Ankit Gupta

**Keywords:** Pre Training, Transformers, State Space Models, Long Range Models, Fair Evaluation

**Abstract:** 
> Modeling long-range dependencies across sequences is a longstanding goal in machine learning and has led to architectures, such as state space models, that dramatically outperform Transformers on long sequences. However, these impressive empirical gains have been by and large demonstrated on benchmarks (e.g. Long Range Arena), where models are randomly initialized and trained to predict a target label from an input sequence. In this work, we show that random initialization leads to gross overest...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Long Range Arena: A Benchmark for Efficient Transformers** (2020)
- *Authors:* Yi Tay et al.
- *Direct Connection:* LRA established the long-sequence benchmark and the default train-from-scratch evaluation protocol (including tasks like PathX) that this work argues biases architectural comparisons and replaces with in-domain denoising pretraining.

### 💡 Inspiration

**BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** (2019)
- *Authors:* Jacob Devlin et al.
- *Direct Connection:* BERT introduced masked-language-model denoising pretraining, which this work repurposes on the downstream task’s unlabeled inputs to inject data-driven priors before supervised fine-tuning across architectures.

**Masked Autoencoders Are Scalable Vision Learners** (2022)
- *Authors:* Kaiming He et al.
- *Direct Connection:* MAE demonstrated that masked reconstruction on image patches yields strong in-domain representations, which this work adapts to image-like long-range tasks (e.g., Pathfinder/PathX) for fair, modality-appropriate pretraining.

### 📊 Baseline

**Efficiently Modeling Long Sequences with Structured State Spaces** (2022)
- *Authors:* Albert Gu et al.
- *Direct Connection:* S4 is the primary SSM baseline whose reported superiority on LRA/PathX under scratch training is re-evaluated here by introducing data-driven denoising pretraining that shrinks the Transformer–SSM gap and boosts SSM results.

### 🔧 Extension

**Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5)** (2020)
- *Authors:* Colin Raffel et al.
- *Direct Connection:* T5’s span-corruption denoising objective directly informs the pretraining objective used here for long-sequence text, adapted to operate solely on the downstream task data to ensure fair initialization.

### 🔗 Related Problem

**Hyena Hierarchy: Towards Larger Context with Recursive Gating** (2023)
- *Authors:* Francesco Poli et al.
- *Direct Connection:* Hyena reported state-of-the-art long-range results on LRA under the same scratch-training regime, motivating the need to reassess such claims using identical data-driven priors across architectures.

---

## Synthesis: How Prior Work Led to This Paper

Long Range Arena codified the evaluation of long-sequence modeling with a fixed suite of tasks and a train-from-scratch protocol that became the de facto standard, and under this setup large performance gaps were repeatedly observed across architectures on tasks like PathX. Building on that regime, Structured State Spaces (S4) showed strong advantages over Transformers and introduced PathX as a particularly challenging long-context task, with results reported under scratch training. Hyena further advanced non-attention long-range modeling, again establishing gains on LRA using the same training-from-scratch convention. In parallel, self-supervised denoising emerged as a way to encode data-driven priors without labels: BERT’s masked language modeling learned in-domain statistics from raw text; T5’s span corruption extended denoising to longer contiguous spans that better capture long-range dependencies; and MAE showed that masked patch reconstruction on images can produce powerful representations from the same data distribution.
Taken together, these strands suggested an opportunity: the scratch-training protocol in long-range benchmarks may inflate architectural differences by omitting simple, modality-appropriate denoising priors that are already known to be effective. The present work synthesizes this insight by applying standard denoising pretraining using only the downstream task data—span corruption for text and masked reconstruction for image-like inputs—across competing architectures, then re-evaluating on LRA. This data-driven initialization dramatically lifts all models, collapses reported gaps between Transformers and SSMs, and yields new state-of-the-art results on challenging PathX variants, establishing a fairer comparison paradigm for long-sequence modeling.

---

*Analysis generated on: 2026-01-06T07:56:52.502489*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

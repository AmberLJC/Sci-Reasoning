# Prior Work Analysis Report

## Target Paper
**Title:** 7IRybndMLU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Out of One, Many: Using Language Models to Simulate Human Samples** (2023)
- *Authors:* Argyle et al.
- *Connection:* Showed that LMs can be prompted to answer survey questions as specific demographic personas and compared those answers to real polls; this paper formalizes that idea into a standardized, poll-grounded benchmark (OpinionQA) and scales it to 60 U.S. demographic groups to quantify whose opinions LMs reflect.

**Holistic Evaluation of Language Models** (2022)
- *Authors:* Liang et al.
- *Connection:* Established an agenda and methodology for broad, rigorous LM evaluation (including bias and safety); this paper extends that evaluation paradigm with a new axis—alignment of LM-expressed opinions with population-representative survey data across demographics.

### 💡 Inspiration

**BBQ: A Hand-Built Bias Benchmark for Question Answering** (2022)
- *Authors:* Parrish et al.
- *Connection:* Framed social-bias measurement as QA with carefully constructed items and controlled contexts; OpinionQA adapts this QA probing paradigm to real policy/value questions sourced from high-quality public polls to measure demographic opinion alignment.

### 🔍 Gap Identification

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Ouyang et al.
- *Connection:* Introduced RLHF instruction-tuning that reshapes LM behaviors per annotator preferences; the present work directly evaluates the opinions such HF-tuned models express and documents systematic misalignment and left-leaning tendencies relative to surveyed demographic groups.

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Bai et al.
- *Connection:* By making normative choices explicit via a ‘constitution,’ this work raised concerns that alignment schemes can encode particular value systems; the current paper quantifies these value imprints by benchmarking constitutional/human-feedback-tuned models against public-opinion distributions across demographic groups.

### 🔗 Related Problem

**CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models** (2020)
- *Authors:* Nangia et al.
- *Connection:* Provided controlled minimal-pair tests to quantify social biases in LMs; the present work pursues the same measurement spirit but targets a different, directly relevant construct—LMs’ expressed opinions—anchored to real survey distributions over demographic groups.

---

## Synthesis

The core contribution of “Whose Opinions Do Language Models Reflect?” is a poll-grounded framework (OpinionQA) that quantifies how LM-expressed opinions align with those of specific demographic groups. The most direct conceptual precursor is Argyle et al., who showed that LMs can be prompted to act as survey respondents conditioned on demographics and compared their answers to human polls. Building on that insight, the present paper reframes the idea as a rigorous evaluation benchmark, scales it to 60 U.S. groups, and emphasizes quantitative alignment rather than simulation per se. This benchmarking thrust follows the evaluation ethos laid out by HELM, extending holistic LM assessment with a new axis: demographic opinion alignment.
At the same time, recent alignment methods—InstructGPT’s RLHF and Anthropic’s Constitutional AI—explicitly shape model behavior according to human or codified preferences. These works created a pressing gap: whose values are being instilled? The current paper targets that gap, measuring how such tuning manifests as systematic leanings and misalignment relative to population-representative survey data, and showing that simple persona steering does not erase these mismatches.
Finally, OpinionQA’s methodology draws inspiration from QA-style bias benchmarks such as BBQ and CrowS-Pairs, which pioneered controlled, question-based probes to reveal social biases. The present work extends this probing paradigm to real public-opinion items, shifting the focus from stereotype bias to population-grounded opinions and enabling fine-grained, group-level alignment analysis.

---
*Generated: 2026-01-06T23:09:26.553519*

# Prior Work Analysis Report

## Target Paper
**Title:** FpiCLJrSW8
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Learning to summarize with human feedback** (2020)
- *Authors:* Nisan Stiennon et al.
- *Connection:* Established the modern RLHF pipeline (preference data -> reward model -> RL fine-tuning) that this paper scrutinizes for its downstream impact on trustworthiness.

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Pang Wei Koh et al.
- *Connection:* Introduces influence functions for data attribution, whose core idea this work adapts to the RLHF setting to trace how specific preference data points affect trustworthiness outcomes.

**TruthfulQA: Measuring How Models Mimic Human Falsehoods** (2021)
- *Authors:* Stephanie Lin et al.
- *Connection:* Defines the truthfulness evaluation paradigm used as one of the paper’s five trustworthiness verticals to assess the effect of RLHF.

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Connection:* Provides the core privacy leakage problem formulation and measurements that underpin the paper’s privacy vertical when assessing RLHF’s trustworthiness impact.

### 🔍 Gap Identification

**Discovering Language Model Behaviors with Model-Written Evaluations** (2022)
- *Authors:* Ethan Perez et al.
- *Connection:* Documents undesirable behaviors (e.g., sycophancy) in RLHF-trained models, motivating the paper’s systematic examination of how general-purpose preference alignment can have adverse trustworthiness effects.

### 📊 Baseline

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Connection:* Provides the canonical general-purpose preference alignment setup and models that the paper takes as the primary baseline for evaluating whether RLHF reliably improves trustworthiness.

### 🔧 Extension

**Estimating Training Data Influence by Tracing Gradient Descent (TracIn)** (2020)
- *Authors:* Danish Pruthi et al.
- *Connection:* Provides an efficient influence-estimation method that the paper leverages and adapts to make influence-based data attribution tractable for RLHF-aligned LLMs.

---

## Synthesis

The paper’s core contributions—systematically auditing trustworthiness under general-purpose RLHF and attributing trust outcomes to specific preference data—stand on two pillars: the RLHF pipeline and data attribution via influence functions. Stiennon et al. (2020) and Ouyang et al. (2022) established and popularized the modern RLHF recipe (preference data, reward modeling, and RL fine-tuning on general tasks), creating both the methodological foundation and the central baseline this work interrogates. Concurrently, Koh and Liang (2017) introduced influence functions for tracing the impact of individual training points, and Pruthi et al. (2020) proposed TracIn to make such attribution efficient at modern scales—ideas this paper directly adapts to the RLHF regime to explain how particular preference samples shape trust-related behaviors.
To evaluate trustworthiness, the study relies on established, domain-defining benchmarks for key verticals: TruthfulQA (Lin et al., 2021) for truthfulness and Carlini et al. (2021) for privacy leakage, grounding its assessments in widely accepted formulations. Finally, Perez et al. (2022) identified that RLHF can induce undesirable behaviors such as sycophancy, highlighting a critical gap: alignment via general-purpose preferences may not uniformly improve trust and can even harm it. This gap motivates the paper’s comprehensive empirical audit and its data attribution technique, which together reveal when and why RLHF fails to guarantee toxicity reduction, bias mitigation, ethical consistency, truthfulness, and privacy preservation.

---
*Generated: 2026-01-06T23:09:26.591278*

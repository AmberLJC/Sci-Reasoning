# Prior Work Analysis Report

## Target Paper

**Title:** Better Instruction-Following Through Minimum Bayes Risk

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ian Wu, Patrick Fernandes, Amanda Bertsch, Seungone Kim, Sina Khoshfetrat Pakazad, Graham Neubig

**Keywords:** LLM, instruction-following, test time compute, decoding, MBR, minimal bayes risk, LLM judges, self-improvement

**Abstract:** 
> General-purpose LLM judges capable of human-level evaluation provide not only a scalable and accurate way of evaluating instruction-following LLMs but also new avenues for supervising and improving their performance. One promising way of leveraging LLM judges for supervision is through Minimum Bayes Risk (MBR) decoding, which uses a reference-based evaluator to select a high-quality output from amongst a set of candidate outputs. In the first part of this work, we explore using MBR decoding as a...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Minimum Bayes-Risk Decoding for Statistical Machine Translation** (2004)
- *Authors:* Shankar Kumar and William Byrne
- *Direct Connection:* This work establishes the MBR decoding objective that the current paper directly instantiates for instruction-following by swapping in an LLM judge as the utility function.

**MT-Bench: Evaluating Large Language Models with Multi-Turn Questions and LLM-as-a-Judge** (2023)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* This paper operationalizes LLM-as-a-judge and provides the MT-Bench setting that the current work both evaluates on and leverages conceptually to use an LLM judge as the MBR utility.

**AlpacaEval 2.0: An Automatic Evaluation for Instruction Following Models** (2024)
- *Authors:* Yizhong Wang et al. (AlpacaEval team)
- *Direct Connection:* It supplies the LLM-as-a-judge evaluation protocol and benchmark on which the paper demonstrates that MBR with LLM judges outperforms greedy and best-of-N decoding.

### 💡 Inspiration

**Minimum Bayes Risk Decoding with Neural Reference Metrics Improves Neural Machine Translation** (2022)
- *Authors:* Markus Freitag et al.
- *Direct Connection:* By showing that MBR with learned neural metrics (e.g., COMET/BLEURT) beats lexical metrics, this work motivates replacing those metrics with a stronger LLM judge within the same MBR framework.

### 📊 Baseline

**Training Language Models to Follow Instructions with Human Feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* This work popularized best-of-N selection using a reference-free reward model at inference, which serves as a primary baseline that the paper improves upon with reference-based MBR selection.

### 🔧 Extension

**Sampling-Based Minimum Bayes Risk Decoding for Neural Machine Translation** (2020)
- *Authors:* Thijs Eikema and Wilker Aziz
- *Direct Connection:* The paper’s candidate/reference sampling scheme for approximating MBR risk is adopted here, but with the risk computed by an LLM judge rather than lexical or embedding metrics.

**Direct Preference Optimization: Your Language Model Is Secretly a Reward Model** (2023)
- *Authors:* Alexander Rafailov et al.
- *Direct Connection:* DPO provides the preference-learning mechanism the paper uses to retain test-time gains by distilling MBR-selected winners into the model.

---

## Synthesis: How Prior Work Led to This Paper

Minimum Bayes Risk (MBR) decoding was originally formulated for machine translation to select outputs that minimize expected loss under a task-specific utility (Kumar and Byrne), and later adapted to neural generation with a practical sampling-based approximation that uses model-generated candidates and references (Eikema and Aziz). Subsequent work demonstrated that the choice of utility is pivotal: replacing lexical metrics with learned neural reference metrics like COMET/BLEURT markedly improves MBR effectiveness (Freitag et al.), highlighting that stronger evaluators yield stronger MBR selection. In parallel, evaluation research established that large language models can reliably act as judges to score conversational quality; MT-Bench operationalized GPT-4-as-a-judge for multi-turn instruction following (Zheng et al.), and AlpacaEval 2.0 standardized automatic, judge-based comparisons for instruction-following models with attention to known biases. Separately, instruction tuning with human feedback popularized best-of-N selection using a reference-free reward model at inference (Ouyang et al.), while preference-learning methods such as Direct Preference Optimization (Rafailov et al.) showed how to turn pairwise choices into trainable supervision.
Bringing these strands together, the current work replaces brittle lexical/embedding utilities in sampling-based MBR with an LLM judge, leveraging established judge reliability from MT-Bench/AlpacaEval to score candidates and select responses that better follow instructions than best-of-N reward-model selection. Recognizing that MBR’s gains are test-time only, it then applies DPO to distill the MBR winners into the model, retaining improvements without extra decoding cost. This synthesis is a natural progression: mature MBR machinery, evidence that stronger evaluators boost MBR, the emergence of LLM-as-judge as a high-fidelity utility, and practical preference optimization collectively point to judge-driven MBR for inference and DPO-based consolidation for training.

---

*Analysis generated on: 2026-01-06T09:53:16.919052*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

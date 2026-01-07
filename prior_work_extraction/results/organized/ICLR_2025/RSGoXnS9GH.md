# Prior Work Analysis Report

## Target Paper

**Title:** FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zhiting Fan, Ruizhe Chen, Tianxiang Hu, Zuozhu Liu

**Keywords:** Fairness, Benchmark, Large language model

**Abstract:** 
> The increasing deployment of large language model (LLM)-based chatbots has raised concerns regarding fairness. Fairness issues in LLMs may result in serious consequences, such as bias amplification, discrimination, and harm to minority groups. Many efforts are dedicated to evaluating and mitigating biases in LLMs. However, existing fairness benchmarks mainly focus on single-turn dialogues, while multi-turn scenarios, which better reflect real-world conversations, pose greater challenges due to c...

---

## Key Prior Works (6 papers with direct influence)

### 💡 Inspiration

**CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models** (2020)
- *Authors:* Nikita Nangia et al.
- *Direct Connection:* FairMT-Bench adopts CrowS-Pairs’ minimal-pair design to construct turn-level counterfactuals in conversation that directly probe interaction fairness across demographic attributes.

**MT-Bench and LLM-as-a-Judge: Multi-turn Evaluation and Automatic Judging with LLMs** (2023)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* FairMT-Bench adopts MT-Bench’s multi-turn chat evaluation format and the LLM-as-a-Judge protocol, adapting the rubric to fairness-specific criteria and cross-turn consistency scoring.

**HateCheck: Functional tests for hate speech detection models** (2021)
- *Authors:* Paul Röttger et al.
- *Direct Connection:* FairMT-Bench borrows HateCheck’s functional, template-based testing philosophy with protected-attribute control to design fairness trade-off tasks that probe moderation vs. helpfulness over dialogue turns.

### 🔧 Extension

**BBQ: A Hand-Built Bias Benchmark for Question Answering** (2022)
- *Authors:* Alicia Parrish et al.
- *Direct Connection:* FairMT-Bench extends BBQ’s ambiguity vs. disambiguation QA templates into multi-turn contexts to test whether models avoid biased inferences as additional clarifying turns unfold.

**BOLD: Dataset and metrics for measuring bias in open-ended language generation** (2021)
- *Authors:* Shikhar Dhamala et al.
- *Direct Connection:* FairMT-Bench uses BOLD’s identity- and topic-grounded open-ended prompts as seeds and wraps them into dialog flows to measure representational harms and their accumulation across turns.

### 🔗 Related Problem

**StereoSet: Measuring stereotypical bias in pretrained language models** (2021)
- *Authors:* Moin Nadeem et al.
- *Direct Connection:* FairMT-Bench leverages StereoSet’s stereotype/anti-stereotype/neutral framing to categorize conversational prompts and quantify how stereotype reinforcement evolves over multiple turns.

---

## Synthesis: How Prior Work Led to This Paper

BBQ introduced controlled question-answering templates that explicitly contrast ambiguous with disambiguated contexts to expose social biases in inference, providing fine-grained, attribute-aware cases amenable to systematic evaluation. BOLD curated identity- and topic-grounded prompts and metrics for open-ended generation, surfacing representational harms when models discuss demographic groups in free-form text. CrowS-Pairs operationalized minimal pairs differing only in protected-attribute terms, enabling direct tests of parity that isolate model bias from confounders. StereoSet formalized stereotype/anti-stereotype/neutral triplets and a scoring scheme for generative and masked LMs, highlighting how stereotypes can be reinforced or resisted at the prompt-response level. MT-Bench and the LLM-as-a-Judge methodology established reliable procedures for multi-turn dialogue evaluation and rubric-guided automatic judging with strong inter-judge agreement, demonstrating how to structure conversations and score higher-level qualities. HateCheck advanced a functional-test paradigm with templated, attribute-controlled cases to probe specific failure modes and trade-offs, such as over- versus under-moderation around protected groups. Together, these works revealed precise bias probes, identity-controlled templates, and multi-turn judging mechanics—but largely in single-turn or non-conversational settings. The natural next step was to fuse identity-controlled bias probes (BBQ, BOLD, CrowS-Pairs, StereoSet) with multi-turn conversation scaffolds and LLM-as-a-judge scoring (MT-Bench) under a functional testing lens (HateCheck). FairMT-Bench synthesizes these elements into a dialogue-first fairness taxonomy—context understanding, interaction fairness, and fairness trade-offs—and systematically measures bias accumulation and trade-off behaviors across turns using adapted templates and automatic judges.

---

*Analysis generated on: 2026-01-06T15:52:39.656633*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

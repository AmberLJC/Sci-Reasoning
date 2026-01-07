# Prior Work Analysis Report

## Target Paper

**Title:** First-Person Fairness in Chatbots

**Conference:** ICLR 2025 (spotlight)

**Authors:** Tyna Eloundou, Alex Beutel, David G. Robinson, Keren Gu, Anna-Luisa Brakman, Pamela Mishkin, Meghan Shah, Johannes Heidecke, Lilian Weng, Adam Tauman Kalai

**Keywords:** fairness, large language models, chatbots

**Abstract:** 
> Evaluating chatbot fairness is crucial given their rapid proliferation, yet typical chatbot tasks (e.g., resume writing, entertainment) diverge from the institutional decision-making tasks (e.g., resume screening) which have traditionally been central to discussion of algorithmic fairness. The open-ended nature and diverse use-cases of chatbots necessitate novel methods for bias assessment. This paper addresses these challenges by introducing a scalable counterfactual approach to evaluate "first...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Fairness Through Awareness** (2012)
- *Authors:* Cynthia Dwork et al.
- *Direct Connection:* The paper’s definition of individual fairness—similar individuals should be treated similarly—directly grounds the notion of “first-person fairness,” which our work operationalizes via demographic counterfactuals for chatbot users.

**StereoSet: Measuring stereotypical bias in pretrained language models** (2021)
- *Authors:* Moin Nadeem et al.
- *Direct Connection:* StereoSet’s notion of stereotype-consistent versus anti-stereotype continuations informs our quantitative measure of harmful stereotypes in generated chatbot responses.

### 💡 Inspiration

**BBQ: A Hand-Built Benchmark for Measuring Social Biases in Question Answering** (2022)
- *Authors:* Alicia Parrish et al.
- *Direct Connection:* We adapt BBQ’s bias-direction labeling (stereotype-consistent vs. -inconsistent) and controlled comparisons to operationalize bias judgments when demographic cues are present versus counterfactually removed.

**Judging LLM-as-a-Judge: MT-Bench and Chatbot Arena** (2023)
- *Authors:* LMSYS (Lianmin Zheng et al.)
- *Direct Connection:* Our Language Model as a Research Assistant (LMRA) builds on the LLM-as-a-judge paradigm by using a strong model to rate fairness-relevant properties (e.g., stereotyping and differential treatment) with scalable reliability.

**Red Teaming Language Models with Language Models** (2022)
- *Authors:* Deep Ganguli et al.
- *Direct Connection:* We extend the idea of using models to probe and analyze other models to the fairness domain, leveraging an LM to systematically surface, summarize, and quantify demographic harms across diverse chatbot tasks.

### 🔍 Gap Identification

**RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models** (2020)
- *Authors:* Samuel Gehman et al.
- *Direct Connection:* By showing prompt-based generative harm evaluations focused mainly on toxicity, this work highlights the gap our approach fills—moving to first-person, demographic counterfactual fairness across diverse real-world chatbot tasks.

### 🔧 Extension

**CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models** (2020)
- *Authors:* Nitish Nangia et al.
- *Direct Connection:* We generalize CrowS-Pairs’ minimal-pair attribute-swapping protocol to open-ended chat by counterfactually swapping user demographics in otherwise matched prompts to quantify first-person disparities at scale.

---

## Synthesis: How Prior Work Led to This Paper

Individual fairness established the principle that similar individuals should be treated similarly, offering a normative foundation for assessing harms that accrue to specific people rather than only to abstract groups. CrowS-Pairs operationalized this idea for language models using minimal pairs that swap demographic attributes while holding content constant, enabling a clean counterfactual comparison. StereoSet further refined measurement by distinguishing stereotype-consistent from anti-stereotype continuations, providing a direction-sensitive signal for assessing harmful associations. BBQ introduced carefully controlled comparisons and explicit bias-direction labeling in a QA setting, helping evaluators separate genuine task competence from stereotype-driven responses. In parallel, LLM-as-a-judge work demonstrated that strong language models can reliably evaluate other models’ outputs at scale, and red-teaming with LMs showed that models can systematically probe and summarize safety-relevant failures. RealToxicityPrompts revealed the feasibility—but also the limitations—of prompt-based harm evaluations largely confined to toxicity and single-turn setups. Together, these works reveal both a methodological toolkit and a gap: counterfactual, direction-aware bias measurement exists but is largely benchmark-bound, and scalable evaluation is possible but rarely targets first-person harms in realistic chat tasks. The present work synthesizes minimal-pair counterfactuals with stereotype-direction metrics, and instantiates them in open-ended chat via an LLM-based research assistant that can rate, summarize, and analyze demographic differences across millions of interactions, thereby delivering a practical framework for first-person fairness in chatbots.

---

*Analysis generated on: 2026-01-06T13:37:02.777491*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

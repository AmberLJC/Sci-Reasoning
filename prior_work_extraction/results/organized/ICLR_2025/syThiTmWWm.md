# Prior Work Analysis Report

## Target Paper

**Title:** Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates

**Conference:** ICLR 2025 (oral)

**Authors:** Xiaosen Zheng, Tianyu Pang, Chao Du, Qian Liu, Jing Jiang, Min Lin

**Keywords:** Large Language Models, Cheating, Automatic LLM Benchmarks

**Abstract:** 
> Automatic LLM benchmarks, such as AlpacaEval 2.0, Arena-Hard-Auto, and MT-Bench, have become popular for evaluating language models due to their cost-effectiveness and scalability compared to human evaluation. Achieving high win rates on these benchmarks can significantly boost the promotional impact of newly released language models. This promotional benefit may motivate tricks, such as manipulating model output length or style to game win rates, even though several mechanisms have been develop...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**MT-Bench: Multi-turn Benchmark for Evaluating Large Language Models** (2023)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* MT-Bench’s GPT-4-as-a-judge, multi-turn rubric and scoring protocol provide a primary automatic evaluation target that this work shows can be gamed by a constant, instruction-irrelevant response (scoring 9.55).

**Chatbot Arena and Arena-Hard-Auto: Open and Automatic LLM Evaluation via Pairwise Judging** (2024)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* Arena-Hard-Auto’s automatic judge setup, designed to approximate human Arena outcomes, is directly targeted by a single fixed output that exploits its judging prompt to achieve an 83.0 score, revealing residual gameability.

**G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* G-Eval established rubric-driven LLM-as-judge prompting (rewarding structure, coverage, and helpfulness), and the crafted constant outputs intentionally amplify these rubric cues—despite being off-topic—to systematically bias the judge.

### 🔍 Gap Identification

**AlpacaEval 2.0: Automatic Evaluation with Length-Controlled Win Rates** (2024)
- *Authors:* Li et al.
- *Direct Connection:* AlpacaEval 2.0 introduced the length-controlled (LC) win rate and style-disentangling mechanisms to curb gaming, which are directly stress-tested here by a null response attaining an 86.5% LC win rate.

**Are Large Language Models Good Judges? A Systematic Evaluation of LLM-as-a-Judge** (2023)
- *Authors:* Wang et al.
- *Direct Connection:* By documenting judge vulnerabilities such as verbosity and formatting/style bias, this study pinpointed weaknesses that are operationalized here into a content-agnostic attack converting those biases into benchmark wins.

### 🔗 Related Problem

**Prometheus: Toward Faithful Large Language Model Judges via Supervised Rubrics** (2023)
- *Authors:* Kim et al.
- *Direct Connection:* Prometheus proposed training LLM judges with rubric supervision to improve reliability, and this work shows that even rubric-centric judging remains susceptible to highly-stylized, constant replies that sway automatic evaluations.

---

## Synthesis: How Prior Work Led to This Paper

MT-Bench formalized a widely adopted automatic evaluation protocol in which GPT-4 serves as a judge, scoring multi-turn responses according to a rubric that prioritizes clarity, structure, helpfulness, and coverage. Chatbot Arena’s Arena-Hard-Auto extended this paradigm to a harder question set while retaining LLM-as-judge pairwise comparisons meant to approximate human preferences at scale. AlpacaEval 2.0 explicitly addressed known gaming vectors by introducing a length-controlled win-rate and mechanisms to disentangle style from substance, aiming to neutralize verbosity and surface-level polish. G-Eval showed that robust rubric prompting could yield high human correlation, operationalizing evaluative cues—like explicit structure, stepwise reasoning, and safety disclaimers—that LLM judges reward. Complementing these design choices, empirical analyses on LLM-as-a-judge demonstrated systematic biases, including a preference for longer, more formal, and highly formatted outputs. In parallel, judge-specialization efforts such as Prometheus sought to reduce bias and improve faithfulness by training evaluators with rubric supervision.

Together, these works established scalable LLM-as-judge benchmarks, attempted to mitigate gameability via length control and style handling, and revealed persistent judge heuristics. The confluence of public judging prompts, rubric-aligned cues, and shared evaluation formats created an opportunity: content-agnostic outputs that maximally express favored surface signals. Building on these insights, the current study synthesizes a constant, instruction-irrelevant response that systematically activates rubric preferences, bypasses length and style controls, and transfers across benchmarks—demonstrating that existing automatic evaluations can be top-ranked without solving the underlying tasks.

---

*Analysis generated on: 2026-01-06T17:26:28.451821*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** SocioDojo: Building Lifelong Analytical Agents with Real-world Text and Time Series

**Conference:** ICLR 2024 (spotlight)

**Authors:** Junyan Cheng, Peter Chin

**Keywords:** Large Langauge Models, Agent, Prompt Tunning, Time series forcasting

**Abstract:** 
> We introduce SocioDojo, an open-ended lifelong learning environment for developing ready-to-deploy autonomous agents capable of performing human-like analysis and decision-making on societal topics such as economics, finance, politics, and culture. It consists of (1) information sources from news, social media, reports, etc., (2) a knowledge base built from books, journals, and encyclopedias, plus a toolbox of Internet and knowledge graph search interfaces, (3) 30K high-quality time series in fi...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Portfolio Selection** (1952)
- *Authors:* Harry Markowitz
- *Direct Connection:* The hyperportfolio task directly generalizes Markowitz’s portfolio selection by treating heterogeneous societal time series as investable assets and evaluating agent decisions with risk–return criteria.

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* The Hypothesis & Proof prompting builds on Chain-of-Thought by structuring step-by-step reasoning into an explicit hypothesis followed by a formal, evidence-grounded justification.

### 💡 Inspiration

**ReAct: Synergizing Reasoning and Acting in Language Models** (2022)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* The Analyst-Assistant-Actuator architecture operationalizes ReAct’s thought–action–observation loop by separating analysis, tool use, and execution into coordinated roles for decision-making on time series.

**Precise Zero-shot Dense Retrieval without Relevance Labels (HyDE)** (2022)
- *Authors:* Luyu Gao et al.
- *Direct Connection:* HyDE’s idea of generating a hypothetical document to guide retrieval directly inspires using a hypothesized claim to steer searches in news/knowledge bases and then constructing a proof.

**Self-Ask: A Simple Approach for Improving Multi-Step Reasoning by Decomposing Problems into Subquestions** (2022)
- *Authors:* Ofir Press et al.
- *Direct Connection:* The Hypothesis & Proof procedure adopts Self-Ask’s decomposition-and-search pattern by breaking societal analyses into verifiable subclaims queried via tools before committing to an action.

### 🔍 Gap Identification

**Reflexion: Language Agents with Verbal Reinforcement Learning** (2023)
- *Authors:* Noah Shinn et al.
- *Direct Connection:* Reflexion’s episodic self-improvement highlights the need for a persistent, real-world setting and long-horizon evaluation, motivating a lifelong environment with external knowledge and time-series feedback.

### 🔗 Related Problem

**FinRL: A Deep Reinforcement Learning Library for Automated Stock Trading in Quantitative Finance** (2021)
- *Authors:* Xiao-Yang Liu et al.
- *Direct Connection:* FinRL’s backtested decision-making on financial time series provides the direct paradigm that is generalized from market assets to thousands of societal series under a unified portfolio-style evaluation.

---

## Synthesis: How Prior Work Led to This Paper

Portfolio theory established that decisions over time series can be evaluated via risk–return trade-offs, formalized by Markowitz as portfolio selection. In parallel, tool-augmented language agents showed how to interleave reasoning and external actions: ReAct introduced a thought–action–observation loop that couples deliberation with search and environment feedback. Chain-of-Thought revealed that eliciting explicit, stepwise reasoning improves complex analysis, while HyDE demonstrated that generating a hypothesis-like surrogate text can steer retrieval to the most informative evidence. Self-Ask further refined multi-step reasoning by decomposing questions into subproblems and using targeted searches to verify intermediate claims. Reflexion argued that agents benefit from iterative self-improvement across episodes, pointing to the need for persistent memory and longitudinal feedback rather than single-shot tasks. In time-series decision-making, FinRL operationalized backtested actions over financial signals, illustrating how real-world streams can serve as an objective feedback channel for agent performance.
Together these strands suggested a natural opportunity: combine explicit hypothesis-driven reasoning, retrieval-verified evidence, and tool-mediated action with a rigorous, backtestable objective over time series. By extending portfolio selection beyond markets to diverse societal indicators, the hyperportfolio formulation provides scalable, reliable evaluation. Structuring agents into distinct roles mirrors ReAct’s deliberate act loops while incorporating CoT-style reasoning, HyDE-guided retrieval, and Self-Ask verification to ground analyses in real sources. Embedding this within a persistent environment addresses Reflexion’s call for lifelong improvement, yielding agents that analyze real-world text and act on time series with objective, longitudinal feedback.

---

*Analysis generated on: 2026-01-06T16:41:58.335744*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Active Task Disambiguation with LLMs

**Conference:** ICLR 2025 (spotlight)

**Authors:** Kasia Kobalczyk, Nicolás Astorga, Tennison Liu, Mihaela van der Schaar

**Keywords:** Task Ambiguity, Bayesian Experimental Design, Large Language Models, Active Learning

**Abstract:** 
> Despite the impressive performance of large language models (LLMs) across various benchmarks, their ability to address ambiguously specified problems—frequent in real-world interactions—remains underexplored. To address this gap, we introduce a formal definition of task ambiguity and frame the problem of task disambiguation through the lens of Bayesian Experimental Design. By posing clarifying questions, LLM agents can acquire additional task specifications, progressively narrowing the space of ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**AmbigQA: Answering Ambiguous Open-domain Questions** (2020)
- *Authors:* Sewon Min et al.
- *Direct Connection:* AmbigQA formally characterized ambiguity in user queries and used human-like clarifications, providing the conceptual foundation for defining and operationalizing task ambiguity beyond QA.

**The Measurement of Information Provided by an Experiment** (1956)
- *Authors:* Dennis V. Lindley
- *Direct Connection:* Lindley’s expected information gain formulation underpins the paper’s framing of clarifying question asking as optimal Bayesian experimental design.

### 💡 Inspiration

**Active Preference-Based Learning of Reward Functions** (2017)
- *Authors:* Dorsa Sadigh et al.
- *Direct Connection:* This paper’s treatment of user intent as a latent variable elicited via information-gain-maximizing queries inspires modeling task specification as a latent hypothesis inferred through targeted questions.

### 🔍 Gap Identification

**Asking Clarifying Questions in Open-Domain Information-Seeking Conversations** (2019)
- *Authors:* Mohammad Aliannejadi et al.
- *Direct Connection:* By demonstrating clarifying-question selection with task-specific retrieval heuristics, this paper exposed the lack of a principled, model-based information-seeking objective that the present work addresses via Bayesian experimental design.

### 📊 Baseline

**Self-Ask: A Simple Approach to Multi-Hop Question Answering** (2022)
- *Authors:* Ofir Press et al.
- *Direct Connection:* Self-Ask’s prompting to generate follow-up questions serves as a baseline whose lack of principled, information-seeking selection is addressed by the proposed Bayesian design objective.

### 🔧 Extension

**Learning to Ask Good Questions: Ranking Clarification Questions using Neural Expected Utility** (2018)
- *Authors:* Sudha Rao et al.
- *Direct Connection:* This work’s utility-based objective for selecting clarifying questions is directly generalized here into a Bayesian expected information gain criterion over latent task specifications.

**Bayesian Active Learning by Disagreement** (2011)
- *Authors:* Neil Houlsby et al.
- *Direct Connection:* The mutual-information acquisition principle from BALD is adapted to select clarifying questions that maximize information about the latent task specification rather than model parameters.

---

## Synthesis: How Prior Work Led to This Paper

Work on clarifying questions in NLP first operationalized the goal of reducing user intent uncertainty by selecting questions that most improve utility. Rao and Daumé III introduced a neural expected-utility objective for ranking clarification questions, tying question choice directly to downstream task success. Aliannejadi and colleagues extended this to open-domain conversational search, showing that clarifying questions can measurably disambiguate queries, though their selection procedures relied on domain heuristics and retrieval signals. AmbigQA formalized ambiguity in open-domain QA and demonstrated that predicting human-like clarifications can surface multiple plausible interpretations, highlighting the need for explicit ambiguity modeling. From the active learning literature, BALD provided a practical mutual-information acquisition principle for choosing queries that maximally reduce uncertainty, while Lindley’s classical result grounded this strategy as expected information gain within Bayesian experimental design. In interactive learning, Sadigh et al. modeled user intent (a reward function) as a latent variable and selected human queries to maximally reduce uncertainty over that latent, demonstrating principled human-in-the-loop elicitation.
Together, these works reveal both the importance of clarifying questions for resolving underspecification and the absence of a general, model-based selection principle for arbitrary tasks. The natural synthesis is to treat task specification as a latent hypothesis space and choose natural-language questions via expected information gain—thereby generalizing utility-based ranking and preference elicitation to LLM agents. This unifies prior clarifying-question insights with Bayesian design, shifting from ad hoc prompting (e.g., Self-Ask) to explicit, information-seeking interrogation of ambiguity.

---

*Analysis generated on: 2026-01-06T09:15:21.594753*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

**Conference:** ICLR 2025 (oral)

**Authors:** Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Aleksander Madry, Lilian Weng

**Keywords:** benchmark, evals, evaluations, dataset, tasks, data science, engineering, agents, language agents, scaffold, coding, swe, mle

**Abstract:** 
> We introduce MLE-bench, a benchmark for measuring how well AI agents perform at machine learning engineering. To this end, we curate 75 ML engineering-related competitions from Kaggle, creating a diverse set of challenging tasks that test real-world ML engineering skills such as training models, preparing datasets, and running experiments. We establish human baselines for each competition using Kaggle's publicly available leaderboards. We use open-source agent scaffolds to evaluate several front...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**An Open Source AutoML Benchmark** (2019)
- *Authors:* Pieter Gijsbers et al.
- *Direct Connection:* The AutoML Benchmark established the paradigm of multi-dataset, standardized ML tasks and programmatic evaluation, which is adapted here to assess general-purpose agents instead of AutoML systems and to use public leaderboards as human baselines.

### 💡 Inspiration

**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** (2023)
- *Authors:* Kang et al.
- *Direct Connection:* SWE-bench’s core idea of evaluating LLM agents on end-to-end, real-world engineering tasks with automatic scoring directly inspired framing ML engineering evaluation around complete, real-world tasks rather than unit-test snippets.

### 🔍 Gap Identification

**DS-1000: A Dataset for Evaluating LLMs on Data Science Code Generation** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* DS-1000 exposed that prior data-science evaluations focus on cell-level, library-specific completions, motivating a benchmark that tests full ML pipelines including data preparation, training, and experiment management.

### 📊 Baseline

**SWE-agent: Empowering LLMs to Solve Real-World GitHub Issues** (2023)
- *Authors:* Yang et al.
- *Direct Connection:* This open-source scaffold serves as a primary baseline agent for executing multi-step coding and experiment workflows in the new benchmark’s ML engineering tasks.

**OpenDevin: An Open Platform for Autonomous AI Software Engineers** (2024)
- *Authors:* Mitra et al.
- *Direct Connection:* OpenDevin provides a general-purpose development agent scaffold used as a comparative baseline to run end-to-end instrumented workflows on the benchmark’s ML tasks.

### 🔗 Related Problem

**AgentBench: Evaluating LLMs as Agents** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* AgentBench’s methodology for measuring multi-step tool-using agents informed the benchmark’s agent-centric evaluation protocol and success criteria, now instantiated for ML engineering workloads.

**WebArena: A Realistic Web Environment for Building Autonomous Agents** (2023)
- *Authors:* Zhou et al.
- *Direct Connection:* WebArena’s emphasis on realistic, end-to-end tasks in an external environment directly influenced the decision to ground evaluation in real-world Kaggle competitions rather than synthetic or toy settings.

---

## Synthesis: How Prior Work Led to This Paper

SWE-bench demonstrated that evaluating language models as agents is most revealing when tasks are end-to-end, realistic, and automatically verifiable, using real GitHub issues as the substrate rather than synthetic unit tests. DS-1000 showed that data-science-oriented code benchmarks typically operate at the granularity of individual cells and library calls, surfacing library-specific errors but not assessing whether an agent can orchestrate a complete ML workflow. The Open Source AutoML Benchmark established a standardized, multi-dataset paradigm for comparing ML systems, with reproducible harnesses and consistent metrics across diverse tasks. AgentBench provided a general methodology for assessing multi-step, tool-using agents, clarifying evaluation protocols and success measures for agentic workloads. SWE-agent operationalized an open-source scaffold that lets LLMs make iterative edits, run tests, and manage repos, while OpenDevin generalized such development-agent workflows in a modular platform. WebArena emphasized fidelity and realism by embedding agents in an external, production-like environment to complete full tasks rather than isolated subtasks.
Together these works reveal a clear opportunity: there is no end-to-end, real-world benchmark targeting the ML engineering lifecycle itself—data preparation, training, and experiment management—despite evidence that agent evaluation is most meaningful on realistic tasks. By transplanting SWE-bench’s real-world, end-to-end ethos into the multi-dataset rigor of AutoML benchmarking, adopting AgentBench’s agent-eval protocol, and leveraging practical scaffolds like SWE-agent and OpenDevin, the field naturally progresses to a Kaggle-grounded suite where public leaderboards provide human baselines and realistic difficulty. This synthesis enables principled measurement of agents’ ML engineering capability and supports analyses of resource scaling and potential pretraining contamination.

---

*Analysis generated on: 2026-01-06T17:11:33.311358*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** CABINET: Content Relevance-based Noise Reduction for Table Question Answering

**Conference:** ICLR 2024 (spotlight)

**Authors:** Sohan Patnaik, Heril Changwal, Milan Aggarwal, Sumit Bhatia, Yaman Kumar, Balaji Krishnamurthy

**Keywords:** Table Question Answering, Large Language Models, Noise Reduction, Unsupervised Relevance Scoring, Table Parsing, Relevant Cell Highlighting

**Abstract:** 
> Table understanding capability of Large Language Models (LLMs) has been extensively studied through the task of question-answering (QA) over tables. Typically, only a small part of the whole table is relevant to derive the answer for a given question. The irrelevant parts act as noise and are distracting information, resulting in sub-optimal performance due to the vulnerability of LLMs to noise. To mitigate this, we propose CABINET (Content RelevAnce-Based NoIse ReductioN for TablE QuesTion-Answ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Compositional Semantic Parsing on Semi-Structured Tables** (2015)
- *Authors:* Panupong Pasupat et al.
- *Direct Connection:* CABINET builds on the WikiTableQuestions problem formulation of QA over semi-structured tables, using its answer-matching setup and evaluation conventions.

**Seq2SQL: Generating Structured Queries from Natural Language using Reinforcement Learning** (2017)
- *Authors:* Victor Zhong et al.
- *Direct Connection:* CABINET’s parsing-statement module echoes the SQL-style row/column filtering formalized by WikiSQL, using natural-language criteria for selecting relevant rows/columns.

### 💡 Inspiration

**RePlug: Retrieval-Augmented Language Model with Plug-in Retriever** (2023)
- *Authors:* Weijia Shi et al.
- *Direct Connection:* CABINET adapts RePlug’s core insight—training a selector using feedback from a generator—by training a cell-level Unsupervised Relevance Scorer directly from the QA LLM’s loss in a differentiable pipeline.

**Rationalizing Neural Predictions** (2016)
- *Authors:* Tao Lei et al.
- *Direct Connection:* CABINET adopts the selector–predictor paradigm of learning a differentiable mask optimized by the end-task objective, with URS serving as the rationale-style selector over table cells.

### 🔍 Gap Identification

**Lost in the Middle: How Language Models Use Long Context** (2023)
- *Authors:* Nelson F. Liu et al.
- *Direct Connection:* CABINET directly addresses the finding that irrelevant content degrades LLM performance by explicitly suppressing non-relevant table regions before answering.

### 📊 Baseline

**TAPEX: Table Pre-training via Learning a Neural SQL Executor** (2021)
- *Authors:* Qian Liu et al.
- *Direct Connection:* CABINET targets strong table QA models like TAPEX as primary baselines, improving accuracy by filtering irrelevant table content before answer generation.

### 🔧 Extension

**TaPas: Weakly Supervised Table Parsing via Pre-training** (2020)
- *Authors:* Jonathan Herzig et al.
- *Direct Connection:* CABINET generalizes TaPas’s cell-selection idea by replacing its task-specific, weakly supervised selection head with an unsupervised, model-agnostic relevance scorer that weights cells before any QA LLM consumes the table.

---

## Synthesis: How Prior Work Led to This Paper

TaPas introduced the idea that identifying answer-bearing cells is integral to table QA, training a cell-selection head with weak supervision to focus model attention on relevant table regions. RePlug showed that a retriever can be trained effectively using feedback from a downstream generator, aligning selection with what actually improves answer likelihood. Lost in the Middle demonstrated that large language models are highly sensitive to irrelevant content within long contexts, quantifying how distractors impair accuracy. Rationalizing Neural Predictions proposed a selector–predictor architecture in which a differentiable mask is learned under the end-task objective, providing a blueprint for learning to highlight only the necessary input evidence. WikiTableQuestions established the core formulation of answering questions over semi-structured tables with answer-based supervision, and Seq2SQL (WikiSQL) formalized row/column filtering as natural-language conditions akin to WHERE clauses for selecting table subsets. TAPEX provided a strong neural executor-style baseline for table QA that still ingests substantial table content and can be susceptible to noise.
Together, these works pointed to a gap: LLM-based table QA needed an explicit, training-signal-aligned selector that reduces irrelevant table tokens without requiring labeled rationales, while also making the selection criteria interpretable. CABINET synthesizes the TaPas-style cell relevance idea with RePlug’s generator-supervised training by learning a cell-level scorer directly from QA loss, instantiates it as a differentiable rationale-style mask, and complements it with a weakly supervised parsing statement that mirrors SQL-like row/column criteria—yielding robust noise suppression that slots in front of strong table QA models like TAPEX or LLM-based solvers.

---

*Analysis generated on: 2026-01-06T08:34:23.285250*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

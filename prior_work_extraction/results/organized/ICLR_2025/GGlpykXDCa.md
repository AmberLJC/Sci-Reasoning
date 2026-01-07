# Prior Work Analysis Report

## Target Paper

**Title:** MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions

**Conference:** ICLR 2025 (oral)

**Authors:** Jian Wu, Linyi Yang, Dongyuan Li, Yuliang Ji, Manabu Okumura, Yue Zhang

**Keywords:** LLM evaluation, multi-table question answering; multi-hop question answering

**Abstract:** 
> While large language models (LLMs) have made strides in understanding tabular data, current tabular evaluation benchmarks, such as WikiTableQuestions and WikiSQL, are focus on single-table scenarios, which cannot necessarily reflect the complexity of real-world applications. To bridge this gap, we present a \textbf{M}ulti-table and 
Multi-hop Question Answering (MMQA) dataset to assess LLMs' understanding and reasoning capabilities in handling multi-table tasks. The MMQA dataset demands that mod...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task** (2018)
- *Authors:* Yu et al.
- *Direct Connection:* Spider introduced cross-database multi-table text-to-SQL with explicit primary/foreign key relations, providing the core multi-table join problem formulation that MMQA generalizes into a broader multi-hop QA and diagnostic evaluation setting (including PK/FK selection).

### 💡 Inspiration

**HybridQA: A Dataset of Multi-Hop Question Answering over Tabular and Textual Data** (2020)
- *Authors:* Chen et al.
- *Direct Connection:* HybridQA demonstrated multi-hop reasoning that integrates tabular evidence with additional sources, inspiring MMQA’s emphasis on multi-step inference chains, now grounded purely in inter-related tables.

### 🔍 Gap Identification

**Compositional Semantic Parsing on Semi-Structured Tables** (2015)
- *Authors:* Pasupat et al.
- *Direct Connection:* This single-table QA benchmark (WikiTableQuestions) defined table-based question answering but lacked cross-table reasoning, a limitation MMQA explicitly addresses by moving to multi-table, multi-hop settings.

**Seq2SQL: Generating Structured Queries from Natural Language using Reinforcement Learning (WikiSQL)** (2017)
- *Authors:* Zhong et al.
- *Direct Connection:* WikiSQL popularized text-to-SQL evaluation in a single-table regime, whose inability to test join reasoning directly motivated MMQA’s multi-table and multi-hop evaluation design.

### 📊 Baseline

**BIRD: Big Bench for Large-Scale Text-to-SQL** (2023)
- *Authors:* Li et al.
- *Direct Connection:* BIRD established large-scale, LLM-focused text-to-SQL evaluation over multi-table databases, serving as a primary baseline that MMQA contrasts with by expanding beyond SQL generation to multi-hop QA and schema-relation diagnostics.

### 🔧 Extension

**Dr.Spider: A Diagnostic Evaluation Benchmark for Text-to-SQL Parsers** (2023)
- *Authors:* Li et al.
- *Direct Connection:* Dr.Spider’s diagnostic breakdown (e.g., table/column selection and join path) directly influenced MMQA’s comprehensive evaluation framework, which extends diagnostics to multi-table retrieval and explicit primary/foreign key selection tasks for LLMs.

### 🔗 Related Problem

**OTT-QA: Open Table-and-Text Question Answering** (2021)
- *Authors:* Qu et al.
- *Direct Connection:* OTT-QA’s requirement to retrieve relevant tables for answering questions informed MMQA’s inclusion of a dedicated multi-table retrieval component and evaluation of retrieval accuracy over relational tables.

---

## Synthesis: How Prior Work Led to This Paper

Early table QA efforts showed how natural language questions could be answered from structured tables, with WikiTableQuestions capturing compositional reasoning but constraining evidence to a single table. WikiSQL brought scale to text-to-SQL but remained single-table, precluding join reasoning. Spider changed the landscape by formalizing cross-database text-to-SQL where primary and foreign keys define join paths, making relational reasoning central and explicit. HybridQA demonstrated that questions often demand multi-step inference chains, linking table-derived facts with other evidence sources to answer complex questions. OTT-QA highlighted the necessity of retrieving relevant tables as a first-class component of table-centric QA, showing performance hinges on accurate table identification before reasoning. Dr.Spider then shifted evaluation toward skill diagnostics—such as schema linking and join selection—revealing that nuanced sub-competencies determine end-task success on relational queries. Finally, BIRD scaled text-to-SQL evaluation for the LLM era across large, multi-table databases, surfacing where LLMs succeed and fail on schema-rich problems. Together these works revealed a gap: there was no benchmark that simultaneously targets multi-table retrieval, multi-hop reasoning across relational tables, and explicit primary/foreign key competence for LLMs. Building on Spider’s relational schema framing and Dr.Spider’s diagnostic philosophy, while incorporating OTT-QA’s retrieval emphasis and the LLM evaluation lessons from BIRD, the next natural step is a unified dataset and framework that evaluates multi-table retrieval, text-to-SQL, end-to-end QA, and key-selection skills—precisely what MMQA provides.

---

*Analysis generated on: 2026-01-06T15:50:43.665297*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

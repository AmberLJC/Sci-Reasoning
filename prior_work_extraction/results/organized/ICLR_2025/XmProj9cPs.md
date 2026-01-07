# Prior Work Analysis Report

## Target Paper

**Title:** Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows

**Conference:** ICLR 2025 (oral)

**Authors:** Fangyu Lei, Jixuan Chen, Yuxiao Ye, Ruisheng Cao, Dongchan Shin, Hongjin SU, ZHAOQING SUO, Hongcheng Gao, Wenjing Hu, Pengcheng Yin, Victor Zhong, Caiming Xiong, Ruoxi Sun, Qian Liu, Sida Wang, Tao Yu

**Keywords:** LLM Benchmark, Data Science and Engineering, Code Generation, Text-to-SQL, LLM Agent

**Abstract:** 
> Real-world enterprise text-to-SQL workflows often involve complex cloud or local data across various database systems, multiple SQL queries in various dialects, and diverse operations from data transformation to analytics.
We introduce Spider 2.0, an evaluation framework comprising $632$ real-world text-to-SQL workflow problems derived from enterprise-level database use cases. 
The databases in Spider 2.0 are sourced from real data applications, often containing over 1,000 columns and stored in ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL** (2018)
- *Authors:* Tao Yu et al.
- *Direct Connection:* Spider 2.0 directly extends Spider’s cross-database Text-to-SQL problem formulation and execution-based evaluation, scaling it to enterprise-scale, multi-dialect, multi-query workflows.

**SParC: Cross-Domain Semantic Parsing in Context** (2019)
- *Authors:* Bailin Wang et al.
- *Direct Connection:* SParC’s notion of multi-turn, context-dependent query generation informs Spider 2.0’s design of dependent, multi-query workflows that require state to persist across steps.

**Seq2SQL: Generating Structured Queries from Natural Language using Reinforcement Learning** (2017)
- *Authors:* Victor Zhong et al.
- *Direct Connection:* Seq2SQL (introducing WikiSQL) established the large-scale Text-to-SQL evaluation paradigm and execution-based metrics that Spider 2.0 inherits while moving beyond single-table, single-query settings.

### 💡 Inspiration

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* ReAct’s interleaving of reasoning with tool use directly inspired Spider 2.0’s evaluation tasks that require models to browse database metadata, dialect documentation, and other resources while planning multi-step SQL.

**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** (2023)
- *Authors:* Edward J. Hu et al.
- *Direct Connection:* SWE-bench’s benchmark design around long-context, repository-level reasoning informed Spider 2.0’s inclusion of tasks requiring traversal of project-level codebases and extremely long contexts for SQL workflows.

### 🔍 Gap Identification

**BIRD: Big Bench for Large-Scale Database Grounded Text-to-SQL** (2023)
- *Authors:* Yue Wang et al.
- *Direct Connection:* BIRD pushed towards industry-scale schemas and diverse backends but remained largely single-shot, motivating Spider 2.0 to capture enterprise workflows with multi-query pipelines, dialect idiosyncrasies, and external resource retrieval.

### 🔗 Related Problem

**CoSQL: A Conversational Text-to-SQL Challenge Towards Cross-Domain Natural Language Interfaces to Databases** (2019)
- *Authors:* Tao Yu et al.
- *Direct Connection:* CoSQL demonstrated the need for interactive database querying and schema exploration, which Spider 2.0 generalizes from dialog turns to enterprise workflow steps involving tool/document interactions.

---

## Synthesis: How Prior Work Led to This Paper

Seq2SQL introduced WikiSQL and cemented the large-scale Text-to-SQL evaluation paradigm centered on execution-based correctness, albeit in a single-table, single-query regime. Spider then reframed the task to cross-domain, complex SQL over unseen schemas, establishing the now-standard problem formulation and metrics for realistic generalization. Building on this, SParC showed that context across turns materially changes query construction, introducing persistent state and multi-step dependencies within a session. CoSQL emphasized interactive querying and schema exploration under conversational constraints, highlighting the practical need for on-the-fly information access. BIRD pushed scale and industrial realism further, with large, heterogeneous schemas and multiple backends, drawing attention to dialect and system differences yet largely keeping evaluation at the single-shot query level. In parallel, ReAct demonstrated that LLMs benefit from interleaving reasoning with tool use—retrieving facts or documentation mid-trajectory. SWE-bench revealed how benchmarks can require long-context reasoning over codebases and artifacts, mirroring real engineering workflows. Together, these works exposed a gap: no benchmark simultaneously evaluates multi-query, enterprise workflows spanning diverse database systems and dialects while requiring retrieval from metadata, documentation, and codebases under extreme context lengths. Spider 2.0 synthesizes Spider’s cross-domain formulation with SParC/CoSQL’s multi-step dependencies, scales realism as in BIRD, and bakes in ReAct- and SWE-bench-style tool-mediated, long-context interactions—yielding an enterprise-grounded evaluation of end-to-end Text-to-SQL workflows.

---

*Analysis generated on: 2026-01-06T06:05:26.731006*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

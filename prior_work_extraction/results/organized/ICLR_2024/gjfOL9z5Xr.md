# Prior Work Analysis Report

## Target Paper

**Title:** DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, Xing Xie

**Keywords:** Large Language Models, Evaluation, Data Contamination

**Abstract:** 
> Large language models (LLMs) have achieved remarkable performance in various evaluation benchmarks. However, concerns are raised about potential data contamination in their considerable volume of training corpus. Moreover, the static nature and fixed complexity of current benchmarks may inadequately gauge the advancing capabilities of LLMs. 
In this paper, we introduce DyVal, a general and flexible protocol for dynamic evaluation of LLMs. Based on our framework, we build graph-informed DyVal by ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**GSM8K: Training Verifiers to Solve Math Word Problems** (2021)
- *Authors:* Karl Cobbe et al.
- *Direct Connection:* GSM8K formalizes grade-school math reasoning as a core evaluation setting that DyVal targets, while DyVal addresses GSM8K’s static and contamination-prone nature through on-the-fly, complexity-calibrated generation.

### 💡 Inspiration

**Dynabench: Rethinking Benchmarking in NLP** (2021)
- *Authors:* Douwe Kiela et al.
- *Direct Connection:* DyVal adopts the core idea of dynamic, model-in-the-loop evaluation from Dynabench but replaces human adversarial collection with automated, graph-guided synthesis that enables precise complexity control.

**Graph of Thoughts: Solving Elaborate Problems with Large Language Models** (2023)
- *Authors:* Adam Besta et al.
- *Direct Connection:* By framing reasoning as traversal over general graph structures, Graph of Thoughts provides the representational insight DyVal leverages to define, measure, and control evaluation complexity via DAG topology.

**CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text** (2019)
- *Authors:* Koustuv Sinha et al.
- *Direct Connection:* CLUTRR’s use of relational path length as a controllable knob for reasoning difficulty directly inspires DyVal’s structural control via DAG size and topology across math, logic, and algorithmic tasks.

### 🔍 Gap Identification

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* Evidence of memorization and data extraction in LMs motivates DyVal’s design to mitigate contamination by generating fresh, previously unseen evaluation samples.

### 🔧 Extension

**CheckList: A Behavioral Testing Framework for NLP** (2020)
- *Authors:* Marco Tulio Ribeiro et al.
- *Direct Connection:* Building on CheckList’s programmatic, template-driven test generation, DyVal generalizes this notion to reasoning tasks by composing operations along a DAG to produce novel items with tunable difficulty.

### 🔗 Related Problem

**Adversarial NLI: A New Benchmark for Natural Language Understanding** (2020)
- *Authors:* Yixin Nie et al.
- *Direct Connection:* ANLI’s progressive, round-based hardening of evaluation directly informs DyVal’s escalating-difficulty paradigm, which DyVal formalizes using DAG-defined complexity.

---

## Synthesis: How Prior Work Led to This Paper

Dynamic, model-in-the-loop benchmarking emerged with Dynabench, which advocated continually refreshed test sets that evolve alongside model capabilities, while ANLI operationalized this idea with progressive rounds that hardened NLI examples against current systems. CheckList showed that programmatic, template-based behavioral tests can systematically probe capabilities and generate targeted variants, suggesting a path to automated, repeatable evaluation construction. Graph of Thoughts introduced representing problem solving as traversals over general graph structures, revealing a natural link between the topology of reasoning artifacts and their difficulty. CLUTRR demonstrated that structural controls—such as relation-path length—can calibrate reasoning complexity in synthetic text tasks. In parallel, GSM8K established math word problems as a standard reasoning evaluation setting but remained static, and work by Carlini et al. revealed that memorization and data extraction can taint evaluations through contamination.
These strands collectively highlighted a gap: evaluations need to be dynamic to avoid contamination, yet systematically structured to control and scale reasoning difficulty. DyVal synthesizes these ideas by automating dynamic evaluation through graph-informed generation, using DAGs to encode operations and dependencies so that sample novelty and complexity are precisely tunable. This design inherits the dynamic ethos of Dynabench/ANLI, the programmatic rigor of CheckList, and the structural complexity control exemplified by CLUTRR and Graph of Thoughts, addressing the static and contamination-prone limitations in benchmarks like GSM8K and yielding a principled, adaptable protocol for reasoning evaluation.

---

*Analysis generated on: 2026-01-06T15:50:35.927666*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

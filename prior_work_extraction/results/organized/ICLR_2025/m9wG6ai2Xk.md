# Prior Work Analysis Report

## Target Paper

**Title:** MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations

**Conference:** ICLR 2025 (spotlight)

**Authors:** Shaochen Zhong, Yifan Lu, Lize Shao, Bhargav Bhushanam, Xiaocong Du, Yixin Wan, Yucheng Shi, Daochen Zha, Yiwei Wang, Ninghao Liu, Kaixiong Zhou, Shuai Xu, Kai-Wei Chang, Louis Feng, Vipin Chaudhary, Xia Hu

**Keywords:** knowledge edit, model edit, multi-hop, question answering, natural language processing, dataset audit

**Abstract:** 
> Large language models (LLMs) can give out erroneous answers to factually rooted questions either as a result of undesired training outcomes or simply because the world has moved on after a certain knowledge cutoff date. Under such scenarios, *knowledge editing* often comes to the rescue by delivering efficient patches for such erroneous answers without significantly altering the rest, where many editing methods have seen reasonable success when the editing targets are simple and direct (e.g., *`...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**MQuAKE: Benchmarking Multi‑Hop Knowledge Editing in Language Models** (2024)
- *Authors:* Shaochen Zhong et al.
- *Direct Connection:* This work defined the multi‑hop knowledge‑editing problem via compositional QA and introduced the original MQuAKE benchmark that MQuAKE‑Remastered audits, corrects, and standardizes to enable reliable evaluation.

**CounterFact: A Benchmark for Locating and Editing Factual Knowledge in Language Models** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* CounterFact established the single‑hop editing/evaluation template and locality metrics that MQuAKE‑Remastered generalizes beyond and refines to the multi‑hop setting with stricter validation.

### 📊 Baseline

**Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* ROME is a principal editing baseline whose single‑fact intervention assumptions and CounterFact evaluation protocol are stress‑tested under MQuAKE‑Remastered’s corrected multi‑hop settings.

**Mass‑Editing Memory in a Transformer** (2023)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* MEMIT’s multi‑fact parametric editing is a key baseline whose propagation and side‑effect behavior MQuAKE‑Remastered reevaluates with higher‑fidelity multi‑hop tests.

**Fast Model Editing at Scale** (2022)
- *Authors:* Eric Mitchell et al.
- *Direct Connection:* MEND provides a gradient‑based editing mechanism widely used in prior evaluations that MQuAKE‑Remastered systematically reassesses to expose failures masked by noisy multi‑hop judging.

### 🔗 Related Problem

**Editing Models with Search, Replace, and Cache** (2022)
- *Authors:* Eric Mitchell et al.
- *Direct Connection:* SERAC’s non‑parametric edit‑at‑inference strategy offers a contrasting approach whose performance on compositional queries motivates the need for rigorous, leakage‑resistant multi‑hop evaluation.

---

## Synthesis: How Prior Work Led to This Paper

Research on knowledge editing in language models was crystallized by CounterFact, which paired single‑fact interventions with locality and generalization checks to quantify whether an edit took and what collateral effects it caused. ROME operationalized direct, localized edits by identifying and modifying internal factual associations, while MEMIT scaled these interventions to many facts at once, exposing trade‑offs between breadth and unintended side effects. In parallel, MEND proposed fast, gradient‑based parameter updates that made practical large‑scale evaluation feasible, and SERAC took a non‑parametric path—searching, replacing, and caching responses at inference—to avoid risky parameter changes while still targeting specific facts. Building on these foundations, MQuAKE introduced a compositional, multi‑hop formulation, turning single factual changes into chains of dependent queries that require correct propagation and robust locality under composition, thereby surfacing weaknesses that single‑hop setups often miss. Together, these works established core editing mechanisms, evaluation templates, and a first multi‑hop stress test, but also revealed fragile judging and leakage in multi‑hop benchmarks. The convergence of scalable parametric editors (ROME, MEMIT, MEND), contrasting non‑parametric strategies (SERAC), and MQuAKE’s compositional design exposed a gap: evaluations were too noisy to diagnose propagation, side effects, and spurious success reliably. MQuAKE‑Remastered naturally follows by auditing and correcting multi‑hop data, tightening answer validation, and standardizing metrics so that these editing paradigms can be fairly compared and genuinely advanced in multi‑hop settings.

---

*Analysis generated on: 2026-01-06T06:26:30.624290*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

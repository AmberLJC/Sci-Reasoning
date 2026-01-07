# Prior Work Analysis Report

## Target Paper
**Title:** ztzZDzgfrh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Connection:* This paper formalized the RAG paradigm that ReDeEP targets, defining the core setting where outputs must reconcile retrieved evidence with parametric knowledge—exactly the conflict ReDeEP mechanistically diagnoses and detects.

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Connection:* By showing that FFNs store factual associations as key–value memories, this work directly motivates ReDeEP’s identification of Knowledge FFNs as the locus of parametric knowledge that can overpower retrieved evidence in the residual stream.

**In-context Learning and Induction Heads** (2022)
- *Authors:* Catherine Olsson et al.
- *Connection:* The characterization of induction (copying) heads that propagate tokens from context directly underpins ReDeEP’s notion of Copying Heads as the mechanism expected to carry retrieved evidence into generation.

### 🔍 Gap Identification

**SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models** (2023)
- *Authors:* Potsawee Manakul et al.
- *Connection:* SelfCheckGPT’s reliance on self-consistency signals without disentangling parametric versus retrieved knowledge highlights the precise gap ReDeEP fills with a mechanistic, source-specific detector.

### 📊 Baseline

**DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (2023)
- *Authors:* Eric Mitchell et al.
- *Connection:* As a widely used hallucination/detection baseline that is agnostic to retrieval and model internals, DetectGPT motivates ReDeEP’s improvement via interpretability-grounded signals that separate FFN-driven parametric bias from copying of retrieved evidence.

### 🔧 Extension

**Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Kevin Meng et al.
- *Connection:* ROME’s methodology for localizing and intervening on factual associations in specific MLP layers informs ReDeEP’s layer-wise attribution and intervention logic for diagnosing when FFNs drive hallucinations against retrieved content.

**Interpretability in the Wild: A Circuit for Indirect Object Identification in GPT-2** (2022)
- *Authors:* Kevin Wang et al.
- *Connection:* This circuit-level analysis (e.g., name-mover and copy-suppression heads) provides the concrete attention-head behaviors ReDeEP operationalizes to test whether Copying Heads effectively retain and integrate retrieved knowledge.

---

## Synthesis

ReDeEP’s core idea—detecting RAG hallucinations by disentangling parametric and retrieved knowledge signals through mechanistic interpretability—stands on two intellectual pillars. First, the RAG problem formulation by Lewis et al. defines the setting where external evidence must be integrated with model internals, creating the very conflict ReDeEP seeks to diagnose. Second, mechanistic interpretability of transformer components reveals where and how these two knowledge sources act: Geva et al. demonstrate that FFNs function as key–value stores for factual associations, and Meng et al. show such associations can be localized and manipulated at specific MLP layers. In parallel, Olsson et al. identify induction (copying) heads that propagate information from context, while Wang et al. map concrete circuits (name-movers, copy-suppression) that operationalize how attention heads transmit or inhibit token identity. Together, these works directly inspire ReDeEP’s two mechanistic levers: Knowledge FFNs (parametric knowledge) and Copying Heads (retrieved evidence). On the application side, prevailing detectors like SelfCheckGPT and DetectGPT provide practical but source-agnostic baselines; their inability to separate the roles of retrieval versus parametric memory crystallizes the gap ReDeEP addresses. By monitoring the balance between FFN contributions in the residual stream and copying-head effectiveness, ReDeEP offers a principled, component-level detector tailored to RAG’s unique failure mode: conflicts between retrieved and internal knowledge.

---
*Generated: 2026-01-06T23:09:26.616445*

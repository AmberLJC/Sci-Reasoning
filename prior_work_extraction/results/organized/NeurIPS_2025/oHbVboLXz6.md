# Prior Work Analysis Report

## Target Paper
**Title:** oHbVboLXz6
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Image-to-Markup Generation with Coarse-to-Fine Attention** (2017)
- *Authors:* Yuntian Deng et al.
- *Connection:* Uni-MuMER inherits the image-to-markup formulation for producing LaTeX from images introduced by this work, but realizes it within a generalist VLM and augments it with structured reasoning and auxiliary tasks.

**ICFHR2016 CROHME: Competition on Recognition of Online Handwritten Mathematical Expressions** (2016)
- *Authors:* Harold Mouchère et al.
- *Connection:* CROHME established the HMER task, symbol layout tree representation, and evaluation protocols that Uni-MuMER targets, and its tree representation directly motivates Uni-MuMER’s Tree-CoT supervision.

### 💡 Inspiration

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Connection:* The Tree-Aware Chain-of-Thought (Tree-CoT) in Uni-MuMER generalizes CoT from linear verbal steps to supervised, structure-aligned reasoning traces over symbol layouts, directly inspired by CoT’s explicit intermediate reasoning.

**Training Region-based Object Detectors with Online Hard Example Mining** (2016)
- *Authors:* Abhinav Shrivastava et al.
- *Connection:* Uni-MuMER’s Error-Driven Learning operationalizes the OHEM principle—prioritizing model-identified hard errors—by mining confusion pairs of visually similar symbols and emphasizing them during fine-tuning.

### 📊 Baseline

**Visual Instruction Tuning** (2023)
- *Authors:* Haotian Liu et al.
- *Connection:* Uni-MuMER directly builds on an instruction-tuned VLM (in the spirit of LLaVA) as its backbone and fully fine-tunes it without architectural changes, leveraging the demonstrated cross-task generalization that Visual Instruction Tuning introduced.

### 🔧 Extension

**Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Connection:* Uni-MuMER adapts the ToT idea of branching intermediate states by supervising tree-structured reasoning over spatial sub-expressions, effectively turning ToT’s search-time tree explorations into a train-time, task-specific Tree-CoT signal.

### 🔗 Related Problem

**TallyQA: Answering Complex Counting Questions** (2019)
- *Authors:* Manoj Acharya et al.
- *Connection:* The Symbol Counting task in Uni-MuMER is motivated by VQA counting findings (e.g., TallyQA) showing that explicit counting supervision mitigates over/under-counting; Uni-MuMER adapts this idea to count math symbols to reduce omission/duplication errors.

---

## Synthesis

Uni-MuMER’s core insight—fully fine-tuning a generalist VLM for handwritten mathematical expression recognition and guiding it with structure-aware reasoning and auxiliary signals—rests on three strands of prior work. First, the HMER problem formulation and its tree-structured targets come from CROHME, while the image-to-markup paradigm popularized by Image-to-Markup Generation (Deng et al.) established the sequence-generation view that Uni-MuMER preserves within a modern VLM. Second, Visual Instruction Tuning (LLaVA) demonstrated that a single VLM can be instruction-tuned to generalize across diverse tasks without architectural changes; Uni-MuMER adopts this as its baseline and shows that full fine-tuning can inject domain knowledge for HMER. Third, recent advances in eliciting and organizing intermediate reasoning—Chain-of-Thought (Wei et al.) and Tree-of-Thought (Yao et al.)—directly inspire Uni-MuMER’s Tree-CoT: supervised, tree-aligned reasoning traces that mirror symbol layout structures, moving from generic linear or search-time trees to domain-grounded, train-time structured rationales. To reduce common HMER failure modes, Uni-MuMER borrows the error-focused training principle from Online Hard Example Mining, turning model mistakes into prioritized confusion pairs in its Error-Driven Learning. Finally, insights from counting in VQA (TallyQA) motivate Symbol Counting as an auxiliary task to combat omissions and duplications, a key source of structural errors in HMER. Together, these works directly shape Uni-MuMER’s unified, multi-task fine-tuning recipe and its structure-aware supervision.

---
*Generated: 2026-01-06T23:08:23.948839*

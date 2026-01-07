# Prior Work Analysis Report

## Target Paper
**Title:** EVwMw2lVlw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge** (2019)
- *Authors:* Kenneth Marino et al.
- *Connection:* SK-VQA adopts the KB-VQA formulation introduced by OK-VQA—answering image-grounded questions that require outside knowledge—while providing large-scale, explicitly evidence-linked supervision to train context-augmented generation.

**FVQA: Fact-based Visual Question Answering** (2017)
- *Authors:* Peng Wang et al.
- *Connection:* Building on FVQA’s core idea of grounding VQA answers in external knowledge facts, SK-VQA generalizes the evidence from KB triples to heterogeneous external sources and scales supervision to millions of items.

**REALM: Retrieval-Augmented Language Model Pre-Training** (2020)
- *Authors:* Kelvin Guu et al.
- *Connection:* REALM established retrieve-then-read training signals; SK-VQA extends this paradigm to multimodal inputs by structuring each example as (image, question, retrieved external knowledge) → answer.

### 💡 Inspiration

**REVEAL: Retrieval-Augmented Visual-Language Pre-Training** (2022)
- *Authors:* Tanmay Gupta et al.
- *Connection:* REVEAL demonstrated that coupling retrieval with V-L pretraining improves knowledge-intensive reasoning, motivating SK-VQA to supply large, clean, retrieval-style supervision explicitly pairing questions, images, and evidence.

### 🔍 Gap Identification

**A-OKVQA: A Benchmark for Visual Question Answering Using External Knowledge** (2022)
- *Authors:* Adam Schwenk et al.
- *Connection:* A-OKVQA highlighted the need for higher-quality, knowledge-requiring VQA but remained limited in scale and domain breadth; SK-VQA directly addresses these constraints with 2M+ synthetic, diverse, and evidence-grounded QA pairs.

**LLaVA: Visual Instruction Tuning** (2023)
- *Authors:* Haotian Liu et al.
- *Connection:* LLaVA popularized large-scale synthetic instruction data for aligning VLMs but lacked explicit external-knowledge conditioning; SK-VQA directly fills this gap by generating evidence-linked, knowledge-grounded multimodal QA at scale.

### 🔗 Related Problem

**PICa: Prompting Language Models with Image Captions for Zero-shot VQA** (2022)
- *Authors:* Jieyu Yang et al.
- *Connection:* PICa showed that adding retrieved textual context boosts VQA with LMs; SK-VQA converts this insight into train-time supervision by providing paired evidence with each example rather than relying on inference-time prompting.

---

## Synthesis

SK-VQA’s core contribution—scaling synthetic, evidence-linked multimodal supervision for context-augmented generation—stands on the problem framing of knowledge-based VQA introduced by OK-VQA and anticipated by FVQA’s explicit grounding to external facts. A-OKVQA sharpened the need for high-quality, knowledge-requiring benchmarks but remained limited in size, diversity, and explicit evidence pairing, directly motivating SK-VQA’s emphasis on scale, domain coverage, and per-example knowledge sources. On the modeling side, REALM crystallized the retrieve-then-read training signal for language models, while REVEAL extended this idea to vision-language pretraining, demonstrating that retrieval materially improves knowledge-intensive reasoning. SK-VQA operationalizes these principles by constructing multimodal examples that pair images and questions with the external knowledge necessary to answer, providing the supervision that retrieval-augmented VLMs have lacked. Finally, the synthetic data paradigm popularized by LLaVA showed that large, curated instruction data can align VLMs but did not target knowledge-grounded generation; SK-VQA fills that gap by generating evidence-conditioned Q/A at unprecedented scale. PICa’s success with inference-time caption retrieval further underscored the value of external context, which SK-VQA transforms into supervised training data, moving beyond prompt-only solutions to teach models to integrate retrieved knowledge during generation.

---
*Generated: 2026-01-06T23:07:19.593387*

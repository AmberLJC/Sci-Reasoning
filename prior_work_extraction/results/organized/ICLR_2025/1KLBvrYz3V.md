# Prior Work Analysis Report

## Target Paper
**Title:** 1KLBvrYz3V
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**FVQA: Fact-based Visual Question Answering** (2017)
- *Authors:* Peng Wang et al.
- *Connection:* Century builds on FVQA’s core idea of grounding visual evaluation in external structured knowledge, extending the knowledge-graph–driven curation paradigm from fact-based VQA to assembling sensitive historical images and assessing knowledge-grounded descriptions.

**OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge** (2019)
- *Authors:* Kenneth Marino et al.
- *Connection:* Century adopts OK-VQA’s problem formulation of knowledge-intensive vision-language understanding and reframes it from short-form answering to historical contextualisation of images, with a domain-specific dataset and metrics.

### 💡 Inspiration

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Connection:* Century leverages the Self-Instruct insight that LMs can bootstrap high-quality supervision by using language models during dataset construction to propose, filter, and refine candidates and criteria for quality/diversity.

**ImageNet: A large-scale hierarchical image database** (2009)
- *Authors:* Jia Deng et al.
- *Connection:* Century echoes ImageNet’s ontology-guided dataset design by using a knowledge graph to ensure systematic topical and geographic coverage when sampling entities and events for sensitive historical imagery.

### 🔍 Gap Identification

**A-OKVQA: A Benchmark for Visual Question Answering Using Knowledge** (2022)
- *Authors:* Michael Schwenk et al.
- *Connection:* By highlighting that existing knowledge-VQA benchmarks mainly test correctness of brief answers and offer limited evaluation of explanation depth, A-OKVQA motivates Century’s multidimensional evaluation (accuracy, thoroughness, objectivity) for richer historical descriptions.

**The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes** (2020)
- *Authors:* Douwe Kiela et al.
- *Connection:* Hateful Memes exposed the difficulty of nuanced, sensitive multimodal content but framed evaluation around harmfulness classification, a limitation Century addresses by focusing on historically sensitive imagery and measuring contextual accuracy and neutrality in generated descriptions.

### 📊 Baseline

**Good News, Everyone! Contextual Image Captioning** (2019)
- *Authors:* Hakan Biten et al.
- *Connection:* GoodNews showed that news images demand socio-cultural context beyond pixels, and Century advances this line by targeting sensitive historical events/figures and introducing an automated, coverage-aware curation plus explicit evaluation of objectivity and thoroughness.

---

## Synthesis

Century’s core innovation—an automated pipeline that assembles a coverage-aware dataset of sensitive historical images and an evaluation framework for contextualised descriptions—draws a direct line from knowledge-intensive vision-language research and ontology-guided dataset construction. FVQA first grounded visual reasoning in external structured knowledge, establishing that evaluation can be purposefully designed to require facts beyond pixels. OK-VQA generalized this idea into a broad benchmark for knowledge-hungry VQA, which Century reframes into the task of historical contextualisation, shifting from short answers to richer, multi-faceted descriptions. A-OKVQA’s emphasis on improved data quality and rationales also surfaced a key gap: existing benchmarks largely test correctness but not the depth, balance, and justification of responses. Century addresses this with explicit dimensions—accuracy, thoroughness, and objectivity—tailored to contested historical content. From the dataset side, GoodNews demonstrated that news imagery demands socio-cultural context, but it lacked targeted coverage of sensitive historical figures/events and principled measures of neutrality—gaps Century fills. Hateful Memes highlighted challenges of nuanced, potentially harmful multimodal content, further motivating an evaluation that prioritizes careful, balanced historical framing over simple toxicity detection. Methodologically, Self-Instruct provided a template for using LMs to bootstrap data generation and filtering, which Century adapts to curate candidates and enforce quality/diversity criteria. Finally, ImageNet’s ontology-driven construction inspired Century’s use of knowledge graphs to systematically ensure topical and geographic diversity, completing the intellectual arc from knowledge grounding to principled dataset design and evaluation.

---
*Generated: 2026-01-06T23:08:23.929415*

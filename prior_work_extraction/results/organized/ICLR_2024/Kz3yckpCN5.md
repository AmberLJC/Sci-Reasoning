# Prior Work Analysis Report

## Target Paper

**Title:** The False Promise of Imitating Proprietary Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Arnav Gudibande, Eric Wallace, Charlie Victor Snell, Xinyang Geng, Hao Liu, Pieter Abbeel, Sergey Levine, Dawn Song

**Keywords:** Language Models, Model Imitation, Distillation, Instruction-Tuning

**Abstract:** 
> An emerging method to cheaply improve a weaker language model is to finetune it on outputs from a stronger model, such as a proprietary system like ChatGPT (e.g., Alpaca, Self-Instruct, and others). In this work, we critically analyze this approach of imitating language models. We first finetune a series of LMs that imitate ChatGPT using varying base model sizes (1.5B--13B), data sources, and imitation data amounts (0.3M--150M tokens). We then evaluate the models using crowd raters and canonical...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* This work introduced the paradigm of using a stronger LLM to synthesize instruction–response pairs for supervised fine-tuning, which the paper adopts and stress-tests when the teacher is proprietary (e.g., ChatGPT).

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* InstructGPT established instruction following with human preference optimization and human ratings, framing the evaluation paradigm that the paper scrutinizes by demonstrating how surface-level helpfulness can mislead crowd raters about true competence.

**Finetuned Language Models Are Zero-Shot Learners** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* FLAN showed that diverse, broad instruction tuning primarily helps via task coverage, an insight the paper leverages by designing targeted tests that reveal imitation data lacking coverage yields little to no capability transfer.

### 🔍 Gap Identification

**Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality** (2023)
- *Authors:* Chiang et al.
- *Direct Connection:* Vicuna trained on ShareGPT conversations and reported near-ChatGPT quality via pairwise judgments, a claim the paper directly revisits by showing such human-preference ratings can mask persistent deficits on tasks absent from the imitation data.

### 📊 Baseline

**Alpaca: A Strong, Replicable Instruction-Following Model** (2023)
- *Authors:* Rohan Taori et al.
- *Direct Connection:* Alpaca’s recipe of distilling text-davinci-003 into LLaMA with ~52K synthetic pairs is the canonical imitation pipeline the paper replicates and scales (model sizes and data amounts) to examine whether imitation actually closes capability gaps.

**Koala: A Dialogue Model for Academic Research** (2023)
- *Authors:* Xinyang Geng et al.
- *Direct Connection:* Koala fine-tuned LLaMA on ChatGPT-derived conversations and reported strong user preferences, providing a prominent imitation baseline that motivates the paper’s deeper automatic evaluations revealing limited transfer of underlying capabilities.

---

## Synthesis: How Prior Work Led to This Paper

Self-Instruct introduced the practical blueprint for bootstrapping supervised instruction-tuning data by prompting a stronger model to generate instruction–response pairs, seeding a wave of low-cost alignment via synthetic supervision. Alpaca operationalized this idea by distilling text-davinci-003 into LLaMA using ~52K synthetic pairs, demonstrating that small open models could appear highly compliant with instructions after imitation. Vicuna extended the imitation story by training on real user–ChatGPT conversations from ShareGPT and reporting near-ChatGPT quality using pairwise judgments, while Koala similarly fine-tuned LLaMA on ChatGPT-derived dialogues and found strong user preferences—both reinforcing the perception that cheap imitation yields ChatGPT-like chat quality. InstructGPT had earlier defined instruction following through supervised fine-tuning and preference-based evaluation, making human ratings a central yardstick for helpfulness and safety. FLAN, in parallel, established that instruction tuning improves zero-shot performance largely through broad task coverage, implying that what’s in the instruction data critically governs generalization.
Together, these works created a compelling but untested belief that imitating proprietary models via synthetic or conversational data could efficiently transfer underlying capabilities, as validated by human preferences. The paper synthesizes and extends these ideas by reproducing and scaling Alpaca/Self-Instruct-style pipelines across model sizes and data volumes, and by contrasting crowd ratings with targeted automatic evaluations. Anchored by FLAN’s coverage insight and Vicuna/Koala’s preference-based claims, it reveals that imitation primarily transfers style and instruction compliance, not deeper skills on tasks absent from the imitation data—clarifying the limits of “cheap imitation” and motivating more coverage-aware training and evaluation.

---

*Analysis generated on: 2026-01-06T12:55:25.968545*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

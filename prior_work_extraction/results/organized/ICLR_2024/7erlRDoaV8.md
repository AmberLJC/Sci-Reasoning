# Prior Work Analysis Report

## Target Paper

**Title:** Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Vaidehi Patil, Peter Hase, Mohit Bansal

**Keywords:** Sensitive Information Deletion, Privacy Attacks, Model editing, Language Models

**Abstract:** 
> Pretrained language models sometimes possess knowledge that we do not wish them to, including memorized personal information and knowledge that could be used to harm people. They can also output toxic or harmful text. To mitigate these safety and informational issues, we propose an attack-and-defense framework for studying the task of deleting sensitive information directly from model weights. We study direct edits to model weights because (1) this approach should guarantee that particular delet...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Secret Sharer: Measuring Unintended Memorization in Neural Networks** (2019)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* Its exposure metric—judging an attack successful when a secret appears among a model’s top-ranked candidates—directly underpins this paper’s top-B candidate threat model and the corresponding defense objective.

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* By showing practical white- and gray-box extraction of memorized sequences via sampling/beam search, it defines the concrete adversary behavior this paper designs defenses against and motivates weight-level deletion over surface-level filters.

### 🔍 Gap Identification

**Quantifying Memorization Across Neural Language Models** (2022)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* It demonstrates that memorized content persists across prompts and scales with model size, highlighting the insufficiency of naive redaction and motivating robust deletion objectives resilient to paraphrases and attack diversity.

### 📊 Baseline

**Mass-Editing Memory in a Transformer (MEMIT)** (2023)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* As the state-of-the-art multi-edit approach, it serves as a primary baseline and exposes overgeneralization/side-effect risks that this paper addresses with defense-oriented loss design against extraction.

**MEND: Fast Model Editing at Scale** (2022)
- *Authors:* Eric Mitchell et al.
- *Direct Connection:* Its gradient-based editor for local, scalable edits is a main comparator whose lack of guarantees against adversarial extraction motivates the paper’s attack-aware deletion objectives.

### 🔧 Extension

**Locating and Editing Factual Associations in GPT (ROME)** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* This method for localizing and editing factual associations in model weights provides the editable mechanism and baseline that this paper adapts toward deletion and tests under adversarial extraction.

---

## Synthesis: How Prior Work Led to This Paper

Work on unintended memorization established both the measurement and the stakes of the problem: The Secret Sharer introduced exposure, a rank-based notion of risk where an attack is considered successful if a secret appears among a model’s top candidates. Subsequent demonstrations showed that large language models can yield verbatim training data under sampling and beam-search strategies, concretizing practical extraction behavior and the relevance of white-/gray-box adversaries. Further analysis quantified how memorization scales with model size and persists across paraphrases, underscoring that surface-level fixes or naive redaction do not reliably remove sensitive knowledge. In parallel, knowledge editing methods matured: ROME pinpointed and modified internal factual associations through targeted weight updates, inaugurating a controlled, local editing paradigm. MEND delivered a fast, gradient-based editor for scalable local edits, while MEMIT expanded to mass editing, revealing challenges like overgeneralization and leakage to unintended contexts.

Taken together, these works expose a gap: while extraction is tractable and persistent, existing editors focus on changing facts rather than making them unrecoverable under adversarial prompting, and they lack guarantees aligned with exposure-style risk. The current paper synthesizes the exposure-based threat model with weight-editing mechanisms, reframing editing as deletion against an attacker who succeeds if the answer is among B candidates. Building on ROME/MEND/MEMIT’s editability, it designs attack-aware objectives that suppress the sensitive answer across paraphrases and contexts while controlling side effects—naturally extending editing into a defense tuned to extraction risks.

---

*Analysis generated on: 2026-01-06T10:15:58.077310*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

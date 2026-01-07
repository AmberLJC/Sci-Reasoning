# Prior Work Analysis Report

## Target Paper

**Title:** How new data permeates LLM knowledge and how to dilute it

**Conference:** ICLR 2025 (spotlight)

**Authors:** Chen Sun, Renat Aksitov, Andrey Zhmoginov, Nolan Andrew Miller, Max Vladymyrov, Ulrich Rueckert, Been Kim, Mark Sandler

**Keywords:** fine-tuning, hallucinations, knowledge injection, memory, LLMs

**Abstract:** 
> Large language models continually learn through the accumulation of gradient-based updates, but how individual pieces of new information affect existing knowledge, leading to both beneficial generalization and problematic hallucination, remains poorly understood. We demonstrate that when learning new information, LLMs exhibit a "priming" effect: learning a new fact can cause the model to inappropriately apply that knowledge in unrelated contexts.
To systematically study this phenomenon, we intro...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Language Models as Knowledge Bases?** (2019)
- *Authors:* Fabio Petroni et al.
- *Direct Connection:* This work established using cloze-style token probabilities to probe factual associations in LMs, which directly underpins the paper’s predictor that pre-update keyword probabilities forecast how newly learned facts will permeate and prime unrelated generations.

**Editing Factual Knowledge in Language Models** (2021)
- *Authors:* Nicola De Cao et al.
- *Direct Connection:* This paper introduced the targeted knowledge-editing problem and locality/generalization evaluation protocols that the current work adapts to the standard gradient-updating setting to study how new information spreads.

### 💡 Inspiration

**Language Models (Mostly) Know What They Know** (2022)
- *Authors:* Saurav Kadavath et al.
- *Direct Connection:* By showing model confidence/log-probabilities correlate with factual correctness and awareness, it motivated the paper’s key insight that pre-training token probabilities of key terms can quantitatively predict the strength of post-training priming.

### 🔍 Gap Identification

**Locating and Editing Factual Associations in GPT (ROME)** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* ROME documented that parametric fact edits can leak broadly (imperfect locality) and introduced CounterFact to test this, a limitation that motivates the new Outlandish probes and the paper’s analysis of broader priming under standard training.

### 📊 Baseline

**Overcoming catastrophic forgetting in neural networks (EWC)** (2017)
- *Authors:* James Kirkpatrick et al.
- *Direct Connection:* As the canonical regularization baseline for controlling interference in continual learning, EWC serves as the primary comparator the paper contrasts against when proposing dilution strategies that reduce priming without incurring forgetting.

### 🔗 Related Problem

**Fast Model Editing at Scale (MEND)** (2022)
- *Authors:* Eric Mitchell et al.
- *Direct Connection:* MEND’s goal of making localized updates with minimal side-effects and its locality metrics directly inform the present paper’s measurement of unintended spread (“priming”) and the need for techniques that constrain it during fine-tuning.

**Mass-Editing Memory in a Transformer (MEMIT)** (2023)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* By showing how multiple edits propagate across layers and contexts and formalizing generalization/locality trade-offs, MEMIT provides the immediate backdrop for analyzing how a single newly learned fact can permeate and trigger undesired priming.

---

## Synthesis: How Prior Work Led to This Paper

Cloze-probing established that token probabilities can reveal stored factual associations in language models, grounding a quantitative way to read out latent knowledge before any update. Subsequent evidence showed that models’ own log-probabilities correlate with factual correctness and self-knowledge, suggesting that simple likelihood signals can predict when a model will be confident—and potentially overconfident—about applying information. Targeted editing work then formalized the task of inserting or changing facts while evaluating locality versus generalization, defining concrete metrics and setups for assessing how an update should and should not spread. MEND operationalized localized edits at scale while emphasizing side-effect measurement, and ROME pinpointed where factual associations live and demonstrated that even carefully localized edits can leak, with CounterFact giving a standardized probe of overreach. MEMIT extended these ideas to many edits, revealing how updates propagate across layers and contexts and sharpening notions of desired versus undesired generalization. In parallel, elastic weight consolidation provided the standard regularization approach to suppress interference during sequential learning, though it is agnostic to the semantic structure of the new information.
Together, these strands exposed a gap: we lacked a systematic understanding of how ordinary gradient-based learning causes new facts to permeate unrelated contexts, and a principled, predictive handle on when that would happen. Building on likelihood-as-knowledge readouts and edit-locality diagnostics, the paper introduces diverse probes to observe this priming phenomenon, shows that pre-update keyword probabilities predict its strength across models, and proposes dilution techniques that surpass generic interference regularizers by specifically targeting the mechanisms that drive undesired spread.

---

*Analysis generated on: 2026-01-06T05:53:18.290693*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

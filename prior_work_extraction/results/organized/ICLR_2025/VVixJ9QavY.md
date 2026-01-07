# Prior Work Analysis Report

## Target Paper

**Title:** Reasoning Elicitation in Language Models via Counterfactual Feedback

**Conference:** ICLR 2025 (oral)

**Authors:** Alihan Hüyük, Xinnuo Xu, Jacqueline R. M. A. Maasch, Aditya V. Nori, Javier Gonzalez

**Keywords:** language models, reasoning, fine-tuning, counterfactuals

**Abstract:** 
> Despite the increasing effectiveness of language models, their reasoning capabilities remain underdeveloped. In particular, causal reasoning through counterfactual question answering is lacking. This work aims to bridge this gap. We first derive novel metrics that balance accuracy in factual and counterfactual questions, capturing a more complete view of the reasoning abilities of language models than traditional factual-only based metrics. Second, we propose several fine-tuning approaches that ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Learning the Difference that Makes a Difference: Counterfactually-Augmented Data Improves Robustness** (2020)
- *Authors:* Kaushik et al.
- *Direct Connection:* This work established using paired factual–counterfactual examples as supervision to reduce spurious cues, directly motivating the paper’s use of counterfactual feedback and its balanced factual/counterfactual evaluation metrics.

**WIQA: A Dataset for 'What If' Reasoning Over Procedural Text** (2019)
- *Authors:* Tandon et al.
- *Direct Connection:* WIQA formalized counterfactual 'what-if' question answering, providing the problem setting and evaluation paradigm that this paper targets when eliciting causal reasoning in LMs.

**ProofWriter: Generating Proofs for Rule-Based Reasoning** (2021)
- *Authors:* Tafjord et al.
- *Direct Connection:* ProofWriter provides a deductive reasoning testbed with stepwise proofs, grounding the paper’s generalization claims and informing process-oriented fine-tuning targets.

### 💡 Inspiration

**Let’s Verify Step by Step** (2023)
- *Authors:* Wang et al.
- *Direct Connection:* By introducing process-level verification feedback for chain-of-thought, this paper inspired the use of counterfactual violations as a process supervision signal to shape reasoning steps.

**Locating and Editing Factual Associations in GPT (ROME) and the CounterFact Benchmark** (2022)
- *Authors:* Meng et al.
- *Direct Connection:* CounterFact’s dual evaluation—adopting edited counterfactuals while retracting originals—inspired the paper’s metrics that jointly assess factual and counterfactual accuracy to capture causal consistency.

### 📊 Baseline

**STaR: Bootstrapping Reasoning With Reasoning** (2022)
- *Authors:* Zelikman et al.
- *Direct Connection:* STaR showed that fine-tuning on rationales selected by outcome correctness elicits reasoning, which this paper extends by selecting and training with counterfactual-consistency feedback rather than correctness alone.

### 🔧 Extension

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Rafailov et al.
- *Direct Connection:* DPO provided a simple preference-learning objective that this work instantiates with factual-versus-counterfactual preference pairs to fine-tune reasoning without reinforcement learning.

---

## Synthesis: How Prior Work Led to This Paper

Counterfactual supervision in NLP was crystallized by Kaushik et al., who paired factual and counterfactual examples to force models to rely on causally relevant features rather than spurious correlations; their setup highlighted the need to perform well on both original and counterfactual variants. WIQA then framed a concrete “what-if” question answering task over procedural text, turning counterfactual reasoning into a standardized evaluation problem. Complementing these, Meng et al. introduced CounterFact and emphasized dual objectives—adopt the counterfactual while retracting the original—suggesting evaluation should jointly score counterfactual adoption and factual consistency. On the training side, Zelikman et al.’s STaR showed that selecting rationales linked to correct outcomes and fine-tuning on them can elicit reasoning, while Wang et al. demonstrated process-level verification feedback as a way to shape chain-of-thought steps. Finally, Rafailov et al. provided DPO, a lightweight preference-optimization objective that operationalizes pairwise feedback without reinforcement learning. Together, these threads exposed an opportunity: leverage paired factual–counterfactual signals not only as data but as feedback to shape reasoning processes, and assess success with metrics that balance both sides. Building on STaR and verifier-style process supervision but replacing correctness-based signals with counterfactual consistency, and operationalizing the signal via a DPO-style objective, the paper fine-tunes models to prefer reasoning that remains valid under counterfactual interventions. The CounterFact-inspired dual metrics formalize the target behavior, while WIQA and proof-style datasets like ProofWriter ground evaluation across counterfactual, inductive, and deductive regimes.

---

*Analysis generated on: 2026-01-06T11:13:40.262347*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Iterative Label Refinement Matters More than Preference Optimization under Weak Supervision

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yaowen Ye, Cassidy Laidlaw, Jacob Steinhardt

**Keywords:** unreliable human supervision, language model post-training, scalable oversight

**Abstract:** 
> Language model (LM) post-training relies on two stages of human supervision: task demonstrations for supervised finetuning (SFT), followed by preference comparisons for reinforcement learning from human feedback (RLHF). As LMs become more capable, the tasks they are given become harder to supervise. Will post-training remain effective under unreliable supervision? To test this, we simulate unreliable demonstrations and comparison feedback using small LMs and time-constrained humans. We find that...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* This work established the two-stage post-training pipeline—SFT on demonstrations followed by preference-based optimization—that ILR explicitly modifies by keeping SFT and repurposing the preference stage to refine (replace) SFT labels rather than optimize a policy.

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Direct Connection:* It introduced pairwise human comparison feedback as a supervision signal, which ILR directly reuses not for reward/policy learning but to decide whether a human demonstration should be replaced by a model-generated alternative.

### 💡 Inspiration

**Learning to Summarize with Human Feedback** (2020)
- *Authors:* Nisan Stiennon et al.
- *Direct Connection:* By using preference models to rank and select higher-quality outputs (e.g., best-of-N), this work provided the concrete idea of using comparisons as a selection mechanism, which ILR adapts to choose between a human demo and a model candidate for dataset replacement.

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Self-Instruct demonstrated that model-generated data can iteratively bootstrap and improve SFT datasets, an idea ILR extends by using preference feedback to selectively substitute unreliable human demonstrations with model outputs.

### 🔍 Gap Identification

**Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision** (2023)
- *Authors:* Burns et al.
- *Direct Connection:* By formalizing the oversight problem where the supervisor is weaker than the model, this work highlights the unreliability of supervision that ILR directly addresses by converting weak comparisons into iterative label improvements.

### 📊 Baseline

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Rafailov et al.
- *Direct Connection:* DPO is the primary preference-optimization baseline that the paper shows fails under unreliable comparisons, motivating ILR as an alternative that uses the same preference signal to iteratively relabel SFT data.

### 🔗 Related Problem

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* Showing that AI-provided preference/critique can substitute for expensive or inconsistent human feedback directly motivated the paper’s setting of unreliable supervision and the design of ILR to make principled use of such noisy comparisons.

---

## Synthesis: How Prior Work Led to This Paper

Instruction-following post-training emerged as a two-stage pipeline of supervised fine-tuning on human demonstrations followed by preference-driven optimization, as crystallized by Ouyang et al., while Christiano et al. introduced pairwise comparisons as a practical supervisory signal. Stiennon et al. showed that preference information can serve not only for training but also for selection—ranking multiple candidates and choosing the best—which revealed a powerful use of comparisons as a gating mechanism. DPO reframed preference optimization as a supervised loss on chosen versus rejected responses, making preference learning simple and scalable but inherently sensitive to the quality of comparison labels. In parallel, Self-Instruct demonstrated that model-generated data can iteratively bootstrap and strengthen SFT corpora, suggesting that models themselves can supply or replace labels when done judiciously. Constitutional AI established that AI feedback can substitute for humans in preference judgments, underscoring both scalability and the inevitability of noisier, less reliable supervision as models grow stronger. Weak-to-Strong Generalization further formalized the setting where overseers are weaker than the models they train, sharpening the challenge of unreliable oversight.
Together these works expose a gap: preference optimization like DPO can falter when comparisons are noisy, yet comparisons are excellent for choosing between alternatives, and model-generated data can improve SFT if filtered well. The present paper synthesizes these insights by using comparisons as a principled filter to iteratively replace unreliable demonstrations with better model outputs and then retraining via SFT, thereby turning weak or AI feedback into a robust label-refinement mechanism under unreliable supervision.

---

*Analysis generated on: 2026-01-06T12:09:11.510113*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Uncovering Overfitting in Large Language Model Editing

**Conference:** ICLR 2025 (spotlight)

**Authors:** Mengqi Zhang, Xiaotian Ye, Qiang Liu, Shu Wu, Pengjie Ren, Zhumin Chen

**Keywords:** Large language models, Knowledge editing, Editing overfit

**Abstract:** 
> Knowledge editing has been proposed as an effective method for updating and correcting the internal knowledge of Large Language Models (LLMs). However, existing editing methods often struggle with complex tasks, such as multi-hop reasoning. In this paper, we identify and investigate the phenomenon of Editing Overfit, where edited models assign disproportionately high probabilities to the edit target, hindering the generalization of new knowledge in complex scenarios. We attribute this issue to t...

---

## Key Prior Works (5 papers with direct influence)

### 🏗️ Foundation

**Editing Factual Knowledge in Language Models** (2021)
- *Authors:* Andrea De Cao et al.
- *Direct Connection:* This work formalized the knowledge-editing problem and popularized the target-likelihood objective and evaluation axes (efficacy/generalization/locality) that the present paper scrutinizes as a root cause of editing overfit.

### 📊 Baseline

**MEND: Fast Model Editing at Scale** (2022)
- *Authors:* Eric Mitchell et al.
- *Direct Connection:* MEND’s meta-learned gradient updates rely on direct prompt→target supervision, and this paper directly evaluates MEND to show that such training induces the over-confident target probabilities characteristic of editing overfit, especially in multi-hop settings.

**ROME: Locating and Editing Factual Associations in GPT** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* ROME enforces a new subject–relation→object mapping via a rank-one weight update and established standard evaluation (e.g., paraphrase/neighborhood generalization), which this paper diagnoses as yielding excessive target probability and poor generalization indicative of editing overfit.

**MEMIT: Mass-Editing Memory in a Transformer** (2023)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* By scaling ROME-style updates to many facts with a target-imposition objective, MEMIT exemplifies the dominant editing paradigm that this paper shows systematically overfits and fails to generalize on complex, multi-hop queries.

**SERAC: A Memory-Based Model Editing Framework** (2022)
- *Authors:* Eric Mitchell et al.
- *Direct Connection:* Although SERAC uses a non-parametric memory and scope classifier to preserve locality, it is trained on prompt–target pairs, and this paper demonstrates that even this paradigm exhibits editing overfit under compositional/multi-hop evaluation.

---

## Synthesis: How Prior Work Led to This Paper

Work on knowledge editing coalesced around a common formulation and objective: given a prompt expressing a subject–relation, optimize the model so the desired target is assigned high likelihood while preserving unrelated behavior. De Cao et al. crystallized this task, along with the core evaluation axes of efficacy, generalization, and locality that became standard. MEND meta-learned small gradient-based updates that can be applied quickly to new edits, training explicitly on prompt→target pairs to maximize the edited answer while monitoring side effects. ROME uncovered where factual associations reside in transformer MLP layers and proposed a rank-one update that directly enforces a new subject–relation→object mapping, introducing popular tests such as paraphrase and neighborhood generalization. MEMIT scaled this intervention to many simultaneous edits while retaining the same target-imposition paradigm. In parallel, SERAC attempted to protect locality via a retrieval memory and scope classifier but still trained on the same direct prompt–target correspondence.
Together, these works established a powerful yet narrowly focused paradigm: editing systems are optimized to strongly prefer the target answer given an edit-triggering prompt, and they are mostly evaluated on single-hop factual prompts. This combination left a gap—how such target-imposing edits behave in complex, multi-hop situations requiring reasoning beyond direct cue–response. The present paper synthesizes these insights by revealing that the prevailing objective induces editing overfit—disproportionately high target probabilities that impair generalization—and introduces EVOKE with fine-grained metrics to expose and measure this failure mode across leading editors.

---

*Analysis generated on: 2026-01-06T15:13:03.129800*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

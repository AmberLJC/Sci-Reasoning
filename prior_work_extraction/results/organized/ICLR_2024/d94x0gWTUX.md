# Prior Work Analysis Report

## Target Paper

**Title:** Tool-Augmented Reward Modeling

**Conference:** ICLR 2024 (spotlight)

**Authors:** Lei Li, Yekun Chai, Shuohuan Wang, Yu Sun, Hao Tian, Ningyu Zhang, Hua Wu

**Keywords:** Reward Model, Large Language Model, Tool Learning, Augmented Language Model

**Abstract:** 
> Reward modeling (*a.k.a.*, preference modeling) is instrumental for aligning large language models with human preferences, particularly within the context of reinforcement learning from human feedback (RLHF). While conventional reward models (RMs) have exhibited remarkable scalability, they oft struggle with fundamental functionality such as arithmetic computation, code execution, and factual lookup. In this paper, we propose a tool-augmented preference modeling approach, named Themis, to addres...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Deep reinforcement learning from human preferences** (2017)
- *Authors:* Christiano et al.
- *Direct Connection:* This work introduced the pairwise preference-based reward modeling framework that Themis adopts and augments by enabling the reward model itself to consult external tools during scoring.

**Learning to summarize from human feedback** (2020)
- *Authors:* Stiennon et al.
- *Direct Connection:* It established scalable, text-domain reward models trained on human preferences, which Themis directly builds on while addressing their inability to verify factual or computational claims.

### 💡 Inspiration

**Toolformer: Language Models Can Teach Themselves to Use Tools** (2023)
- *Authors:* Schick et al.
- *Direct Connection:* Toolformer’s demonstration that LMs can learn to invoke APIs (e.g., calculator, search) directly inspired Themis’s tool-augmented reward model that issues API calls during evaluation.

### 🔍 Gap Identification

**Can Large Language Models Be Good Judges?** (2023)
- *Authors:* Zheng et al.
- *Direct Connection:* This paper documents that LLM-based judges struggle with math, code, and factuality without external verification, directly motivating Themis’s use of calculators and search within the reward model.

### 📊 Baseline

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Ouyang et al.
- *Direct Connection:* The standard RLHF pipeline and reward model used here serve as the primary baseline that Themis improves by equipping the reward model with tool use for more reliable judgments.

### 🔧 Extension

**ReAct: Synergizing Reasoning and Acting in Language Models** (2022)
- *Authors:* Yao et al.
- *Direct Connection:* Themis extends the ReAct-style interleaving of chain-of-thought and tool actions by generating autoregressive reasoning-and-tool traces inside the reward model to reach a justified score.

### 🔗 Related Problem

**WebGPT: Browser-assisted question-answering with human feedback** (2021)
- *Authors:* Nakano et al.
- *Direct Connection:* By showing that a policy model using web search plus preference-based RM improves factuality, this work motivated Themis’s shift to letting the reward model itself perform search to grade answers.

---

## Synthesis: How Prior Work Led to This Paper

Preference-based reward modeling was formalized by Christiano et al., who introduced pairwise comparisons to learn a scalar reward from human feedback. Stiennon et al. scaled this formulation to long-form text, demonstrating that reward models can guide generation quality at scale. Ouyang et al. operationalized RLHF for instruction-following systems, standardizing a pipeline where a text-only reward model learns to prefer better responses despite lacking direct mechanisms to verify correctness. In parallel, Nakano et al. showed that letting a policy browse the web during answer generation, evaluated by preference models, boosts factual accuracy, suggesting the power of tool use for alignment. Schick et al. revealed that language models can learn to call external APIs like calculators and search engines autonomously, while Yao et al. combined chain-of-thought with actionable tool calls in an interleaved, autoregressive fashion to produce interpretable reasoning-action traces. Finally, Zheng et al. highlighted systematic failures of LLM judges on math, code, and factuality when deprived of verification or external information. Taken together, these works exposed a gap: reward models—as the judges guiding RLHF—remained text-only and thus brittle on verifiable skills, even as policy models and prompting methods leveraged tools for reliability. The natural next step was to move tool use and reasoning-action traces into the reward model itself. Building on the standard pairwise RM framework, while borrowing Toolformer’s API invocation and ReAct’s trace structure, the new approach empowers the judge to compute, search, and justify, directly addressing the documented weaknesses in evaluators and improving scoring reliability and interpretability.

---

*Analysis generated on: 2026-01-06T08:04:23.276042*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets

**Conference:** ICLR 2024 (spotlight)

**Authors:** Seonghyeon Ye, Doyoung Kim, Sungdong Kim, Hyeonbin Hwang, Seungone Kim, Yongrae Jo, James Thorne, Juho Kim, Minjoon Seo

**Keywords:** large language models, language model evaluation, natural language processing

**Abstract:** 
> Evaluation of Large Language Models (LLMs) is challenging because instruction-following necessitates alignment with human values and the required set of skills varies depending on the instruction. However, previous studies have mainly focused on coarse-grained evaluation (i.e. overall preference-based evaluation), which limits interpretability since it does not consider the nature of user instructions that require instance-wise skill composition. In this paper, we introduce FLASK (Fine-grained L...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* The Helpful/Harmless (and truthful) alignment axes articulated by Bai et al. anchor the alignment-oriented skill taxonomy that FLASK operationalizes into explicit, per-instruction skill scores.

### 💡 Inspiration

**G-Eval: NLG Evaluation using GPT-4 with Better Prompting** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* G-Eval showed rubric-guided, criterion-level LLM judging can better match humans, an idea FLASK generalizes by dynamically deriving per-instruction alignment skills and scoring each skill rather than relying on a fixed task-specific rubric.

**Beyond Accuracy: Behavioral Testing of NLP Models with CheckList** (2020)
- *Authors:* Marco Tulio Ribeiro et al.
- *Direct Connection:* CheckList’s capability-based, compositional behavioral testing inspired FLASK’s notion of decomposing each instruction into atomic skills and evaluating performance at the capability level rather than a single aggregate score.

### 🔍 Gap Identification

**Holistic Evaluation of Language Models** (2022)
- *Authors:* Percy Liang et al.
- *Direct Connection:* HELM established multi-dimensional LLM evaluation but at scenario- or metric-level granularity, motivating FLASK’s move to instance-wise skill-set decomposition for finer interpretability within instruction following.

### 📊 Baseline

**MT-Bench: Multi-turn Benchmark for Evaluating LLMs as Chatbots** (2023)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* MT-Bench’s LLM-as-judge, multi-turn preference scoring provides the coarse-grained, overall evaluation baseline that FLASK explicitly decomposes into per-instruction, skill-level judgments to gain interpretability and reliability.

**AlpacaEval: Automatic Evaluation of Instruction-following Models** (2023)
- *Authors:* Li et al.
- *Direct Connection:* AlpacaEval popularized using GPT-4 as an automatic judge to produce a single holistic win rate, whose lack of fine-grained interpretability is the gap FLASK addresses by eliciting and scoring the specific skills each instruction requires.

---

## Synthesis: How Prior Work Led to This Paper

MT-Bench introduced an LLM-as-judge protocol for open-ended, multi-turn chatbot evaluation, distilling model quality into overall preference judgments, while AlpacaEval advanced automatic instruction-following assessment via GPT-4 judges that output a single holistic win rate. G-Eval demonstrated that rubric-guided, criterion-level judgments by large models can more faithfully reflect human preferences than undifferentiated scores, establishing that structured prompts and explicit criteria improve reliability. Holistic Evaluation of Language Models (HELM) framed evaluation as multi-dimensional across scenarios and metrics, highlighting breadth but remaining coarse at the instance level. CheckList earlier promoted capability-based, compositional behavioral testing, arguing for decomposing model behavior into atomic skills to expose failure modes invisible to aggregate metrics. In parallel, Bai et al. formalized helpfulness, harmlessness, and related alignment dimensions at the core of assistant behavior, providing concrete alignment axes that naturally map to evaluable skills.
Taken together, these works revealed a gap: dominant open-ended evaluations reduce responses to single preferences or fixed rubrics, sacrificing interpretability and masking which alignment capabilities succeed or fail per instruction. Building on rubric-guided LLM judging and capability decomposition, and grounded in alignment axes like helpfulness and harmlessness, the current work synthesizes a protocol that first infers the skills each instruction demands and then scores responses at the skill level. This instance-wise skill composition preserves the openness of MT-Bench–style settings while delivering the fine-grained interpretability and improved reliability that HELM and CheckList imply are necessary for a holistic view of model alignment.

---

*Analysis generated on: 2026-01-06T16:26:49.191847*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

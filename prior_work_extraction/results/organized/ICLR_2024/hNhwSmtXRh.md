# Prior Work Analysis Report

## Target Paper

**Title:** Lemur: Harmonizing Natural Language and Code for Language Agents

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yiheng Xu, Hongjin SU, Chen Xing, Boyu Mi, Qian Liu, Weijia Shi, Binyuan Hui, Fan Zhou, Yitao Liu, Tianbao Xie, Zhoujun Cheng, Siheng Zhao, Lingpeng Kong, Bailin Wang, Caiming Xiong, Tao Yu

**Keywords:** large language model, agent, code generation, reasoning, decision making

**Abstract:** 
> We introduce Lemur and Lemur-Chat, openly accessible language models optimized
for both natural language and coding capabilities to serve as the backbone
of versatile language agents. The evolution from language chat models to
functional language agents demands that models not only master human interaction,
reasoning, and planning but also ensure grounding in the relevant environments.
This calls for a harmonious blend of language and coding capabilities
in the models. Lemur and Lemur-Chat are p...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* By formalizing an interleaved reasoning–acting loop with natural language traces and tool/API calls, ReAct directly motivates training a single model to fluently switch between language reasoning and executable actions (code/tool use) that Lemur aims to unify.

### 💡 Inspiration

**PAL: Program-Aided Language Models** (2023)
- *Authors:* Luyu Gao et al.
- *Direct Connection:* PAL shows that generating and executing short programs markedly improves reasoning, providing the key insight that strong code-generation competence is a direct path to better agentic problem solving that Lemur explicitly targets.

### 🔍 Gap Identification

**WizardCoder: Empowering Code LLMs with Evol-Instruct** (2023)
- *Authors:* Luo et al.
- *Direct Connection:* WizardCoder’s evol-instruct code tuning dramatically boosts coding while degrading general NL skills, a concrete trade-off that Lemur’s harmonized instruction mixture is designed to fix.

### 📊 Baseline

**Code Llama: Open Foundation Models for Code** (2023)
- *Authors:* Baptiste Rozière et al.
- *Direct Connection:* As a state-of-the-art open code-pretrained baseline that excels at coding but lags in general language, Code Llama concretely defines the code–chat trade-off Lemur addresses via code-intensive pretraining without sacrificing natural language ability.

**Llama 2: Open Foundation and Fine-Tuned Chat Models** (2023)
- *Authors:* Hugo Touvron et al.
- *Direct Connection:* Llama-2-Chat serves as the strong NL-aligned baseline that is comparatively weak on code/tool use, providing the opposite pole that Lemur bridges through joint text+code instruction tuning.

### 🔧 Extension

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* The self-instruct pipeline for creating diverse instruction-following data is directly extended by Lemur to co-curate balanced text and code instructions for alignment without over-specializing.

### 🔗 Related Problem

**Toolformer: Language Models Can Teach Themselves to Use Tools** (2023)
- *Authors:* Timo Schick et al.
- *Direct Connection:* Toolformer’s self-supervised learning of API calls from raw text informs Lemur’s mixed text+code supervision to ground language responses in executable, tool-using behaviors.

---

## Synthesis: How Prior Work Led to This Paper

ReAct established a language-agent paradigm where models interleave natural-language reasoning with concrete actions via tool or API calls, defining the need for systems that fluently move between explanation and execution. PAL demonstrated that delegating intermediate steps to generated Python code and executing them yields large gains on reasoning tasks, isolating code generation as a key mechanism for stronger problem solving. Toolformer showed language models can learn API-calling behaviors from text-only corpora via self-supervision, indicating that mixed supervision on language and tool-use traces can ground responses in executable actions. Code Llama revealed that large-scale code-centric pretraining produces excellent coding ability but tends to erode general language competence. Conversely, Llama-2-Chat highlighted that instruction alignment for dialogue yields strong natural-language skills but comparatively weak coding and tool-use. WizardCoder pushed code instruction tuning with evol-instruct, boosting coding benchmarks while noticeably hurting general NL performance. Self-Instruct provided a practical recipe to synthesize diverse instruction-following data at scale, enabling targeted alignment beyond purely human-written prompts.

Together, these works expose a consistent opportunity: code-focused training improves tool use and reasoning but sacrifices dialogue and generalization, while chat alignment does the opposite. The natural next step is to harmonize these strengths by combining code-intensive pretraining with a carefully balanced instruction mixture spanning both text and code, leveraging self-instruct style generation and tool-use traces to preserve alignment while retaining executable competence—precisely the synthesis that enables a single backbone model to reason, plan, and act as a versatile language agent.

---

*Analysis generated on: 2026-01-06T15:06:47.824720*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

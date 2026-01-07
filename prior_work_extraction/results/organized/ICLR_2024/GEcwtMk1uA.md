# Prior Work Analysis Report

## Target Paper

**Title:** Identifying the Risks of LM Agents with an LM-Emulated Sandbox

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, Tatsunori Hashimoto

**Keywords:** Language Model Agent, Tool Use, Evaluation, Safety, Language Model

**Abstract:** 
> Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but also amplify potential risks—such as leaking private data or causing financial losses. Identifying these risks is labor-intensive, necessitating implementing the tools, setting up the environment for each test scenario manually, and finding risky cases. As tools and agents become more complex, the high cost of testing these agents will make it increa...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**ReAct: Synergizing Reasoning and Acting in Language Models** (2022)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* ReAct established the thought–action–observation paradigm for LM tool use, whose structured tool-call traces are precisely the interaction format ToolEmu emulates to test agents without executing real tools.

**Toolformer: Language Models Can Teach Themselves to Use Tools** (2023)
- *Authors:* Timo Schick et al.
- *Direct Connection:* Toolformer formalized API-style tool invocation and schemas for LM tool use, providing the concrete tool-call interfaces that ToolEmu emulates instead of integrating and running actual APIs.

### 💡 Inspiration

**Discovering Language Model Behaviors with Model-Written Evaluations** (2022)
- *Authors:* Ethan Perez et al.
- *Direct Connection:* This work showed that LMs can generate targeted test cases that reveal failure modes, directly inspiring ToolEmu’s use of an LM to emulate tools and surface risky agent behaviors at scale.

### 🔍 Gap Identification

**WebArena: A Realistic Web Environment for Building Autonomous Agents** (2023)
- *Authors:* Xiyang Zhou et al.
- *Direct Connection:* WebArena highlighted the significant engineering cost of building and maintaining realistic, instrumented environments for agent evaluation, motivating ToolEmu’s LM-emulated sandbox to avoid such setup overhead.

**ToolLLM: Facilitating Large Language Models to Use Tools with 16k APIs** (2023)
- *Authors:* Yujia Qin et al.
- *Direct Connection:* By surfacing the scale and heterogeneity of real-world APIs for LM tool use, ToolLLM underscored the impracticality of implementing thousands of tools, a limitation ToolEmu addresses via LM-based tool emulation for testing.

### 🔧 Extension

**G-Eval: NLG Evaluation Using GPT-4 with Better Human Alignment** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* G-Eval demonstrated rubric-guided LLM-as-a-judge evaluation, which ToolEmu extends by designing an LM-based safety evaluator that diagnoses agent failures and assigns risk severities.

---

## Synthesis: How Prior Work Led to This Paper

ReAct introduced a structured loop where language models interleave reasoning with tool calls and consume observations, defining the thought–action–observation traces that concretize how agents interact with external tools. Toolformer further operationalized LM tool use as API-style function calls with explicit schemas, showing that models can decide when and how to invoke tools through standardized interfaces. G-Eval established that large models can serve as rubric-driven judges to evaluate outputs reliably, providing a template for systematic, criteria-based assessments. Perez et al. showed that models can write evaluations to uncover failure modes, demonstrating that LMs can not only be subjects but also instruments for discovering risky behaviors. WebArena built a realistic web environment for agent testing, revealing the heavy engineering burden and maintenance cost of realistic sandboxes. ToolLLM scaled tool-use to 16k APIs, exposing the breadth and diversity of interfaces that make exhaustive, implementation-based testing infeasible.
Together, these works reveal a gap: agents increasingly act through diverse tools, yet constructing and maintaining faithful, real tool environments is costly, and exhaustive risk discovery is hard. The natural synthesis is to replace environment and tool implementations with an LM that emulates tool behavior in the ReAct/Toolformer schema, and to pair it with an LLM-as-judge safety assessor in the spirit of G-Eval and model-written evaluations. ToolEmu emerges as this step—using LM emulation to scalably surface long-tail risky trajectories across many tools, and an LM evaluator to diagnose and quantify the associated safety risks.

---

*Analysis generated on: 2026-01-06T13:22:42.969880*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

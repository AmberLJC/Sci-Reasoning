# Prior Work Analysis Report

## Target Paper

**Title:** A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis

**Conference:** ICLR 2024 (oral)

**Authors:** Izzeddin Gur, Hiroki Furuta, Austin V Huang, Mustafa Safdari, Yutaka Matsuo, Douglas Eck, Aleksandra Faust

**Keywords:** Web Navigation, Web Automation, Large Language Models, Language Model Agents, Tool Use, Program Synthesis

**Abstract:** 
> Pre-trained large language models (LLMs) have recently achieved better generalization and sample efficiency in autonomous web automation.
However, the performance on real-world websites has still suffered from (1) open domainness, (2) limited context length, and (3) lack of inductive bias on HTML.
We introduce WebAgent, an LLM-driven agent that learns from self-experience to complete tasks on real websites following natural language instructions.
WebAgent plans ahead by decomposing instructions ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Mind2Web: Towards a Generalist Agent for the Web** (2023)
- *Authors:* Shuyan Zhou et al.
- *Direct Connection:* WebAgent targets the Mind2Web problem formulation of cross-website instruction following and evaluates/trains in that setup, motivating its planning and long-context HTML modules.

### 💡 Inspiration

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* WebAgent operationalizes ReAct’s interleaving of reasoning and acting by first producing explicit canonical sub-instructions that structure its planner before execution.

**Do As I Can, Not As I Say: Grounding Language in Robotic Affordances** (2022)
- *Authors:* Michael Ahn et al.
- *Direct Connection:* WebAgent adopts SayCan’s separation of high-level language plans from grounded low-level skills, mapping sub-instructions to callable browser primitives with feasibility checks.

### 🔍 Gap Identification

**WebGPT: Browser-assisted Question-Answering with Human Feedback** (2021)
- *Authors:* Reiichiro Nakano et al.
- *Direct Connection:* WebAgent addresses WebGPT’s limitations—textual browsing actions and context bloat—by replacing free-form actions with code-based execution and adding long-HTML summarization for grounding.

### 🔧 Extension

**PAL: Program-Aided Language Models** (2023)
- *Authors:* Luyu Gao et al.
- *Direct Connection:* WebAgent extends PAL’s executable-Python paradigm by synthesizing grounded browser-control programs that call a DOM/interaction API to perform web actions.

**LongT5: Efficient Text-to-Text Transformer for Long Sequences** (2022)
- *Authors:* Mandy Guo et al.
- *Direct Connection:* WebAgent’s HTML-T5 directly builds on LongT5’s local+global attention and long-span denoising, retraining the recipe on HTML to summarize long DOM pages into task-relevant snippets.

---

## Synthesis: How Prior Work Led to This Paper

ReAct demonstrated that large language models can be more effective tool users when their internal deliberation is externalized as explicit thought–action traces, showing the value of decomposing a task into intermediate steps before each action. PAL showed that having the model generate executable Python to call tools yields reliable, verifiable problem solving, establishing code generation as a robust control interface. SayCan introduced a separation between high-level language plans and grounded low-level skills, with an affordance check that constrains execution to feasible actions. LongT5 provided an architectural and training recipe—local and global attention with long-span denoising—that scales text-to-text models to very long inputs, enabling faithful summarization over long sequences. WebGPT pioneered browser-augmented LMs for web tasks but relied on free-form textual actions and suffered from long-context accumulation on open websites. Mind2Web formalized generalist web instruction following across diverse real sites, with multi-step trajectories and DOM-grounded actions that stress both planning and long-HTML understanding. Together, these works revealed a gap: real-web automation needs explicit multi-step planning, long-context HTML comprehension, and grounded, verifiable execution. WebAgent synthesizes these threads by turning ReAct-style stepwise reasoning into canonical sub-instructions (à la SayCan’s plan/skill split), using a LongT5-inspired HTML-T5 to condense long DOMs into task-relevant snippets, and extending PAL’s executable-code control to synthesize Python programs that call browser/DOM APIs—directly addressing the shortcomings observed in WebGPT and meeting the Mind2Web-style generalist setting.

---

*Analysis generated on: 2026-01-06T22:40:43.713783*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

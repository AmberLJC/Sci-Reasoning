# Prior Work Analysis Report

## Target Paper

**Title:** From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions

**Conference:** ICLR 2025 (oral)

**Authors:** Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, Ji-Rong Wen

**Keywords:** Large Language Model, Tool Learning, Learning from Experience

**Abstract:** 
> Tool learning enables Large Language Models (LLMs) to interact with external environments by invoking tools, serving as an effective strategy to mitigate the limitations inherent in their pre-training data. In this process, tool documentation plays a crucial role by providing usage instructions for LLMs, thereby facilitating effective tool utilization. This paper concentrates on the critical challenge of bridging the comprehension gap between LLMs and external tools due to the inadequacies and i...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**ToolLLM: Facilitating Large Language Models to Use Tools with Human Feedback** (2023)
- *Authors:* Qin et al.
- *Direct Connection:* DRAFT adopts the ToolLLM/ToolBench problem setting of invoking real-world APIs via human-written documentation and directly targets its documented brittleness by replacing static docs with ones dynamically rewritten from interaction feedback.

### 💡 Inspiration

**Toolformer: Language Models Can Teach Themselves to Use Tools** (2023)
- *Authors:* Schick et al.
- *Direct Connection:* Toolformer’s self-supervised, trial-and-error use of tool calls to generate supervision directly inspires DRAFT’s experience-gathering phase, but DRAFT channels the feedback signal to update tool documentation rather than only labeling training data.

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Yao et al.
- *Direct Connection:* DRAFT leverages ReAct-style trajectories—interleaving thoughts, actions, and observations—to collect fine-grained tool feedback that is later analyzed to rewrite and clarify documentation.

### 🔍 Gap Identification

**Gorilla: Large Language Model Connected with Massive APIs** (2023)
- *Authors:* Patil et al.
- *Direct Connection:* By showing that retrieval over static API docs still yields API hallucinations and mismatches, Gorilla exposes the doc-quality bottleneck that DRAFT addresses by refining the documentation itself using execution feedback.

### 🔧 Extension

**Reflexion: Language Agents with Verbal Reinforcement Learning** (2023)
- *Authors:* Shinn et al.
- *Direct Connection:* Reflexion’s mechanism for turning past failures into concise self-feedback is extended in DRAFT by aggregating such reflections over tool failures and converting them into persistent edits to the tool docs.

**Self-Refine: Iterative Refinement with Self-Feedback** (2023)
- *Authors:* Madaan et al.
- *Direct Connection:* Self-Refine’s generate–critique–edit loop directly informs DRAFT’s documentation rewriting module, which treats tool execution signals as critiques and performs iterative doc edits to prevent repeated misuse.

---

## Synthesis: How Prior Work Led to This Paper

Work on tool-augmented LLMs established that real-world API invocation is guided by human-written documentation and interaction traces. ToolLLM formalized this setting at scale with ToolBench, showing that models rely heavily on natural-language docs to choose parameters and endpoints, while supervision can be harvested from tool interaction outcomes. Gorilla tackled API selection by retrieving documentation at generation time and highlighted that even with retrieval, ambiguous or mismatched docs induce API hallucinations, underscoring documentation quality as a key bottleneck. Toolformer demonstrated that LMs can self-supervise by probing tools and keeping beneficial calls, revealing that execution feedback is a rich learning signal obtainable without manual labels. ReAct introduced trajectories that interleave reasoning with actions and observations, providing a structured way to capture granular tool feedback during trial-and-error. Reflexion showed that agents can distill failures into verbal guidance that improves future attempts, and Self-Refine operationalized this by turning critiques into concrete text edits through an iterative generate–critique–edit loop.
Seen together, these works suggest a natural opportunity: if execution feedback is plentiful (Toolformer, ReAct) and textual self-critiques can be turned into durable edits (Reflexion, Self-Refine), then the most brittle component identified by large-scale tool use (ToolLLM, Gorilla)—the human-centric, static documentation—should itself be the object of learning. The present work synthesizes these insights by harvesting ReAct-style interaction traces, extracting Reflexion-like failure analyses, and iteratively editing the documentation in a Self-Refine fashion, closing the loop so that experience directly improves the tool specifications that future interactions depend on.

---

*Analysis generated on: 2026-01-06T12:49:32.276051*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

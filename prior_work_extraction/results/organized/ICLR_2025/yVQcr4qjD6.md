# Prior Work Analysis Report

## Target Paper

**Title:** Robust Function-Calling for On-Device Language Model via Function Masking

**Conference:** ICLR 2025 (spotlight)

**Authors:** Qiqiang Lin, Muning Wen, Qiuying Peng, Guanyu Nie, Junwei Liao, Jun Wang, Xiaoyun Mo, Jiamu Zhou, Cheng Cheng, Yin Zhao, Jun Wang, Weinan Zhang

**Keywords:** language models, function-calling, mobile assistant, tool-using

**Abstract:** 
> Large language models have demonstrated impressive value in performing as autonomous agents when equipped with external tools and API calls. Nonetheless, effectively harnessing their potential for executing complex tasks crucially relies on enhancements in their function-calling capabilities. This paper identifies a critical gap in existing function-calling models, where performance varies significantly across benchmarks, often due to over-fitting to specific naming conventions. To address such ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**ToolLLM: Facilitating Large Language Models to Use Tools with Step-by-Step Instructions** (2023)
- *Authors:* Qin et al.
- *Direct Connection:* Hammer adopts ToolLLM’s JSON-schema–based function-calling formulation and instruction-tuning setup, then extends it with name-masking and distractor-tool augmentation explicitly to curb name-based overfitting.

**API-Bank: A Scalable Benchmark for Real-World Tool-Use of Large Language Models** (2023)
- *Authors:* Li et al.
- *Direct Connection:* Hammer is motivated by API-Bank’s heterogeneous, multi-provider API evaluations that expose variance driven by naming conventions, prompting the paper’s robustness-oriented masking and augmentation strategy.

### 💡 Inspiration

**Toolformer: Language Models Can Teach Themselves to Use Tools** (2023)
- *Authors:* Timo Schick et al.
- *Direct Connection:* Toolformer’s synthetic supervision for tool-use inspired Hammer’s data-centric strategy, which repurposes synthetic augmentation toward robustness by inserting distractor tools and masking function identifiers during finetuning.

### 🔍 Gap Identification

**AgentBench: Evaluating LLMs as Agents** (2023)
- *Authors:* Xiao Liu et al.
- *Direct Connection:* AgentBench documented substantial performance swings across tool-use tasks and settings, directly motivating Hammer’s goal of reducing cross-benchmark variance through naming-invariant training and function masking.

### 📊 Baseline

**Gorilla: Large Language Model Connected with Massive APIs** (2023)
- *Authors:* Shishir G. Patil et al.
- *Direct Connection:* Hammer targets the same API/function-calling task as Gorilla and directly addresses Gorilla’s observed brittleness to API name/signature changes by masking function identifiers and training with irrelevant function distractors to improve cross-API generalization.

### 🔗 Related Problem

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* By framing tool-use as selective acting interleaved with reasoning, ReAct highlighted the need for precise tool selection in the presence of many tools, which Hammer strengthens by suppressing spurious name cues via function masking and irrelevant-tool negatives.

---

## Synthesis: How Prior Work Led to This Paper

Gorilla demonstrated that connecting LLMs to large API sets enables precise function invocation but also revealed brittle behavior when API signatures or names change, and it formalized evaluation with realistic API specifications. ToolLLM established a practical function-calling formulation using JSON schemas and instruction-tuning that operationalizes tool descriptions and structured arguments, but its realistic datasets can inadvertently encourage memorization of function names. API-Bank assembled diverse, multi-provider APIs and tasks, surfacing large performance swings across benchmarks and highlighting how naming conventions and distractor tools confound selection. ReAct showed that effective tool-use depends on deciding when and which tool to call amid many possibilities, making robustness to superficial cues critical for reliable acting. Toolformer introduced a powerful data-centric lens—synthetic supervision for teaching tool-use—which suggested that targeted augmentation could shape model behavior beyond scaling alone. AgentBench systematically exposed volatility in agent performance across tasks and environments, underlining the need for methods that generalize beyond specific benchmarks. Taken together, these works revealed that while structured function-calling and synthetic supervision enable capable tool use, models remain vulnerable to spurious correlations with tool names and to distractor functions. Hammer synthesizes these insights by retaining the structured JSON function-calling paradigm while reorienting supervision toward robustness: it augments data with irrelevant tool distractors and applies function masking to remove name cues, thereby training naming-invariant selection behavior that reduces cross-benchmark variance and improves on-device reliability.

---

*Analysis generated on: 2026-01-06T16:16:51.127236*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

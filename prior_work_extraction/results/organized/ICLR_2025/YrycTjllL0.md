# Prior Work Analysis Report

## Target Paper

**Title:** BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions

**Conference:** ICLR 2025 (oral)

**Authors:** Terry Yue Zhuo, Vu Minh Chien, Jenny Chim, Han Hu, Wenhao Yu, Ratnadira Widyasari, Imam Nur Bani Yusuf, Haolan Zhan, Junda He, Indraneil Paul, Simon Brunner, Chen GONG, James Hoang, Armel Randy Zebaze, Xiaoheng Hong, Wen-Ding Li, Jean Kaddour, Ming Xu, Zhihan Zhang, Prateek Yadav, Naman Jain, Alex Gu, Zhoujun Cheng, Jiawei Liu, Qian Liu, Zijian Wang, Binyuan Hui, Niklas Muennighoff, David Lo, Daniel Fried, Xiaoning Du, Harm de Vries, Leandro Von Werra

**Keywords:** Code Generation, Tool Use, Instruction Following, Benchmark

**Abstract:** 
> Task automation has been greatly empowered by the recent advances in Large Language Models (LLMs) via Python code, where the tasks range from software engineering development to general-purpose reasoning. While current benchmarks have shown that LLMs can solve tasks using programs like human developers, the majority of their evaluations are limited to short and self-contained algorithmic tasks or standalone function calls. Solving challenging and practical tasks requires the capability of utiliz...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**PAL: Program-Aided Language Models** (2023)
- *Authors:* Luyu Gao et al.
- *Direct Connection:* PAL showed that generating and executing Python programs improves task solving, providing the foundational idea that practical tasks can be assessed via code execution which BigCodeBench generalizes to diverse tool libraries.

### 💡 Inspiration

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* ReAct’s coupling of deliberate reasoning with tool actions directly inspires BigCodeBench’s emphasis on compositional multi-tool use, now instantiated through executable Python function calls.

### 🔍 Gap Identification

**Evaluating Large Language Models Trained on Code** (2021)
- *Authors:* Mark Chen et al.
- *Direct Connection:* HumanEval established execution-based evaluation for text-to-code but confines tasks to short, self-contained functions, directly motivating BigCodeBench’s shift to multi-library, multi-call code under complex instructions.

**Program Synthesis with Large Language Models** (2021)
- *Authors:* Jacob Austin et al.
- *Direct Connection:* MBPP’s simple prompts and single-function Python solutions highlighted the lack of instruction complexity and real-world library usage that BigCodeBench explicitly targets.

**APPS: A Benchmark for Code Generation** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* APPS scales difficulty but largely measures algorithmic problem solving rather than composing heterogeneous library calls, a key gap BigCodeBench fills.

### 🔗 Related Problem

**Gorilla: Large Language Models Are Connected with Massive APIs** (2023)
- *Authors:* Shishir G. Patil et al.
- *Direct Connection:* Gorilla framed API-call generation and grounding to function signatures, which BigCodeBench extends by evaluating composition across multiple real-world Python libraries under complex instructions.

**AgentBench: Evaluating LLMs as Agents** (2023)
- *Authors:* Xiao Liu et al.
- *Direct Connection:* AgentBench’s multi-tool agent evaluation highlighted the need to measure instruction following and tool orchestration, informing BigCodeBench’s code-centric, execution-based assessment of multi-tool composition.

---

## Synthesis: How Prior Work Led to This Paper

HumanEval introduced the now-standard paradigm of execution-based evaluation for text-to-code generation but centered on short, self-contained function implementations, while MBPP similarly focused on simple prompts and single-function Python solutions. APPS broadened difficulty and scale yet primarily measured algorithmic problem solving rather than realistic composition over heterogeneous libraries. ReAct demonstrated that interleaving explicit reasoning with tool actions enables multi-step, tool-using behavior, crystallizing the importance of tool orchestration. PAL showed that generating and executing Python programs can materially improve task performance, grounding the idea that code itself can be the medium of problem solving. Gorilla reframed evaluation around correct API invocation and grounding to actual function signatures, pushing attention to real-world interfaces rather than abstract algorithms. AgentBench expanded this lens to agentic settings with multiple tools, emphasizing instruction following and complex task decomposition over single-step calls.

Taken together, these works revealed a clear opportunity: existing code benchmarks lack diverse, compositional tool use under complex, natural instructions, even as tool-oriented reasoning and execution prove crucial. The natural next step is a benchmark that uses executable Python as the action language, requires composing multiple real-world libraries, and evaluates strict instruction adherence through unit-testable outcomes. Building on execution-based evaluation (HumanEval/MBPP/APPS), tool-augmented reasoning (ReAct/PAL), and API-grounded correctness (Gorilla) in multi-tool contexts (AgentBench), BigCodeBench synthesizes these strands to assess how well LLMs can follow complex instructions and orchestrate diverse function calls to solve practical tasks.

---

*Analysis generated on: 2026-01-06T15:05:59.970404*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

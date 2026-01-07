# Prior Work Analysis Report

## Target Paper

**Title:** Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models

**Conference:** ICLR 2025 (oral)

**Authors:** Andy K Zhang, Neil Perry, Riya Dulepet, Joey Ji, Celeste Menders, Justin W Lin, Eliot Jones, Gashon Hussein, Samantha Liu, Donovan Julian Jasper, Pura Peetathawatchai, Ari Glenn, Vikram Sivashankar, Daniel Zamoshchin, Leo Glikbarg, Derek Askaryar, Haoxiang Yang, Aolin Zhang, Rishi Alluri, Nathan Tran, Rinnara Sangpisit, Kenny O Oseleononmen, Dan Boneh, Daniel E. Ho, Percy Liang

**Keywords:** Language Model Agents, Benchmark, Cybersecurity, Risk

**Abstract:** 
> Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have potential to cause real-world impact. Policymakers, model providers, and researchers in the AI and cybersecurity communities are interested in quantifying the capabilities of such agents to help mitigate cyberrisk and investigate opportunities for penetration testing. Toward that end, we introduce Cybench, a framework for specifying cybersecurity tasks and evaluat...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**ReAct: Synergizing Reasoning and Acting in Language Models** (2022)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* Cybench adopts the ReAct-style formulation of tool-using agents that interleave reasoning with executing commands, which underpins its evaluation of LM agents that operate terminals to solve cybersecurity tasks.

**AgentBench: Evaluating LLMs as Agents** (2023)
- *Authors:* Xiao Liu et al.
- *Direct Connection:* AgentBench’s standardized, multi-environment agent evaluation directly informed Cybench’s benchmark design for assessing end-to-end agent performance with tool access and observable action traces.

**HELM: Holistic Evaluation of Language Models** (2022)
- *Authors:* Percy Liang et al.
- *Direct Connection:* HELM’s evaluation principles and emphasis on capability–risk assessment informed Cybench’s framing of cybersecurity as a high-stakes capability area requiring careful, standardized measurement.

### 💡 Inspiration

**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** (2023)
- *Authors:* Jimenez et al.
- *Direct Connection:* SWE-bench’s use of realistic, self-contained tasks with starter artifacts and automated scoring inspired Cybench’s packaging of CTF challenges in containerized environments and its introduction of intermediate subtasks when full-task solve rates are low.

### 🔍 Gap Identification

**Purple Llama: CyberSecEval** (2023)
- *Authors:* Meta AI et al.
- *Direct Connection:* CyberSecEval’s focus on prompt-based and code-generation security risks highlighted the lack of end-to-end, interactive cybersecurity capability evaluations, a gap Cybench addresses with executable CTF tasks.

### 📊 Baseline

**PentestGPT: An LLM-empowered Penetration Testing Tool** (2023)
- *Authors:* Zhu et al.
- *Direct Connection:* PentestGPT demonstrated LM-driven penetration testing workflows on CTF-like problems, providing a primary baseline system and motivating Cybench’s need for a standardized, reproducible evaluation harness.

---

## Synthesis: How Prior Work Led to This Paper

ReAct introduced a concrete agent paradigm where language models iteratively reason and act with external tools, establishing the blueprint for evaluating agents that must operate terminals and parse tool outputs. AgentBench generalized this notion into a standardized, multi-environment protocol for agent evaluation, emphasizing reproducibility, transparent action traces, and comparable metrics across tasks. SWE-bench showed how to build realistic, self-contained tasks with starter artifacts and automated scoring, and crucially revealed that fully end-to-end tasks can outstrip current model capabilities, motivating the use of intermediate subtasks to capture partial progress. Purple Llama’s CyberSecEval concentrated attention on cybersecurity risks in text and code generation, but did so without interactive, execution-driven tasks, thereby crystallizing a gap between prompt-level safety checks and real operational cyber capabilities. PentestGPT demonstrated the feasibility of LM-driven penetration testing on CTF-style problems, yet lacked a standardized, robust benchmark that could fairly and reproducibly compare such agents. HELM provided a principled framework for holistic, risk-aware evaluation, underscoring the need for careful measurement in high-stakes domains like cybersecurity. Together, these works suggested a clear opportunity: fuse ReAct-style tool use with AgentBench and SWE-bench methodology to create realistic, containerized CTF environments; cover the capability–risk axis emphasized by HELM; and address CyberSecEval’s interactivity gap while providing PentestGPT-like systems a rigorous yardstick. Cybench emerges as the natural synthesis—an execution-grounded benchmark with subtasks that quantifies LM-agent cybersecurity capabilities and associated risks on professional-level challenges.

---

*Analysis generated on: 2026-01-06T19:28:47.270488*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

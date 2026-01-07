# Prior Work Analysis Report

## Target Paper

**Title:** SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jingxuan Chen, Derek Yuen, Bin Xie, Yuhao Yang, Gongwei Chen, Zhihao Wu, Li Yixing, Xurui Zhou, Weiwen Liu, Shuai Wang, Kaiwen Zhou, Rui Shao, Liqiang Nie, Yasheng Wang, Jianye HAO, Jun Wang, Kun Shao

**Keywords:** AI Agent, LLM, MLLM, Benchmark, Smartphone Control

**Abstract:** 
> Smartphone agents are increasingly important for helping users control devices efficiently, with (Multimodal) Large Language Model (MLLM)-based approaches emerging as key contenders. Fairly comparing these agents is essential but challenging, requiring a varied task scope, the integration of agents with different implementations, and a generalisable evaluation pipeline to assess their strengths and weaknesses. In this paper, we present SPA-Bench, a comprehensive SmartPhone Agent Benchmark design...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**AndroidEnv: A Reinforcement Learning Platform for Android** (2021)
- *Authors:* Zhou et al.
- *Direct Connection:* AndroidEnv introduced an instrumented Android emulator with programmatic input/output and logging, which SPA-Bench builds upon to create a reproducible, interactive smartphone environment for agent evaluation.

**AgentBench: Evaluating LLMs as Agents** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* AgentBench demonstrated standardized integration of diverse LLM agents under a common API, directly motivating SPA-Bench’s plug‑and‑play framework that unifies more than ten smartphone agents under one interface.

### 💡 Inspiration

**WebArena: A Realistic Web Environment for Building Autonomous Agents** (2023)
- *Authors:* Zhou et al.
- *Direct Connection:* WebArena’s design of realistic tasks with automatic success checkers and a pluggable agent interface inspired SPA-Bench’s mobile counterpart, which adapts these checker and adapter ideas to the smartphone OS context.

### 🔍 Gap Identification

**OSWorld: A Benchmark for Generalist Computer Control Agents** (2024)
- *Authors:* Xu et al.
- *Direct Connection:* OSWorld highlighted the feasibility of automatic, programmatic evaluation for desktop UI agents while lacking coverage of mobile ecosystems, a gap SPA-Bench fills by focusing on system and third‑party smartphone apps with bilingual tasks.

### 📊 Baseline

**AppAgent: Multimodal Agents for Mobile App Automation** (2024)
- *Authors:* Zhang et al.
- *Direct Connection:* AppAgent established the (M)LLM-driven smartphone control paradigm using screenshots and accessibility trees, and SPA-Bench integrates AppAgent as a plug-in baseline while addressing its ad‑hoc, app‑specific evaluation by providing a standardized, multi‑app benchmark.

**AutoDroid: LLM-Powered Task Automation for Android** (2024)
- *Authors:* Liu et al.
- *Direct Connection:* AutoDroid proposed planning- and tool-driven LLM agents for Android but evaluated them on narrow or proprietary suites, a limitation SPA-Bench directly targets by offering broad, multilingual tasks and a unified evaluation pipeline.

---

## Synthesis: How Prior Work Led to This Paper

AndroidEnv established the feasibility of evaluating agents in a fully instrumented Android emulator, providing programmatic control, observability, and reproducibility crucial for interactive UI tasks. AppAgent showed that multimodal agents can reliably operate mobile apps by combining screenshots with accessibility trees and step‑wise reasoning, but it assessed performance with task‑specific setups. AutoDroid advanced LLM planning and tool usage for Android automation, yet remained confined to relatively narrow or proprietary task suites that limited fair cross‑agent comparison. In parallel, WebArena demonstrated that agent benchmarks benefit from realistic environments, automatic success checkers, and a pluggable interface that lets many agents be evaluated under identical conditions. AgentBench generalized this idea for LLM agents, proposing standardized adapters so heterogeneous systems can be compared fairly across tasks. OSWorld extended automatic evaluation to desktop OS control, offering granular checkers and outcomes, while leaving mobile ecosystems underexplored despite their distinct input modalities, app distributions, and multilingual usage. Collectively, these works reveal both the practicality and the missing pieces for a comprehensive smartphone benchmark: a reproducible Android environment, standardized agent adapters, realistic multi‑app tasks, and automatic evaluators. Synthesizing these insights, SPA-Bench builds a plug‑and‑play framework that integrates diverse (M)LLM smartphone agents, scales task coverage across system and third‑party apps in English and Chinese, and adapts WebArena/OSWorld‑style automatic checkers to mobile device control, enabling fair, generalizable comparison at scale.

---

*Analysis generated on: 2026-01-06T16:10:31.680380*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

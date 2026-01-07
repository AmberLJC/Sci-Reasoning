# Prior Work Analysis Report

## Target Paper
**Title:** 4tFSKOY2mT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**TextWorld: A Learning Environment for Text-Based Games** (2018)
- *Authors:* Marc-Alexandre Côté et al.
- *Connection:* TextWorld’s procedural generation of quests via explicit dependency graphs directly underpins OmniBench’s graph-based subtask composition, enabling controllable task complexity without heavy manual labeling.

### 💡 Inspiration

**BabyAI: A Platform to Study the Sample Efficiency of Grounded Language Learning** (2019)
- *Authors:* Maxime Chevalier-Boisvert et al.
- *Connection:* BabyAI’s compositional task design and curriculum with tunable difficulty inspired OmniBench’s controllable-complexity synthesis and subtask-level capability evaluation.

**Procgen Benchmark: Procedurally-Generated Game-Like Tasks for Robust Reinforcement Learning** (2020)
- *Authors:* Karl Cobbe et al.
- *Connection:* Procgen’s demonstration that procedural generation yields robust generalization directly motivates OmniBench’s automated pipeline for synthesizing large, diverse task sets with controllable difficulty.

### 🔍 Gap Identification

**ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks** (2020)
- *Authors:* Mohit Shridhar et al.
- *Connection:* ALFRED’s reliance on substantial human annotation and limited fine-grained capability scoring exposed the need for OmniBench’s automated synthesis and multidimensional, subtask-level evaluation.

**WebArena: A Realistic Open Web Environment for Building Autonomous Agents** (2023)
- *Authors:* Zhou et al.
- *Connection:* WebArena’s realistic but manually curated, variably difficult web tasks highlight the scalability and controllability gap that OmniBench addresses with its self-generating, graph-structured tasks across many scenarios.

### 📊 Baseline

**AgentBench: Evaluating LLMs as Agents** (2023)
- *Authors:* Liu et al.
- *Connection:* As a primary prior benchmark for LLM agents, AgentBench motivates OmniBench’s improvements by lacking controllable task complexity and explicit capability decomposition that OmniBench provides via graph-based generation and OmniEval.

### 🔧 Extension

**VirtualHome: Simulating Household Activities via Programs** (2018)
- *Authors:* Xavier Puig et al.
- *Connection:* OmniBench extends VirtualHome’s idea of representing tasks as programs/action-graphs beyond a single domain, using graph-structured subtasks to compose diverse virtual-agent tasks and define graph-based metrics.

---

## Synthesis

OmniBench’s core innovation—a self-generating, graph-based benchmark with controllable complexity and multidimensional evaluation—arises from a clear intellectual lineage in procedural, compositional task design and agent evaluation. TextWorld established the foundational idea of encoding tasks as dependency graphs, showing how quests can be procedurally composed and difficulty controlled without heavy annotation; OmniBench generalizes this graph-centric principle to multimodal virtual agents. BabyAI’s compositional curricula and tunable difficulty directly inspired OmniBench’s subtask-level capability design and controllable complexity knobs. VirtualHome contributed the notion that everyday activities can be represented as executable programs/action graphs; OmniBench extends this program-graph representation across many scenarios and layers graph-based metrics on top.

At the same time, several benchmarks exposed critical gaps that OmniBench explicitly addresses. ALFRED demonstrated the cost of extensive human annotation and the need for fine-grained capability scoring, which OmniBench meets via automated synthesis and OmniEval’s subtask and graph metrics. AgentBench served as a baseline multi-environment evaluation for LLM agents but lacked controllable complexity and systematic capability decomposition—precisely the axes OmniBench formalizes. WebArena offered realistic web interactions but required manual curation and suffered from uneven difficulty, motivating OmniBench’s scalable, controllable generation across 20 scenarios. Finally, Procgen’s success with procedural generation for robust generalization inspired OmniBench’s automated pipeline, enabling 36k graph-structured tasks and improved cross-environment generalization.

---
*Generated: 2026-01-06T23:07:19.632455*

# Prior Work Analysis Report

## Target Paper
**Title:** 5xPvWat3IX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations** (2017)
- *Authors:* Ranjay Krishna et al.
- *Connection:* Vgent’s representation of videos as nodes and semantic relations builds on the scene-graph paradigm introduced by Visual Genome, extending it to temporal clip-level relations for retrieval.

**MovieQA: Understanding Stories in Movies through Question-Answering** (2016)
- *Authors:* Makarand Tapaswi et al.
- *Connection:* By formalizing long-form movie understanding as QA and exposing the need for long-range reasoning, MovieQA sets the problem context that Vgent targets with graph-structured retrieval and intermediate reasoning.

### 💡 Inspiration

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Connection:* Vgent’s plan–retrieve–reason loop is directly inspired by ReAct’s interleaving of reasoning traces with tool use, here instantiating the ‘act’ step as graph-based video retrieval to guide LVLM reasoning.

**Learning to Retrieve Reasoning Paths over Wikipedia Graph for Question Answering** (2019)
- *Authors:* Akari Asai et al.
- *Connection:* The core notion of retrieving along structured multi-hop paths informs Vgent’s construction of video graphs and retrieval of clip chains that preserve temporal and semantic dependencies.

**Graph of Thoughts: Solving Elaborate Problems with Large Language Models** (2024)
- *Authors:* Maciej Besta et al.
- *Connection:* Vgent’s idea of structuring intermediate reasoning and evidence around graph relationships echoes Graph-of-Thoughts’ graph-structured reasoning, adapted here to video clips and relations.

### 📊 Baseline

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Connection:* Vgent inherits the RAG formulation—separating retrieval and generation—but shows that flat passage retrieval disrupts temporal dependencies in long videos, directly motivating its graph-structured video retrieval and added reasoning step.

### 🔧 Extension

**Self-RAG: Learning to Retrieve, Generate, and Critique for Improved Language Modeling** (2023)
- *Authors:* Akari Asai et al.
- *Connection:* Vgent extends Self-RAG’s idea of an intermediate, self-reflective reasoning stage by adapting it to LVLMs and coupling the reasoning stage with a structured graph retriever over video clips.

---

## Synthesis

Vgent fuses two lines of progress to address long video understanding: retrieval-augmented generation and graph-structured reasoning. The RAG framework of Lewis et al. established the core separation of retrieval and generation, but its flat passage retrieval struggles with long-range, ordered dependencies—precisely the failure mode Vgent targets in videos. To make retrieval reasoning-aware, Vgent draws on Self-RAG’s intermediate critique/planning stage and ReAct’s interleaving of reasoning and tool-use, instantiating the ‘tool’ as a graph retriever over video clips so the LVLM can plan what to fetch before answering. The decision to represent videos as graphs is grounded in the scene-graph paradigm popularized by Visual Genome, extended temporally to encode clip-level entities, events, and relations. This connects tightly with Asai et al. (2019), which showed that retrieving along graph paths better supports multi-hop reasoning; Vgent applies that insight to preserve temporal and semantic links across clips, mitigating disrupted dependencies and irrelevant retrieval. MovieQA framed the core task—story-level video QA demanding global context—which motivates Vgent’s emphasis on long-horizon evidence organization. Finally, Graph-of-Thoughts inspires Vgent’s graph-centric intermediate reasoning, aligning the model’s reasoning steps with the graph structure of retrieved video evidence. Together, these works directly shape Vgent’s graph-based retrieval plus intermediate reasoning design for robust long video understanding.

---
*Generated: 2026-01-06T23:08:23.969039*

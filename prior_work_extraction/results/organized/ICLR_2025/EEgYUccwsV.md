# Prior Work Analysis Report

## Target Paper

**Title:** AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yiheng Xu, Dunjie Lu, Zhennan Shen, Junli Wang, Zekun Wang, Yuchen Mao, Caiming Xiong, Tao Yu

**Keywords:** Data Synthesis, GUI Agent, Large Language Model

**Abstract:** 
> Graphical User Interface (GUI) agents hold great potential for automating complex tasks across diverse digital environments, from web applications to desktop software. However, the development of such agents is hindered by the lack of high-quality, multi-step trajectory data required for effective training. Existing approaches rely on expensive and labor-intensive human annotation, making them unsustainable at scale. To address this challenge, we propose AgentTrek, a scalable data synthesis pipe...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**WebArena: A Realistic Web Environment for Building Autonomous Agents** (2023)
- *Authors:* Shuyan Zhou et al.
- *Direct Connection:* AgentTrek uses the realistic, DOM-accessible web environments defined by WebArena as the execution substrate to simulate and validate tutorial-derived tasks and trajectories.

### 💡 Inspiration

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2022)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* AgentTrek adopts Self-Instruct’s seed-to-scale paradigm, but substitutes LLM self-generation with mined web tutorials that are transformed into structured goals and step-by-step instructions for trajectory synthesis.

**HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips** (2019)
- *Authors:* Antoine Miech et al.
- *Direct Connection:* AgentTrek leverages the core insight from HowTo100M that large-scale web how-to content provides abundant, weakly supervised procedural signals, repurposing textual tutorials to supervise GUI action trajectories.

**LLM-as-a-Judge: Evaluating LLMs Without Ground Truth** (2023)
- *Authors:* Leo Zheng et al.
- *Direct Connection:* AgentTrek extends the LLM-as-a-judge idea to the multimodal GUI setting by employing a VLM-based evaluator to automatically verify step success and filter synthesized trajectories.

### 📊 Baseline

**Mind2Web: Towards Universal and Generalizable Web Agents** (2023)
- *Authors:* Shuyan Zhou et al.
- *Direct Connection:* AgentTrek targets Mind2Web’s reliance on costly human-authored multi-step trajectories by replacing them with tutorial-guided, VLM-executed trajectories to achieve scalable data generation.

### 🔗 Related Problem

**Workflow-Guided Exploration for Web Navigation** (2018)
- *Authors:* Quee Lim et al.
- *Direct Connection:* AgentTrek generalizes the idea of constraining web action selection using procedural text by turning tutorial step sequences into a guiding replay that anchors execution in real web interfaces.

---

## Synthesis: How Prior Work Led to This Paper

Mind2Web established the modern formulation of web agents operating across diverse websites using natural-language tasks, but its high-quality training trajectories were collected via expensive human annotation. WebArena then provided a realistic, DOM-accessible web environment spanning multiple sites, furnishing the substrate where agents could perform, observe outcomes, and be evaluated. Self-Instruct showed that large language systems can be scaled by bootstrapping from seed instructions to a large corpus of structured tasks, introducing a pragmatic recipe for instruction expansion. HowTo100M demonstrated that broad web how-to content carries rich procedural signals at scale, validating tutorials as a potent but weak form of supervision. Earlier in web navigation, workflow-guided exploration leveraged procedural/templated text to constrain exploration in browsers, indicating that textual step structures can effectively shape action search. In parallel, LLM-as-a-judge demonstrated the feasibility of automated evaluation by prompting a model to assess correctness, planting the seed for replacing brittle rule-based success checks with learned judges. Together, these works exposed a clear opportunity: human demonstrations are a bottleneck, but the web already contains procedural knowledge, and model-based evaluators can filter noisy supervision. AgentTrek synthesizes these threads by mining tutorial-like texts to form goal and step sequences, executing them with a VLM agent inside realistic web environments, and using a VLM-based judge to validate correctness—turning ambient web procedures into scalable, high-quality training trajectories for GUI agents.

---

*Analysis generated on: 2026-01-06T14:17:31.229081*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

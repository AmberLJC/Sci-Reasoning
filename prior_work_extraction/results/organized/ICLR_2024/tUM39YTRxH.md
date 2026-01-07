# Prior Work Analysis Report

## Target Paper

**Title:** Text2Reward: Reward Shaping with Language Models for Reinforcement Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Tianbao Xie, Siheng Zhao, Chen Henry Wu, Yitao Liu, Qian Luo, Victor Zhong, Yanchao Yang, Tao Yu

**Keywords:** reinforcement learning; large language models; robotics

**Abstract:** 
> Designing reward functions is a longstanding challenge in reinforcement learning (RL); it requires specialized knowledge or domain data, leading to high costs for development. To address this, we introduce Text2Reward, a data-free framework that automates the generation and shaping of dense reward functions based on large language models (LLMs). Given a goal described in natural language, Text2Reward generates shaped dense reward functions as an executable program grounded in a compact represent...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Policy invariance under reward transformations: Theory and application to reward shaping** (1999)
- *Authors:* Andrew Y. Ng et al.
- *Direct Connection:* This work formalized potential-based reward shaping, providing the theoretical basis and motivation for constructing dense, shaped rewards that preserve optimal policies, which the paper operationalizes through programmatically generated dense rewards.

**Maximum Entropy Inverse Reinforcement Learning** (2008)
- *Authors:* Brian D. Ziebart et al.
- *Direct Connection:* As a canonical IRL approach requiring demonstrations to infer rewards, it establishes the data-dependent baseline that the paper explicitly sidesteps by generating rewards directly from language without expert trajectories.

**Grounding English Commands to Reward Functions** (2015)
- *Authors:* James MacGlashan et al.
- *Direct Connection:* This paper established the natural language-to-reward formulation, demonstrating that instructions can be mapped to executable reward semantics, which the paper scales up with general-purpose LLM program synthesis instead of task-specific parsers.

### 💡 Inspiration

**Voyager: An Open-Ended Embodied Agent with Large Language Models** (2023)
- *Authors:* Guanzhi Wang et al.
- *Direct Connection:* By showing LLMs can write executable, environment-aware code that leverages existing APIs and libraries, it provided the coding paradigm the paper repurposes to emit reward functions that call simulation/tool packages.

### 🔍 Gap Identification

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Direct Connection:* By showing that learning reward models from pairwise human comparisons is effective but costly, it highlights the data and annotation burden that the paper addresses via data-free, LLM-authored reward programs guided only by textual goals.

### 📊 Baseline

**Eureka: Human-Level Reward Design via Coding Large Language Models** (2023)
- *Authors:* Daniel Freeman et al.
- *Direct Connection:* It directly inspired using LLMs to author reward code, and the paper extends this idea to produce shaped, dense reward programs grounded in compact state representations with iterative refinement rather than largely heuristic or sparse formulations.

### 🔗 Related Problem

**Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning** (2018)
- *Authors:* Rodrigo Toro Icarte et al.
- *Direct Connection:* This work demonstrated interpretable, program-like structured reward representations and their benefits for RL, motivating the paper’s choice of free-form, editable reward programs to achieve interpretability without automata constraints.

---

## Synthesis: How Prior Work Led to This Paper

Potential-based reward shaping established that dense, shaped rewards can preserve optimal behavior while accelerating learning, anchoring the idea that reward design should extend beyond sparse terminal signals. Maximum Entropy IRL and related apprenticeship learning formalized inferring rewards from demonstrations, but at the cost of requiring expert data and solving difficult inverse problems. Human-preference-based reward learning further showed that good rewards can be learned from comparisons, while making clear the heavy annotation and data requirements. Earlier work in mapping natural language to reward functions proved that instructions can be grounded into executable reward semantics via parsing, albeit with task-specific datasets and constrained formalisms. In parallel, LLMs were shown capable of authoring executable, environment-aware code that calls external APIs, as exemplified by open-ended agents generating skills via code. Most directly, coding LLMs have been used to author reward programs that enable challenging skills, highlighting the feasibility and power of programmatic reward design.
Together, these threads exposed an opportunity: combine the interpretability and learning advantages of shaped rewards with the data-free, executable code synthesis abilities of LLMs, while avoiding the data demands of IRL and preference learning. The paper synthesizes these insights by prompting LLMs to generate free-form, dense reward programs grounded in compact environment states and existing packages, then enabling iterative human-in-the-loop refinement. This is a natural next step that inherits the structure and editability of programmatic rewards, the grounding and tool-use of LLM code generation, and the theoretical guarantees motivating shaping, to deliver practical, interpretable reward design without demonstrations or pairwise labels.

---

*Analysis generated on: 2026-01-06T12:27:08.516284*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

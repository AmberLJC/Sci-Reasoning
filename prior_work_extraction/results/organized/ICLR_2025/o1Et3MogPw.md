# Prior Work Analysis Report

## Target Paper

**Title:** Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence

**Conference:** ICLR 2025 (spotlight)

**Authors:** Weize Chen, Ziming You, Ran Li, yitong guan, Chen Qian, Chenyang Zhao, Cheng Yang, Ruobing Xie, Zhiyuan Liu, Maosong Sun

**Keywords:** llm agent, multi-agent

**Abstract:** 
> The rapid advancement of large language models (LLMs) has paved the way for the development of highly capable autonomous agents. However, existing multi-agent frameworks often struggle with integrating diverse capable third-party agents due to reliance on agents defined within their own ecosystems. They also face challenges in simulating distributed environments, as most frameworks are limited to single-device setups. Furthermore, these frameworks often rely on hard-coded communication pipelines...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**FIPA Agent Communication Language (ACL) Specifications** (2002)
- *Authors:* FIPA (Foundation for Intelligent Physical Agents)
- *Direct Connection:* IoA’s agent integration protocol echoes FIPA ACL’s core idea of standardized performatives and message envelopes, adapting classical MAS interoperability principles to LLM-based agents and modern networked settings.

### 💡 Inspiration

**HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in HuggingFace** (2023)
- *Authors:* Yongliang Shen et al.
- *Direct Connection:* IoA builds on HuggingGPT’s core insight of using an LLM as a router to external capabilities, but formalizes this with a general agent integration protocol and dynamic teaming that overcome HuggingGPT’s task-specific, centralized scheduling pipeline.

### 🔍 Gap Identification

**MetaGPT: Meta Programming for Multi-Agent Collaborative Framework** (2023)
- *Authors:* Huang et al.
- *Direct Connection:* IoA directly targets MetaGPT’s rigidity—its SOP-driven, fixed role pipelines within a single framework—by enabling adaptive conversation flow control and plug-and-play agents defined outside the host ecosystem.

**ChatDev: Communicative Agents for Software Development** (2023)
- *Authors:* Wang et al.
- *Direct Connection:* IoA addresses ChatDev’s hard-coded, domain-specific chat pipelines by providing a generic, IM-like communication substrate and dynamic team formation that adapts to changing task requirements.

### 📊 Baseline

**AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation** (2023)
- *Authors:* Wu et al.
- *Direct Connection:* IoA generalizes AutoGen’s intra-process GroupChat paradigm by replacing its hard-coded, single-ecosystem agent classes with an instant-messaging bus and a protocol that allows heterogeneous, third-party agents to interoperate across devices.

### 🔗 Related Problem

**Generative Agents: Interactive Simulacra of Human Behavior** (2023)
- *Authors:* Joon Sung Park et al.
- *Direct Connection:* IoA leverages the insight that rich, message-based interactions can yield emergent coordination, but extends it with a standardized protocol and distributed runtime to support real heterogeneous agents rather than a single simulated environment.

---

## Synthesis: How Prior Work Led to This Paper

AutoGen established a practical template for multi-agent LLM applications by scripting agent roles and their turn-taking with a GroupChat orchestrator; while effective, its agents are defined within the same framework and typically live in a single process, making communication patterns rigid. HuggingGPT demonstrated that an LLM can schedule and route tasks to diverse external models, revealing the power of integrating third-party capabilities, albeit through a centralized, task-specific pipeline tightly coupled to one ecosystem. MetaGPT operationalized multi-agent workflows with SOP-like role playbooks, delivering structured outputs but fixing collaboration into static sequences bound to its own agent definitions. ChatDev showed the utility of chat-like, role-based software teams but relied on pre-scripted, domain-tuned pipelines that lack adaptability. Generative Agents highlighted how message-driven social interactions can produce emergent coordination, though within a self-contained simulation rather than a heterogeneous, distributed system. Longstanding FIPA ACL specifications formalized interoperable agent communication via standardized message types and envelopes, setting a precedent for protocol-based agent interoperability. Together, these works expose a clear opportunity: multi-agent systems need the interoperability of classical MAS, the routing power of LLM controllers, and the flexibility of chat-style interactions—without rigid pipelines or single-ecosystem lock-in. The current paper synthesizes these threads by introducing a protocol that standardizes how heterogeneous agents connect, an instant-messaging-like bus for scalable, distributed communication, and dynamic teaming and flow-control policies that generalize beyond fixed scripts—a natural next step given the limitations and insights of prior frameworks.

---

*Analysis generated on: 2026-01-06T06:18:43.617068*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper
**Title:** n9PDaFNi8t
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**OSWorld-G: A GUI Grounding Benchmark for Computer-Use Agents** (2024)
- *Authors:* Qiushi Sun et al.
- *Connection:* OSWorld-G formalized executable GUI grounding (mapping instructions to actionable UI targets/locators), which OS-ATLAS explicitly scales up across Windows/Linux/macOS/Android/web via a synthesis toolkit and trains a model specialized for this formulation.

**Mind2Web: Towards a Generalist Agent for the Web** (2023)
- *Authors:* Shuyan Zhou et al.
- *Connection:* Mind2Web introduced a generalist web-agent problem formulation with instruction-to-action trajectories and emphasized separating high-level planning from low-level execution; OS-ATLAS builds on this by focusing the low-level executable grounding component and generalizing beyond the web to full OS GUIs.

### 💡 Inspiration

**Kosmos-2: Grounding Multimodal Large Language Models to the World** (2023)
- *Authors:* Wang et al.
- *Connection:* Kosmos-2 popularized fine-grained grounding via region/box outputs in MLLMs; OS-ATLAS adapts this idea to executable GUI grounding, training models to localize actionable UI elements and emit precise click/interaction targets.

### 🔍 Gap Identification

**OSWorld: Benchmarking Multimodal Agents for Open-Ended Computer Use** (2024)
- *Authors:* Qiushi Sun et al.
- *Connection:* OSWorld established the modern computer-use agent benchmark and highlighted that open-source VLMs severely underperform (especially in GUI grounding and OOD cases), a concrete shortcoming OS-ATLAS directly targets with a cross-platform grounding corpus and an action-centric foundation model.

### 📊 Baseline

**LLaVA: Large Language and Vision Assistant** (2023)
- *Authors:* Haotian Liu et al.
- *Connection:* LLaVA represents the de facto open-source VLM baseline that OS-ATLAS consistently surpasses on GUI grounding and OOD agentic tasks, addressing LLaVA’s limitations in precise UI element localization and executable action prediction.

### 🔗 Related Problem

**WebArena: A Realistic Web Environment for Building Autonomous Agents** (2023)
- *Authors:* Zhou et al.
- *Connection:* WebArena demonstrated that realistic, visually rich environments expose agents’ grounding/OOD weaknesses; OS-ATLAS adopts this insight by creating a much broader, cross-platform GUI grounding corpus to improve robustness beyond the web domain.

---

## Synthesis

OS-ATLAS crystallizes from a line of work that progressively sharpened the need for executable GUI grounding in realistic, open-ended environments. Mind2Web framed generalist web agency and underscored a separation between strategic planning and low-level action execution, motivating a specialized component that can accurately ground instructions into concrete UI actions. WebArena then showed that realistic, visually rich interfaces exacerbate grounding and generalization challenges, suggesting that scaling data diversity is essential.

This trajectory converged in OSWorld and its GUI grounding benchmark, OSWorld-G, which formalized executable grounding for computer-use agents and—critically—revealed a stark gap between closed-source and open-source VLMs in GUI grounding and OOD performance. OS-ATLAS directly addresses this gap by constructing a cross-platform synthesis toolkit and the largest open-source grounding corpus spanning Windows, Linux, macOS, Android, and the web, and by training a foundation action model tailored to this formulation.

On the modeling side, OS-ATLAS draws inspiration from Kosmos-2’s fine-grained, box-level grounding in multimodal LLMs, adapting region/coordinate supervision to the executable GUI setting so the model learns where and how to act. LLaVA serves as the representative open-source baseline whose localization and OOD shortcomings OS-ATLAS overcomes. Together, these works define the problem, expose the core limitations, and supply the technical hooks—data generation and fine-grained grounding—that OS-ATLAS extends into a generalist, cross-platform foundation action model for GUI agents.

---
*Generated: 2026-01-06T23:09:26.599694*

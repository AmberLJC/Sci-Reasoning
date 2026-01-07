# Prior Work Analysis Report

## Target Paper

**Title:** EQA-MX: Embodied Question Answering using Multimodal Expression

**Conference:** ICLR 2024 (spotlight)

**Authors:** Md Mofijul Islam, Alexi Gladstone, Riashat Islam, Tariq Iqbal

**Keywords:** multimodal representation learning, visual-language models, embodied question answering

**Abstract:** 
> Humans predominantly use verbal utterances and nonverbal gestures (e.g., eye gaze and pointing gestures) in their natural interactions. For instance, pointing gestures and verbal information is often required to comprehend questions such as "what object is that?" Thus, this question-answering (QA) task involves complex reasoning of multimodal expressions (verbal utterances and nonverbal gestures). However, prior works have explored QA tasks in non-embodied settings, where questions solely contai...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Embodied Question Answering** (2018)
- *Authors:* Abhishek Das et al.
- *Direct Connection:* This work defined the EQA problem—an agent must navigate a 3D environment to answer a question—which EQA-MX directly extends by incorporating deictic nonverbal cues (gaze/pointing) and multi-perspective inputs into the same embodied QA formulation.

**SQA3D: Situated Question Answering in 3D Scenes** (2022)
- *Authors:* Fei Xia et al.
- *Direct Connection:* This work formalized QA grounded in reconstructed 3D scenes, providing the situated-3D QA framing that EQA-MX scales to interactive embodied settings with multi-view and multimodal expressions.

### 💡 Inspiration

**ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes** (2020)
- *Authors:* Panos Achlioptas et al.
- *Direct Connection:* By showing that referring expressions in 3D are viewpoint-sensitive and require grounding to scene geometry, this work motivates EQA-MX’s multi-view visual perspectives and deictic language (“this/that”) disambiguation in embodied QA.

**Where are they looking?** (2015)
- *Authors:* Adria Recasens et al.
- *Direct Connection:* By establishing gaze as a reliable cue for locating referents in images, this work directly inspires EQA-MX’s use of eye gaze as a nonverbal deictic signal to resolve ambiguous references in embodied questions.

### 🔍 Gap Identification

**ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks** (2020)
- *Authors:* Mohit Shridhar et al.
- *Direct Connection:* By demonstrating embodied language understanding with only verbal instructions and no nonverbal cues, ALFRED highlights the limitation EQA-MX addresses by introducing gestures and gaze into embodied QA.

### 📊 Baseline

**Neural Modular Control for Embodied Question Answering** (2018)
- *Authors:* Daniel Gordon et al.
- *Direct Connection:* As a leading EQA modeling approach, this paper’s modular perception–navigation–answering pipeline serves as a primary baseline framework that EQA-MX augments by injecting explicit gesture channels and multimodal expression reasoning.

### 🔗 Related Problem

**ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language** (2020)
- *Authors:* Dave Zhenyu Chen et al.
- *Direct Connection:* This paper’s technique for aligning natural language to 3D objects underscores the need for precise cross-modal grounding that EQA-MX generalizes to embodied question answering with additional nonverbal signals.

---

## Synthesis: How Prior Work Led to This Paper

Embodied Question Answering introduced the core idea of an agent navigating a 3D world to answer questions, crystallizing the embodied QA formulation that subsequent methods adopted. Neural Modular Control for EQA operationalized this with a modular perception–navigation–answering pipeline, a practical template for building embodied QA agents. In parallel, ReferIt3D showed that referring expressions in 3D are intrinsically viewpoint-sensitive and demand explicit grounding to geometric context, while ScanRefer demonstrated effective alignment of language to objects in RGB-D scans, reinforcing the need for precise cross-modal representations in 3D. Earlier, Where are they looking? established human gaze as a strong deictic cue for localizing targets, pointing toward the utility of nonverbal signals in resolving ambiguous references like “that.” SQA3D formalized situated QA over reconstructed 3D scenes, shifting focus from flat images to spatially coherent environments. ALFRED expanded embodied language understanding to longer-horizon tasks but remained text-only, revealing a missing piece: nonverbal communication.
Together these works expose an opportunity: embodied QA agents that reason not just over language and 3D scenes, but also over deictic gestures and multiple visual perspectives to disambiguate references. EQA-MX emerges as the natural synthesis—extending the EQA and situated 3D QA formulations with gaze/pointing signals and multi-view inputs, and learning representations tailored to deictic, viewpoint-dependent expressions—while benchmarking against modular EQA pipelines and 3D grounding techniques they directly build upon.

---

*Analysis generated on: 2026-01-06T11:10:48.140290*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

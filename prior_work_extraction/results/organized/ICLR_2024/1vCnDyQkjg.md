# Prior Work Analysis Report

## Target Paper

**Title:** Unified Human-Scene Interaction via Prompted Chain-of-Contacts

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zeqi Xiao, Tai Wang, Jingbo Wang, Jinkun Cao, Wenwei Zhang, Bo Dai, Dahua Lin, Jiangmiao Pang

**Keywords:** Human-Scene Interaction, Chain-of-Contacts, Unified, LLM

**Abstract:** 
> Human-Scene Interaction (HSI) is a vital component of fields like embodied AI and virtual reality. Despite advancements in motion quality and physical plausibility, two pivotal factors, versatile interaction control and the development of a user-friendly interface, require further exploration before the practical application of HSI. This paper presents a unified HSI framework, UniHSI, which supports unified control of diverse interactions through language commands. The framework defines interact...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**PartNet: A Large-scale Benchmark for Fine-grained and Hierarchical Part-level 3D Object Understanding** (2019)
- *Authors:* Mo et al.
- *Direct Connection:* PartNet’s object-part taxonomy underpins the ‘object part’ side of UniHSI’s joint–part CoC tokens and enables the LLM planner to reference parts (e.g., handle, seat) consistently across objects.

**GRAB: A Dataset of Whole-Body Human Grasping of Objects** (2020)
- *Authors:* Taheri et al.
- *Direct Connection:* GRAB’s dense joint–object contact maps provide concrete supervision and validation for representing interactions via explicit joint-to-object contacts that UniHSI extends beyond grasping to whole-body, part-aware interactions.

### 💡 Inspiration

**Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan)** (2022)
- *Authors:* Ahn et al.
- *Direct Connection:* UniHSI’s LLM Planner adopts SayCan’s core idea of decomposing language instructions into a sequence of affordance-grounded substeps, but grounds each substep as a Chain-of-Contacts (joint–object-part pair) rather than robot skills.

### 🔍 Gap Identification

**BEHAVE: Dataset and Method for Tracking the 3D Human Body in the Wild with Interactions** (2022)
- *Authors:* Bhatnagar et al.
- *Direct Connection:* BEHAVE evidences that interaction categories tightly correlate with consistent contact regions yet lacks a unified, language-driven control interface, motivating UniHSI’s CoC formulation and LLM planning.

### 📊 Baseline

**Human Motion Diffusion Model** (2023)
- *Authors:* Tevet et al.
- *Direct Connection:* UniHSI builds its unified controller on an MDM-style diffusion backbone and augments it with explicit contact conditioning so that CoC steps can be faithfully executed in scenes.

### 🔧 Extension

**OmniControl: Control at All Levels for Human Motion Generation** (2023)
- *Authors:* Zhang et al.
- *Direct Connection:* UniHSI generalizes OmniControl’s multi-signal motion conditioning paradigm to object-part-aware contact constraints, enabling a single controller to execute diverse human–scene interactions from a unified CoC representation.

### 🔗 Related Problem

**Language Models as Zero-Shot Planners: A Step-by-Step Approach** (2022)
- *Authors:* Huang et al.
- *Direct Connection:* UniHSI leverages the step-by-step prompting strategy from this work to elicit coherent multi-step plans and formats those steps explicitly as contact-centric CoC plans.

---

## Synthesis: How Prior Work Led to This Paper

SayCan introduced a practical recipe for translating natural language into sequences of executable steps by grounding each step in affordances, while subsequent work on zero-shot planning with language models showed that carefully prompted, step-by-step decomposition can reliably elicit such structured plans. In motion generation, OmniControl demonstrated that a single generator can be conditioned by heterogeneous control signals (e.g., trajectories, contacts), hinting that a unified controller can execute diverse behaviors if the control tokens are designed properly. The Human Motion Diffusion Model provided a strong diffusion backbone that can accept rich conditioning for high-quality motion synthesis. On the perception and representation side, PartNet established a fine-grained, hierarchical taxonomy of object parts—handles, doors, seats—that standardizes how parts are referenced across categories. BEHAVE presented real human–object interaction sequences with contact, revealing that interaction categories correlate with consistent contact regions, though it did not offer a language-driven interface. GRAB supplied dense joint-to-object contact maps, validating contact as an explicit supervision signal for interaction representation.
Together, these works suggest a path: represent interaction steps explicitly as contacts with object parts, elicit those steps from language via LLM planning, and execute them with a unified, diffusion-based controller. UniHSI synthesizes these insights by defining a Chain-of-Contacts tokenization tied to object-part semantics (PartNet), planning CoC sequences from prompts (SayCan/zero-shot planning), and extending multi-signal motion control (OmniControl/MDM) to part-aware contact execution, thereby closing the gap left by datasets like BEHAVE and GRAB that lacked a unified, language-controllable interface.

---

*Analysis generated on: 2026-01-06T18:25:37.657511*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

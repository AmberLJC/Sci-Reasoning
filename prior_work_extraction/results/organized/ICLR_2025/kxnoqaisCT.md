# Prior Work Analysis Report

## Target Paper

**Title:** Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents

**Conference:** ICLR 2025 (oral)

**Authors:** Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su

**Keywords:** GUI Agents, Visual Grounding, Multimodal Large Language Models, GUI Grounding, Large Language Model

**Abstract:** 
> Multimodal large language models (MLLMs) are transforming the capabilities of graphical user interface (GUI) agents, facilitating their transition from controlled simulations to complex, real-world applications across various platforms. However, the effectiveness of these agents hinges on the robustness of their grounding capability. Current GUI agents predominantly utilize text-based representations such as HTML or accessibility trees, which, despite their utility, often introduce noise, incomp...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**WebArena: A Realistic Web Environment for Building Autonomous Agents** (2023)
- *Authors:* Zhou et al.
- *Direct Connection:* WebArena established the modern web-agent setting (typically using accessibility/HTML trees), providing the primary benchmark and problem context that this work rethinks with pixel-only grounding.

### 💡 Inspiration

**Shikra: Unleashing Multimodal LLMs with Region-Level Capabilities** (2023)
- *Authors:* Chen et al.
- *Direct Connection:* Shikra’s idea of using normalized box/point tokens to elicit region-level grounding from MLLMs informs this paper’s simple recipe for making a LLaVA-style model output pixel coordinates given referring expressions.

**Pix2Struct: Screen Understanding via Image-to-Text Pretraining** (2023)
- *Authors:* Kenton Lee et al.
- *Direct Connection:* Pix2Struct demonstrated that large-scale, web-based synthetic screen data with programmatic annotations is highly effective for screen understanding, a data strategy this paper adopts for GUI grounding.

### 🔍 Gap Identification

**Mind2Web: Towards a Generalist Agent for the Web** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* Mind2Web’s reliance on HTML/DOM trees and its documented brittleness/noise motivate this paper’s shift to purely visual grounding that avoids text-based environment representations.

### 📊 Baseline

**Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Vocabulary Detection** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* As the prevailing open-vocabulary text-to-box grounding baseline, Grounding DINO is a direct comparator that this paper aims to surpass on GUI referring expressions with an MLLM-based approach.

### 🔧 Extension

**Visual Instruction Tuning (LLaVA)** (2023)
- *Authors:* Haotian Liu et al.
- *Direct Connection:* The current paper directly adapts the LLaVA architecture and training paradigm to a coordinate-prediction setup for GUI elements, leveraging its instruction-following visual-language backbone for grounding.

### 🔗 Related Problem

**Kosmos-2: Grounding Multimodal Large Language Models to the World** (2023)
- *Authors:* Zhang et al.
- *Direct Connection:* Kosmos-2’s grounded MLLM showed that LLMs can output spatial pointers tied to language, an approach that informs the coordinate-formatting and grounding supervision used here for GUI targets.

---

## Synthesis: How Prior Work Led to This Paper

Instruction-following multimodal LLMs such as LLaVA showed that a lightweight vision-language alignment plus dialogue-style decoding can reliably connect images to natural-language intents. Building on this, Shikra introduced simple tokenization schemes for normalized coordinates, demonstrating that the same class of models can be coaxed to point to regions with referring expressions. In parallel, Pix2Struct established that synthetic, programmatically labeled web screenshots are a powerful substrate for screen understanding, indicating that scalable browser-based generation can cover diverse UI layouts and semantics. Web agents matured with environments like WebArena, where systems typically access accessibility/HTML trees to act, while Mind2Web documented that such textual structures can be noisy, incomplete, and brittle for generalization. For grounding as a capability, Grounding DINO supplied a strong open-vocabulary text-to-box detector, and Kosmos-2 generalized grounded outputs within MLLMs, reinforcing that language and spatial predictions can be unified.
Together these threads expose a clear opening: leverage synthetic, web-rendered supervision to teach MLLMs to point, but target GUI elements directly from pixels to avoid DOM noise and to generalize across platforms. Adapting a LLaVA-style backbone with Shikra/Kosmos-2-like coordinate formatting provides a minimal architectural change while keeping instruction-following intact. Grounding DINO offers a rigorous baseline for referring expressions, and WebArena/Mind2Web contextualize the shift away from text-based representations. The resulting synthesis—a visual-only, universally grounded GUI model trained on scalable web-based synthetic data—emerges as the natural next step.

---

*Analysis generated on: 2026-01-06T14:10:54.491997*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

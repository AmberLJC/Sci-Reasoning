# Prior Work Analysis Report

## Target Paper
**Title:** IYOksPHJKT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**AffectNet: A Database for Facial Expression, Valence, and Arousal in the Wild** (2017)
- *Authors:* Ali Mollahosseini et al.
- *Connection:* SEPM builds on AffectNet’s discrete emotion and valence–arousal formulations, explicitly targeting the fine-grained emotion distinctions and misclassification patterns documented on this benchmark.

### 💡 Inspiration

**Least-to-Most Prompting Enables Complex Reasoning in Language Models** (2022)
- *Authors:* Denny Zhou et al.
- *Connection:* SEPM’s Confidence-Guided Coarse-to-Fine Inference directly operationalizes least-to-most prompting for multimodal emotion recognition by first solving simpler affective sub-tasks (e.g., polarity/valence or broad categories) and then refining to specific emotions conditioned on the model’s confidence.

### 🔍 Gap Identification

**EMOTIC: Contextual Emotion Recognition in Images** (2017)
- *Authors:* A. Kosti et al.
- *Connection:* EMOTIC’s demonstration that background context can mislead image-based emotion recognition motivates SEPM’s Focus-on-Emotion design to downweight irrelevant regions and foreground key emotional cues during MLLM inference.

### 📊 Baseline

**LLaVA: Large Language and Vision Assistant** (2023)
- *Authors:* Haotian Liu et al.
- *Connection:* LLaVA serves as a primary MLLM baseline that SEPM augments in a training-free manner, with SEPM directly improving LLaVA’s zero-shot emotion classification and reasoning through its coarse-to-fine, confidence-guided inference.

**InstructBLIP: Towards General-Purpose Vision-Language Models with Instruction Tuning** (2023)
- *Authors:* Wenliang Dai et al.
- *Connection:* InstructBLIP is a core MLLM baseline targeted by SEPM; the proposed training-free pipeline plugs into its inference to sharpen emotional perception without additional fine-tuning or annotations.

### 🔧 Extension

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2022)
- *Authors:* Xuezhi Wang et al.
- *Connection:* SEPM extends the self-consistency idea by using model-derived confidence to select and escalate among candidate emotion predictions at inference time, mitigating confusions between semantically similar emotions without any parameter updates.

**Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization** (2017)
- *Authors:* Ramprasaath R. Selvaraju et al.
- *Connection:* SEPM’s Focus-on-Emotion module leverages gradient/attention-based localization to emphasize emotion-relevant regions and suppress distractions, directly extending the Grad-CAM principle to guide MLLMs’ visual focus during inference.

---

## Synthesis

SEPM’s training-free approach sits at the intersection of reasoning-oriented prompting and emotion-centric visual grounding. At the reasoning level, Least-to-Most Prompting (Zhou et al., 2022) provides the core inspiration: tackling a complex task by progressively solving simpler subproblems. SEPM adopts this idea in a multimodal setting, decomposing emotion understanding into easy-to-hard stages and adding a confidence gate to decide when to refine to more specific labels. This confidence mechanism closely aligns with Self-Consistency (Wang et al., 2022), which showed that inference-time aggregation can correct errors; SEPM extends that spirit by explicitly using confidence to escalate or halt the refinement process, thereby reducing confusions among semantically similar emotions.

On the model side, LLaVA (Liu et al., 2023) and InstructBLIP (Dai et al., 2023) are the practical MLLM baselines that SEPM aims to improve without any parameter updates or additional data—demonstrating plug-and-play benefits at inference. For visual focus, SEPM’s Focus-on-Emotion module is a targeted extension of Grad-CAM (Selvaraju et al., 2017), using gradient/attention localization to foreground emotionally salient regions and suppress distractors. Finally, the problem formulation and the key failure modes SEPM tackles are grounded in AffectNet (Mollahosseini et al., 2017), which defines the discrete and dimensional affect space, and EMOTIC (Kosti et al., 2017), which exposed how background context can mislead emotion recognition. Together, these works directly shape SEPM’s coarse-to-fine, confidence-guided, and region-focused design for sharpening emotion perception in MLLMs.

---
*Generated: 2026-01-06T23:07:19.626757*

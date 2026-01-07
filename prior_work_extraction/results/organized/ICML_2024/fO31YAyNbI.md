# Prior Work Analysis Report

## Target Paper
**Title:** fO31YAyNbI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Connection:* VoT explicitly inherits the Chain-of-Thought principle of decomposing complex problems into sequential sub-steps, providing the core reasoning template that VoT adapts from language to video.

**Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations** (2017)
- *Authors:* Ranjay Krishna et al.
- *Connection:* Visual Genome introduced scene graphs as a structured representation of objects, attributes, and relations, which MotionEpic generalizes to the video domain via spatio-temporal scene graphs for fine-grained grounding.

**Action Genome: Actions as Compositions of Spatio-Temporal Scene Graphs** (2020)
- *Authors:* Ji et al.
- *Connection:* Action Genome operationalized spatio-temporal scene graphs (STSG) for video, directly enabling MotionEpic’s choice of STSG as the backbone representation for pixel-level spatio-temporal grounding.

**TVQA: Localized, Compositional Video Question Answering** (2018)
- *Authors:* Jie Lei et al.
- *Connection:* TVQA formalized temporally localized, multi-step video QA, shaping the problem setup that VoT targets and motivating its need for temporal grounding plus compositional reasoning.

### 💡 Inspiration

**Least-to-Most Prompting Enables Complex Reasoning in Large Language Models** (2022)
- *Authors:* Denny Zhou et al.
- *Connection:* The least-to-most strategy of solving easier perceptual subproblems before higher-level reasoning directly motivates VoT’s staged pipeline from pixel-level perception to cognitive interpretation.

### 🔍 Gap Identification

**Video-ChatGPT: Towards Detailed Video Understanding via Large Vision-Language Models** (2023)
- *Authors:* Maaz et al.
- *Connection:* As a representative Video-LLM, Video-ChatGPT relies on coarse clip/frame features and lacks fine-grained grounding, a limitation VoT/MotionEpic addresses by integrating STSG and step-wise reasoning.

### 🔗 Related Problem

**CLEVRER: CoLlision Events for Video REasoning** (2020)
- *Authors:* Kexin Yi et al.
- *Connection:* CLEVRER’s emphasis on causal, counterfactual video reasoning exposed the gap between low-level perception and high-level cognition, directly motivating VoT’s perception-to-cognition reasoning pipeline.

---

## Synthesis

Video-of-Thought (VoT) fuses two threads of prior work: step-wise reasoning from language models and structured spatio-temporal perception from video understanding. Chain-of-Thought (Wei et al., 2022) provides the core template of decomposing complex tasks into intermediate steps, while Least-to-Most Prompting (Zhou et al., 2022) specifically inspires VoT’s curriculum-like flow from easier perceptual subproblems to harder cognitive inference—mirrored in VoT’s progression from pixel-grounded observations to semantic/causal conclusions. On the perception side, Visual Genome (Krishna et al., 2017) established scene graphs as a structured interface between vision and language, and Action Genome (2020) extended this to videos as spatio-temporal scene graphs (STSG). MotionEpic builds directly on this lineage by embedding STSG into an MLLM to achieve fine-grained, pixel-level spatial-temporal grounding that prior Video-LLMs lacked. Representative video MLLMs such as Video-ChatGPT (Maaz et al., 2023) crystallized the gap: strong language priors but coarse visual grounding, motivating VoT’s integration of STSG with step-by-step reasoning. Finally, problem formulations from TVQA (Lei et al., 2018)—localized, compositional, temporally grounded QA—and the causal demands highlighted by CLEVRER (Yi et al., 2020) define the reasoning challenges VoT targets. Together, these works directly shape VoT’s core innovation: a video-native, STSG-grounded, chain-of-thought framework that bridges low-level perception and high-level cognition.

---
*Generated: 2026-01-06T23:09:26.496577*

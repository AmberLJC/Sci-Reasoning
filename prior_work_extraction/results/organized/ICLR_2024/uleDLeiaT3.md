# Prior Work Analysis Report

## Target Paper

**Title:** GROOT: Learning to Follow Instructions by Watching Gameplay Videos

**Conference:** ICLR 2024 (spotlight)

**Authors:** Shaofei Cai, Bowei Zhang, Zihao Wang, Xiaojian Ma, Anji Liu, Yitao Liang

**Keywords:** Agent, Goal-conditioned Policy, Imitation Learning, Open World, Minecraft

**Abstract:** 
> We study the problem of building a controller that can follow open-ended instructions in open-world environments. We propose to follow reference videos as instructions, which offer expressive goal specifications while eliminating the need for expensive text-gameplay annotations. A new learning framework is derived to allow learning such instruction-following controllers from gameplay videos while producing a video instruction encoder that induces a structured goal space. We implement our agent G...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**VIMA: General Robot Manipulation with Multimodal Prompts** (2023)
- *Authors:* Yunfan Jiang et al.
- *Direct Connection:* VIMA introduced the formulation of following short visual demonstrations as task instructions via a learned prompt encoder, providing the core modality—‘video as instruction’—that this paper adopts and adapts to open-world gameplay.

**Generative Adversarial Imitation from Observation** (2019)
- *Authors:* Faraz Torabi et al.
- *Direct Connection:* By formalizing imitation-from-observation without action labels through aligning expert and learner state distributions, this work underpins the paper’s learning-from-video paradigm where trajectories are matched to instruction videos without action supervision.

### 💡 Inspiration

**Learning Latent Plans from Play** (2019)
- *Authors:* Corey Lynch et al.
- *Direct Connection:* This paper showed that unlabeled play can supervise goal-conditioned control by extracting a latent plan from a demo snippet, directly inspiring the idea of conditioning a policy on a compact representation of a reference video segment.

### 🔍 Gap Identification

**MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge** (2022)
- *Authors:* Linxi (Jim) Fan et al.
- *Direct Connection:* MineDojo (via MineCLIP) framed open-ended Minecraft goals using video–text pairs, highlighting the reliance on expensive text-gameplay alignment that this paper explicitly avoids by using videos themselves as instructions and learning an instruction encoder without text.

### 📊 Baseline

**Learning to Play Minecraft with Video PreTraining** (2022)
- *Authors:* Bowen Baker et al.
- *Direct Connection:* This work established the dominant Minecraft imitation-learning baseline by training policies from labeled human play, which the current paper directly challenges by removing the need for action/text annotations and outperforming it while conditioning on reference videos as instructions.

### 🔧 Extension

**Visual Reinforcement Learning with Imagined Goals (RIG)** (2018)
- *Authors:* Ashvin Nair et al.
- *Direct Connection:* RIG’s key idea of learning a latent goal space from visual observations is extended here to sequence-level video embeddings, so the video instruction encoder induces a structured goal space that conditions the policy.

---

## Synthesis: How Prior Work Led to This Paper

Video-pretrained Minecraft agents demonstrated that large-scale human gameplay can train competent policies, but relied on labeled actions and heavy annotation pipelines (Baker et al.). MineDojo broadened the setting to open-ended goals and introduced MineCLIP to align text with video, crystallizing an instruction-following formulation in Minecraft yet depending on curated text–video pairs (Fan et al.). In robotics, Learning Latent Plans from Play showed that unlabeled play trajectories contain rich supervision: a short demonstration snippet can be encoded into a compact latent plan that conditions a goal-conditioned policy over long horizons (Lynch et al.). VIMA advanced this promptable-control view by using short visual demonstrations as multimodal instructions and learning an instruction encoder that policies can follow (Jiang et al.). Complementing these, RIG established that learning a latent goal space from raw observations enables goal-conditioned control without explicit symbolic goals (Nair et al.), while Generative Adversarial Imitation from Observation formalized learning policies from videos alone via state-distribution alignment rather than action labels (Torabi et al.). Together, these works suggest a path: use videos directly as instruction specifications, learn an encoder that maps instruction clips into a structured goal space, and condition a policy on this representation to follow open-ended tasks in an open world. The present paper synthesizes these insights by replacing text with reference gameplay videos as goals, learning a video-instruction encoder that induces a compositional goal space, and training a causal-transformer policy to align its rollouts to those instruction embeddings, thereby surpassing labeled-data-heavy Minecraft baselines in open-ended skill execution.

---

*Analysis generated on: 2026-01-06T20:08:28.574366*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

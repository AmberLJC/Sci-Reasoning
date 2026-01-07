# Prior Work Analysis Report

## Target Paper

**Title:** RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jiayuan Gu, Sean Kirmani, Paul Wohlhart, Yao Lu, Montserrat Gonzalez Arenas, Kanishka Rao, Wenhao Yu, Chuyuan Fu, Keerthana Gopalakrishnan, Zhuo Xu, Priya Sundaresan, Peng Xu, Hao Su, Karol Hausman, Chelsea Finn, Quan Vuong, Ted Xiao

**Keywords:** robotics, robot learning, robot manipulation, task representation, behavior cloning, multitask imitation learning, goal conditioning

**Abstract:** 
> Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Hindsight Experience Replay** (2017)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* RT-Trajectory directly adapts HER’s core idea of hindsight relabeling—relabeling each rollout with what was actually achieved—by generating “hindsight trajectory sketches” from executed end-effector paths and using them as conditioning goals.

### 💡 Inspiration

**Learning from Play: Unsupervised Learning to Imitate** (2019)
- *Authors:* Corey Lynch et al.
- *Direct Connection:* Building on the play-data paradigm that relabels unlabeled trajectories into useful supervision, RT-Trajectory leverages the same hindsight principle but replaces outcome- or language labels with automatically derived 2D trajectory sketches to supervise multi-task policies.

### 🔍 Gap Identification

**Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan)** (2022)
- *Authors:* Michael Ahn et al.
- *Direct Connection:* SayCan highlighted that language alone often lacks the low-level geometric specificity needed for precise manipulation, a limitation RT-Trajectory addresses via motion-centric sketch prompts.

**RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** (2023)
- *Authors:* Anthony Brohan et al.
- *Direct Connection:* RT-2 showed strong semantic and object generalization but struggled to extrapolate to novel motor programs, motivating RT-Trajectory’s trajectory-sketch prompt that encodes new action geometry directly.

### 🔧 Extension

**RT-1: Robotics Transformer for Real-World Control at Scale** (2022)
- *Authors:* Anthony Brohan et al.
- *Direct Connection:* RT-Trajectory extends the RT-1 transformer policy framework by adding a trajectory-sketch conditioning channel and training procedure, effectively turning RT-1 into a sketch-conditioned multi-task policy.

### 🔗 Related Problem

**CLIPort: What and Where Pathways for Robotic Manipulation** (2021)
- *Authors:* Mohit Shridhar et al.
- *Direct Connection:* CLIPort demonstrated the power of spatial goal representations (per-pixel affordance maps) for language-conditioned manipulation, a spatial-conditioning insight RT-Trajectory generalizes using user-provided trajectory overlays.

---

## Synthesis: How Prior Work Led to This Paper

Hindsight Experience Replay established that trajectories can be retroactively relabeled with achieved goals to unlock learning signals from otherwise sparse feedback, introducing a powerful paradigm of hindsight conditioning. Learning from Play pushed this further for robot manipulation by transforming unstructured play into supervision via hindsight relabeling, showing that rich multi-task behaviors can emerge from relabeled trajectories. RT-1 showed that a transformer-based policy trained at scale on diverse, language-labeled demonstrations can perform many real-world tasks from raw pixels, cementing a practical architecture and data recipe for multi-task imitation learning. SayCan revealed that while language is a flexible interface, it often fails to convey the precise low-level geometry needed for manipulation, especially when tasks require new motion patterns. RT-2 scaled vision-language-action models and improved semantic transfer but still struggled with novel motor programs that language alone does not specify. CLIPort highlighted the benefits of spatially grounded conditioning through per-pixel affordances, underscoring that spatial structure in the input can simplify manipulation learning.
Taken together, these works suggested an opportunity: combine hindsight relabeling with an explicitly spatial, motion-centric prompt to provide the missing geometric specificity that language lacks, while retaining the practicality of large-scale multi-task training. RT-Trajectory synthesizes these ingredients by auto-generating “hindsight trajectory sketches” from executed rollouts and integrating them into an RT-1-style policy, enabling users to specify new tasks via rough sketches and allowing the policy to generalize to novel motor programs that prior language-only systems could not execute.

---

*Analysis generated on: 2026-01-06T12:45:43.824954*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

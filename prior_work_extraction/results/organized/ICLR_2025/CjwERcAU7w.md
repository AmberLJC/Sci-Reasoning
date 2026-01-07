# Prior Work Analysis Report

## Target Paper
**Title:** CjwERcAU7w
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Connection:* SCoRe adopts the core RL-from-feedback formulation introduced here—optimizing a language policy with scalar feedback—while replacing external human labels with self-generated multi-turn feedback to specifically train self-correction.

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Connection:* SCoRe directly builds on the online RL paradigm (policy optimization on-model rollouts) established for LLMs by InstructGPT, but substitutes human preference signals with self-produced correction feedback to target multi-turn self-correction.

### 💡 Inspiration

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Connection:* Constitutional AI’s critique-and-revise loop and AI-generated feedback demonstrate that models can supervise themselves; SCoRe generalizes this idea by training an LLM to generate, evaluate, and update its own multi-turn corrections via online RL without a stronger teacher.

### 🔍 Gap Identification

**STaR: Bootstrapping Reasoning With Reasoning** (2022)
- *Authors:* Eric Zelikman et al.
- *Connection:* STaR’s offline SFT on self-generated traces motivates SCoRe’s claim that offline SFT suffers distribution mismatch; SCoRe addresses this by training online on the model’s own multi-turn correction rollouts.

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2022)
- *Authors:* Yizhong Wang et al.
- *Connection:* Self-Instruct popularized offline SFT on self-generated data; SCoRe explicitly targets the resulting limitations (mode collapse and training–inference mismatch) by moving from offline SFT to online RL on self-generated correction trajectories.

### 📊 Baseline

**Self-Refine: Iterative Refinement with Self-Feedback** (2023)
- *Authors:* Shivanshu Madaan et al.
- *Connection:* Self-Refine establishes the inference-time iterative self-correction protocol that SCoRe turns into a training objective; SCoRe’s online RL learns to produce and act on effective self-feedback rather than relying on untrained iteration.

### 🔗 Related Problem

**Reflexion: Language Agents with Verbal Reinforcement Learning** (2023)
- *Authors:* Noah Shinn et al.
- *Connection:* Reflexion shows multi-turn reflection can improve agents but lacks a principled training scheme; SCoRe formalizes multi-turn self-correction as an online RL problem and trains the base LLM to internalize effective correction strategies.

---

## Synthesis

SCoRe’s key contribution—teaching an LLM to self-correct through multi-turn online reinforcement learning with entirely self-generated data—sits at the intersection of RL-from-feedback and self-critique/refinement lines of work. The RL foundation comes from Christiano et al. and InstructGPT, which established optimizing language policies from scalar feedback via online rollouts. Constitutional AI then demonstrated that models can supervise themselves through AI-generated critiques and revisions, motivating SCoRe’s decision to remove reliance on stronger teachers or humans and to let the policy generate and act on its own feedback. On the other side, STaR and Self-Instruct showed that offline SFT on model-generated traces can bootstrap capabilities, but they also revealed critical shortcomings—distribution mismatch and mode preference—that SCoRe directly addresses by training on-policy and online over the model’s own correction trajectories. Self-Refine codified iterative, inference-time self-correction without training; SCoRe turns that protocol into a learning problem, explicitly optimizing the policy to produce effective critiques and revisions. Finally, Reflexion highlighted the promise of multi-turn reflection for agents but lacked a principled training mechanism; SCoRe supplies that mechanism via online RL. Together, these works directly shaped SCoRe’s formulation: multi-turn, on-policy RL that uses self-generated feedback to reliably instill self-correction behavior where offline SFT and untrained iteration fall short.

---
*Generated: 2026-01-06T23:09:26.617110*

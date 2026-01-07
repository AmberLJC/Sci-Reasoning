# Prior Work Analysis Report

## Target Paper
**Title:** 1CqtvwHTKQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Contextual Markov Decision Processes** (2015)
- *Authors:* Hallak et al.
- *Connection:* Introduced the formal setting where each episode is drawn from a context-specific MDP, which this paper adopts to reason about cross-episode structure and to formalize shared structure via the variance of the value function across contexts.

**Unifying Count-Based Exploration and Intrinsic Motivation** (2016)
- *Authors:* Bellemare et al.
- *Connection:* Provided the core 'global novelty bonus' formulation via pseudo-counts computed from the agent’s entire experience; this paper directly analyzes when such global bonuses are effective versus episodic ones.

### 💡 Inspiration

**Never Give Up: Learning Directed Exploration Strategies** (2020)
- *Authors:* Badia et al.
- *Connection:* NGU explicitly combines an episodic novelty bonus with a life-long (global) novelty signal; the mixed-bonus design directly motivates this paper’s core question and framework for when each bonus should be used.

### 📊 Baseline

**Curiosity-driven Exploration by Self-supervised Prediction** (2017)
- *Authors:* Pathak et al.
- *Connection:* Established prediction-error intrinsic rewards as a widely used global novelty signal; the current work treats such global curiosity bonuses as primary baselines whose behavior it contrasts with episodic bonuses.

**Exploration by Random Network Distillation** (2019)
- *Authors:* Burda et al.
- *Connection:* RND is a canonical global novelty bonus based on lifelong statistics; this paper uses RND-style global exploration as a key baseline to study when global versus episodic bonuses succeed.

**Episodic Curiosity through Reachability** (2019)
- *Authors:* Savinov et al.
- *Connection:* Introduced an explicit episodic novelty mechanism via an episodic memory and reachability metric; the present paper directly builds on this idea to evaluate and characterize episodic bonuses.

**RIDE: Rewarding Impact-Driven Exploration for Procedurally-Generated Environments** (2020)
- *Authors:* Raileanu and Rocktäschel
- *Connection:* Proposes an intrinsic reward with an episodic component (state-change reward with per-episode normalization) and is used as an episodic-style baseline whose strengths and limitations across varying cross-episode structure this paper analyzes.

---

## Synthesis

The paper’s core innovation—a conceptual framework that explains when global versus episodic exploration bonuses are effective in environments that vary across episodes—rests on two pillars: the contextual MDP formulation and the modern families of intrinsic motivation methods. Hallak et al. introduced contextual MDPs, formalizing the setting where each episode is drawn from a context-specific MDP. This directly enables the authors’ central lens: quantifying shared structure by examining the variance of the value function across contexts. On the exploration side, Bellemare et al. unified count-based exploration and intrinsic motivation, crystallizing the idea of global novelty bonuses derived from lifelong statistics; this notion underpins global methods like Pathak et al.’s curiosity (prediction error) and Burda et al.’s RND, both of which serve as principal global baselines here. In contrast, Savinov et al.’s episodic curiosity operationalized per-episode novelty via episodic memory, providing the prototypical episodic-bonus mechanism that this study evaluates and interprets. Crucially, Badia et al.’s NGU demonstrated that combining episodic and global bonuses can be powerful, but left open when and why each component helps; this paper directly addresses that gap by disentangling the roles of the bonuses and tying them to cross-episode structure. Finally, RIDE contributes an episodic-style intrinsic reward used in procedurally generated settings, giving a concrete episodic baseline whose behavior across varying shared structure the authors scrutinize. Together, these works directly enable and motivate the unified analysis advanced in this paper.

---
*Generated: 2026-01-06T23:09:26.523092*

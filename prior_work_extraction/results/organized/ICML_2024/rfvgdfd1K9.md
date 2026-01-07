# Prior Work Analysis Report

## Target Paper
**Title:** rfvgdfd1K9
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Corrigibility** (2015)
- *Authors:* Nate Soares et al.
- *Connection:* We generalize the corrigibility desideratum—maintaining a human’s ability to intervene and redirect the system—into a formal, forward-looking notion of preserving the human’s long-term agency across AI-human interactions.

**Empowerment: A universal agent-centric measure of control** (2005)
- *Authors:* Alexander S. Klyubin et al.
- *Connection:* Our forward-looking agency evaluations draw on empowerment as an information-theoretic measure of an agent’s control over future states, using it to operationalize the human agency that aligned systems must preserve.

### 💡 Inspiration

**Conservative Agency via Attainable Utility Preservation** (2019)
- *Authors:* Alex Turner et al.
- *Connection:* We adapt AUP’s core insight—penalizing reductions in attainable options—by redirecting the preservation target from the AI’s own options to the human’s future options and decision-making agency.

### 🔍 Gap Identification

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Connection:* By showing that helpful-harmless-honest (truthfulness-focused) alignment can leave users vulnerable to subtle steering of their preferences and choices, we target a core limitation of Constitutional AI and propose explicitly optimizing for human agency preservation.

**Optimal Policies Tend to Seek Power** (2021)
- *Authors:* Alex Turner et al.
- *Connection:* We directly address the general incentive for power-seeking identified here by requiring intent-aligned systems to also preserve—rather than appropriate—human power/agency over time, and by formalizing agency-preserving interactions.

### 📊 Baseline

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Connection:* We take RLHF-style intent alignment as the prevailing baseline and argue that, even when systems faithfully follow or truthfully reflect human intent as learned from preferences, they can still erode users’ long-term agency; our proposal adds an explicit agency-preservation objective to this paradigm.

### 🔧 Extension

**The Off-Switch Game** (2016)
- *Authors:* Dylan Hadfield-Menell et al.
- *Connection:* We extend the off-switch game’s focus on preserving shutdown options to a broader agency-preservation criterion that governs everyday recommendations and interactions, not just emergency overrides.

---

## Synthesis

The paper’s core move—elevating agency preservation to a first-class optimization target alongside intent alignment—emerges from clear limitations in current alignment practice and from option-preservation ideas in safety theory. RLHF (Christiano et al., 2017) and Constitutional AI (Bai et al., 2022) define today’s intent- and truthfulness-focused baselines, but their very success leaves a gap: systems can still steer user preferences and choices while appearing honest and helpful. Foundational work on corrigibility (Soares et al., 2015) and the Off-Switch Game (Hadfield-Menell et al., 2016) established that preserving human control is a central desideratum; our contribution generalizes this from discrete override events to the ongoing, forward-looking preservation of human agency in everyday interactions. Technically, we draw inspiration from Conservative Agency via Attainable Utility Preservation (Turner et al., 2019), shifting the option-preservation lens from the AI’s capabilities to the human’s future options and decisional latitude. Empowerment (Klyubin et al., 2005) provides an operational scaffold for measuring such forward-looking control, enabling explicit agency evaluations. Finally, the power-seeking theorems (Turner et al., 2021) sharpen the problem by showing why generic objectives incentivize control acquisition; we respond by proposing that aligned systems be additionally constrained to preserve human agency. Together, these works directly motivate and enable our formal definition of agency-preserving AI-human interactions and the call to explicitly optimize for human agency, not merely intent conformity.

---
*Generated: 2026-01-06T23:09:26.409430*

# Prior Work Analysis Report

## Target Paper
**Title:** LX3VAhXNTw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Mastering the game of Go without human knowledge** (2017)
- *Authors:* David Silver et al.
- *Connection:* This work introduced the neural network + Monte Carlo Tree Search self-play paradigm that underlies KataGo and other targets; the paper’s core attack explicitly exploits failure modes emerging from this paradigm’s value/search interaction.

**A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning** (2017)
- *Authors:* Marc Lanctot et al.
- *Connection:* The PSRO framework formalizes training best responses to opponent policies; the paper operationalizes this by training an adversarial policy as a best response to KataGo’s play, leveraging the same BR principle to expose exploitability.

### 💡 Inspiration

**Adversarial Policies: Attacking Deep Reinforcement Learning** (2019)
- *Authors:* Adam Gleave et al.
- *Connection:* Gleave et al. showed that learned opponent policies can reliably induce catastrophic errors in DRL agents without input perturbations; the present paper directly scales this idea to superhuman, search-augmented Go AIs and designs policy-level adversaries to elicit blunders.

### 🔍 Gap Identification

**Robust Adversarial Reinforcement Learning** (2017)
- *Authors:* Lerrel Pinto et al.
- *Connection:* RARL proposes adversarial training to improve robustness; the paper directly tests this defense by adversarially training KataGo against their attack and shows the core vulnerability persists, revealing limits of such defenses in this setting.

### 📊 Baseline

**Accelerating Self-Play Learning in Go** (2019)
- *Authors:* David J. Wu
- *Connection:* KataGo (Wu, 2019) is the exact superhuman Go system the paper attacks; the authors use its released models/settings and analyze vulnerabilities tied to its AlphaZero-style neural-MCTS design.

### 🔗 Related Problem

**ELF OpenGo: An Analysis and Open Reimplementation of AlphaZero** (2019)
- *Authors:* Yuandong Tian et al.
- *Connection:* ELF OpenGo is another AlphaZero-style superhuman Go agent; the paper demonstrates zero-shot transfer of their adversarial policy to ELF, using it to validate that the exploited weakness generalizes across the same foundational design.

---

## Synthesis

The paper’s core contribution—training adversarial policies that reliably induce blunders in superhuman Go AIs—rests on the AlphaZero lineage and adversarial-policy research. Silver et al. (2017) established the neural-network-plus-MCTS self-play paradigm that powers modern Go engines; Wu (2019) extended this to KataGo, the specific target attacked here. The vulnerability the authors exploit arises from the interaction of learned value functions and bounded tree search characteristic of this paradigm. The immediate methodological spark comes from Gleave et al. (2019), who showed that one can learn opponent policies that systematically cause deep RL agents to fail without perturbing inputs; this work transposes and scales that idea to the high-stakes, search-augmented Go domain, crafting policies that exploit blind spots rather than “playing Go well.” To construct such exploiters, the authors effectively follow the best-response principle formalized by Lanctot et al. (2017)’s PSRO, training a policy as a BR to KataGo’s play to reveal exploitability. They also directly interrogate defenses proposed by Pinto et al. (2017), adversarially training KataGo to withstand the attack and showing that the central flaw remains, identifying a gap in robustness-through-adversaries for AlphaZero-style systems. Finally, by transferring the attack zero-shot to ELF OpenGo (Tian et al., 2019), they demonstrate that the weakness is not idiosyncratic to KataGo but a systemic consequence of the AlphaZero design, thereby tying the findings back to the foundational paradigm.

---
*Generated: 2026-01-06T23:09:26.557550*

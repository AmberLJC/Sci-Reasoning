# Prior Work Analysis Report

## Target Paper
**Title:** q8SukwaEBy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Proxy Value Propagation (PVP) sits at the intersection of interactive imitation learning and human-feedback-driven reinforcement learning. From DAgger, it inherits the central operational insight that the expert should actively intervene on the learner’s induced state distribution, yielding targeted supervision where it matters most. Unlike action cloning in DAgger, however, PVP encodes these interactions as proxy value labels—high for demonstrated actions, low when the human intervenes.

The mechanism that makes those sparse labels broadly useful is temporal-difference propagation, an idea crystallized in DQfD and DDPGfD: demonstrations seeded into off-policy TD updates can bootstrap and spread value information beyond the labeled transitions. PVP extends this to a reward-free regime, using TD to propagate both positive (demo) and negative (intervention) labels across the agent’s exploratory data.

Human feedback methods such as Deep TAMER and COACH demonstrated that direct, policy-dependent human signals can effectively shape value/policy without environment rewards. PVP adopts this reward-free supervision perspective but simplifies the target by assigning explicit proxy values, which TD then disseminates to unlabeled states, increasing sample efficiency and stability relative to training a separate reward model.

Finally, the emphasis on using negative signals aligns with IRL from Failure, which exploits suboptimal data to learn what not to do. By treating interventions as low-value labels, PVP explicitly suppresses unsafe or undesired actions while propagating this constraint. Together, these strands yield a simple, general, and efficient pipeline: collect demos and interventions, assign proxy values, and rely on TD to propagate human intent throughout the state-action space.

---
*Generated: 2026-01-06T23:42:49.088257*

# Prior Work Analysis Report

## Target Paper
**Title:** iEgaS6wbLa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper dissects when to rely on privileged expert distillation versus directly learning history-dependent policies under partial observability. This question traces to three converging lines of prior work. First, the principle of training-time-only information (Vapnik & Vashist, LUPI) and the mechanics of knowledge transfer (Hinton et al., knowledge distillation; Rusu et al., policy distillation) provide the methodological backbone for distilling a policy that acts from observations from a teacher that enjoys privileged latent state. Second, imitation learning with an oracle (Ross et al., DAgger) crystallizes the learning-to-act-from-an-expert paradigm the paper scrutinizes—especially relevant because the expert’s access to full state yields a Markovian teacher that may not translate cleanly to an observation-based student. Third, practical asymmetric-training schemes in robotics (e.g., Pinto et al.) show large empirical gains from simulator-state privilege yet expose brittleness, motivating a principled account of when such gains persist.
On the theoretical side, the Block MDP framework (Sun et al.) enables clean separation between latent dynamics and observation generation. By introducing a perturbed Block MDP, the paper precisely probes how stochasticity in latent dynamics and slight observation-model violations reshape sample-efficiency and error-propagation, clarifying when distillation inherits the teacher’s optimality versus when direct RL with memory (e.g., DRQN; Hausknecht & Stone) is preferable. Together, these works directly scaffold both the paper’s modeling choice and its central trade-off analysis.

---
*Generated: 2026-01-07T00:21:32.303978*

# Prior Work Analysis Report

## Target Paper
**Title:** mQeZEsdODh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper fuses three mature lines of work—model-based planning, online learning theory, and continual RL—to produce a continual agent that plans with an online world model and provable learning guarantees. From the model-based side, Dyna established that a single dynamics model can be updated continually and reused for many objectives, while PETS and PlaNet showed that model predictive control over learned (often probabilistic or latent) dynamics enables robust decision making and swift adaptation to changing rewards. The present work adopts that planning paradigm but makes the model strictly online and the sole locus of adaptation across a stream of tasks.
On the theory side, the agent’s Follow-The-Leader shallow model and its no-forgetting property are grounded in the FTL/FTRL toolbox from online convex optimization (Shalev-Shwartz), with regret control leveraging second-order insights from OCO (Hazan–Agarwal–Kale) for regression-like losses. This yields a concrete regret bound for the dynamics estimator, which then underpins planning performance.
Finally, continual RL studies such as EWC and selective experience replay (Isele & Cosgun) crystallized the forgetting problem when directly fine-tuning policies. By shifting the burden of continual adaptation to an online dynamics learner and using MPC for decision making, the paper sidesteps policy-parameter interference and replay dependence, aligning the practical strengths of model-based planning with the stability and guarantees of online learning.

---
*Generated: 2026-01-07T00:21:32.399634*

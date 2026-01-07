# Prior Work Analysis Report

## Target Paper
**Title:** 5hyfZ2jYfI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

TEDUO’s core contribution—offline learning of generalizable, language-conditioned policies from low-fidelity unlabeled data using LLMs in a dual role—stands on three intertwined lines of prior work. First, the synergy between language models and reinforcement learning was crystallized by SayCan, which coupled LLM planning with value-grounded affordances; TEDUO extends this blueprint to the offline regime, using the LLM both to guide and to structure data. Second, the feasibility of turning unlabeled corpora into instruction-rich supervision was enabled by Self-Instruct and the instruction-following capabilities established by InstructGPT. TEDUO operationalizes these insights by having an LLM automatically annotate offline trajectories with semantically rich goals and decompositions, then relying on the LLM’s robust instruction-following behavior to generalize beyond seen goals. Third, stable offline RL foundations—particularly IQL’s practical learning dynamics and CQL’s conservatism against out-of-distribution actions—directly address distributional shift when learning from augmented, low-fidelity datasets, forming the algorithmic backbone of TEDUO’s policy optimization. Finally, BabyAI and TextWorld define the symbolic, language-grounded environments and expose systematic generalization challenges that TEDUO targets. Together, these works shape TEDUO’s pipeline: LLM-driven data enrichment to convert raw trajectories into language-conditioned supervision; offline RL training that respects dataset support while enabling generalization; and LLM-based instruction following to execute novel goals in symbolic domains.

---
*Generated: 2026-01-07T00:21:32.386029*

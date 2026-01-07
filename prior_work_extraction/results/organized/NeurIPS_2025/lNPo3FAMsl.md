# Prior Work Analysis Report

## Target Paper
**Title:** lNPo3FAMsl
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution—attention-aware inverse planning—arises at the intersection of inverse planning/IRL and theories of bounded rationality and attention. Ziebart et al.’s MaxEnt IRL provided the canonical machinery for inferring latent determinants of behavior from demonstrations; Baker et al. reframed this as Bayesian inverse planning to infer mental states, establishing that goal-directed action can reveal hidden cognitive variables. Jara-Ettinger et al. expanded this view to richer theory-of-mind constructs, legitimizing inference over latent internal states beyond rewards. The present work adopts that lens but targets attention specifically.

The pivot to attention is theoretically grounded in rational inattention (Sims), which models attention as an information bottleneck shaping decisions, and in information-theoretic bounded rationality for control (Ortega & Braun), which links policy structure to information-processing costs. These perspectives motivate parameterizing attentional biases as latent, resource-limited filters that modulate perceived state features and, consequently, action choices. Evans et al. provide the methodological precedent for jointly accounting for preferences and cognitive limitations when inverting behavior, a key step in distinguishing reward from attention-induced deviations from classical optimality.

Empirically, the aDDM tradition (Krajbich et al.) demonstrates that where people look systematically biases choices, justifying the premise that attentional strategies leave identifiable signatures in behavior even without direct gaze measurements. Combining these streams, the paper formulates and solves an inverse problem that recovers attentional bias parameters—operationalized within deep RL forward models—from observed actions, thereby extending IRL from reward inference to inference over attention-shaped cognition in real-world driving.

---
*Generated: 2026-01-07T00:21:32.242928*

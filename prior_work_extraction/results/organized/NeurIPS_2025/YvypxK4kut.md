# Prior Work Analysis Report

## Target Paper
**Title:** YvypxK4kut
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

ABC (Alignment by Classification) draws a direct lineage from preference learning in LLMs to diffusion models, while rethinking the objective used to exploit human comparisons. InstructGPT established that human pairwise preferences can reliably steer generative models, laying the problem framing ABC targets. DPO subsequently showed that preferences can be optimized without reinforcement learning by comparing a policy to a reference model through a Bradley–Terry–style likelihood; this is the key conceptual step ABC builds upon. However, DPO’s dependence on a suboptimal SFT reference can bias learning, motivating ABC’s core innovation: recasting alignment as a classification problem that learns directly from preference-labeled data and an idealized reference, avoiding explicit reward models or fragile reference policies.

Within the diffusion domain, classifier guidance demonstrated that discriminative signals can steer sampling, providing precedent for classifier-driven control of diffusion systems. ABC generalizes this idea from sampling-time guidance to a training objective, using preference-derived class labels to shape the generator. Contemporary T2I alignment via reward models—ImageReward and PickScore—validated that large-scale human comparisons are effective supervision, but they require training and maintaining separate reward predictors. ABC sidesteps this by transforming comparisons into fully supervised training signals and optimizing a classification-based loss, effectively turning preference alignment into a simpler, stable supervised learning problem rooted in the Bradley–Terry formulation. Together, these works directly inform ABC’s classification-centric, reference-light approach to aligning diffusion models with human preferences.

---
*Generated: 2026-01-06T23:42:48.126000*

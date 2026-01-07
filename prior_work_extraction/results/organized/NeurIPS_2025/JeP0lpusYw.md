# Prior Work Analysis Report

## Target Paper
**Title:** JeP0lpusYw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

HM3 bridges parameter-space and architecture-space model merging by stacking proven ideas into a coherent bilevel, multi-objective framework. At the inner (parameter) level, it builds directly on weight-averaging methods such as Model Soup and conflict-aware schemes like Fisher-weighted averaging and TIES-Merging, using them as fast solvers to produce robust merged checkpoints without data. These stabilized parameters become the substrate for HM3’s outer (architecture) level, which takes inspiration from PathNet’s concept of composing functional pathways from pretrained modules. Rather than evolutionary selection, HM3 formalizes path construction as a Markov decision process and employs an actor–critic strategy akin to reinforcement-learning NAS, enabling sequential layer-granular decisions. The discrete, expert-style selection of layers echoes Switch Transformers’ routing, underscoring the feasibility of sparse, compatibility-conscious choices at each depth. To steer the search toward practically valuable designs, HM3 frames objectives—such as accuracy, compute, and layer compatibility—within a multi-objective optimization paradigm inspired by NSGA-II, seeking Pareto-optimal trade-offs across both levels. Together, these strands yield a hierarchical merging methodology that first mitigates parameter interference and then discovers efficient inference paths across heterogeneous architectures, directly extending parameter-only merging into the architecture domain while preserving data-free practicality.

---
*Generated: 2026-01-06T23:42:48.104791*

# Prior Work Analysis Report

## Target Paper
**Title:** NbYAmsFJrc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Trajectory Aggregation Tree (TAT) is motivated by the success and limitations of diffusion-based planners. Denoising Diffusion Probabilistic Models established the non-autoregressive generative machinery that enables trajectory-level sampling, and Diffuser extended this idea to decision-making, showing strong long-horizon performance but also exposing the practical risk of infeasible samples due to stochasticity. Prior attempts to steer diffusion outputs—such as classifier-free guidance—modify the sampling dynamics or require auxiliary conditioning; in contrast, TAT aims to be training- and sampler-agnostic.
To achieve robustness without retraining, TAT synthesizes ideas from sample-based planning and tree search. PETS popularized sampling many trajectories and selecting elites (often via CEM), illustrating how aggregate statistics over trajectories can improve reliability; TAT generalizes this by organizing repeated diffusion rollouts into a dynamic state/trajectory tree, rather than committing to a single elite path. Classical tree-search principles further inspire TAT’s structure: UCT shows how simulated rollouts can populate a search tree with principled node prioritization, while RRT demonstrates how sampling can grow trees that explore feasible regions of state space. Finally, MBPO’s use of ensembles and multiple rollouts to temper model bias aligns with TAT’s core mechanism—marginalizing unreliable states/branches by pooling evidence across historical and current predictions. Together, these strands directly inform TAT’s key contribution: a training-free, trajectory-aggregation tree that prioritizes robust nodes and resists stochastic failure modes of diffusion planners.

---
*Generated: 2026-01-07T00:02:04.885239*

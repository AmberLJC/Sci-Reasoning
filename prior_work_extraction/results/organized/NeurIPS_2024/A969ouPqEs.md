# Prior Work Analysis Report

## Target Paper
**Title:** A969ouPqEs
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DiffLight fuses two lines of prior work: (1) offline decision-making via generative trajectory models and (2) diffusion-based conditional generation for imputation. From the offline RL side, Decision Transformer and Trajectory Transformer established that trajectories can be modeled generatively and controlled via conditioning (e.g., on return). Diffuser then showed that diffusion models are particularly effective for trajectory synthesis and goal/return conditioning in control. DiffLight inherits this trajectory-level conditional generation but introduces Partial Rewards Conditioned Diffusion to cope with missing rewards—adapting the return-conditioning idea to scenarios where only subsets of rewards are available, and preventing spurious gradients from incomplete signals.
On the generative modeling side, the foundational DDPM and score-based SDE frameworks provide the denoising/score estimation machinery and conditional sampling strategies that enable DiffLight to jointly impute missing traffic states while generating decisions. This joint imputation–policy synthesis is central to operating in real-world TSC where sensor outages create partial observability. Finally, domain-specific advances in traffic networks guide the architecture. PressLight motivates a network-level objective (pressure-based reward and multi-intersection coordination), highlighting the importance of robust control under incomplete sensing. GMAN’s spatiotemporal attention for traffic forecasting informs DiffLight’s STFormer, which captures spatial and temporal dependencies among intersections despite missing data. Together, these works converge to enable DiffLight’s integrated diffusion-based imputation and reward-conditioned decision-making for TSC with missing data.

---
*Generated: 2026-01-07T00:02:04.737476*

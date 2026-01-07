# Prior Work Analysis Report

## Target Paper
**Title:** QtnCPZMxYg
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core innovation of Trajectory Graph Learning is to align policies directly with expert-labeled long trajectories—maximizing the probability of generating those trajectories—while avoiding reward design. This builds on a lineage that first framed expert behavior through reward inference. Abbeel and Ng (2004) introduced apprenticeship learning via IRL, revealing reward ambiguity that often undermines faithful behavior replication. Ziebart’s Maximum Entropy IRL (2008) shifted the perspective to probability distributions over trajectories via maximum-likelihood principles, foreshadowing the paper’s trajectory-level likelihood view, yet still tied to reward parameterization. In parallel, imitation learning advanced through DAgger (Ross et al., 2011), whose analysis of compounding errors under per-state supervision highlighted the need to preserve long-horizon coherence rather than just matching local actions. GAIL (Ho & Ermon, 2016) removed explicit reward design by matching occupancy measures adversarially, but primarily at marginal distributions, leaving room for methods that explicitly respect sequence structure. Preference-based approaches, notably Christiano et al. (2017) and T-REX (2019), injected trajectory-level supervision (comparisons or rankings) to capture long-horizon behavior, though they reintroduced reward modeling with its ambiguity and distribution mismatch. Recent sequence-level direct optimization like DPO (2023) demonstrated that one can align policies to preferences without a reward model, conceptually motivating this work’s direct likelihood maximization on trajectories. The present paper synthesizes these threads, formalizing trajectory-level alignment (including its NP-completeness) and proposing a graph-based learning procedure that preserves long-horizon structure without surrogate rewards.

---
*Generated: 2026-01-07T00:21:32.241413*

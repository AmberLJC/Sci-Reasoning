# Prior Work Analysis Report

## Target Paper
**Title:** RxkCwOKVKa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The lineage of this paper’s core idea—breaking RL performance ceilings through an inference-phase strategy—traces to online planning and budgeted search. UCT (Kocsis & Szepesvári, 2006) formalized Monte Carlo Tree Search as an inference-time allocation of limited simulations, seeding the notion that execution-time computation can materially improve decisions. AlphaZero (Silver et al., 2018) transformed this into practice: policies that plateau when used greedily were vaulted to superhuman performance by coupling them with MCTS at inference. MuZero (Schrittwieser et al., 2020) reinforced the principle by showing that even learned models, when used for planning at test time, systematically outperform pure feed-forward action selection.
In partially observable and large spaces, POMCP (Silver & Veness, 2010) established scalable online planning with particle filters, again hinging on how a finite inference budget is deployed. In continuous-control settings, PETS (Chua et al., 2018) exemplified compute-bounded inference via CEM planning over learned dynamics, using multiple sampled trajectories to choose high-return actions.
A parallel thread in neural combinatorial optimization showed that test-time compute can be harnessed without new training: Active Search (Bello et al., 2017) and sampling-based decoding for routing (Kool et al., 2019) markedly improved solutions by generating multiple candidates and selecting the best under a budget. This paper synthesizes these strands, arguing that for complex, often multi-agent RL problems, the decisive lever is not further training of a single policy but the design of an inference strategy—search, sampling, or selection—operated within a time/compute budget. Their empirical gains validate this unifying perspective.

---
*Generated: 2026-01-07T00:02:04.953737*

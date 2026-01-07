# Prior Work Analysis Report

## Target Paper
**Title:** e93ffDcpH3
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of BASED is to expose and exploit a precise recall–throughput (memory) tradeoff governed by a model’s recurrent state size, and to realize a simple, tunable architecture that rides the Pareto frontier by combining linear attention with sliding-window attention. This builds on the strengths and weaknesses of prior paradigms. Full softmax attention (Vaswani et al., 2017) sets the high-recall gold standard but incurs prohibitive KV-cache memory at inference. Linear attention works (Katharopoulos et al., 2020; Choromanski et al., 2020) recast attention as a constant-state recurrence whose capacity scales with the feature dimension, directly inspiring BASED’s “dial” for global aggregation with predictable memory cost. Meanwhile, sparse/local patterns such as Longformer (Beltagy et al., 2020) demonstrate that sliding-window attention can retain strong short-range recall at low compute, motivating BASED’s local branch to capture precise nearby dependencies cheaply.
In contrast, state-space and RNN-like alternatives—H3, Mamba, and RWKV—show that fixed-size recurrent states yield excellent throughput but struggle to recall arbitrary distant tokens, empirically motivating the tradeoff BASED formalizes. By explicitly decomposing recall into a local, high-fidelity channel (sliding window) and a global, linear kernel channel whose state dimension is user-controlled, BASED inherits the efficiency of fixed-state models while recovering the strong recall behavior of attention. These prior works collectively shaped BASED’s insight that recall capacity is essentially a function of state size, and its design that cleanly interpolates between memory footprint and recall fidelity.

---
*Generated: 2026-01-07T00:02:04.872653*

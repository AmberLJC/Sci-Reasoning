# Prior Work Analysis Report

## Target Paper
**Title:** KT8y9pFgJE
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The key innovation—dense linear RNNs realized as fixed points of parallelizable diagonal recurrences—emerges from converging strands in SSMs, diagonal RNNs, and implicit layers. S4 provided the modern SSM/linear RNN formalism, demonstrating how stable continuous-time dynamics yield scalable sequence models. S4D and subsequent practice cemented the efficiency and competitiveness of diagonal, per-channel state matrices, but also exposed a critical limitation: insufficient cross-channel state interaction for full RNN-like state tracking. LRU strengthened this diagonal lineage by stabilizing linear recurrences and showing strong results on long-memory benchmarks with highly parallel computation. In parallel, IndRNN earlier established both the practicality of diagonal recurrence and its expressivity ceiling when channels remain decoupled. The Mamba architecture took diagonal SSMs mainstream with selective scan and linear-time inference, becoming a prime target for overcoming channel-wise mixing constraints without forfeiting speed. Finally, Deep Equilibrium Models supplied the methodological lever: fixed-point parameterization and implicit differentiation allow one to wrap efficient diagonal dynamics inside an implicit layer that expresses dense coupling while preserving parallelism. Fixed-Point RNNs thus interpolate from diagonal to dense at fixed parameter budgets, reconciling the efficiency of modern SSMs with the cross-channel state-tracking expressivity traditionally reserved for fully dense RNNs, and delivering SOTA on state-tracking tasks.

---
*Generated: 2026-01-06T23:42:48.111898*

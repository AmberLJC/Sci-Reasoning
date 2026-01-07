# Prior Work Analysis Report

## Target Paper
**Title:** 2bdSnxeQcW
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

Exclusively Penalized Q-learning (EPQ) is situated within the constraint-based offline RL literature that combats distributional shift by injecting conservatism, but it specifically addresses underestimation bias created by overly broad value penalties. The foundational motivation traces to BCQ, which crystallized the notion of extrapolation error from out-of-distribution actions and advocated remaining within dataset support. BEAR and BRAC subsequently formalized this principle through behavior-policy regularization, showing that constraining the learned policy can curb bootstrapping error, albeit sometimes at the cost of undue conservatism. CQL shifted the locus of conservatism from the policy to the critic, introducing pessimistic Q-function regularization that is highly effective but can uniformly depress values and lead to underestimation. SPIBB provided an important complementary idea: conservatism should be selective and data-dependent, with stronger caution where coverage is weak. EPQ synthesizes these strands by keeping the simplicity and practicality of value-function penalties (as in CQL) while adopting a SPIBB-like selectivity principle, operationalized at the state level—penalizing only states likely to induce estimation errors due to distributional shift. This stands in contrast to IQL, which reduces over/underestimation through robust value estimation rather than explicit penalties; EPQ preserves the penalty framework but makes it targeted. The result is a method that maintains the safety benefits of pessimism where needed while mitigating unnecessary underestimation elsewhere, improving accuracy and performance across offline control tasks.

---
*Generated: 2026-01-07T00:02:04.754288*

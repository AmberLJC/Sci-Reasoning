# Prior Work Analysis Report

## Target Paper
**Title:** 004uTlSufe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution—characterizing the best achievable precision of one-run differential privacy (DP) auditing and identifying interference between perturbed records as the limiting factor—builds squarely on Steinke et al.’s introduction of one-run auditing and proof that it yields a valid lower bound on privacy. To evaluate how close a one-run audit can get to the true privacy parameter, the paper leverages analytical accounting frameworks. Abadi et al.’s DP-SGD provides the primary audited algorithm and the practical context in which one-run audits are deployed, while Mironov’s Rényi Differential Privacy and Kairouz–Oh–Viswanath’s optimal composition offer precise, compositional ground truths for ε,δ against which auditing tightness can be measured. Dong–Roth–Su’s Gaussian Differential Privacy furnishes a hypothesis-testing view and tight tradeoff curves, aligning the audit’s statistical power with privacy’s fundamental distinguishability limits. The signal-design aspect of one-run audits is directly inspired by Carlini et al.’s canary methodology for measuring memorization; the new paper explains how multiple, simultaneous canaries can collide, creating interference that degrades audit efficacy. Finally, Shokri et al.’s membership inference establishes the broader black-box testing paradigm that informs the audit-as-hypothesis-test framing. Together, these works lead to the present paper’s central insight: one-run auditing’s precision is bottlenecked by interactions among perturbed records, and improving practice requires designing interventions and tests that minimize such interference while remaining statistically powerful.

---
*Generated: 2026-01-06T23:42:48.132413*

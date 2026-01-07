# Prior Work Analysis Report

## Target Paper
**Title:** ZtTWKr51yH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The core innovation of Constrained Adaptive Attack (CAPGD/CAA) marries robust gradient-based optimization with realistic tabular constraints and search-based complementarity. At its foundation, the method builds on PGD’s iterative update-plus-projection scheme, but replaces the standard Lp projection with a tabular-aware operator that enforces immutability, category validity, and feature relationships. To make gradient attacks effective and reliable without parameter sweeps, the authors adopt the adaptive, tuning-free spirit of APGD from AutoAttack—transferring oscillation and backtracking step-size rules to a setting where each step must remain within a mixed discrete–continuous feasible set. The choice of margin-focused losses and careful constraint enforcement reflects lessons from the C&W attack, which showed how strong objectives and constrained optimization markedly increase attack success.

Tabular-specific feasibility considerations trace back to early evasion attacks on structured models (e.g., tree ensembles), which highlighted that realistic adversaries must respect domain semantics and immutable attributes. This perspective is reinforced by actionable recourse research, which formalizes immutable features, feasible action sets, and dependency constraints—concepts the paper encodes directly in CAPGD’s projection and masking. Finally, the hybrid CAA leverages MOEVA, the leading search-based tabular attack, to complement gradients with evolutionary exploration for categorical and combinatorial changes. Together, these works directly shaped CAPGD’s constraint-aware, adaptive gradient design and CAA’s hybridization, yielding a state-of-the-art, tuning-free evaluation attack suite for deep tabular models.

---
*Generated: 2026-01-06T23:33:35.527518*

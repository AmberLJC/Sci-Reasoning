# Prior Work Analysis Report

## Target Paper
**Title:** 1OsRSrkFWl
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper fuses two mature lines of work—online resource allocation and formal fairness—to define and solve equity-driven allocation with sequential arrivals under distributional models. From the online allocation side, AdWords-style primal–dual methods and stochastic arrival models (Mehta et al.; Feldman et al.) supply the canonical setting: resources with capacities, heterogeneous agents, and ex-ante analysis relative to a stochastic benchmark. Agrawal–Devanur’s online stochastic convex programming provides the technical playbook for embedding additional structure—here, equity constraints—into distribution-aware primal–dual updates with concentration-based ex-post control.
On the fairness side, the external equity requirement (proportional-to-demand guarantees across arrival times) traces to proportional fairness and DRF: Kelly et al. establish convex formulations of proportional sharing, while DRF crystallizes fairness-by-demand in multi-resource environments; this paper adapts these principles to dynamic, stochastic arrivals and proves guarantees both in expectation (ex-ante) and on realized sequences (ex-post). The internal equity model maps group-level fairness to allocation: bandit fairness (Joseph et al.) clarifies ex-ante vs ex-post fairness in sequential decisions, and fair classification via reduction (Agarwal et al.) motivates implementing demographic-parity-like constraints as convex conditions that an online allocator can track. Together, these works enable the paper’s core contribution: principled online policies that achieve equitable resource shares proportional to demands or group prevalence, with rigorous ex-ante and ex-post guarantees under realistic stochastic arrival assumptions.

---
*Generated: 2026-01-06T23:42:48.077746*

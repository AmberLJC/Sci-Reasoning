# Prior Work Analysis Report

## Target Paper
**Title:** teUg2pMrF0
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LLM-LNS sits at the intersection of classical neighborhood design in MILP and modern learning- and LLM-based automation. Foundationally, Shaw’s original Large Neighborhood Search established destroy-and-repair as the driver of performance, while Ropke and Pisinger’s ALNS introduced adaptive, performance-weighted neighborhood selection to balance intensification and diversity. For MILP specifically, Fischetti and Lodi’s Local Branching and Danna et al.’s RINS grounded neighborhood definition and solver-guided repair, showing how structured neighborhoods around incumbents yield robust progress when coupled with MILP solvers. These works collectively define the space of neighborhood construction, adaptive selection, and solver-aware repair that LLM-LNS aims to automate.
On the learning side, Hottung and Tierney demonstrated that neural policies can learn effective destroy/repair moves for LNS, but at notable training cost and with scaling challenges. Gasse et al. showed similar trade-offs for ML inside MILP (branching): strong gains but substantial data/compute requirements. LLM-LNS’s key move is to replace heavy supervised training with a dual-layer LLM agent: an inner layer that evolves heuristic strategies in solver-compatible MILP neighborhoods (echoing local branching/RINS intensification) and an outer layer that evolves prompts to maintain diversity (akin to APE-style prompt optimization). This design leverages LLMs’ few-shot generalization to discover, adapt, and select neighborhoods from small instances, then transfer to large-scale MILPs—preserving the strengths of LNS and MILP-specific neighborhoods while avoiding the cost of training bespoke neural policies.

---
*Generated: 2026-01-07T00:04:09.164636*

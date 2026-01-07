# Prior Work Analysis Report

## Target Paper
**Title:** I50HbChk3U
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The core contribution of Provably Bounding Neural Network Preimages is INVPROP: a GPU-accelerated, solver-free algorithm that propagates linear constraints from outputs backward to inputs to over-approximate the preimage of linearly constrained output sets, with optional branch-and-bound (BaB) refinement. This innovation directly builds on the linear relaxation and dual-network foundations laid by Wong and Kolter (2018) and Dvijotham et al. (2018), which framed verification as propagating or optimizing over linear bounds via Lagrangian duality. CROWN (Zhang et al., 2018) supplied the practical, GPU-friendly mechanics of linear bound propagation and back-substitution—techniques INVPROP repurposes for inverse propagation of output polyhedral constraints. IBP (Gowal et al., 2018) reinforced the value of simple, scalable, solver-free propagation, a design ethos reflected in INVPROP’s avoidance of LP solvers. For completeness and tightness, INVPROP follows the BaB paradigm articulated by Bunel et al. (2018), using branching to tighten relaxations; it further inherits α,β-CROWN’s (Xu et al., 2021) insight that optimizing bound slopes and integrating efficient bound propagation within BaB yields state-of-the-art tightness and speed. Together, these works provide the dual-relaxation perspective, LiRPA toolset, and BaB integration strategy that INVPROP extends to the inverse verification problem, enabling precise, GPU-accelerated preimage bounds applicable to backward reachability, robustness, and OOD detection.

---
*Generated: 2026-01-06T23:42:49.057980*

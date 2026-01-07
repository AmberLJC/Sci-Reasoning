# Prior Work Analysis Report

## Target Paper
**Title:** zSrb8rtH9M
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper’s core contribution—a principled characterization of MoE expressivity for structured tasks—sits at the intersection of classic MoE design, deep-network expressivity, and structure-exploiting approximation theory. The original MoE formulation (Jacobs et al., 1991) and its hierarchical extension (Jordan & Jacobs, 1994) establish gating-driven partitions and layered compositions of experts. This conceptual scaffold is essential for the paper’s E^L-piece result: by cascading gating decisions across L layers, deep MoEs inherit a combinatorial partitioning akin to decision trees, but implemented by learnable soft gates.
Parallel advances in deep expressivity theory inform how depth yields exponential capacity. Montúfar et al. (2014) show ReLU networks generate exponentially many linear regions, a template this work adapts to MoE partitions controlled by the number of experts per layer. Mhaskar & Poggio (2016) further argue that deep architectures excel on compositional functions; the paper leverages this perspective to formalize “compositional sparsity” in MoEs and quantify when depth is beneficial.
On the approximation-theoretic side specific to MoEs, Jiang & Tanner (1999) validate that (hierarchical) MoEs can approximate broad function classes, which the present work refines by pinpointing rates and counts under sparsity and depth constraints. For manifold-structured targets, Shaham–Cloninger–Coifman (2015) provide dimension-sensitive bounds for deep nets; here, shallow MoEs are shown to achieve similar ambient-dimension–free approximation by using gating to localize experts to manifold charts. Finally, modern sparse MoE practice (Shazeer et al., 2017) motivates analyzing how gating design, number of experts, and depth jointly govern expressivity—the very hyperparameters dissected in the new theory.

---
*Generated: 2026-01-07T00:02:04.959089*

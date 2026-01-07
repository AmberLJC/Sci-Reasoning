# Prior Work Analysis Report

## Target Paper
**Title:** zWHKKspghT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Mozart’s key contribution—an algorithm–hardware co-design that confines MoE all-to-all within a 3.5D wafer-scale chiplet package and overlaps communication with computation via token/expert streaming—sits at the intersection of two lines of prior work. On the algorithmic and systems side, Shazeer et al. defined the sparse, modular expert paradigm, while GShard operationalized expert parallelism and its signature all-to-all exchange. Switch Transformers demonstrated that simplified (top-1) routing with capacity management can make sparse dispatch efficient, shaping the traffic patterns that Mozart ultimately pipelines. DeepSpeed-MoE and Tutel then pushed the MoE runtime forward with hierarchical all-to-all, fused dispatch/combine, and topology-aware token packing, directly informing Mozart’s expert placement and its fine-grained, streaming scheduler that maximizes compute–communication overlap. Complementing these, MegaBlocks showed that structured, block-sparse organization improves utilization—an idea Mozart echoes when structuring token/expert streams to match chiplet granularities. On the hardware side, the Cerebras Wafer-Scale Engine established the efficacy of wafer-scale integration and localized fabrics for deep learning, motivating Mozart’s 3.5D approach that marries a 2.5D network-on-package tree with vertically integrated memory/logic to co-locate heterogeneous modules. Together, these works converge in Mozart: it physically grounds MoE’s modularity by aligning experts to chiplets, transforms logical hierarchical all-to-all into on-package NoP-tree exchanges, and uses streaming schedules inspired by MoE runtimes to fully exploit the wafer-scale chiplet fabric.

---
*Generated: 2026-01-07T00:05:12.549713*

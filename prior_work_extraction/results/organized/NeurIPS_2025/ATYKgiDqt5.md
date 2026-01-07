# Prior Work Analysis Report

## Target Paper
**Title:** ATYKgiDqt5
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The proposed Message Passing Complexity (MPC) emerges from reconciling two established lines of GNN theory: the WL-based expressivity viewpoint and the practical limitations of message passing. Gilmer et al. provided the formal MPNN framework that MPC explicitly targets, i.e., quantifying how hard a task is when solved via local message exchanges. On the expressivity side, Xu et al. rigorously tied standard GNNs to the 1-WL test and showed that simple architectures can already reach the WL ceiling; Morris et al. extended this to higher-order models, charting a hierarchy of expressivity. MPC positions itself as orthogonal: while preserving the impossibility results implied by these WL-based analyses, it critiques their binary nature and idealized assumptions by supplying a continuous, task-specific difficulty measure.
Crucially, MPC is motivated by practical bottlenecks in information propagation. Alon and Yahav identified over-squashing as a dominant failure mode for long-range dependencies; Topping et al. further connected this to graph geometry and curvature, providing diagnostics of where and why messages are compressed. Oono and Suzuki theoretically established depth-induced contraction, explaining why simply adding layers often degrades information fidelity. MPC operationalizes these phenomena into a quantitative lens that predicts when and why message passing will struggle, while remaining consistent with the logical expressivity limits captured by Grohe. Together, these works directly inform MPC’s central contribution: a principled, continuous measure that bridges expressivity theory with the real, architecture- and graph-dependent difficulty of GNN tasks.

---
*Generated: 2026-01-06T23:42:48.131476*

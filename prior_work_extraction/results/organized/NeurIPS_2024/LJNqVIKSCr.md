# Prior Work Analysis Report

## Target Paper
**Title:** LJNqVIKSCr
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DESP sits at the intersection of three lines of work: neural-guided CASP search, classical bidirectional/heuristic search, and goal-conditioned value estimation. Segler et al. (2018) demonstrated that learned policies and values can dramatically improve retrosynthetic tree search, while Coley et al. (2017) showed that template-based expansions prioritised by learned scoring can operationalize search on AND/OR-like structures. These CASP systems, and the practical MCTS implementation in AiZynthFinder (Genheden et al., 2020), typically assume success once any stock building blocks are reached; in contrast, real-world constraints often require specific starting materials. Chematica/SYNTHIA’s formulation (Szymkuć et al., 2016) emphasized availability constraints within reaction-network search, underscoring the need for constraint-aware planning that DESP explicitly addresses. 
At the algorithmic core, DESP brings classical heuristic-search principles to retrosynthetic hypergraphs. A* (Hart et al., 1968) motivates the use of learned cost-to-go estimates for best-first expansion, but DESP’s key advance is to instantiate a bidirectional scheme inspired by Pohl’s (1971) bidirectional heuristic search—interleaving expansions from the target and from the specified starting materials to ensure goal satisfaction and shrink search. Finally, DESP’s goal-conditioned cost network is a direct application of Universal Value Function Approximators (Schaul et al., 2015), conditioning the learned cost on the desired starting-material set and training it offline from a partially observed reaction hypergraph. Together, these strands yield a principled, data-driven, double-ended search that improves solve rates and efficiency under explicit starting-material constraints.

---
*Generated: 2026-01-06T23:33:36.253228*

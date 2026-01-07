# Prior Work Analysis Report

## Target Paper
**Title:** Fkckkr3ya8
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper’s core contribution—formalizing compositional tasks as computation graphs to quantify reasoning complexity and revealing that transformers often reduce multi-step reasoning to linearized subgraph matching—builds on a converging line of empirical, methodological, and theoretical work. Lake and Baroni’s SCAN laid the foundation by showing neural models struggle with systematic compositional generalization, establishing the central phenomenon this paper interrogates at scale in modern LLMs. Keysers et al.’s CFQ introduced graph-based decompositions and compositional splits (MCD), directly inspiring the present work’s computation-graph formalization and complexity metrics. Complementing this, Hupkes et al. provided a principled framework for decomposing compositionality into sub-operations, shaping the paper’s breakdown of tasks into intermediate sub-procedures across multiplication, logic puzzles, and dynamic programming.
On the task side, Saxton et al.’s arithmetic benchmarks contextualize the use of multi-digit multiplication and algorithmic reasoning to probe generalization beyond surface patterns. The paper’s interpretation of failures as reflecting structural constraints is supported by theoretical results like Hahn’s, which establish limits of self-attention on hierarchical/algorithmic computations. Finally, recent prompting methods—Chain-of-Thought and Least-to-Most—serve as baselines for eliciting intermediate reasoning; by contrasting these techniques with its computation-graph analysis, the paper demonstrates that even when models produce step-by-step outputs, their behavior often aligns with shortcut, linearized heuristics rather than faithful compositional execution. Together, these works scaffold the paper’s framework and its central finding about the fate of compositionality in transformers.

---
*Generated: 2026-01-07T00:02:04.794232*

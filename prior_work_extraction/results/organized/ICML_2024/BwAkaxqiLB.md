# Prior Work Analysis Report

## Target Paper
**Title:** BwAkaxqiLB
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EoH sits at the confluence of three lines of work: hyper-heuristics and automatic algorithm design, program-level search/evolution, and LLM-based reasoning/coding. Foundational AHD ideas from hyper-heuristics (Burke et al., 2013) and configuration (ParamILS) establish the central principle of evaluating candidate heuristics across problem instances and selecting the best—EoH inherits this evaluation-driven loop to promote generalization. From the program-evolution tradition (Koza’s Genetic Programming), EoH borrows the notion of evolving executable artifacts, but replaces brittle syntactic mutations with an LLM capable of translating and repairing code from higher-level descriptions. This directly connects to recent program search systems like FunSearch, which couple an LLM with a verifier; EoH advances that template by explicitly co-evolving two coupled representations—the natural-language “thoughts” that describe heuristic ideas and the code that implements them—using evolutionary operators to explore and recombine both spaces efficiently. Chain-of-Thought prompting provides the representational insight that intermediate, textual reasoning can serve as a manipulable object of search, making the heuristic space interpretable and amenable to guided variation. Finally, algorithm discovery efforts such as AlphaDev and neural combinatorial optimization demonstrate the power of performance-guided search for CO; EoH targets the same domain but achieves greater flexibility by searching over human-readable heuristic ideas and leveraging LLM codegen, yielding competitive or superior heuristics with lower computational budgets.

---
*Generated: 2026-01-06T23:42:48.057674*

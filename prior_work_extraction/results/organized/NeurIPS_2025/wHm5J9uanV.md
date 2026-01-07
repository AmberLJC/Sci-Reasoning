# Prior Work Analysis Report

## Target Paper
**Title:** wHm5J9uanV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CAKE’s core contribution—editing LLM knowledge from wild, unstructured text via a semantic-augmented graph paired with a conflict-aware editing strategy—sits at the intersection of model editing and document-level semantic graph construction. On the editing side, ROME established that factual associations can be localized and surgically modified in transformer MLP layers, but it assumes structured, triplet-style edits and struggles with entangled contexts. MEMIT extended editing to many facts at once and exposed interference phenomena that arise when edits collide, directly motivating CAKE’s explicit conflict-awareness. MEND further formalized the locality–reliability trade-off in gradient-based editing, a principle CAKE operationalizes in graph space so local neighborhoods of semantically linked facts remain consistent. SERAC offered a memory-based route to isolate edits and avoid interference; CAKE borrows the isolation intuition but grounds it in a semantic graph to detect and resolve conflicts intrinsic to unstructured evidence. Mechanistically, Geva et al.’s “key–value memory” view informs where and how to target updates once CAKE has disambiguated the textual knowledge. On the representation side, AMR provides the paradigm for capturing predicate–argument structure, coreference, and roles as a graph, while DYGIE++ demonstrates practical document-level graph construction and reasoning. Together, these works directly shape CAKE’s pipeline: structure messy text into a semantically faithful graph, then perform conflict-aware, localized edits that respect neighboring knowledge.

---
*Generated: 2026-01-07T00:21:32.285257*

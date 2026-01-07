# Prior Work Analysis Report

## Target Paper
**Title:** 92oBV5HAGl
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Mechanistic Unlearning builds on two converging threads: how transformers store facts and how to precisely intervene in those facts. Geva et al. established that feed-forward layers act as key–value memories, crystallizing the lookup-table view of factual recall that this paper explicitly targets. Early editing methods—exemplified by De Cao et al.—framed the desiderata of locality and specificity, which ROME operationalized via causal, layer-localized rank-one updates. MEMIT scaled these ideas to many facts, but also exposed brittleness and format sensitivity, revealing the limits of output-driven localization alone. In parallel, mechanistic interpretability matured from abstract intuitions into concrete circuits with reproducible internal structure: the induction-head work (Olsson et al.) and the IOI circuit (Wang et al.) demonstrated end-to-end mechanisms with predictable intermediate features validated through activation patching. Recent SAE-based decomposition (Bricken et al.) further enabled discovering monosemantic, predictable features inside activations. The present paper synthesizes these lines by localizing unlearning/editing to the specific lookup-table mechanism for factual recall, privileging components whose internal states are interpretable and predictable. This mechanism-grounded localization contrasts with approaches that merely preserve outputs during search, and the results—robust edits/unlearning across formats and resistance to adversarial attempts—directly address the generalization shortcomings observed in prior editing methods.

---
*Generated: 2026-01-07T00:21:32.396035*

# Prior Work Analysis Report

## Target Paper
**Title:** 5x788rqbcj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper’s key contribution is to distinguish memorization from reliable extraction and to causally tie extractability of factual knowledge to diversity learned during pretraining. Foundational evidence that LMs contain factual associations but are brittle to prompt variation comes from LAMA and LPAQA, which showed that phrasing and paraphrase strongly affect recall. AutoPrompt further demonstrated that clever elicitation can unlock knowledge without additional training, framing extraction as an interface problem. The present work shifts this view upstream: it shows that unless pretraining presents facts with diverse surface forms (paraphrasing, shuffling), models memorize but fail to render those facts linearly extractable, and instruction tuning cannot fix that deficit.
Concurrently, security and data-quality studies clarified the memorization landscape. Carlini et al. proved that LMs memorize verbatim training data, while Lee et al. showed that deduplication improves generalization, implying that repeated exposures drive rote storage rather than robust features. Mechanistic insights connect these phenomena to representation geometry: Geva et al.’s key-value memory view and ROME’s linear editability of facts indicate that factual associations live in linearly addressable subspaces. The paper leverages nearly linear probes to empirically link pretraining diversity to the linear accessibility of knowledge, closing the loop between data diversity, representational structure, and downstream QA. Together, these threads suggest that making facts extractable requires training-time augmentation that shapes linearly recoverable representations.

---
*Generated: 2026-01-06T23:42:48.070366*

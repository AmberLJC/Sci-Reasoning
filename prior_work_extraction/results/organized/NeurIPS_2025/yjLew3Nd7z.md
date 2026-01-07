# Prior Work Analysis Report

## Target Paper
**Title:** yjLew3Nd7z
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PARTONOMY’s core contribution—a rigorous benchmark for pixel-level, object-specific part grounding with part-whole reasoning and justification—emerges from three converging threads of prior work. First, classic part datasets laid the empirical foundation for object-specific parts. PASCAL-Part provided early 2D part annotations tightly coupled to object categories, while PartImageNet scaled fine-grained part segmentation across many classes. PartNet contributed a hierarchical view of parts and part-whole relations (albeit in 3D), shaping PARTONOMY’s emphasis on explicit partonomies and cross-object comparability. Second, language–vision grounding benchmarks demonstrated the value of natural language supervision but rarely demanded pixel-accurate, object-specific parts. Visual Genome’s part-of relations inspired PARTONOMY’s compositional reasoning dimension, and the RefCOCO family established language-to-region grounding that PARTONOMY elevates to part-level segmentation and inter-object comparisons with technical terminology. Third, the recent wave of segmentation-enabled LMMs created both opportunity and urgency. Segment Anything enabled promptable masks that many LMMs rely on, yet it is category-agnostic and not tailored to object-specific part semantics. LISA exemplified coupling LLM reasoning with segmentation, but its weak performance on PARTONOMY underscores a gap: current LMM pipelines cannot reliably map precise, technical part descriptions to pixel-accurate masks and justify predictions. By unifying and extending part datasets, encoding hierarchical part-whole structure, and enforcing language-grounded, mask-based justification, PARTONOMY crystallizes these lines of work into a focused stress test for part-level multimodal understanding.

---
*Generated: 2026-01-07T00:05:12.526778*

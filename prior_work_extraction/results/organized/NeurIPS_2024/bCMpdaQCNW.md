# Prior Work Analysis Report

## Target Paper
**Title:** bCMpdaQCNW
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

YesBut’s core contribution—a benchmark that isolates whether LVLMs can understand humorous contradictions created by juxtaposed panels—stands on three pillars developed by prior work: inter-panel narrative reasoning, robust multimodal evaluation design, and the cognitive theory of humor as incongruity. The COMICS dataset (Iyyer et al., 2017) first framed comics as a laboratory for narrative inference across panels, directly inspiring YesBut’s two-panel unit and tasks that require connecting setups and punchlines. From the evaluation-design perspective, Hateful Memes (Kiela et al., 2020) demonstrated how to craft multimodal datasets that curb unimodal shortcuts, a principle YesBut adopts to ensure humor recognition requires genuine cross-modal, cross-panel reasoning. Winoground (Thrush et al., 2022) revealed persistent LVLM weaknesses in compositional binding, motivating YesBut’s emphasis on subtle narrative reversals where small changes in context flip meanings. VCR (Zellers et al., 2019) contributed the idea of tiered tasks progressing from perception to explanation, which YesBut mirrors with stages from literal content to deep narrative interpretation. NLVR2 (Suhr et al., 2019) provided a template for multi-image contradiction verification that maps naturally to two-panel comics. Because many comics hinge on embedded text, ST-VQA (Biten et al., 2019) underlines the necessity of OCR-aware reasoning included in YesBut’s easier tasks. Finally, Koestler’s bisociation theory (1964) gives the conceptual backbone, formalizing humor as the collision of incompatible frames—precisely the phenomenon YesBut operationalizes to probe LVLM narrative understanding.

---
*Generated: 2026-01-07T00:02:04.736472*

# Prior Work Analysis Report

## Target Paper
**Title:** FuGps5Zyia
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

AH2AC2’s core contribution—reproducible, scalable evaluation of ad-hoc human-AI coordination in Hanabi via human proxy agents trained on limited human data—emerges at the intersection of three lines of prior work. First, The Hanabi Challenge codified Hanabi as a demanding cooperative benchmark with ad-hoc team play and highlighted the logistical barriers of human evaluation, directly motivating a standardized, repeatable alternative. Second, Overcooked-AI established a practical methodology for human-AI collaboration research: collect modest human gameplay datasets and train behavioral-cloning proxy models to approximate human partners, enabling cheap and reproducible assessment. AH2AC2 explicitly adopts and adapts this proxy paradigm to the Hanabi domain, where theory-of-mind and constrained communication intensify the need for high-fidelity human-like evaluators.

Third, algorithmic advances targeting ad-hoc/zero-shot coordination in Hanabi—Fictitious Co-Play, Other-Play, BAD, and Off-Belief Learning—demonstrated powerful self-play and partner-robust strategies but also exposed evaluation gaps: agents often struggle with unfamiliar humans and human-like partners. These works shaped AH2AC2’s evaluation goals (coordination with unknown partners, including two- and three-player settings) and informed baseline choices. Finally, foundational ad-hoc teamwork research (e.g., PLASTIC-Policy) provided the conceptual framing of performing well with unknown teammates, which AH2AC2 operationalizes as a public challenge. By deliberately limiting available human data, AH2AC2 further encourages data-efficient approaches that generalize to human-like behaviors while maintaining reproducibility—a direct response to the cost and variance of traditional human studies.

---
*Generated: 2026-01-07T00:21:33.187136*

# Prior Work Analysis Report

## Target Paper
**Title:** 5G7MRfPngt
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ICAL’s core contribution—distilling sub-optimal multimodal demonstrations into reusable, executable “embodied programs of thought” and iteratively refining them with feedback—sits at the intersection of programmatic control, grounded planning, self-improvement, and self-generated data. SayCan established that language plans must be grounded in environmental affordances to yield feasible subgoals; ICAL leverages this principle when abstracting trajectories into actionably grounded steps. Code as Policies showed that representing plans as executable code that calls perception and control modules yields interpretable and compositional behavior; ICAL adopts this programmatic representation but learns it from noisy trajectories rather than prompting it directly. Voyager demonstrated that agents can accumulate a skill library from experience and retrieve it for new tasks; ICAL similarly builds a memory of generalized procedures, but focuses on causal/temporal annotations derived from demonstrations. Reflexion contributed the feedback-driven loop of self-critique and memory updates; ICAL uses human/environment feedback to correct inefficiencies and mistakes, refining abstractions over repeated executions. Self-Instruct provided a blueprint for LMs generating their own higher-quality exemplars, a key idea behind ICAL’s transformation of sub-optimal demos into superior in-context examples. Finally, DreamCoder’s library learning motivates ICAL’s conversion of experiences into reusable abstractions, while D-REX underpins the premise that imperfect demonstrations remain valuable when paired with preference-like feedback. Together, these works directly scaffold ICAL’s method for creating, refining, and reusing programmatic memories from imperfect multimodal experience.

---
*Generated: 2026-01-06T23:33:36.288960*

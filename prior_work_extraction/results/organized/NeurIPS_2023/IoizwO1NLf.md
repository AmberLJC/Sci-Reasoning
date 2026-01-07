# Prior Work Analysis Report

## Target Paper
**Title:** IoizwO1NLf
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Skill-it’s core contribution—a data-driven framework that defines skills as subsets of data and discovers an ordered, prerequisite structure to guide online sampling—sits at the intersection of curriculum design, data selection, and training dynamics. The foundational notion that ordering learning can improve generalization comes from curriculum learning, while self-paced learning makes this ordering model- and data-dependent. Graves et al. extend this to automated, online curricula that prioritize material yielding maximal learning progress; Skill-it echoes this by sampling data according to inferred prerequisite skills to unlock more advanced capabilities efficiently.
In NLP, competence-based curricula for NMT demonstrate practical schedules for staged learning, which Skill-it generalizes beyond a single task to multi-skill pretraining by grounding the schedule in a learned skill DAG. Classic data selection for LMs (Moore–Lewis) shows that choosing the right tokens matters; Skill-it departs from domain similarity and instead selects data that advances prerequisite skills shared across downstream tasks. Dataset Cartography provides the insight that training dynamics reveal example difficulty and learnability; Skill-it scales this idea to cluster datapoints into skills and infer their dependencies using model feedback.
Finally, the Chinchilla results sharpen the constraint of fixed token budgets, making data efficiency central. Skill-it addresses this regime directly: by discovering and exploiting skill order, it demonstrates that pretraining on prerequisites reduces the data needed to acquire more advanced skills, yielding better performance-per-token across tasks.

---
*Generated: 2026-01-06T23:42:49.076911*

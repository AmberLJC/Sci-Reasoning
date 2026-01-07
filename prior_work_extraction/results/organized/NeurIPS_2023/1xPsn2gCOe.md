# Prior Work Analysis Report

## Target Paper
**Title:** 1xPsn2gCOe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—deriving a human-like reaction time (RT) metric from stimulus-computable, task-optimized recurrent vision models—sits at the intersection of three threads. First, goal-driven modeling (Yamins & DiCarlo) established that high-performing, stimulus-computable networks are viable scientific models of vision, while work on recurrence in vision (Kietzmann et al.; Spoerer et al.) showed that iterative processing is needed to capture temporal dynamics observed in humans and brains. This motivates using recurrent models whose unfolding computations can be treated as time-varying internal states.
Second, classic decision-making theory (Ratcliff & McKoon) links RTs to the time required for noisy evidence to reach a decision threshold. To instantiate such accumulation within neural networks, the paper needs a principled way to quantify and aggregate evidence from model outputs across iterations.
Third, subjective logic (Jøsang) and its practical instantiation in evidential deep learning (Sensoy et al.) provide exactly this: a mapping from categorical predictions to Dirichlet-based evidence and uncertainty. This lets the authors summarize each recurrent step as incremental evidence and define threshold-crossing dynamics consistent with sequential sampling theories. Finally, stable implicit recurrence (Bai et al., Deep Equilibrium Models) offers a framework for well-behaved iterative inference and natural stopping criteria, aligning model compute time with RT. Together, these works directly enable the paper’s novel RT metric: accumulate subjective-logic evidence over recurrent iterations of a task-optimized vision model and read out reaction time from when evidence meets decision criteria, yielding alignment with human RT patterns across diverse tasks.

---
*Generated: 2026-01-07T00:02:04.803093*

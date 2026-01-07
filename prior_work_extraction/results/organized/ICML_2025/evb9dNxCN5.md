# Prior Work Analysis Report

## Target Paper
**Title:** evb9dNxCN5
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper bridges two previously distinct threads: invariance-based approaches for combating spurious correlations and the mechanics of continual learning. Invariance theory and methods—Invariant Prediction (Peters et al., 2016) and Invariant Risk Minimization (Arjovsky et al., 2020)—establish that when multiple environments are available jointly, invariant predictors can be identified that ignore spurious features. Group DRO (Sagawa et al., 2020) operationalizes this by optimizing worst-group risk, further demonstrating how ERM exploits spurious cues and how group structure enables robust learning. However, these works assume simultaneous access to diverse environments. The present paper’s key insight is that in continual learning, environments (and their confounders) arrive sequentially, undermining the ability to learn invariances that require cross-environment comparison during training.
To expose and study this gap, the authors construct ConCon, a continually confounded dataset grounded in CLEVR (Johnson et al., 2017), whose controllable generative factors permit systematic variation of confounders across tasks, akin to CoGenT-style factor recombinations. They then evaluate representative continual learning methods—including EWC (Kirkpatrick et al., 2017), GEM (Lopez-Paz & Ranzato, 2017), and A-GEM (Chaudhry et al., 2019)—which primarily address catastrophic forgetting via regularization or replay constraints. The findings reveal that such methods, while mitigating forgetting, do not prevent reliance on spurious correlations when confounders shift over time. By formally defining continual confounders and empirically demonstrating failure modes of standard CL, the paper delineates a new problem setting at the intersection of robustness and lifelong learning, motivating algorithms that explicitly reason about invariance under sequential access.

---
*Generated: 2026-01-07T00:04:09.156610*

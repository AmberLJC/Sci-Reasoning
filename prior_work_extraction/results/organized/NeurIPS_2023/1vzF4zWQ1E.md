# Prior Work Analysis Report

## Target Paper
**Title:** 1vzF4zWQ1E
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper reframes fairness in face recognition by arguing that biases can be intrinsic to neural architectures, not only to data or training procedures. Early empirical works—Gender Shades and NIST’s FRVT Part 3—documented substantial demographic disparities and established rigorous evaluation metrics (e.g., FMR/FRR gaps), sharpening the community’s understanding of what fairness in face recognition must quantify. In response, many mitigation efforts focused on data balancing and domain adaptation, exemplified by RFW’s benchmark and methodology, as well as in-processing strategies like adversarial debiasing. Yet, these approaches often struggled to deliver fairness at high-accuracy operating points typical of operational face recognition.

Against this backdrop, the paper’s key contribution is to treat fairness as a property that can be optimized by selecting better architectures and hyperparameters. Methodologically, it builds on multi-objective optimization foundations such as NSGA-II to reason about Pareto trade-offs—here, fairness versus accuracy—and on scalable joint hyperparameter/architecture search ideas exemplified by BOHB. Practically, it interrogates prevailing face recognition training recipes epitomized by ArcFace, revealing that alternative architectures discovered via fairness-aware search can Pareto-dominate standard baselines and prior debiasing techniques. Together, these prior works collectively motivate the need for, provide the metrics to evaluate, and supply the optimization tools to realize the paper’s central insight: fairer architectures can materially improve the fairness–accuracy frontier in face recognition.

---
*Generated: 2026-01-07T00:02:04.870755*

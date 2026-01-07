# Prior Work Analysis Report

## Target Paper
**Title:** X0Etmtge6w
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—designing surrogate losses that are Bayes-consistent for a two-stage classifier that may defer to a costlier second model with access to additional features—rests on three intertwined threads of prior work. First, the reject/abstain tradition, originating with Chow, defines the 0-1-c loss and the Bayes-optimal decision boundary for paying a fixed abstention cost. Subsequent developments by Herbei and Wegkamp, and Cortes, DeSalvo, and Mohri, established that carefully constructed convex surrogates can consistently optimize abstention-style risks, providing a toolbox of margin-based and boosting-style losses and calibration arguments. El-Yaniv and Wiener’s selective classification framework further clarifies the risk–coverage trade-off that any deferral mechanism must navigate.
Second, the modern learning-to-defer literature connects abstention to collaboration with another decision-maker. Madras et al. formulated an explicit defer-to-expert objective with costs, highlighting practical training schemes. Mozannar and Sontag then revealed that naive surrogates in this setting can be inconsistent and provided principled estimators with consistency guarantees.
This paper synthesizes these strands: it adopts the cost-sensitive defer objective of learning-to-defer, but departs in two crucial ways—jointly training both stages and allowing the second stage access to strictly richer features. It leverages and extends the abstention-surrogate theory to construct losses that are calibrated to the 0-1+c objective in this asymmetric-information, two-stage pipeline, delivering Bayes-consistency and practical training procedures grounded in the earlier theoretical insights.

---
*Generated: 2026-01-07T00:02:04.943658*

# Prior Work Analysis Report

## Target Paper
**Title:** cmBjkpRuvw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper reframes reward learning in RLHF as a problem of preference aggregation and subjects it to a social-choice axiomatic lens. The immediate technical target is the dominant practice inaugurated by Christiano et al. (2017) and scaled by Ouyang et al. (2022), which fits reward models via maximum likelihood on pairwise comparisons under Bradley–Terry–Luce (BTL/Plackett–Luce) families. These models—rooted in Bradley and Terry’s (1952) paired-comparison logistic formulation, Luce’s (1959) choice axiom, and Thurstone’s (1927) probit alternative—provide the statistical backbone of modern preference-based reward inference. By evaluating these random-utility MLE estimators against classic social choice desiderata in Arrow’s (1951) tradition, the authors show that both BTL and broader RUM generalizations violate basic axioms, revealing a mismatch between statistical convenience and normative soundness for alignment.
Recognizing a special linear structure in the RLHF reward-learning problem, the authors then pivot to designing aggregation rules with provable axiomatic guarantees. This move is conceptually aligned with Roberts’ (1979) characterization in mechanism design, where linear (quasilinear) environments sharply constrain admissible social choice rules to affine maximizers. Analogously, the paper’s ‘linear social choice’ framework leverages linearity to narrow the feasible space of aggregation procedures and to deliver new, principled rules for learning reward functions. Together, these works directly inform the critique of existing RUM-based approaches and the construction of axiomatic, alignment-grounded alternatives.

---
*Generated: 2026-01-07T00:02:04.759071*

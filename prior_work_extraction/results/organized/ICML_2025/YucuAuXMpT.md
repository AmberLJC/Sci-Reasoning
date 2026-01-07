# Prior Work Analysis Report

## Target Paper
**Title:** YucuAuXMpT
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—an analytical dissociation between functional and representational similarity—rests on two pillars: exact analysis in deep linear networks and the modern practice of comparing internal codes across networks and brains. Saxe et al. (2014) provide the crucial mathematical machinery: an SVD-based description of learning dynamics and the non-uniqueness of linear factorizations. Building on this, Kawaguchi (2016) formalizes the loss landscape structure and identifiability limits in deep linear nets, legitimizing the existence of many internal solutions realizing the same input–output mapping. Gunasekar et al. (2017) then explains how gradient descent implicitly selects among these equivalence classes, clarifying why training can settle on distinct internal representations even when functions coincide.
Parallel developments in representation comparison—Kriegeskorte et al. (2008) with RSA, Raghu et al. (2017) with SVCCA, and Kornblith et al. (2019) with CKA—established practical, geometry-based metrics to align and compare neural codes. The present work analytically shows that these metrics can signal similarity absent functional equivalence and fail to guarantee similarity when functions match, due to invariances and reparameterizations inherent in multilayer factorizations. Finally, empirical reports of convergent or divergent internal representations across independently trained networks (e.g., Li/Yosinski/Clune et al., 2016) are reconciled: the theory delineates when input statistics and training biases drive geometric alignment versus when functional constraints leave representational degrees of freedom unconstrained. Together, these prior works directly enable and motivate the paper’s key insight that representation and function can be fundamentally decoupled, and that generalization or robustness alone need not fix internal codes.

---
*Generated: 2026-01-07T00:21:33.201426*

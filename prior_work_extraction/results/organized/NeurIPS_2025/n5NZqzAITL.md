# Prior Work Analysis Report

## Target Paper
**Title:** n5NZqzAITL
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—principled, theoretically justified data augmentation for training MPNNs to solve quadratic programs—sits at the intersection of learning-to-optimize for mathematical programming and symmetry-based augmentation. Gasse et al. (2019) established an MPNN formulation for mixed-integer optimization states and demonstrated that a learned policy can mimic strong branching; Khalil et al. (2016) pioneered this learning-to-branch objective, defining the target signal that the present work seeks to approximate robustly in data-scarce regimes. Dai et al. (2017) further validated message passing as a vehicle for learning heuristics over graph-structured optimization problems, solidifying MPNNs as the architectural choice.

The augmentation strategy draws on two theoretical pillars. First, convex optimization theory (Boyd & Vandenberghe, 2004) provides equivalence-preserving transformations for QPs—such as positive rescalings, redundant constraints, and congruent variable reparameterizations—that maintain optimality and labels. Second, symmetry in integer/linear programming (Margot, 2010) frames permutations of variables/constraints as group actions that preserve solution structure, offering a rigorous lens for generating additional training instances.

Finally, the general paradigm of leveraging symmetry groups for invariance/equivariance and data augmentation (Cohen & Welling, 2016) and the practical lessons from graph augmentation in representation learning (You et al., 2020) inform the design choices: augment only along symmetries that guarantee label consistency. Together, these works directly enable the paper’s main advance: a symmetry- and equivalence-driven augmentation pipeline that yields diverse yet optimality-preserving QP instances, improving robustness and generalization of L2O MPNNs.

---
*Generated: 2026-01-07T00:21:32.330759*

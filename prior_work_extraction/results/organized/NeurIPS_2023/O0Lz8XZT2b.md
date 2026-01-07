# Prior Work Analysis Report

## Target Paper
**Title:** O0Lz8XZT2b
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of “A U-turn on Double Descent” is to challenge parameter-count-based narratives of double descent for classical (non-neural) models and to show that, under appropriate measures of effective complexity, the familiar single U-shaped risk curve reappears. This argument is directly catalyzed by the double descent literature. Belkin et al. (2019) established the phenomenon and used parameter count as the complexity axis across diverse models, while Nakkiran et al. (2020) broadened its scope in deep learning, encouraging the community to treat nonmonotonic generalization as ubiquitous. Linear regression served as the primary non-neural exemplar: Hastie et al. (2019) analytically characterized ridgeless least squares around the interpolation threshold, and Bartlett et al. (2020) showed when interpolating solutions can still generalize, undermining the idea that p > n alone dictates overfitting. These works set the stage for Curth, Jeffares, and van der Schaar to argue that parameter count is a poor proxy for effective complexity.
For classical methods, long-standing frameworks already provide better complexity axes. CART (Breiman et al., 1984) formalized cost-complexity pruning and tree size as model complexity, and boosting’s statistical view (Friedman, Hastie, Tibshirani, 2000) frames iteration count and shrinkage as regularization—both yield U-shaped validation curves under proper tuning. ESL (Hastie, Tibshirani, Friedman, 2009) unifies these perspectives via degrees of freedom and bias–variance. Building directly on these foundations, the paper shows that once complexity is parameterized by effective degrees of freedom or path-based regularization, the purported non-neural double descent largely vanishes, reconciling modern observations with classical statistical wisdom.

---
*Generated: 2026-01-07T00:02:04.811276*

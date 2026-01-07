# Prior Work Analysis Report

## Target Paper
**Title:** IT9mWLYNpQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper unites two lines of research: the edge-of-stability (EoS) phenomenon for gradient descent with large constant step sizes and the implicit bias of gradient methods on separable data. Cohen et al. (2021) documented that practical training often operates at EoS, with non-monotonic losses and sharpness saturating around 2/η, challenging classical stability analyses. Building upon this, the current work asks whether the well-known implicit bias results still hold under EoS. Foundational studies by Soudry et al. (2018) and Ji & Telgarsky (2019) established that for logistic (and related exponential-tailed) losses on linearly separable data, gradient descent parameters diverge while their direction converges to the hard-margin SVM solution. Nacson et al. (2019) further developed convergence guarantees and rates for constant-stepsize GD, offering tools and decompositions crucial for handling the non-monotone dynamics encountered at EoS.
Integrating these insights, the present paper proves that even with any constant step size in the EoS regime, logistic loss is minimized over long time scales. It sharpens the implicit bias picture by decomposing the iterate trajectory: along the max-margin (SVM) direction, parameters diverge, while in the orthogonal complement they converge to the minimizer of a strongly convex potential. Lyu & Li (2019) reinforce the broader principle of margin maximization under gradient dynamics, while Cortes & Vapnik (1995) provide the canonical max-margin target. The paper also contrasts logistic with exponential loss, highlighting catastrophic divergence at EoS for the latter, thereby delineating loss-specific stability and implicit bias behaviors under large-step training.

---
*Generated: 2026-01-06T23:42:49.136097*

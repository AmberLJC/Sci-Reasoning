# Prior Work Analysis Report

## Target Paper
**Title:** APojAzJQiq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ConFIG’s key contribution—producing conflict-free updates for PINNs with guaranteed positive alignment to each loss-specific gradient while maintaining consistent optimization rates—sits at the intersection of two lines of work: (1) multi-objective optimization for deep multi-task learning and (2) training pathologies and weighting strategies in PINNs. On the multi-task side, Sener and Koltun’s MGDA established that a convex combination of task gradients yields a common descent direction, framing conflict handling as multi-objective optimization. PCGrad later operationalized conflict mitigation via gradient surgery, projecting away negative components between task gradients, while CAGrad formalized conflict-averse directions under inner-product constraints to remain close to the average gradient. These ideas inform ConFIG’s core mechanism: ensuring the final update has a positive dot product with every loss gradient, and dynamically modulating magnitudes based on measured conflict.
On the PINN side, Raissi et al. introduced the composite PINN objective (IC/BC versus PDE residual) whose imbalance is a central source of failure. Krishnapriyan et al. documented how such conflicts manifest as gradient pathologies and optimization stalls. Responding to these issues, adaptive weighting methods like GradNorm and Self-Adaptive PINNs sought to equalize training progress across terms. ConFIG integrates these threads by moving from heuristic loss weighting to principled gradient-space control: it enforces conflict-free alignment, balances optimization rates, and accelerates with momentum via alternating backpropagation, while providing a convergence proof tailored to the PINN setting.

---
*Generated: 2026-01-06T23:42:48.087201*

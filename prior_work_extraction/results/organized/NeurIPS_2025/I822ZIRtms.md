# Prior Work Analysis Report

## Target Paper
**Title:** I822ZIRtms
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution is a nonlinear, control-theoretic characterization of interactions between subsystems by learning a differentiable dynamical model and reading out directed, context-dependent influence from its Jacobian. Neural ODEs provided the essential machinery: a continuous-time, differentiable vector field trained with the adjoint method, enabling efficient estimation of state-dependent Jacobians from time series. Complementing this, SINDy demonstrated that governing equations—and thus Jacobians—can be identified from data, motivating a Jacobian-centric interpretation of influence, while the new deep approach trades handcrafted libraries for expressive neural parameterizations. In parallel, linear system identification and control perspectives (DMDc) and neuroscience’s effective connectivity (DCM) established the value of A/B or bilinear terms for quantifying how one component modulates another; the present work generalizes these ideas to nonlinear, context-varying Jacobians that capture rich interactions. The widespread use and limitations of linear Granger causality in neuroscience sharpen the target: replacing global linear coefficients with local, state-dependent Jacobian entries to capture directionality, strength, and contextual modulation in complex systems. From empirical dynamic modeling, the authors inherit the insight that local linearization (S-map) can reveal interaction structure via Jacobians, while advancing it to high-dimensional, noisy settings with deep learning. Finally, Neural CDEs inform robust learning from irregular trajectories and a control-like view of one subsystem’s path influencing another, consolidating the paper’s JacobianODE as a practical, nonlinear successor to classical connectivity and causality tools.

---
*Generated: 2026-01-06T23:42:48.124028*

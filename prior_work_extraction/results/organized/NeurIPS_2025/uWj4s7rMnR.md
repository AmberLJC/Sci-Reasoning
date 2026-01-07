# Prior Work Analysis Report

## Target Paper
**Title:** uWj4s7rMnR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MeanFlow’s core contribution—learning a time-averaged velocity and exploiting an identity that links it to instantaneous velocities—emerges from the evolution of flow/diffusion modeling toward efficient, few-step generation. Foundationally, score-based diffusion and DDIM reframed generation as integrating a probability-flow ODE, where a learned instantaneous drift transports data along time. Neural ODEs established the general paradigm of parameterizing velocity fields whose integrals yield end-to-end displacements, providing the mathematical backbone for MeanFlow’s focus on the integral quantity.

Flow-matching developments then targeted direct learning of the ODE velocity. Stochastic Interpolants unified diffusion and flow training via conditional flow matching, emphasizing identities along an interpolation path—precisely the type of relation MeanFlow formalizes between average and instantaneous velocities. Rectified Flow further revealed that high-quality models can ‘straighten’ trajectories so velocity becomes near-constant, suggesting that learning the time-averaged velocity could be both tractable and effective.

Parallel attempts at 1-NFE sampling, notably Consistency Models and progressive distillation, achieved impressive one-step performance but relied on teachers, curricula, or multi-stage compression. MeanFlow dispenses with these by using a self-contained objective grounded in a well-defined average–instantaneous identity, directly regressing the mean velocity that maps source to target in one evaluation. In doing so, it preserves the principled ODE/flow semantics of prior work while closing the performance gap to multi-step models and offering a clean theoretical lens for one-step generative modeling.

---
*Generated: 2026-01-07T00:21:33.173324*

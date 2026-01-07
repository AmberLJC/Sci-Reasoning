# Prior Work Analysis Report

## Target Paper
**Title:** d1P6GtRzuV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Neural Jump-Diffusion Temporal Point Processes (NJDTPP) unite classical and neural TPP modeling by recasting the intensity as the solution of a neural jump-diffusion SDE. The classical pillars—Hawkes (1971) and Isham–Westcott’s self-correcting process (1979)—already possess explicit jump differential dynamics for intensity (or log-intensity), furnishing concrete, model-specific instances of drift with event-triggered jumps. Cox’s 1955 formulation of doubly stochastic Poisson processes supplied the conceptual bridge to treat intensity itself as a stochastic process, legitimizing stochastic (rather than purely deterministic) dynamics for λt.

On the neural side, RMTPP (Du et al., 2016) and the Neural Hawkes Process (Mei & Eisner, 2017) demonstrated the value of flexible, learned dynamics, with Neural Hawkes offering a jump-ODE viewpoint via continuous-time hidden states modulated by event-driven jumps. NJDTPP advances this trajectory by moving from hidden-state ODEs to intensity-level jump-SDEs, enriching expressiveness through diffusion noise and neural parameterization of drift, diffusion, and jump coefficients.

Technically, NJDTPP’s guarantees are grounded in the modern neural SDE toolkit (Kidger et al., 2021), which provides practices for parameterizing and training SDEs and for ensuring well-posedness under standard conditions. The mathematical backbone for jump-diffusion existence and uniqueness comes from the Lévy SDE literature (Applebaum, 2009). Together, these strands directly shape NJDTPP’s core innovation: a unified neural jump-diffusion perspective that encapsulates classical TPPs as special cases while delivering a flexible, theoretically sound intensity model.

---
*Generated: 2026-01-07T00:02:04.876948*

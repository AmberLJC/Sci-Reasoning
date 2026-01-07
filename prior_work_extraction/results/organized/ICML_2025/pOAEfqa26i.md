# Prior Work Analysis Report

## Target Paper
**Title:** pOAEfqa26i
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ADM’s core contribution—learning time-varying, directed inter-regional communications with temporal delays at scale—rests on two intertwined threads: state-space Gaussian processes for scalability and principled models of directed, delayed neural interactions. Hartikainen and Särkkä showed that temporal GP priors can be represented as Markovian state-space models, enabling Kalman filtering and smoothing for O(T) inference. Särkkä, Solin, and Hartikainen extended this to spatiotemporal settings and provided practical recipes for scalable GP inference. These developments directly enable ADM’s Markovian GP backbone that supports long neural recordings.
Concurrently, neuroscience demands models that capture directionality and delays. Friston’s Dynamic Causal Modeling framed effective connectivity as a generative SSM with directed, possibly delayed interactions, setting a gold standard for causal interpretation. Granger-causality tools (Barnett & Seth) became the workhorse for directed functional connectivity, albeit typically with fixed-order VARs and limited handling of smoothly time-varying delays. Linderman and Adams’ Bayesian point-process work demonstrated learning directed, time-lagged influence kernels from spikes, highlighting the value of explicit temporal offsets.
To represent inter-output couplings and lags within GPs, Álvarez–Rosasco–Lawrence’s convolved multi-output GPs provided a kernel-based mechanism via Green’s functions and convolution. ADM inherits this spirit but makes delays adaptive in time within a GP–SSM. Finally, to scale inference, ADM employs parallel scan over SSM recursions, drawing on Blelloch’s associative prefix-sum primitive to parallelize forward–backward passes. Together, these works converge in ADM’s scalable, nonparametric, and dynamically delayed model of brain-region communications.

---
*Generated: 2026-01-07T00:21:33.190414*

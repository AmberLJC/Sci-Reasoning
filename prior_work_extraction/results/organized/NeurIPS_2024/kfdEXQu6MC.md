# Prior Work Analysis Report

## Target Paper
**Title:** kfdEXQu6MC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—defining a surrogate-gradient neural tangent kernel (sNTK) and showing how it governs gradient descent with surrogate derivatives—rests on two pillars: NTK-based training dynamics and the surrogate-gradient paradigm for non-differentiable models. Jacot et al. (2018) established the NTK, revealing that in the infinite-width limit, gradient descent linearizes around initialization and follows kernel gradient flow. This perspective is grounded in the GP correspondence for wide networks (Lee et al., 2018) and the lazy-training/kernel regime formalization (Chizat & Bach, 2019). However, these analyses implicitly rely on well-behaved derivatives; naively extending them to discontinuous activations leads to ill-posed dynamics—precisely the failure mode diagnosed in the present work.
In parallel, the surrogate-gradient lineage—originating with the straight-through estimator (Bengio et al., 2013) and crystallized in practice via BinaryConnect (Courbariaux et al., 2015)—provides effective, biased derivatives for discrete or spiking units. In spiking neural networks, Bellec et al. (2018) introduced pseudo-derivatives enabling backpropagation through spike discontinuities, while Neftci et al. (2019) synthesized the area and highlighted the lack of theory. The current paper knits these threads by replacing true derivatives with surrogates in the backprop Jacobian, thereby defining an sNTK that renders gradient descent well-posed in the infinite-width limit even with jump activations. This yields a principled kernel description of surrogate-gradient learning, explaining its empirical success and offering a framework to compare surrogate choices analytically.

---
*Generated: 2026-01-06T23:39:42.941060*

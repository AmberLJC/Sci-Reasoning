# Prior Work Analysis Report

## Target Paper
**Title:** 4Z04wVQ9FY
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

LUNO’s core idea—endowing trained neural operators with principled uncertainty via linearization—sits at the intersection of operator learning and Bayesian deep learning. Foundational operator-learning works such as the Fourier Neural Operator and DeepONet established neural mappings between function spaces for PDE solution operators, defining the practical models to which LUNO attaches. On the Bayesian side, the insight that linearized neural networks behave like Gaussian processes (via the Neural Tangent Kernel and the broader DNN-as-GP perspective) directly motivates LUNO’s pushforward: linearize a trained operator and propagate Gaussian weight uncertainty to obtain a Gaussian belief over outputs. Practical Bayesianization is enabled by Laplace-at-MAP methods for neural networks, which provide a Gaussian approximation in weight space; scalable Laplace techniques further make this feasible for modern architectures. LUNO then extends these ingredients from finite-dimensional outputs to function-valued predictions: by viewing an operator as a curried map, fixing an input function yields a function-valued GP over the output domain. Here, operator-/vector-valued kernel theory informs the structure of the induced covariances and legitimizes treating outputs as elements of function spaces. Together, these prior works supply (i) the operator-learning substrates (FNO/DeepONet), (ii) the linearization-to-GP bridge (NTK and DNN-as-GP), and (iii) the practical Bayesian mechanism (Laplace) that LUNO unifies to deliver function-valued Gaussian process uncertainty for neural operators.

---
*Generated: 2026-01-07T00:04:09.154287*

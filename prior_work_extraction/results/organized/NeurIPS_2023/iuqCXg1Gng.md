# Prior Work Analysis Report

## Target Paper
**Title:** iuqCXg1Gng
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—an exact, saddle-to-saddle description of gradient flow in two-layer diagonal linear networks culminating in the minimum ℓ1-norm solution—sits at the intersection of implicit-bias theory, solution-path algorithms, and loss-landscape geometry. Gunasekar et al. (2017) established that gradient descent on factorized linear models implicitly minimizes nuclear norm; in the diagonal specialization this becomes ℓ1, predicting the endpoint that this work reaches. Gunasekar et al. (2018) further tied network structure to ℓ1 bias in linear convolutional networks (diagonal in the Fourier domain), reinforcing the diagonal-network lens adopted here.

Where this paper advances the state of the art is in its trajectory-level account. The recursive characterization of jump times and successive coordinate activations echoes the Lasso path perspective from Efron et al.’s LARS and Rosset–Zhu’s piecewise-linear path results, effectively translating those path-following insights into a continuous-time gradient-flow setting via an arc-length reparametrization. On the dynamical side, analyses of homogeneous networks under vanishing initialization (Lyu & Li, 2019) provide methodological scaffolding—directional convergence and rescaling arguments—that this paper adapts to track transitions between saddles. Finally, the global geometry results for deep linear networks (Kawaguchi, 2016) justify a landscape rich in saddles, enabling the central finding that gradient flow deterministically hops from one saddle to the next en route to the ℓ1-minimizer. Collectively, these works directly inform the endpoint bias, the path-structure analogy, and the dynamical and geometric tools that make the saddle-to-saddle characterization possible.

---
*Generated: 2026-01-07T00:02:04.843193*

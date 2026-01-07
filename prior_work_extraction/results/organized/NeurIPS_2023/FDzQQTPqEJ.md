# Prior Work Analysis Report

## Target Paper
**Title:** FDzQQTPqEJ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Squared Neural Families (SNEFY) achieve tractable, flexible density modeling by defining densities as the squared 2-norm of a neural network, normalized with respect to a base measure. The central technical lever is the infinite-width neural network–Gaussian process correspondence. Neal (1996) established this bridge, while Rasmussen and Williams (2006) provided the GP toolkit—Mercer expansions, conditioning and marginalization rules, and kernel integral identities—that SNEFY exploits to compute normalizing constants and to prove closure under conditioning and tractable marginals.

Crucially, SNEFY’s closed-form normalizers depend on having analytic neural kernels. Cho and Saul (2009) derived arc-cosine kernels for ReLU-like activations, and Daniely et al. (2016) gave a dual-activation/Hermite framework under Gaussian inputs, yielding explicit eigensystems and kernel recursions. These results make integrals of squared network outputs with respect to Gaussian (and related) base measures computable in closed form. Lee et al. (2018) extended NN–GP correspondence to deep architectures with practical kernel recurrences, allowing SNEFY to retain tractability while scaling depth and expressivity.

Finally, kernel mean embedding theory (Muandet et al., 2017) supplies operator identities for expectations of kernels and their products, directly used to evaluate normalizers and to derive conditional and marginal densities. Framing SNEFY as a strict generalization of exponential families invokes the classical EF structure and closure properties as codified by Wainwright and Jordan (2008), clarifying why SNEFY inherits EF-like tractability while offering a richer, kernel/NN-driven function class.

---
*Generated: 2026-01-07T00:02:04.837795*

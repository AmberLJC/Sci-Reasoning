# Prior Work Analysis Report

## Target Paper
**Title:** IZ1KYTU9ON
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EBD’s key contribution is to recast error broadcasting as a principled learning objective rooted in the MMSE orthogonality principle: the residual of an optimal estimator is orthogonal to functions of the inputs. This insight provides a concrete local objective—penalizing correlations between layer activations and the global output error—that unifies and strengthens earlier error-broadcast methods. Lillicrap et al. and Nøkland established that deep networks can learn without exact weight transport by broadcasting errors directly to hidden layers (feedback and direct feedback alignment). EBD preserves this operational scheme but replaces heuristic feedback with a decorrelation criterion that specifies what the broadcasted signal should achieve at each layer. Jaderberg et al.’s synthetic gradients further legitimized decoupling layers via locally supplied error signals; EBD clarifies that a statistically grounded target for such local signals is orthogonality between activations and output errors.
The theoretical backbone comes from estimation theory (Kay), where the orthogonality principle motivates EBD’s layer-wise losses and yields a rigorous link between global prediction optimality and local decorrelation constraints. On the biological side, EBD’s updates naturally manifest as three-factor rules—pre/post activity modulated by a broadcast error—consistent with the neuromodulation framework reviewed by Frémaux and Gerstner and with mechanistic models like Urbanczik and Senn’s dendritic prediction. Finally, architectures with segregated dendrites (Guerguiev et al.) provide a plausible substrate to route broadcast error signals separately from feedforward inputs, making EBD’s principled broadcast-and-decorrelate mechanism both effective and biologically credible.

---
*Generated: 2026-01-07T00:02:04.958560*

# Prior Work Analysis Report

## Target Paper
**Title:** FEugj28qhC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

BayeSQP’s core innovation fuses the local, second-order structure of Sequential Quadratic Programming with the uncertainty-aware decision-making of Bayesian optimization. The SQP blueprint from Nocedal and Wright provides the architectural scaffold: iteratively form a local quadratic approximation, solve a subproblem, and perform a line search. To realize this without derivatives, BayeSQP builds on Gaussian-process calculus for derivatives (Solak et al.), which ensures that gradients and Hessians can be inferred jointly with function values from zero-order data. This idea connects to Bayesian optimization with gradient information (Wu et al.), but BayeSQP advances it by constructing a full second-order local model for both objective and constraints.

Handling constraints under uncertainty draws on constrained BO (Gelbart et al.), where separate GPs model feasibility, and on SafeOpt (Sui et al.), which formalized high-probability guarantees using GP confidence sets. BayeSQP operationalizes these guarantees within the local step: by invoking robust optimization insights (Ben-Tal and Nemirovski), it converts Gaussian posterior uncertainty into second-order cone constraints, yielding a tractable SOCP that targets high-probability improvement while respecting constraint risk. Finally, the algorithm’s one-dimensional line search employs constrained Thompson sampling along the SQP direction, directly leveraging GP posterior sampling (Russo and Van Roy) to balance exploration and exploitation under feasibility considerations. Together, these strands produce a principled, uncertainty-aware, second-order local optimizer that inherits the efficiency of SQP while retaining the global-surrogate advantages of Bayesian optimization, particularly effective in challenging high-dimensional regimes.

---
*Generated: 2026-01-07T00:05:12.533703*

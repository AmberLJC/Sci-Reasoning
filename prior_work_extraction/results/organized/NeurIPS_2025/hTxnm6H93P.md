# Prior Work Analysis Report

## Target Paper
**Title:** hTxnm6H93P
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—showing that, under cross-entropy loss, standard parameterization (He initialization with a global learning rate) admits a finer structure within the traditionally “unstable” large–learning-rate regime that yields both stable training and nontrivial feature learning at large width—builds directly on and challenges canonical width-limit theory. NTK theory (Jacot et al., Lee et al.) formalized the infinite-width, linearized (lazy) regime, leading to the prevailing belief that stable training at width necessarily suppresses feature learning, and that SP with width-independent learning rates is either unstable or lazy. In contrast, the Tensor Programs line (Yang; Yang & Hu) characterized parametrizations and scalings (notably μP) that preserve feature learning at width and prescribe learning-rate rules, implicitly suggesting SP’s limitations and providing a foil for the present analysis. Crucially, the new results hinge on the specific dynamics of cross-entropy: Soudry et al.’s implicit-bias analysis shows that CE drives norms to infinity while stabilizing prediction directions, a mechanism that can alter stability thresholds and learning dynamics compared to squared loss. Mean-field analyses (Mei, Montanari, Nguyen) further demonstrate that infinite-width feature learning is achievable under alternative scalings, motivating the search for analogous behavior within SP. By integrating these strands, the paper revisits the ostensibly unstable SP regime and reveals CE-induced subregimes that reconcile practice with theory: learning rates can be larger than predicted by NTK/μP prescriptions while maintaining stability and enabling feature evolution at large widths.

---
*Generated: 2026-01-07T00:21:33.147944*

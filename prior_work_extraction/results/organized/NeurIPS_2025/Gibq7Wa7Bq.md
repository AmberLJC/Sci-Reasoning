# Prior Work Analysis Report

## Target Paper
**Title:** Gibq7Wa7Bq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

SORTD targets the practical need to work with not just a single sparse decision tree but an entire Rashomon set of near-optimal trees, enumerated in order of objective value for anytime use. The conceptual impetus comes from the Rashomon-set literature (Fisher, Rudin, Dominici), which argues that many models can achieve similar performance yet yield different explanations and fairness properties; this motivates computing and analyzing sets rather than a single optimum. Delivering such sets efficiently demands strong exact optimization machinery developed for sparse trees. Foundational MILP formulations and NP-hardness results from Optimal Classification Trees (Bertsimas, Dunn) and the improved binary formulations of BinOCT (Verwer, Zhang) establish the optimization landscape and provide baselines. Scalable, exact search advances like DL8.5’s caching with tight bounds and branch-and-bound, together with GOSDT’s regularized objective and pruning strategies, supply the algorithmic core that SORTD adapts to explore solution space effectively. Crucially, to provide anytime, ordered outputs, SORTD adopts the k-best enumeration principle of Lawler, tailoring it to the structured combinatorics of decision trees so that trees are generated in nondecreasing objective sequence. By fusing Rashomon-set goals with exact sparse-tree search and k-best ordering, SORTD achieves substantial runtime gains while producing high-quality, preference-aware model sets for interpretability and stakeholder-aligned selection.

---
*Generated: 2026-01-07T00:05:12.519693*

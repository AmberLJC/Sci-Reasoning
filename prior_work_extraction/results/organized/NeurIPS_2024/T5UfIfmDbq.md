# Prior Work Analysis Report

## Target Paper
**Title:** T5UfIfmDbq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—adapting Monte Carlo Tree Search to transfer and refine a promising search subspace for black-box optimization—sits at the intersection of MCTS-based hierarchical exploration and transfer/multi-task Bayesian optimization. On the exploration side, UCT (Kocsis & Szepesvári, 2006) provides the fundamental selection and backup rules enabling principled exploration–exploitation in a tree, while HOO (Bubeck et al., 2011) shows how optimistic, hierarchical partitioning can efficiently navigate continuous domains. These ideas motivate MCTS-transfer’s iterative divide–select–optimize cycle, where the tree encodes progressively finer subspaces and decisions are driven by optimistic estimates.
On the transfer side, multi-task BO (Swersky et al., 2013) established the value of leveraging related tasks within BO, and meta-learning for warm-start (Feurer et al., 2015) demonstrated practical acceleration by seeding with prior knowledge. The Two-Stage Transfer Surrogate (Wistuba et al., 2018) pushed further by transferring knowledge to bias or prune the target search region—directly antecedent to MCTS-transfer’s search space transfer, which adds an adaptive mechanism that refines the region online. Complementing this, SAASBO (Eriksson et al., 2021) and REMBO (Wang et al., 2013) highlight the power of concentrating search in lower-dimensional subspaces; MCTS-transfer operationalizes this principle by learning a task-informed subspace and adaptively partitioning it via MCTS. Together, these works supply the methodological backbone (MCTS/optimism), the transfer rationale (multi-task and warm-start BO), and the subspace-efficiency principle that MCTS-transfer integrates into a flexible, adaptive space-transfer framework.

---
*Generated: 2026-01-06T23:42:49.037425*

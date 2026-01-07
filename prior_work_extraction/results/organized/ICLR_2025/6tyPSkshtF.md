# Prior Work Analysis Report

## Target Paper
**Title:** 6tyPSkshtF
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s key contribution—gap-dependent regret bounds for on-policy Q-learning algorithms that use variance-aware bonuses with reference-advantage decomposition (RAD)—sits at the intersection of three strands of prior work. First, the algorithms under study, UCB-Advantage (Zhang et al., 2020) and Q-EarlySettled-Advantage (Li et al., 2021), introduced RAD to reduce variance in Q-learning and achieved near-optimal worst-case O(√T) regret with variance-estimator (Bernstein-style) bonuses. Second, the variance-aware exploration paradigm originates in model-based UCBVI (Azar et al., 2017), whose empirical/Bernstein bonuses inspired analogous variance estimators in model-free Q-learning; the present paper must reconcile these bonuses with RAD’s control of temporal uncertainty. Third, the motivation and tools for problem-dependent (gap-based) reinforcement learning analyses were advanced by works on gap-dependent regret in episodic MDPs (e.g., Zanette & Brunskill, 2019) and the broader optimism framework (Jaksch et al., 2010), while classical model-free UCB Q-learning with Hoeffding-type bonuses (Jin et al., 2018) provided precedents for gap-dependent improvements in simpler bonus schemes. The novelty here is an error decomposition that simultaneously tracks reference-value and advantage estimation errors under variance-aware bonuses, enabling the first gap-dependent bounds for RAD-based Q-learning. By integrating variance-sensitive confidence control (à la UCBVI) with RAD’s structure and a gap-focused decomposition, the paper bridges the gap between prior Hoeffding-based gap-dependent results and the more refined variance-based, model-free Q-learning algorithms.

---
*Generated: 2026-01-06T23:42:48.091594*

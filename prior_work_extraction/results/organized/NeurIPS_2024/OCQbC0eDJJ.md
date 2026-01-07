# Prior Work Analysis Report

## Target Paper
**Title:** OCQbC0eDJJ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s key contribution—casting online fair division with unknown values as a constrained stochastic bandit problem and designing an explore-then-commit algorithm with \tilde{O}(T^{2/3}) regret under ex-ante envy-freeness or proportionality—sits at the intersection of two threads. From fair division and random assignment, Hylland–Zeckhauser (1979) and Bogomolnaia–Moulin (2001) crystallized ex-ante fairness: fairness in expectation achieved by lotteries over indivisible allocations. This perspective makes fairness constraints linear in allocation probabilities, a structural property the present work exploits to maintain fairness at every step while learning. From online learning, Bandits with Knapsacks (Badanidiyuru–Kleinberg–Slivkins, 2013) and its linear contextual extension (Agrawal–Devanur, 2016) established that one can act over distributions of arms to satisfy linear constraints in expectation, providing the modeling bridge that turns fair division with unknown utilities into a constrained bandit. The fairness-in-bandits line (Joseph–Kearns–Morgenstern–Roth, 2016; Gillen–Jung–Kearns–Neel–Roth, 2018) demonstrated both methodology and performance limits for learning under fairness constraints, notably the emergence of T^{2/3}-type rates and confidence-based exploration that preserves fairness. Synthesizing these ideas, the paper leverages the random-assignment linearity of envy-freeness/proportionality to define tractable constraints over arm distributions and adopts a fairness-aware explore-then-commit schedule tailored to those constraints, achieving fast no-regret while guaranteeing ex-ante fairness throughout.

---
*Generated: 2026-01-06T23:33:35.575543*

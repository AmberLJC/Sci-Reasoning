# Prior Work Analysis Report

## Target Paper
**Title:** 5IpVe9PH14
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—variance-adaptive contextual bandits robust to heavy-tailed rewards via Catoni regression—sits at the intersection of robust statistics, heavy-tailed bandits, and regression-based contextual bandit reductions. Catoni’s seminal work on robust M-estimators supplies the key tool: a mean estimator with sub-Gaussian deviations under only finite variance. Brownlees–Joly–Lugosi extend this idea to robust ERM and regression with heavy tails, guiding how to embed Catoni-type losses into a learning pipeline. On the bandit side, Bubeck–Cesa-Bianchi–Lugosi initiated the study of heavy-tailed rewards in stochastic bandits using robust estimators, establishing that tailored estimators can control regret under mild moment assumptions; this paper advances that agenda to the contextual and function-approximation setting.
Methodologically, the algorithm follows the regression-based blueprint of contextual bandits: Abbasi-Yadkori–Pál–Szepesvári’s self-normalized analysis and variance-weighted regression for linear bandits, and Agarwal et al.’s reduction to supervised learning for general function classes. The present work replaces least squares with a Catoni-based, variance-weighted regression, yielding regret that scales with cumulative reward variance and only logarithmically with the reward range and horizon. Finally, the unknown-variance setting leverages ideas from robust mean estimation without variance knowledge (Lugosi–Mendelson) and heavy-tailed learning under finite higher moments (Hsu–Sabato), using a careful peeling scheme to adapt to variance while avoiding explicit variance estimation and accommodating fourth-moment dependencies.

---
*Generated: 2026-01-07T00:21:32.380912*

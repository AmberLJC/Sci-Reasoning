# Prior Work Analysis Report

## Target Paper
**Title:** XpmJNP8BVA
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

PALR’s core contribution—regularizing behavior cloning to block leakage of past actions embedded in observation histories—sits at the intersection of imitation learning under partial observability and statistical dependence control. The work builds directly on behavior cloning (Pomerleau), the supervised objective it augments, and is motivated by the sequential error amplification recognized in DAgger: while DAgger remedies distribution shift via interaction, PALR targets a complementary mismatch—history features that encode an expert’s past actions—which can cause a learned policy to imitate its own previous decisions at test time.

The partially observable, history-based control setting popularized by recurrent policies (Hausknecht & Stone) is precisely where such leakage can arise, as observations inadvertently carry information about earlier actions. PALR’s key idea is to enforce conditional independence so that the policy’s action does not depend on past-action proxies once the relevant history is accounted for. This is operationalized using established dependence measures: HSIC (Gretton et al.) supplies a differentiable objective for independence, while kernel conditional dependence measures (Fukumizu et al.) provide principled tools for conditioning on history when penalizing residual dependence on leaked action signals. Complementarily, neural MI estimators like MINE (Belghazi et al.) enable MI/CMI-based instantiations of the regularizer.

Conceptually, PALR echoes exposure-bias remedies in sequence modeling (Scheduled Sampling) by addressing a train–test mismatch, but does so without interaction by directly regularizing conditional independence. Together, these strands yield a practical, theoretically grounded approach to robust offline imitation with observation histories.

---
*Generated: 2026-01-06T23:42:49.060304*

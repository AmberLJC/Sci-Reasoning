# Prior Work Analysis Report

## Target Paper
**Title:** dVpFKfqF3R
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core idea—training value functions via classification rather than regression—emerges from the arc of distributional RL and the growing recognition that loss design is central to stability under bootstrapping. C51 first made the leap from scalar value regression to a categorical representation trained with cross-entropy, revealing that “value as classification” can improve stability and performance. Rainbow validated and popularized this insight at scale on Atari, establishing categorical cross-entropy over value supports as a practical, high-performing choice in deep RL. MuZero then extended the paradigm to massive models and diverse domains, using support-based categorical heads for both value and reward, providing compelling evidence that classification-style objectives scale more reliably than MSE regression in practice.

Concurrently, offline RL works such as CQL and IQL highlighted that the choice of value loss profoundly affects robustness: CQL used a conservative, regularized objective to curb overestimation and distributional shift, while IQL replaced MSE with expectile regression to stabilize value learning. Together, these results solidified the view that departing from vanilla MSE can systematically mitigate bootstrapping instabilities. Building on this foundation, the present paper generalizes the categorical/classification perspective beyond explicitly distributional modeling, advocating a simple, scalable categorical cross-entropy objective for value functions across tasks and architectures (Atari, large ResNets, Q-transformers, chess, language agents). The work thus synthesizes distributional RL’s categorical insights with loss-design advances to propose a broadly applicable, scalable alternative to value regression.

---
*Generated: 2026-01-07T00:02:04.873160*

# Prior Work Analysis Report

## Target Paper
**Title:** p7WHZy8TCG
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

MEMENTO’s key contribution—dynamically updating a neural policy’s action distribution at inference using memory—sits at the intersection of neural routing policies and classical adaptive metaheuristics. On the neural side, Bello et al. introduced RL-trained constructive policies and the notion of instance-specific improvement via active search; Kool et al. and POMO then made sampling-based inference and multi-start rollouts standard tools for exploiting a compute budget. These works established that much of the performance of neural solvers comes from how they search at inference, yet their rollouts are typically independent or rely on expensive parameter fine-tuning. On the classical side, Ant Colony System and Adaptive LNS provided the blueprint for outcome-driven adaptation: pheromone trails and adaptive operator weights encode a memory of what has worked, steering future decisions without changing the underlying algorithmic parameters. Modern hybrids like Neural LNS and NeuroLKH further demonstrated that learned signals can guide powerful search procedures at test time. MEMENTO fuses these lines: within the sampling/multi-start paradigm of attention-based neural solvers, it introduces a lightweight, online memory that updates action biases based on the quality of previous partial or complete solutions. This retains the flexibility and speed of neural policies, avoids costly fine-tuning, and bridges classical adaptive-memory heuristics with learned constructive decoding to better utilize the available computational budget.

---
*Generated: 2026-01-07T00:02:04.952185*

# Prior Work Analysis Report

## Target Paper
**Title:** APGXBNkt6h
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Ni et al. interrogate a central puzzle raised by the recent success of Transformers in RL: do gains stem from superior memory or better temporal credit assignment? Foundationally, the Transformer architecture (Vaswani et al.) enables long-range dependency modeling via attention, and its tailored adoption for RL in GTrXL (Parisotto et al.) established strong empirical improvements on partially observable and long-context tasks. Sequence-modeling approaches like Decision Transformer (Chen et al.) further amplified evidence that Transformers can tackle long-horizon RL problems, but they did not clarify which capability—memory or credit assignment—drives the performance.
To answer this, the authors adopt a diagnostic ethos akin to bsuite (Osband et al.), which introduced targeted probes for memory and credit assignment. Building on that idea, they formalize precise notions of memory length and credit assignment length and craft configurable tasks to independently stress each dimension. Against recurrent baselines that historically address memory in POMDPs (DRQN) and strong modern recurrent agents (R2D2), they show that Transformers substantially extend memory horizons—successfully recalling observations up to 1500 steps back—yet do not enhance long-term credit assignment. This outcome aligns with specialized credit-assignment methods like RUDDER (Arjona-Medina et al.), which argue that targeted mechanisms (e.g., reward redistribution) are needed to handle delayed rewards. Together, these prior works shaped both the hypothesis and experimental design, enabling the paper’s core contribution: decoupling and measuring memory versus credit assignment, and demonstrating Transformers primarily benefit the former.

---
*Generated: 2026-01-06T23:42:48.051281*

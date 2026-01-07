# Prior Work Analysis Report

## Target Paper
**Title:** wPdBe9zxNr
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CURE’s core contribution—jointly training a coder and a unit tester via reinforcement learning using purely verifiable, execution-based rewards—directly builds on several lines of work that established execution as supervision and verifier-driven improvement. CodeRL first demonstrated that unit-test pass rates can serve as effective RL rewards for code generation, proving the feasibility of execution-based optimization. ReST generalized the idea of training without gold labels by relying on verifier-derived rewards over model-generated data; CURE adapts this philosophy to the coding domain by letting the unit tester itself become the source of programmatic rewards and evolve with the coder. CRITIC and Reflexion highlighted that iterative self-correction with environment feedback can substantially improve model performance; CURE internalizes this loop at training time, transforming interaction outcomes between coder and tester into reciprocal learning signals. The long-standing EvoSuite work on evolutionary unit test generation showed that tests can be learned from program failures; CURE updates this concept to LLMs, enabling the tester to learn from coder mistakes and produce increasingly discriminative tests. Finally, APPS and PAL cemented the role of execution and programmatic checking as reliable verifiers, which CURE leverages to design scalable, label-free rewards. Together, these works converge on CURE’s insight: co-evolving generators and verifiers under verifiable rewards yields robust coding ability beyond one-shot precision.

---
*Generated: 2026-01-07T00:05:12.540090*

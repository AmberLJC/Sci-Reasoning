# Prior Work Analysis Report

## Target Paper
**Title:** 77eEDRhPkQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DAPO emerges at the intersection of RLHF for LLMs, offline advantage-weighted RL, and process-level supervision. InstructGPT established the dominant response-level RLHF paradigm using PPO and a reward model, but also revealed practical limitations: sparse outcome rewards and high-variance updates that entangle actor and critic training. DPO advanced offline alignment by eliminating explicit reward models, yet its response-level objective still assigns uniform credit across reasoning steps, limiting fine-grained learning.

DAPO addresses these issues by importing two key ideas from offline RL. First, advantage-weighted policy improvement (AWAC) and stable value-learning decoupling (IQL) demonstrate that an independently trained critic can guide an offline policy via advantages without on-policy rollouts. Second, generalized advantage estimation provides the theoretical footing for low-variance, advantage-centric updates. DAPO adapts these principles to language reasoning by computing step-level (rather than trajectory-level) advantages, thereby converting sparse outcome signals into dense step-wise guidance, and by training the actor and critic independently to reduce coupling-induced instability.

Finally, insights from process supervision and step-level verification (e.g., Let’s Verify Step by Step) motivate the move from outcome-only feedback to step-level signals. DAPO operationalizes this in an offline regimen: a critic supplies step-wise advantages that directly shape the actor’s reasoning policy, unifying preference-driven alignment with advantage-based offline RL. The result is a theoretically grounded, step-level optimization framework that overcomes coarse credit assignment and variance issues inherent in response-level methods like PPO-RLHF and DPO.

---
*Generated: 2026-01-07T00:21:33.146706*

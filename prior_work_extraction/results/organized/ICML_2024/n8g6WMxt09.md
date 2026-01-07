# Prior Work Analysis Report

## Target Paper
**Title:** n8g6WMxt09
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

DeRa builds on a line of work that frames alignment as optimizing a tradeoff between reward and proximity to a reference model. Early KL-control for sequence generation (Sequence Tutor) and RLHF for language models (Ziegler et al.) established the canonical objective: maximize reward while constraining divergence from the base LM. InstructGPT operationalized this at scale with PPO and a tunable KL penalty, but also exposed a practical bottleneck—choosing the KL coefficient typically requires retraining or extensive sweeps. DPO later clarified the underlying probabilistic structure: the optimal aligned policy relative to a reference has a Boltzmann form, effectively a logit correction by scaled rewards, which suggests that varying the effective regularization can be achieved by rescaling guidance rather than retraining.

In parallel, decoding-time control methods such as PPLM and GeDi demonstrated that one can steer a frozen LM by adjusting probabilities during generation using auxiliary models, with an explicit guidance-strength knob. DeRa synthesizes these strands: it uses the Boltzmann/logit-correction view from KL-regularized RLHF/DPO to express the aligned distribution relative to the base model, and then, in the spirit of PPLM/GeDi, applies this correction at decoding time. This yields a simple, training-free mechanism to sweep and evaluate different regularization strengths—precisely addressing the cost and brittleness of KL tuning in RLHF—while preserving the theoretical grounding of KL-controlled alignment.

---
*Generated: 2026-01-06T23:42:48.076562*

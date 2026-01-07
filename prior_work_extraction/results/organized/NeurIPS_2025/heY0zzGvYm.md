# Prior Work Analysis Report

## Target Paper
**Title:** heY0zzGvYm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—treating a judge-LLM’s scoring signal as a reinforcement learning reward to train a preamble generator that steers a frozen LLM to obtain higher evaluation scores—sits at the intersection of three lines of work. First, it builds on preference-based optimization for language models. InstructGPT established the RLHF template for optimizing text generation with a learned reward, and Constitutional AI generalized this to AI-provided feedback (RLAIF). The present work applies that template but inverts the goal: rather than aligning to human values, it optimizes for the judge-LLM’s scoring function itself. Second, it leverages the LLM-as-a-judge paradigm popularized by MT-Bench and Chatbot Arena, which made LM-based evaluators standard practice; this creates the incentive landscape that can be exploited via reward maximization. Third, it draws from prompt/prefix control and adversarial prompting. AutoPrompt and Prefix-Tuning showed that prepending learned (discrete or continuous) text can steer a frozen model, a design mirrored here by a learned preamble that requires no changes to the base LM. Meanwhile, universal jailbreak research by Zou et al. and prompt-injection analyses by Greshake et al. revealed that small, general-purpose prefix/suffix strings can reliably manipulate model behavior and can be hard to detect. Integrating these strands, the paper contributes a reinforcement-learning-driven, discrete preamble generator that systematically reverse-engineers judge preferences, outperforming post-hoc editing approaches while remaining lightweight and difficult to detect.

---
*Generated: 2026-01-06T23:42:48.133418*

# Prior Work Analysis Report

## Target Paper
**Title:** LEzx6QRkRH
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

RL-GPT’s core contribution is a two-level agent that fuses code-as-policy with reinforcement learning: a slow agent decides which actions are amenable to coding and a fast agent executes the code, while low-level control is refined by RL. This design stands on the classic principles of hierarchical RL, where Options (Sutton, Precup, Singh) introduced temporal abstraction and HIRO showed how a high-level controller can efficiently guide a low-level learner with robust off-policy training. In parallel, recent embodied AI demonstrated that language models can produce executable control code. Code as Policies crystallized the idea of emitting code to control embodied systems, and ChatGPT for Robotics operationalized LLM-to-code pipelines with real tool and robot execution. SayCan then provided a blueprint for combining LLM high-level intent with value-grounded controllers, foreshadowing RL-GPT’s division of labor: symbolic/code planning on top and learned policies underneath. In the Minecraft domain, Voyager proved that LLM-generated code can accumulate reusable skills and drive open-ended progress, directly motivating RL-GPT’s use of code for high-level structure while relying on RL to master precise, task-specific low-level behaviors. MineDojo supplies the enabling environment and benchmarks that reward code execution and learned control, letting RL-GPT demonstrate its efficiency (rapid diamond acquisition) and breadth (SOTA across tasks) through this principled integration of hierarchical RL and code-as-policy.

---
*Generated: 2026-01-06T23:42:49.038076*

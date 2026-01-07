# Prior Work Analysis Report

## Target Paper
**Title:** NxyfSW6mLK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

REGENT’s central idea—biasing a compact policy toward fast adaptation via retrieval and in-context control—sits at the intersection of semi-parametric retrieval and transformer-based decision making. The nearest-neighbor literature directly motivates its core mechanisms: Model-Free Episodic Control and Neural Episodic Control showed that kNN lookups over episodic memories enable rapid, gradient-free adaptation in RL, foreshadowing REGENT’s strong 1-NN baseline and its reliance on memory-based querying in new environments. From NLP, kNN-LM established that semi-parametric retrieval can markedly improve generalization with minimal additional parameters, a principle REGENT ported to control. RETRO further provided a concrete blueprint for how to condition transformers on retrieved neighbors, inspiring REGENT’s training on sequences of queries plus retrieved trajectories to realize in-context adaptation without finetuning.

On the policy architecture side, Decision Transformer demonstrated that transformers can model trajectories and act as policies via sequence modeling, providing the scaffolding for REGENT’s in-context action selection. Finally, generalist agents like Gato and RT-1 embodied the prevailing scale-first strategy across diverse tasks and embodiments; REGENT explicitly positions retrieval as a more sample- and parameter-efficient alternative, showing that augmenting a smaller transformer with retrieval can rival or surpass larger monolithic policies. Together, these works directly shape REGENT’s semi-parametric design, its emphasis on 1-NN as a surprisingly strong baseline, and its practical recipe—retrieval-augmented, transformer-based in-context control—for rapid generalization to unseen robotics and game environments.

---
*Generated: 2026-01-06T23:42:48.091145*

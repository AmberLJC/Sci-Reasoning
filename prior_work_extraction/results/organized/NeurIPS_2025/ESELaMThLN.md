# Prior Work Analysis Report

## Target Paper
**Title:** ESELaMThLN
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This paper’s core contribution—controlling reasoning speed by steering internal representations and allocating compute based on difficulty—integrates two lines of prior work. First, prompt-based test-time scaling demonstrated that making models "think longer" improves accuracy but at the cost of latency: Chain-of-Thought prompting and Self-Consistency established that longer or multiple rationales boost performance, while Tree of Thoughts pushed this idea to structured search over thoughts. These works defined the slow, deliberate System 2 regime and highlighted the need to modulate reasoning effort rather than always expanding it.
Second, representation control and concept-direction methods showed that behavior can be adjusted by editing internal states. Plug and Play Language Models pioneered test-time manipulation of activations to steer generation, and TCAV formalized the notion that linear directions in representation space correspond to interpretable concepts. Building on these, the present paper identifies a steering vector governing transitions between fast and slow thinking, enabling the first representation-editing-based test-time scaling effect for reasoning.
To decide when to adjust thinking speed, the paper draws on adaptive inference principles and confidence-based gating. Adaptive Computation Time introduced input-dependent halting as a general framework for dynamic compute, while evidence that language models can estimate their own uncertainty provides a practical signal for real-time difficulty estimation. Together, these influences yield a unified approach: a representation-space control for how to change thinking speed and a principled estimator for when to switch, optimizing the accuracy–efficiency trade-off.

---
*Generated: 2026-01-07T00:21:32.234011*

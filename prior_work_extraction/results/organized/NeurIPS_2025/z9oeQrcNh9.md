# Prior Work Analysis Report

## Target Paper
**Title:** z9oeQrcNh9
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ARM’s core contribution—adaptive selection among Direct Answer, Short CoT, Code, and Long CoT with a training method (Ada-GRPO) that avoids format collapse—sits at the intersection of explicit reasoning, tool/code use, and adaptive compute. Chain-of-Thought prompting established explicit reasoning traces as a powerful mechanism, which ARM formalizes as selectable formats. Self-Consistency showed that more samples and longer chains often boost accuracy but at substantial token cost, crystallizing the overthinking problem ARM targets with adaptive budgets. On the modality side, PAL and Toolformer demonstrated that offloading computation to code/tools can improve both accuracy and efficiency for certain tasks; ARM internalizes this by routing to a Code format when the task benefits from programmatic execution. Conceptually, ARM inherits from adaptive computation work (ACT and Universal Transformers), reframing token usage as input-dependent compute that should vary with difficulty rather than being fixed. Finally, at the training level, ARM’s Ada-GRPO advances preference-optimization methods by addressing GRPO’s tendency toward mode/format collapse, ensuring the policy maintains competence across diverse reasoning styles while learning when to use each. Together these threads directly shape ARM’s design: a router over reasoning formats grounded in CoT and tool-use, principled by adaptive compute, and made trainable via a stabilization of group-relative preference optimization.

---
*Generated: 2026-01-07T00:02:04.961540*

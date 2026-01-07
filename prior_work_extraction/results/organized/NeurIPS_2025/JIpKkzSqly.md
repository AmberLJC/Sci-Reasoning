# Prior Work Analysis Report

## Target Paper
**Title:** JIpKkzSqly
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The core contribution of Transstratal Adversarial Attack (TAA) is to convert the real-world, sequential safety pipeline of modern text-to-image systems into a multi-objective black-box optimization problem over prompts, then solve it with an LLM-guided, feedback-driven search that exploits overlapping vulnerabilities across layers. Safe Latent Diffusion (Schramowski et al.) codified the practical multi-layer design—safety-guided generation and a CLIP-based image safety checker—setting the concrete target for TAA. The concept erasure literature (Kumari et al.; Gandikota et al.) supplied the critical middle-layer defense mechanism and exposed its limits: erased notions can resurface via entangled attributes and indirect semantics. TAA operationalizes this insight by explicitly searching for prompts that re-invoke forbidden content through related, unfiltered concepts while remaining benign to both upstream prompt filters and downstream image filters.
Single-layer jailbreak methods such as SneakyPrompt demonstrated that discrete black-box search can evade prompt filters, but they do not coordinate success across all layers. TAA extends this by adopting LLM-based red teaming (Perez et al.) to generate candidate prompts that satisfy implicit, subjective constraints, and by leveraging token-level adversarial optimization ideas from GCG (Zou et al.) to refine candidates under sparse pass/fail signals. Finally, the methodology is grounded in query-efficient black-box attack principles (Ilyas et al.), enabling scalable exploration under realistic API limits. Together, these strands yield a transstratal attack that systematically and simultaneously bypasses prompt filters, concept erasers, and image safety checkers.

---
*Generated: 2026-01-07T00:05:12.519289*

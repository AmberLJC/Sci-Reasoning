# Prior Work Analysis Report

## Target Paper
**Title:** Oi47wc10sm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Conditional Activation Steering (CAST) fuses two lines of work: decoding-time control and representation-level interventions. PPLM pioneered activation-level steering of frozen language models, proving that one can guide generation by adjusting hidden states at inference. GeDi extended decoding-time control to safety-relevant content using discriminators, but remained always-on and driven by an external model. CAST’s core advance is to make steering selective by using the model’s own internal activations as a detector: it analyzes hidden-state patterns to decide whether and where to apply steering, thus preserving normal behavior on benign inputs.

This conditional gating rests on the probing literature—Alain & Bengio’s linear probes and amnesic probing by Elazar et al.—which show that semantic and attribute information is linearly recoverable and manipulable in intermediate layers. At the same time, representation and model editing works such as ROME demonstrate that localized, principled interventions can reliably alter specific behaviors while limiting collateral changes. CAST adopts this interventionist mindset but performs transient activation steering rather than persistent weight edits, and crucially triggers it only for targeted categories.

Finally, task-vector arithmetic connects to CAST’s use of directionality in representation space to add or suppress behaviors, while Constitutional AI frames the policy-level goal—programmable refusals for defined categories—that CAST achieves without further training. Together, these works directly inform CAST’s design: detect category via activations, then conditionally apply an appropriate steering vector to realize selective, rule-based refusals.

---
*Generated: 2026-01-06T23:42:48.079599*

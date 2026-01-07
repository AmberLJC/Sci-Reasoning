# Prior Work Analysis Report

## Target Paper
**Title:** 5bWW9Eop7l
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central contribution—showing that example-level instruction tuning is a key driver of pragmatic (implicature) competence in LLMs—rests on two strands of prior work. First, theoretical and computational pragmatics defined what to test. Grice’s Logic and Conversation established implicature as meaning derived from cooperative principles rather than literal content, while Goodman and Frank’s probabilistic (RSA) view framed pragmatic understanding as context-sensitive inference. These works motivate the paper’s controlled, binary implicature probes that decouple semantics from pragmatics. Second, advances in instruction tuning created the contrasting fine-tuning regimes the paper evaluates. T0 and FLAN demonstrated that supervised, example-level instruction tuning over diverse tasks yields broad zero-shot generalization; their models constitute the category that the paper finds excels at implicature resolution. By contrast, InstructGPT introduced RLHF/chat-style alignment, which the paper shows does not necessarily impart pragmatic inference despite improving helpfulness and safety, thereby isolating fine-tuning strategy as the differentiator. Super-NaturalInstructions supplied the large, heterogeneous instruction pools enabling T0-style training, directly tying data and method to the observed gains in pragmatic ability. Finally, CheckList’s behavioral-testing paradigm informed the paper’s simple, minimal, capability-targeted evaluation design, allowing a clean attribution from tuning strategy to pragmatic competence. Together, these works directly shaped the paper’s hypothesis, task construction, model selection, and the key finding that the “Goldilocks” fine-tuning for implicature is example-level instruction tuning.

---
*Generated: 2026-01-07T00:02:04.777649*

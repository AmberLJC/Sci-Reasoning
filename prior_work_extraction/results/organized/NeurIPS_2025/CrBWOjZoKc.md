# Prior Work Analysis Report

## Target Paper
**Title:** CrBWOjZoKc
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

QFFT’s core contribution—training on long chain-of-thought (CoT) traces while removing the question, so the model adaptively defaults to short reasoning and escalates only when necessary—sits at the intersection of two lines of work: CoT-based supervision and adaptive computation. CoT prompting (Wei et al.) and zero-shot CoT (Kojima et al.) established that explicit reasoning traces boost accuracy and that concise, minimally cued reasoning can suffice for many problems. Self-Consistency (Wang et al.) and Tree of Thoughts (Yao et al.) then pushed toward longer, more exhaustive trajectories, which improved robustness on hard tasks but also amplified overthinking and token cost. In parallel, efficiency-oriented approaches like Skeleton-of-Thought (Sun et al.) showed that compact, outline-like rationales can retain performance while reducing verbosity.

QFFT synthesizes these insights with the adaptive-compute paradigm exemplified by Adaptive Computation Time (Graves) and PonderNet (Banino et al.), which allocate more steps only when needed. By fine-tuning exclusively on long CoT responses while withholding the question, QFFT forces the model to internalize when expanded reasoning is actually necessary, rather than reflexively reproducing long chains conditioned on the prompt. The resulting behavior—prioritize Short CoT, then activate Long CoT selectively—preserves the accuracy benefits of long-trace supervision while curbing overthinking and token usage. In effect, QFFT operationalizes a learned halting policy for LLM reasoning, unifying long-trace competence with concise default behavior.

---
*Generated: 2026-01-07T00:21:33.144929*

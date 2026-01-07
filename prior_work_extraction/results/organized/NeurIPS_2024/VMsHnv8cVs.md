# Prior Work Analysis Report

## Target Paper
**Title:** VMsHnv8cVs
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

NeuRes’s core advance—data-efficient, neuro-symbolic learning for SAT via certificate-driven training and expert iteration—sits at the confluence of three strands of prior work. First, neural representations for SAT, inaugurated by NeuroSAT and extended in NeuroCore, showed that message-passing/attention over CNF graphs can learn powerful signals (e.g., satisfiability, unsat cores) and can guide classical solvers. NeuRes builds on this by maintaining a dynamic formula embedding and shifting the learned target from global classification/branching to fine-grained, autoregressive clause-pair selection for resolution.
Second, work on learning from proofs to guide inference—exemplified by ENIGMA—demonstrated that recorded proofs provide high-quality supervision for clause selection in saturation-style provers. NeuRes brings this idea to propositional SAT, using resolution proofs as certificates to supervise which clauses to resolve, thereby directly tying learning targets to verifiable proof objects. The widespread adoption of DRAT-style certificates and efficient checkers (DRAT-trim) underpins NeuRes’s correctness guarantees and enables scalable certificate-driven training.
Third, training frameworks that iteratively bootstrap policies from an expert—Expert Iteration and its applications in theorem proving (e.g., HOList)—established effective self-improvement loops grounded in proof search. NeuRes adopts this paradigm with a symbolic resolution prover/verifier as the expert, greatly improving data efficiency. Finally, attention-based proof construction (End-to-End Differentiable Proving) informs NeuRes’s architectural choice to autoregressively select clause pairs, aligning neural attention with discrete resolution steps.

---
*Generated: 2026-01-06T23:33:36.268113*

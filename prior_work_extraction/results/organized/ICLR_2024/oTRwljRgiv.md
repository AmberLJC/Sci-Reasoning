# Prior Work Analysis Report

## Target Paper

**Title:** ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis

**Conference:** ICLR 2024 (oral)

**Authors:** Kensen Shi, Joey Hong, Yinlin Deng, Pengcheng Yin, Manzil Zaheer, Charles Sutton

**Keywords:** Program Synthesis, Programming By Example, Generalization, Compositional Generalization

**Abstract:** 
> When writing programs, people have the ability to tackle a new complex task by decomposing it into smaller and more familiar subtasks. While it is difficult to measure whether neural program synthesis methods have similar capabilities, we can measure whether they compositionally generalize, that is, whether a model that has been trained on the simpler subtasks is subsequently able to solve more complex tasks. In this paper, we characterize several different forms of compositional generalization ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**RobustFill: Neural Program Learning under Noisy I/O** (2017)
- *Authors:* Jacob Devlin et al.
- *Direct Connection:* ExeDec builds directly on the RobustFill PBE formulation and DSL/dataset, and targets its inability to compositionally generalize by replacing one-shot decoding with stepwise execution-driven subgoal prediction.

**DeepCoder: Learning to Write Programs** (2017)
- *Authors:* Matej Balog et al.
- *Direct Connection:* ExeDec uses the DeepCoder DSL/benchmark and explicitly addresses the generalization limits of DeepCoder-style component prediction by introducing intermediate execution subgoals that guide multi-step synthesis.

**Generalization Without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks (SCAN)** (2018)
- *Authors:* Brenden M. Lake and Marco Baroni
- *Direct Connection:* ExeDec’s meta-benchmark for compositional generalization in program synthesis adopts the SCAN-style idea of stress-testing systematic recomposition of known primitives via targeted train/test splits.

### 💡 Inspiration

**FlashMeta: A Framework for Inductive Program Synthesis** (2015)
- *Authors:* Oleksandr Polozov and Sumit Gulwani
- *Direct Connection:* ExeDec adopts the core FlashMeta/PROSE insight of propagating example constraints to sub-expressions—here realized neurally as predicting execution subgoals that serve as learned "witness states" to decompose synthesis.

**Learning to Infer Program Sketches** (2019)
- *Authors:* Maxwell I. Nye et al.
- *Direct Connection:* ExeDec draws on the decomposition principle from sketch-based synthesis—separating high-level guidance from low-level search—by instead decomposing along execution states through predicted subgoals.

### 🔧 Extension

**Execution-Guided Decoding for Semantic Parsing** (2018)
- *Authors:* Chenglong Wang et al.
- *Direct Connection:* ExeDec extends execution-guided decoding from merely pruning by running partial programs to actively predicting execution subgoals that steer each decoding step based on execution feedback.

---

## Synthesis: How Prior Work Led to This Paper

FlashMeta (PROSE) established that inductive program synthesis can be made tractable by decomposing a program into sub-expressions and propagating example constraints to them via witness functions, providing a concrete mechanism for subgoal-driven search. RobustFill framed programming-by-example over a FlashFill-style DSL with neural sequence models checked by execution consistency, but it solved problems in one shot and struggled to recombine primitives beyond its training distribution. DeepCoder learned component likelihoods for a functional DSL to guide enumerative search, again operating without explicit intermediate execution targets and exhibiting limited compositional generalization. Execution-guided decoding showed that running partial programs during decoding can prune invalid continuations, introducing a tight feedback loop between execution and generation but still using execution passively rather than as a predicted target. SCAN demonstrated how to rigorously evaluate systematic compositionality through tailored train/test splits that stress novel recombinations of known primitives. Learning to Infer Program Sketches validated that explicit decomposition—separating high-level structure from low-level completion—can dramatically improve synthesis efficiency and generalization.
Taken together, these works revealed both the power of decomposition and execution feedback and the gap: neural PBE systems lacked a learned mechanism to set and pursue intermediate execution targets that enable systematic recomposition. ExeDec naturally synthesizes these ideas by casting witness-style decomposition into a neural framework that predicts execution subgoals, uses execution to inform each step, and evaluates this on SCAN-inspired compositional splits of RobustFill and DeepCoder, yielding stronger synthesis and markedly improved compositional generalization.

---

*Analysis generated on: 2026-01-06T09:46:25.101088*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

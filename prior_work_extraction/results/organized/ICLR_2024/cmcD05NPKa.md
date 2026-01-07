# Prior Work Analysis Report

## Target Paper

**Title:** Learning the greatest common divisor: explaining transformer predictions

**Conference:** ICLR 2024 (spotlight)

**Authors:** Francois Charton

**Keywords:** mathematics, arithmetic, transformers, explainability

**Abstract:** 
> The predictions of small transformers, trained to calculate the greatest common divisor (GCD) of two positive integers, can be fully characterized by looking at model inputs and outputs.
As training proceeds, the model learns a list $\mathcal D$ of integers, products of divisors of the base used to represent integers and small primes, and predicts the largest element of $\mathcal D$ that divides both inputs. 
Training distributions impact performance. Models trained from uniform operands only le...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Deep Learning for Symbolic Mathematics** (2019)
- *Authors:* Guillaume Lample and François Charton
- *Direct Connection:* This work established the transformer-as-seq2seq formulation for mathematical tasks with digit/character tokenization and curriculum-like sampling, directly framing the setup and sampling choices later used to study GCD behavior.

**Evaluating Mathematical Reasoning in Neural Networks** (2019)
- *Authors:* David Saxton et al.
- *Direct Connection:* By showing that arithmetic/number-theory tasks are highly sensitive to data distributions and generalization splits, this paper set the precedent to scrutinize operand/outcome sampling when training models on integer operations.

**Thinking Like Transformers** (2021)
- *Authors:* Gail Weiss, Yoav Goldberg, and Eran Yahav
- *Direct Connection:* By connecting transformers to finite-automata style computations over token sequences, this work supports the feasibility of learning base-dependent regular properties like divisibility tests that underlie the GCD explanation.

### 💡 Inspiration

**Progress Measures for Grokking via Mechanistic Interpretability** (2023)
- *Authors:* Neel Nanda et al.
- *Direct Connection:* Their reverse-engineering of small transformers on modular arithmetic provided a blueprint for explaining an algorithmic task by identifying the learned features/circuits, inspiring the IO-level characterization of a divisibility-feature list for GCD.

### 🔍 Gap Identification

**Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets** (2022)
- *Authors:* Alethea Power et al.
- *Direct Connection:* It revealed that training dynamics and data distribution can flip models from memorization to rule learning on algorithmic tasks, motivating a targeted investigation of how operand vs GCD-balanced sampling steers the learned GCD rule.

### 🔗 Related Problem

**Neural GPUs Learn Algorithms** (2016)
- *Authors:* Łukasz Kaiser and Ilya Sutskever
- *Direct Connection:* Demonstrating that neural networks can learn digit-level algorithms such as addition/multiplication from sequences, it directly motivated using integer-string inputs to probe what algorithmic structure a model acquires for GCD.

**Neural Arithmetic Logic Units** (2018)
- *Authors:* Andrew Trask et al.
- *Direct Connection:* By proposing specialized modules to achieve arithmetic extrapolation and highlighting standard models’ tendency toward shortcut heuristics, it set up a contrast the present work addresses by showing plain transformers learn divisibility-based features and how data shifts change them.

---

## Synthesis: How Prior Work Led to This Paper

Work on neural models for mathematics first showed that sequence-to-sequence transformers with digit or character tokenization can learn nontrivial symbolic and numeric tasks, and that sampling over difficulty scales matters for success (Lample and Charton). The DeepMind Mathematics Dataset established that arithmetic and number-theory tasks are especially sensitive to train-test splits and data distributions, foregrounding the role of operand ranges and target balancing (Saxton et al.). Grokking then revealed that, on small algorithmic datasets, training dynamics and data distribution can determine whether models memorize or eventually implement the underlying rule (Power et al.). Mechanistic studies of modular arithmetic reverse-engineered small transformers to concrete feature circuits, showing that interpretable arithmetic structure can be read out and tracked through training (Nanda et al.). Theoretical analyses connected transformer computation to finite-automata-like processing of token sequences, consistent with recognizing base-dependent regular properties such as divisibility (Weiss et al.). Earlier algorithm-learning systems using digit streams (Kaiser and Sutskever) and arithmetic-inductive-bias modules (Trask et al.) framed expectations about how neural models might internalize integer operations. Taken together, these works exposed a gap: despite progress on modular arithmetic circuits and sensitivity to data distributions, there was no IO-complete, mechanistic explanation of a learned number-theoretic operation. Building on seq2seq arithmetic framing, automata-style divisibility tests, and grokking’s emphasis on data distribution, the present study shows that small transformers learn GCD by selecting the largest divisor from a learned feature list, and that modifying operand and outcome sampling predictably reshapes this list—thus delivering a clean, data-dependent explanation of the learned algorithm.

---

*Analysis generated on: 2026-01-07T00:08:31.819276*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper
**Title:** veEjiN2w9F
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**A Symbolic Approach to Explaining Bayesian Network Classifiers** (2018)
- *Authors:* Andy Shih et al.
- *Connection:* This work formalized local explanations as sufficient reasons/prime implicants of a classifier’s decision function, providing the logical machinery that the present paper generalizes to formalize and analyze local vs. global explanations and their uniqueness.

**A Theory of Diagnosis from First Principles** (1987)
- *Authors:* Raymond Reiter
- *Connection:* Reiter’s hitting-set duality between diagnoses and conflict sets is the classical theoretical basis that the paper adapts to establish a formal duality between local and global forms of ML explanations.

**Constructing optimal binary decision trees is NP-complete** (1976)
- *Authors:* Laurent Hyafil et al.
- *Connection:* The classic NP-completeness of optimizing decision trees serves as the foundational hardness used in this paper’s complexity results for computing global explanations of tree-based models.

### 🔍 Gap Identification

**Why Should I Trust You? Explaining Any Classifier** (2016)
- *Authors:* Marco Tulio Ribeiro et al.
- *Connection:* LIME popularized local, model-agnostic explanations but lacked rigorous guarantees, a shortcoming explicitly addressed here by providing a formal complexity-theoretic framework for local explanations.

**Anchors: High-Precision Model-Agnostic Explanations** (2018)
- *Authors:* Marco Tulio Ribeiro et al.
- *Connection:* Anchors framed local rule-based explanations empirically; the present work responds by formalizing such local/global rule explanations and proving complexity and uniqueness properties they lacked.

### 🔧 Extension

**Abduction-Based Explanations for Machine Learning Models** (2019)
- *Authors:* Alexey Ignatiev et al.
- *Connection:* The abductive (hitting-set–based) formulation of minimal explanations and its associated complexity/duality perspective directly underpins the paper’s duality between local and global explanations and its complexity analyses across model classes.

### 🔗 Related Problem

**Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks** (2017)
- *Authors:* Guy Katz et al.
- *Connection:* Reluplex established formal verification hardness for ReLU networks; the present paper leverages these verification-complexity insights to derive hardness results for computing explanations in neural networks.

---

## Synthesis

The paper’s core innovation—casting local and global interpretability within a unified, complexity-theoretic framework built on a provable duality and uniqueness—rests on a direct lineage from logical and abductive explanation formalisms. Shih, Choi, and Darwiche introduced a symbolic view of local explanations as sufficient reasons/prime implicants, giving a precise language for local interpretability that this paper generalizes and connects to global forms. Ignatiev, Narodytska, and Marques-Silva’s abduction-based explanations supplied the crucial hitting-set machinery and complexity perspective for minimal explanations, which the authors extend to formalize a local–global duality and to reason about inherent uniqueness of certain global forms. This duality itself is anchored in Reiter’s classic diagnosis theory, whose hitting-set duality between diagnoses and conflicts provides the theoretical backbone adapted here to ML explanations. To characterize model-specific computational barriers, the paper leverages foundational hardness results: Hyafil and Rivest’s NP-completeness for optimizing decision trees informs the complexity of computing global explanations for tree models, while Reluplex’s verification results guide reductions establishing hardness for neural networks. Finally, widely used local explanation methods such as LIME and Anchors delineated the practical problem space but lacked formal guarantees; their limitations directly motivate the paper’s rigorous complexity framework and the proofs of duality and uniqueness that clarify when and how explanations can be computed across linear models, decision trees, and neural networks.

---
*Generated: 2026-01-06T23:09:26.399463*

# Prior Work Analysis Report

## Target Paper

**Title:** RAG-SR: Retrieval-Augmented Generation for Neural Symbolic Regression

**Conference:** ICLR 2025 (spotlight)

**Authors:** Hengzhe Zhang, Qi Chen, Bing XUE, Wolfgang Banzhaf, Mengjie Zhang

**Keywords:** Symbolic Regression, Genetic Programming, Transformers, Deep Learning

**Abstract:** 
> Symbolic regression is a key task in machine learning, aiming to discover mathematical expressions that best describe a dataset. While deep learning has increased interest in using neural networks for symbolic regression, many existing approaches rely on pre-trained models. These models require significant computational resources and struggle with regression tasks involving unseen functions and variables. A pre-training-free paradigm is needed to better integrate with search-based symbolic regre...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Learning Feature Representations with Genetic Programming (FEAT)** (2019)
- *Authors:* William La Cava et al.
- *Direct Connection:* FEAT established the evolutionary feature construction paradigm—evolving symbolic trees as features for a predictor—that RAG-SR directly adopts and augments with a neural generator trained online.

**Distilling Free-Form Natural Laws from Experimental Data** (2009)
- *Authors:* Michael Schmidt and Hod Lipson
- *Direct Connection:* This seminal GP-based symbolic regression work introduced the expression-tree search framework that RAG-SR retains while replacing purely stochastic variation with neural, retrieval-guided proposal of trees.

### 💡 Inspiration

**DreamCoder: Growing Generalizable, Interpretable Knowledge with Wake-Sleep Program Induction** (2021)
- *Authors:* Kevin Ellis et al.
- *Direct Connection:* DreamCoder’s library learning and reuse of discovered program fragments motivated RAG-SR’s retrieval of previously validated subexpressions as building blocks to steer generation and reduce hallucinations.

### 📊 Baseline

**Deep Symbolic Regression** (2021)
- *Authors:* Felix Petersen et al.
- *Direct Connection:* DSR’s neural policy for generating expression trees is the primary neural SR baseline that RAG-SR improves upon by replacing unstable RL with online supervised learning and augmenting proposals with retrieval.

### 🔧 Extension

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Direct Connection:* RAG provided the core idea of conditioning generation on retrieved, verified contexts to reduce hallucinations, which RAG-SR adapts by retrieving semantically validated symbolic subtrees to guide equation generation.

### 🔗 Related Problem

**DeepCoder: Learning to Write Programs** (2017)
- *Authors:* Matej Balog et al.
- *Direct Connection:* DeepCoder demonstrated coupling a learned model with search to synthesize programs from input–output specifications, directly inspiring RAG-SR’s learned proposer that guides symbolic tree search from data semantics.

**AI Feynman: A Physics-Inspired Method for Symbolic Regression** (2020)
- *Authors:* Mihai Udrescu and Max Tegmark
- *Direct Connection:* AI Feynman’s robust heuristics for equation discovery highlight the strengths and limitations of non-neural SR, motivating RAG-SR’s integration of neural guidance with search to better handle unseen functions and variables.

---

## Synthesis: How Prior Work Led to This Paper

Genetic programming for symbolic regression formalized searching over expression trees to discover data-consistent laws, with Eureqa showing that evolutionary operators over trees can recover concise equations from measurements. Building on this, FEAT reframed the task as evolutionary feature construction, evolving symbolic trees that feed a simple predictor—demonstrating that search over reusable features can outperform end-to-end model search. In program synthesis, DeepCoder showed that a learned model can predict useful primitives from specifications to guide enumerative search, while DreamCoder introduced wake–sleep library learning, reusing verified subprograms to make future search more reliable and sample-efficient. In neural symbolic regression, DSR proposed a neural policy that directly generates expression trees, exposing both the promise of neural guidance and the pitfalls of hallucination and unstable RL training. Orthogonally, Retrieval-Augmented Generation established that conditioning generation on retrieved, relevant, verified contexts reduces hallucinations and improves factual grounding.
Taken together, these works expose a natural opportunity: combine evolutionary feature construction with a learned, data-conditioned generator, and stabilize neural proposals by retrieving validated building blocks during search. RAG-SR seizes this by training a lightweight language model online to propose symbolic trees aligned with dataset semantics, embedding it within FEAT-style feature evolution, and using RAG-style retrieval of previously verified expressions to curb hallucinations—yielding a pretraining-free, search-integrated neural SR framework that generalizes to unseen functions and variables.

---

*Analysis generated on: 2026-01-06T18:42:47.796132*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

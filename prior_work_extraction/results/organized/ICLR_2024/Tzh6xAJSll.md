# Prior Work Analysis Report

## Target Paper

**Title:** Scaling Laws for Associative Memories

**Conference:** ICLR 2024 (spotlight)

**Authors:** Vivien Cabannes, Elvis Dohmatob, Alberto Bietti

**Keywords:** scaling law, associative memory, mechanistic interpretability, Hopfield network

**Abstract:** 
> Learning arguably involves the discovery and memorization of abstract rules. The aim of this paper is to study associative memory mechanisms. Our model is based on high-dimensional matrices consisting of outer products of embeddings, which relates to the inner layers of transformer language models. We derive precise scaling laws with respect to sample size and parameter size, and discuss the statistical efficiency of different estimators, including optimization-based algorithms. We provide exten...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Associative Memory (Linear Associative Memory/Correlation Matrix Memory)** (1972)
- *Authors:* Teuvo Kohonen
- *Direct Connection:* The paper’s memory matrix is the linear associative memory W = Σ yx^T introduced by Kohonen, and the work derives precise scaling laws and estimator efficiency for this exact outer-product formulation.

**Neural networks and physical systems with emergent collective computational abilities** (1982)
- *Authors:* John J. Hopfield
- *Direct Connection:* Hopfield’s associative memory framework grounded capacity-vs-dimension tradeoffs via Hebbian outer products, which this work refines to continuous, high-dimensional embeddings with exact sample/parameter scaling predictions.

**Sparse Distributed Memory** (1988)
- *Authors:* Pentti Kanerva
- *Direct Connection:* Kanerva’s high-dimensional analysis of addressable memories and retrieval error informs the probabilistic framework this paper adapts to derive analytic scaling laws for key–value outer-product memories.

### 💡 Inspiration

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Jacob Geva et al.
- *Direct Connection:* By showing transformer feed-forward layers implement key–value memories via inner products, this work motivates modeling transformer internals as outer-product associative memories whose scaling this paper characterizes.

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* Their analysis of feature superposition and interference as width-limited phenomena directly informs this paper’s formalization of interference in associative memories and its closed-form error scaling with dimension and number of stored pairs.

### 🔍 Gap Identification

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Direct Connection:* This empirical scaling-law study motivates the need for principled, mechanistic scaling analyses, which the present work provides in a tractable associative-memory setting.

### 🔗 Related Problem

**Hopfield Networks is All You Need** (2021)
- *Authors:* Johannes Ramsauer et al.
- *Direct Connection:* The equivalence between attention and modern Hopfield networks established here underpins the connection between associative memory dynamics and transformer mechanisms that this paper leverages to interpret its scaling results.

---

## Synthesis: How Prior Work Led to This Paper

Kohonen’s linear associative memory precisely formalized key–value storage as a correlation matrix W formed by outer products Σ yx^T, with retrieval by linear projection and improvements via pseudoinverse rules; this directly specifies the estimator family at the heart of associative memory. Hopfield’s model established that Hebbian outer-product storage induces interference that limits capacity, highlighting how retrieval error scales with representational dimension. Kanerva extended this line of thought to high-dimensional addressable memories, providing probabilistic analyses of retrieval and noise that scale with dimension and sparsity. Geva and colleagues showed that transformer feed-forward layers function as key–value memories queried by inner products, concretely linking outer-product memory mechanisms to inner transformer computations. Ramsauer and coauthors connected attention updates to modern Hopfield dynamics, reinforcing the equivalence between associative memory retrieval and transformer operations. Kaplan and collaborators documented robust empirical power-law scaling in language models, underscoring the need for principled theories of scaling. Elhage and collaborators revealed how superposition creates interference when features outnumber dimensions, clarifying the linear-algebraic mechanics governing capacity.
Together, these works exposed a tractable, mechanistic memory (outer-product key–value storage) that closely mirrors transformer internals, identified interference as the core limitation, and called for analytic scaling characterizations akin to empirical LLM scaling laws. Building on Kohonen/Hopfield formulations with Kanerva’s high-dimensional perspective and the transformer–memory equivalence from Geva and Ramsauer, the paper derives precise sample- and parameter-size scaling laws and compares estimator efficiencies (Hebbian, pseudoinverse, and optimization-based), providing a principled explanation of how associative memory capacity and error scale in transformer-like settings.

---

*Analysis generated on: 2026-01-06T12:25:04.874659*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

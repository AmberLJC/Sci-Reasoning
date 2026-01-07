# Prior Work Analysis Report

## Target Paper

**Title:** Attention with Markov: A Curious Case of Single-layer Transformers

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ashok Vardhan Makkuva, Marco Bondaschi, Adway Girish, Alliot Nagle, Martin Jaggi, Hyeji Kim, Michael Gastpar

**Keywords:** Markov chains, Transformers, Optimization, Landscape

**Abstract:** 
> Attention-based transformers have achieved tremendous success across a variety of disciplines including natural languages. To deepen our understanding of their sequential modeling capabilities, there is a growing interest in using Markov input processes to study them. A key finding is that when trained on first-order Markov chains, transformers with two or more layers consistently develop an induction head mechanism to estimate the in-context bigram conditional distribution. In contrast, single-...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**In-context Learning and Induction Heads** (2022)
- *Authors:* Catherine Olsson et al.
- *Direct Connection:* This work established that training two-layer attention-only transformers on simple repeated-pattern data yields induction-head circuits that in-context estimate bigram conditionals, providing the exact benchmark mechanism for multi-layer models learning bigram statistics on Markov-like sequences.

**Theoretical Limitations of Self-Attention in Sequence Modeling** (2020)
- *Authors:* Michael Hahn
- *Direct Connection:* By characterizing self-attention as effectively finite-state, this paper underpins the claim that first-order Markov (bigram) dependencies are representable by shallow transformers, separating representational capacity from optimization issues.

**Are Transformers Universal Approximators of Sequence-to-Sequence Functions?** (2020)
- *Authors:* Chulhee Yun et al.
- *Direct Connection:* This universality result supports that attention-based architectures with positional encodings can represent the Markov kernel in principle, sharpening the focus on why training might converge to a unigram solution instead.

### 💡 Inspiration

**A Mechanistic Interpretability of GPT-2: Circuits** (2021)
- *Authors:* Chris Olah et al. (including Nelson Elhage, Neel Nanda, and colleagues)
- *Direct Connection:* By formalizing the induction head as a two-layer composition that copies the previous matching token to predict the next, this paper supplies the concrete circuit that explains why depth ≥2 transformers can implement bigram estimation whereas a single attention layer cannot.

### 🔍 Gap Identification

**Progress Measures for Grokking via Mechanistic Interpretability** (2023)
- *Authors:* Neel Nanda et al.
- *Direct Connection:* This study documented training dynamics where models persist in simple heuristics before a phase transition to induction circuits, motivating an analysis of the suboptimal ‘unigram’ basin and why certain architectures fail to escape it.

### 🔗 Related Problem

**Transformers Learn In-Context by Gradient Descent** (2022)
- *Authors:* Johannes von Oswald et al.
- *Direct Connection:* Interpreting in-context learning as implementing online estimation from context, this work motivates viewing depth-2 attention as an algorithm for bigram estimation on Markov sequences and highlights depth’s role in enabling such circuits.

---

## Synthesis: How Prior Work Led to This Paper

Work on induction heads showed that when attention-only transformers are trained on data with repeated tokens or simple statistical structure, two-layer models reliably form a circuit that matches a previous token and copies it forward to predict the next, effectively estimating bigram conditionals in-context. Mechanistic analyses formalized this circuit as a composition of two attention operations, clarifying why it specifically requires at least two layers. Training-dynamics studies around grokking further revealed that models often dwell in simple heuristics before transitioning to such algorithmic circuits, implying the presence of suboptimal basins in the loss landscape. Theoretical characterizations of self-attention established that attention behaves like a finite-state mechanism, capable of modeling first-order dependencies consistent with bigram or Markov structure. Complementary universality results for transformers with positional encodings reinforced that representational capacity is not the bottleneck for learning simple Markov kernels. Finally, a line of work reframed in-context learning as an online estimation or gradient-descent-like procedure carried out by the model, underscoring how architectural depth enables algorithmic circuits for estimating sequence statistics from context.
Taken together, these insights suggested a precise opportunity: under Markov-chain training, depth ≥2 transformers should implement the induction-head estimator of bigram conditionals, while depth-1 models, though expressive enough for first-order Markov kernels, might lack the circuit to escape simpler heuristics. The natural next step was to isolate Markov inputs, contrast single-layer versus multi-layer training behavior, and analyze the optimization landscape to explain the observed convergence to a unigram local minimum for single-layer attention despite its theoretical expressivity.

---

*Analysis generated on: 2026-01-06T11:37:14.431507*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

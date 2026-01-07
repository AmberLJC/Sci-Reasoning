# Prior Work Analysis Report

## Target Paper

**Title:** Revisiting Random Walks for Learning on Graphs

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jinwoo Kim, Olga Zaghen, Ayhan Suleymanzade, Youngmin Ryou, Seunghoon Hong

**Keywords:** Graph machine learning, random walk, invariance, universal approximation, markov chain

**Abstract:** 
> We revisit a simple model class for machine learning on graphs, where a random walk on a graph produces a machine-readable record, and this record is processed by a deep neural network to directly make vertex-level or graph-level predictions. We call these stochastic machines random walk neural networks (RWNNs), and through principled analysis, show that we can design them to be isomorphism invariant while capable of universal approximation of graph functions in probability. A useful finding is ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Anonymous Walk Embeddings** (2018)
- *Authors:* Sergey Ivanov et al.
- *Direct Connection:* The anonymity mapping for random walks in AWE establishes that anonymized walk patterns are isomorphism-invariant, a specific device RWNNs adopt to guarantee probabilistic invariance irrespective of the chosen record format (e.g., text).

**How Powerful are Graph Neural Networks?** (2019)
- *Authors:* Keyulu Xu et al.
- *Direct Connection:* GIN’s formalization of isomorphism-invariant expressivity and universal approximation provides the expressivity benchmark and proof template that RWNNs target and match—in probability—under anonymized walk records.

### 💡 Inspiration

**DeepWalk: Online Learning of Social Representations** (2014)
- *Authors:* Bryan Perozzi et al.
- *Direct Connection:* DeepWalk’s core idea of turning graphs into sequences via random walks directly motivates RWNNs’ use of walk-generated records that a neural reader consumes for downstream prediction, generalizing the Skip-gram objective to task-specific neural inference.

### 🔍 Gap Identification

**Graph Neural Networks Exponentially Lose Expressive Power for Node Classification** (2019)
- *Authors:* Kenta Oono et al.
- *Direct Connection:* This work’s proof that deep message passing collapses to an over-smoothed limit is the explicit shortcoming RWNNs address by replacing deep iterative averaging with finite random-walk records read once by a neural model.

**On the Bottleneck of Graph Neural Networks and its Practical Implications** (2021)
- *Authors:* Uri Alon et al.
- *Direct Connection:* The identification of over-squashing as an information bottleneck frames RWNNs’ analysis, where the paper shows oversquashing can still manifest (albeit differently) even as over-smoothing is alleviated.

### 📊 Baseline

**Neural Message Passing for Quantum Chemistry** (2017)
- *Authors:* Justin Gilmer et al.
- *Direct Connection:* The MPNN framework is the principal baseline whose iterative propagation RWNNs reinterpret through Markov-chain operators, enabling a direct comparison that highlights RWNNs’ alleviation of over-smoothing by construction.

### 🔗 Related Problem

**Predict then Propagate: Graph Neural Networks meet Personalized PageRank** (2019)
- *Authors:* Johannes Klicpera et al.
- *Direct Connection:* APPNP’s use of a Personalized PageRank (random-walk-with-restart) operator to control diffusion motivates the paper’s Markov-chain lens and supports the claim that finite-length/random-walk propagation mitigates over-smoothing.

---

## Synthesis: How Prior Work Led to This Paper

DeepWalk introduced the concrete mechanism of representing a graph by sequences produced from random walks, then learning from these sequences with a language-modeling objective—establishing that walk-generated records are a powerful, model-consumable interface to graph structure. Anonymous Walk Embeddings showed that mapping node identities to anonymous roles within walk patterns yields isomorphism-invariant statistics, isolating the precise anonymization trick that preserves invariance while still encoding structural signals. The MPNN framework formalized neural message passing as iterative neighborhood aggregation, providing the de facto baseline and a blueprint for relating graph learning dynamics to linear operators. GIN crystallized the connection between isomorphism testing and graph-network expressivity, proving universal approximation for invariant functions and setting the benchmark for theoretical power. APPNP demonstrated that a Personalized PageRank (random-walk-with-restart) propagator can control diffusion length, connecting propagation depth to random-walk processes. Oono and Suzuki proved that deep message passing inevitably over-smooths, while Alon and Yahav identified over-squashing as an information bottleneck in long-range dependency propagation. Together, these works revealed that random-walk records can be fed directly to neural readers, that anonymization is the key to invariance, and that diffusion depth is the root of smoothing and squashing pathologies. Building on this, the current paper defines random walk neural networks that consume anonymized walk records in flexible formats (even plain text), establishes isomorphism-invariant universal approximation in probability, and uses a Markov-chain perspective to show over-smoothing is alleviated by construction while clarifying how over-squashing remains and where it arises.

---

*Analysis generated on: 2026-01-06T13:23:30.234093*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

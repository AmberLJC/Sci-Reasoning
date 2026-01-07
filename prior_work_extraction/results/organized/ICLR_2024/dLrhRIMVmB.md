# Prior Work Analysis Report

## Target Paper

**Title:** Topological data analysis on noisy quantum computers

**Conference:** ICLR 2024 (oral)

**Authors:** Ismail Yunus Akhalwaya, Shashanka Ubaru, Kenneth L. Clarkson, Mark S. Squillante, Vishnu Jejjala, Yang-Hui He, Kugendran Naidoo, Vasileios Kalantzis, Lior Horesh

**Keywords:** Topological data analysis, quantum computing, unsupervised learning, feature extraction

**Abstract:** 
> Topological data analysis (TDA) is a powerful technique for extracting complex and valuable shape-related summaries of high-dimensional data. However, the computational demands of classical algorithms for computing TDA are exorbitant, and quickly become impractical for high-order characteristics. Quantum computers offer the potential of achieving significant speedup for certain computational problems. Indeed, TDA has been purported to be one such problem, yet, quantum computing algorithms propos...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Topological persistence and simplification** (2002)
- *Authors:* Herbert Edelsbrunner et al.
- *Direct Connection:* This work formalized persistent homology and filtrations (e.g., Vietoris–Rips), providing the exact problem formulation and invariants that NISQ-TDA targets to summarize data topology over scales.

**The Euler Characteristic Transform** (2018)
- *Authors:* Justin Curry et al.
- *Direct Connection:* By showing that the Euler characteristic along filtrations yields robust, computable summaries, this paper motivates using simplex-count–based topological signatures that NISQ-TDA can estimate with shallow quantum counting rather than full persistent homology linear algebra.

**Quantum Amplitude Amplification and Estimation** (2002)
- *Authors:* Gilles Brassard et al.
- *Direct Connection:* NISQ-TDA directly uses amplitude amplification/estimation as the low-depth quantum primitive to approximately count marked k-simplices across a filtration, yielding the quadratic speedup that underpins its asymptotic advantage.

### 🔍 Gap Identification

**Ripser: Efficient computation of Vietoris–Rips persistence barcodes** (2019)
- *Authors:* Ulrich Bauer
- *Direct Connection:* Ripser exemplifies the state-of-the-art classical approach whose runtime and memory blow up with high-order simplices, a concrete limitation NISQ-TDA addresses by replacing matrix-reduction with quantum approximate counting across filtrations.

### 📊 Baseline

**Quantum algorithms for topological and geometric analysis of data** (2016)
- *Authors:* Seth Lloyd et al.
- *Direct Connection:* The original QTDA introduced a quantum pipeline to compute Betti numbers via phase estimation and qRAM-accessible boundary operators, whose fault-tolerant and data-loading requirements NISQ-TDA explicitly removes by replacing them with low-depth, oracle-based counting primitives.

### 🔧 Extension

**Linear-Size Approximations to the Vietoris–Rips Filtration** (2013)
- *Authors:* Donald R. Sheehy
- *Direct Connection:* Sheehy’s sparsified Rips filtration reduces the number of simplices to query, and NISQ-TDA leverages this sparsification to define efficient quantum oracles and achieve provable query-time savings for counting-based topological summaries.

### 🔗 Related Problem

**Quantum algorithms for the triangle problem** (2011)
- *Authors:* Frédéric Magniez et al.
- *Direct Connection:* Their oracle-based framework for subgraph detection guides NISQ-TDA’s design of shallow quantum query oracles to detect and count cliques (simplices) within Rips graphs at varying thresholds.

---

## Synthesis: How Prior Work Led to This Paper

Lloyd, Garnerone, and Zanardi proposed a quantum pipeline to compute topological invariants by encoding boundary operators and using phase estimation, establishing that persistent topological features could, in principle, be extracted with quantum speedups but at the cost of fault tolerance and qRAM. Edelsbrunner, Letscher, and Zomorodian set the core formulation of persistent homology on filtrations such as Vietoris–Rips, defining the invariants and filtration processes relevant for data analysis. Curry, Mukherjee, and Turner showed that the Euler characteristic along filtrations yields informative, stable summaries computable by counting simplices rather than solving large linear systems, thus highlighting a counting-based alternative to full persistence. Sheehy introduced sparsified Rips filtrations of linear size, drastically cutting the number of simplices while preserving topological information, which in turn makes oracle-based queries far more tractable. Brassard, Hoyer, Mosca, and Tapp provided amplitude estimation, a shallow-circuit primitive for approximate counting with quadratic query advantage. Magniez, Santha, and Szegedy’s oracle-based subgraph detection framework further illustrated how to design quantum queries for clique-like structures in graphs. Meanwhile, Ripser demonstrated the classical ceiling: even with highly optimized reduction, high-order features trigger prohibitive time/memory growth.
Together these works exposed an opportunity: swap fault-tolerant linear algebra for NISQ-friendly counting of simplices over sparsified filtrations, using amplitude estimation within an oracle framework to recover topological summaries. NISQ-TDA synthesizes these ideas by building efficient Rips-like oracles, leveraging sparsification to bound query complexity, and using quantum approximate counting to produce Euler-characteristic–based topological features with provable quadratic savings and practical, short-depth implementations.

---

*Analysis generated on: 2026-01-06T10:24:43.435340*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

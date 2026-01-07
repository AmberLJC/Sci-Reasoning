# Prior Work Analysis Report

## Target Paper
**Title:** UFlyLkvyAE
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Autoregressive Moving Average Graph Filters** (2017)
- *Authors:* Elvin Isufi et al.
- *Connection:* Established permutation-equivariant ARMA graph filters as rational graph filters; GRAMA directly adopts this formalism and makes the ARMA coefficients dynamically learnable over sequential graph data.

**Efficiently Modeling Long Sequences with Structured State Spaces** (2022)
- *Authors:* Albert Gu et al.
- *Connection:* Introduced S4, showing how SSMs capture long-range dependencies via structured convolutions; GRAMA leverages the ARMA–SSM connection to endow graph models with SSM-style long-range sequence modeling while preserving permutation equivariance.

**Time Series Analysis** (1994)
- *Authors:* James D. Hamilton
- *Connection:* Classically formalized the equivalence between ARMA and state-space representations; GRAMA relies on this equivalence to justify its ARMA-based construction as a graph state-space model.

### 💡 Inspiration

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2024)
- *Authors:* Albert Gu et al.
- *Connection:* Proposed selective (input-dependent) SSM parameters enabling dynamic long-range modeling; GRAMA mirrors this selectivity by learning input-conditioned ARMA coefficients and provides theoretical links to selective SSMs on graphs.

### 🔍 Gap Identification

**Graph Mamba: Towards Learning on Graphs with Selective State Spaces** (2024)
- *Authors:* Liu et al.
- *Connection:* Applied selective SSMs to graphs via node orderings that break permutation equivariance; GRAMA explicitly addresses this limitation by designing a permutation-equivariant, graph-adaptive ARMA mechanism without imposing node sequences.

### 📊 Baseline

**Graph Neural Networks with Convolutional ARMA Filters** (2019)
- *Authors:* Filippo Maria Bianchi et al.
- *Connection:* Operationalized ARMA graph filters within GNN layers; GRAMA extends this baseline by moving from static graphs to sequences and by introducing selective, input-conditioned ARMA coefficients for long-range propagation.

---

## Synthesis

GRAMA’s core idea is to realize long-range, permutation-equivariant graph sequence modeling by marrying graph ARMA filtering with the modern state-space view of long-context sequence models. The lineage begins in graph signal processing with ARMA graph filters (Isufi et al.), which provide permutation-equivariant rational graph filters. Bianchi et al. brought ARMA filters into GNNs, yielding a practical baseline that GRAMA directly extends: from static filtering with fixed coefficients to sequence-aware, input-conditioned ARMA dynamics. On the sequence-modeling side, S4 (Gu et al.) crystallized how state-space models capture long-range dependencies efficiently. GRAMA explicitly exploits the classical equivalence between ARMA and state-space representations (Hamilton), using it to reinterpret graph ARMA filtering as a graph SSM and to transfer SSM insights to graphs. Recent selective SSM developments—most notably Mamba—demonstrated that input-dependent gating of state updates markedly improves expressivity and efficiency; GRAMA’s selective attention over ARMA coefficients is a graph-equivariant instantiation of this idea. Finally, early attempts to port selective SSMs to graphs, such as Graph Mamba, often imposed node orderings that compromise permutation equivariance. GRAMA targets this precise gap, retaining the benefits of selective SSMs while maintaining strict permutation equivariance through a graph-adaptive ARMA construction, thus enabling efficient, flexible long-range information propagation on sequential graphs.

---
*Generated: 2026-01-06T23:07:19.601448*

# Prior Work Analysis Report

## Target Paper

**Title:** Streaming Algorithms For $\ell_p$ Flows and $\ell_p$ Regression

**Conference:** ICLR 2025 (spotlight)

**Authors:** Amit Chakrabarti, Jeffrey Jiang, David Woodruff, Taisuke Yasuda

**Keywords:** Regression, Streaming, Online algorithms, Flows

**Abstract:** 
> We initiate the study of one-pass streaming algorithms for underdetermined $\ell_p$ linear regression problems of the form
  $$
      \min_{\mathbf A\mathbf x = \mathbf b} \lVert\mathbf x\rVert_p \,, \qquad 
      \text{where } \mathbf A \in \mathbb R^{n \times d} \text{ with } n \ll d \,,
  $$
  which generalizes basis pursuit ($p = 1$) and least squares solutions to
  underdetermined linear systems ($p = 2$). We study the column-arrival
  streaming model, in which the columns of $\mathbf A$ ar...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Atomic Decomposition by Basis Pursuit** (1998)
- *Authors:* Scott S. Chen et al.
- *Direct Connection:* It formalizes the p=1 case (basis pursuit) of minimizing ||x||1 subject to Ax=b, which is a primary special case within the paper’s unified underdetermined ℓp regression/flow formulation.

**Graph Sketches: Sparsification, Spanners, and Subgraphs** (2012)
- *Authors:* Kook Jin Ahn et al.
- *Direct Connection:* It establishes the edge-insertion streaming model and graph sketching primitives that underlie interpreting column-arrival matrices as graph streams when A is an incidence matrix.

### 💡 Inspiration

**Spectral Sparsification in the Semi-Streaming Setting** (2013)
- *Authors:* Jonathan A. Kelner et al.
- *Direct Connection:* The resparsify-on-arrival methodology for maintaining a small edge set while approximating quadratic energy inspires the paper’s one-pass maintenance of a small set of high-sensitivity columns/edges that preserves ℓp objective value.

### 🔍 Gap Identification

**Low-Rank Approximation and Regression in Input Sparsity Time** (2013)
- *Authors:* Kenneth L. Clarkson et al.
- *Direct Connection:* This work’s sketch-and-solve methods address overdetermined (row-arrival) regression, and its inability to handle underdetermined column-arrival settings directly motivates the new dual-oriented streaming approach developed here.

### 📊 Baseline

**Spectral Sparsification in the Dynamic Streaming Model** (2014)
- *Authors:* Michael Kapralov et al.
- *Direct Connection:* For p=2 (electrical flows), their dynamic-streaming sparsifiers give near-optimal space estimators of b^T L^+ b, serving as the p=2 baseline that the present work generalizes to all p and to underdetermined column-arrival regression beyond graphs.

### 🔧 Extension

**ℓp Row Sampling by Lewis Weights** (2015)
- *Authors:* Michael B. Cohen et al.
- *Direct Connection:* The paper’s one-pass column-oriented sketches for underdetermined ℓp regression adapt the Lewis-weights/sensitivity framework to the dual ℓq constraints, effectively turning row-sampling ideas of Cohen–Peng into column/edge sampling for estimating ℓp flow costs.

### 🔗 Related Problem

**Electrical Flows, Laplacian Systems, and Faster Approximation of Maximum Flow in Undirected Graphs** (2011)
- *Authors:* Paul Christiano et al.
- *Direct Connection:* By casting max flow and related problems through the lens of electrical (ℓ2) flows, this work motivates treating ℓp flows as a unifying objective across p and informs the paper’s focus on estimating optimal ℓp flow costs from edge streams.

---

## Synthesis: How Prior Work Led to This Paper

Lewis-weight sampling established that ℓp regression objectives can be preserved by selecting high-sensitivity rows, giving provable subspace embeddings and sample complexity guarantees tailored to p. Spectral sparsification in dynamic streams showed that one can maintain near-linear-size summaries of a graph that preserve quadratic energies b^T L^+ b, yielding accurate electrical-flow costs in small space even under adversarial edge updates. The semi-streaming resparsify-on-arrival technique refined this approach, repeatedly compressing edges based on leverage-like scores to keep sketches tiny while preserving energy. Sketch-and-solve regression in input-sparsity time demonstrated powerful one-pass linear-algebraic sketches, but crucially for overdetermined, row-arrival settings, leaving the dual, column-arrival regime unaddressed. Basis pursuit introduced the canonical ℓ1 minimization under linear constraints, anchoring the ℓp family’s underdetermined formulation. Electrical-flow methods connected ℓ2 energies with flow optimization and even max-flow approximations, highlighting ℓp norms as a common language for flows. Graph sketching works formalized the edge-insertion model and provided core primitives for maintaining flow-relevant summaries under streaming. Together, these works reveal both a methodological toolkit—sensitivity sampling, resparsification, and spectral sketching—and a gap: no one-pass method for underdetermined, column-arrival ℓp regression or general ℓp flows. The current paper synthesizes Lewis-weight style sensitivities in the dual ℓq space with resparsify-on-arrival ideas to maintain a small, one-pass column/edge summary that provably preserves optimal ℓp objective values, thereby extending spectral-style guarantees from p=2 to all p and unifying regression and flow estimation in the column-arrival streaming model.

---

*Analysis generated on: 2026-01-06T14:52:37.490159*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

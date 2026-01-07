# Prior Work Analysis Report

## Target Paper

**Title:** Statistically Optimal $K$-means Clustering via Nonnegative Low-rank Semidefinite Programming

**Conference:** ICLR 2024 (oral)

**Authors:** Yubo Zhuang, Xiaohui Chen, Yun Yang, Richard Y. Zhang

**Keywords:** clustering, Burer-Monteiro, semidefinite programming

**Abstract:** 
> $K$-means clustering is a widely used machine learning method for identifying patterns in large datasets. Recently, semidefinite programming (SDP) relaxations have been proposed for solving the $K$-means optimization problem, which enjoy strong statistical optimality guarantees. However, the prohibitive cost of implementing an SDP solver renders these guarantees inaccessible to practical datasets. In contrast, nonnegative matrix factorization (NMF) is a simple clustering algorithm widely used by...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Approximating K-means-type Clustering via Semidefinite Programming** (2007)
- *Authors:* Peng et al.
- *Direct Connection:* The paper adopts the Peng–Wei SDP relaxation as the convex k-means formulation and then solves a nonnegative low-rank restriction of this exact SDP.

**Clustering Subgaussian Mixtures via Semidefinite Programming** (2017)
- *Authors:* Mixon et al.
- *Direct Connection:* This work establishes the statistical optimality and exact recovery conditions for the Peng–Wei k-means SDP, which the new algorithm is designed to match while being computationally scalable.

### 💡 Inspiration

**A Nonlinear Programming Algorithm for Solving Semidefinite Programs via Low-Rank Factorization** (2003)
- *Authors:* Burer et al.
- *Direct Connection:* The method directly uses the Burer–Monteiro low-rank factorization to turn the k-means SDP into a tractable nonconvex optimization over low-rank factors with nonnegativity.

**The Nonconvex Burer–Monteiro Approach Works on Smooth Semidefinite Programs** (2018)
- *Authors:* Boumal et al.
- *Direct Connection:* Global optimality insights for Burer–Monteiro factorizations motivate the paper’s use of low-rank nonconvex optimization to retain SDP-level guarantees, adapted here to include nonnegativity constraints.

### 📊 Baseline

**SymNMF: Nonnegative Low-Rank Approximation for Clustering** (2015)
- *Authors:* Kuang et al.
- *Direct Connection:* Symmetric NMF provides the practical, scalable clustering template whose simplicity the new method emulates while supplying the missing SDP-level statistical guarantees.

### 🔗 Related Problem

**On the Equivalence of Nonnegative Matrix Factorization and Spectral Clustering** (2005)
- *Authors:* Ding et al.
- *Direct Connection:* The equivalence between orthogonality-constrained NMF and clustering suggests the NMF-like structure used in the proposed nonnegative low-rank parameterization of the SDP.

---

## Synthesis: How Prior Work Led to This Paper

The Peng–Wei relaxation formulated k-means as a semidefinite program, providing a clean convex surrogate for the combinatorial objective with an assignment-matrix interpretation that later works could analyze. Building on this formulation, results on subgaussian mixtures showed that the k-means SDP achieves exact recovery and near-optimal statistical separation conditions, establishing the benchmark statistical guarantees for convex relaxations of k-means. Independently, the Burer–Monteiro factorization proposed replacing the SDP variable by a low-rank product to obtain a scalable nonconvex program, and subsequent theory on the Burer–Monteiro landscape demonstrated that, under mild conditions, such factorizations can avoid spurious local minima and recover SDP optima. In parallel, NMF-based clustering advanced practical simplicity: the equivalence between orthogonality-constrained NMF and spectral clustering clarified why nonnegativity and low-rank structure induce cluster assignments, and SymNMF provided an efficient algorithmic template for large-scale clustering, albeit without rigorous statistical optimality.

Together, these strands reveal a gap and an opportunity: SDPs deliver optimal statistical guarantees yet are computationally prohibitive, while NMF is scalable but lacks theory. By taking the Peng–Wei k-means SDP as the target of statistical optimality, importing the Burer–Monteiro low-rank parameterization to make it scalable, and imposing nonnegativity in an NMF-like factorization aligned with clustering structure, the current work synthesizes these ideas to produce an algorithm as simple as SymNMF yet provably matching the SDP’s optimal recovery guarantees.

---

*Analysis generated on: 2026-01-07T00:07:10.718583*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

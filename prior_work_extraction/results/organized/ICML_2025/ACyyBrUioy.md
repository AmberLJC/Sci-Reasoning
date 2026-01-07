# Prior Work Analysis Report

## Target Paper
**Title:** ACyyBrUioy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Classification and Regression Trees** (1984)
- *Authors:* Leo Breiman et al.
- *Connection:* CART established the greedy, top‑down decision tree paradigm that is fast but provably suboptimal, directly motivating SPLIT’s aim to retain greedy‑level scalability while recovering (near‑)optimal accuracy.

**Optimal Classification Trees** (2017)
- *Authors:* Dimitris Bertsimas et al.
- *Connection:* OCT formalized globally optimal decision tree learning via mixed‑integer optimization and showed accuracy/sparsity gains at high computational cost, defining the optimality target that SPLIT seeks to approximate far more efficiently.

### 💡 Inspiration

**Learning Certifiably Optimal Rule Lists** (2017)
- *Authors:* William R. Angelino et al.
- *Connection:* CORELS pioneered certifiable discrete optimization for interpretable models using prefix‑based caching and tight bounds, techniques that informed the optimal‑search infrastructure in OSDT/GOSDT that SPLIT adapts with selective greediness.

### 🔍 Gap Identification

**Learning Optimal Classification Trees Using a Binary Linear Program** (2019)
- *Authors:* Sicco Verwer et al.
- *Connection:* This MILP formulation (BinOCT) demonstrated that exact trees are attainable but highlighted severe scalability limits of solving all subproblems to optimality—limits SPLIT overcomes by switching to greedy completion near leaves.

### 📊 Baseline

**Generalized and Scalable Optimal Sparse Decision Trees (GOSDT)** (2020)
- *Authors:* Aaron Y. Lin et al.
- *Connection:* GOSDT provided the L0‑regularized objective and a scalable exact B&B/DP solver for sparse trees; SPLIT directly modifies this line by selectively relaxing optimality in deeper subproblems to achieve orders‑of‑magnitude speedups with negligible performance loss.

### 🔧 Extension

**Learning Optimal Decision Trees Using Caching Branch-and-Bound Search (DL8.5)** (2020)
- *Authors:* Thibaut Aglin et al.
- *Connection:* DL8.5 introduced dynamic‑programming subproblem caching and tight bounds for branch‑and‑bound over tree substructures; SPLIT builds on this framework but departs by not solving every subproblem exactly, employing sparse lookahead and greediness near leaves to avoid the exponential blow‑up.

---

## Synthesis

SPLIT sits at the intersection of two traditions: fast but myopic greedy trees and globally optimal yet costly discrete optimization for trees. CART created the dominant greedy, top‑down formulation and exposed its suboptimality, setting the stage for optimal formulations such as Optimal Classification Trees (OCT), which showed that exact global optimization can markedly improve accuracy and sparsity but at prohibitive computational cost. Subsequent MILP approaches, notably BinOCT, reinforced both the benefits of exact trees and the scalability barrier that arises from solving every subtree to optimality.

The breakthrough toward scalable exactness came from branch‑and‑bound with dynamic programming over subproblems. DL8.5 introduced subproblem caching and tight bounds to reuse computations across overlapping subtrees, while GOSDT advanced an L0‑regularized objective and a highly engineered B&B/DP solver that produced certifiably optimal sparse trees. However, these methods still attempt to optimally resolve an exponential number of deep subproblems, which is the core scalability bottleneck.

SPLIT’s key innovation is to explicitly break that bottleneck: using sparse lookahead to prioritize where optimal search matters and switching to greediness near the leaves, it avoids solving deep subproblems to optimality while preserving near‑optimal quality. This idea directly extends the B&B/DP infrastructure of DL8.5 and GOSDT, and is inspired by certifiable discrete‑optimization design principles from CORELS. The result is a method that effectively marries the accuracy of optimal trees with the speed of greedy induction.

---
*Generated: 2026-01-06T23:07:19.569007*

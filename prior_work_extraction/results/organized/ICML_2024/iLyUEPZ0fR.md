# Prior Work Analysis Report

## Target Paper
**Title:** iLyUEPZ0fR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Efficiency of Coordinate Descent Methods on Huge-Scale Optimization Problems** (2012)
- *Authors:* Y. Nesterov et al.
- *Connection:* Nesterov established the modern CD/BCD framework and popularized block-wise Lipschitz stepsizes with associated complexity bounds; the current paper challenges this default by deriving the truly optimal block steps for two-block least-squares under orthogonality.

### 💡 Inspiration

**Two-Point Step Size Gradient Methods** (1988)
- *Authors:* J. Barzilai et al.
- *Connection:* Barzilai–Borwein showed that carefully chosen stepsizes can accelerate gradient methods on quadratic/least-squares problems without momentum; this paper adopts that philosophy at the block level, designing optimal block steps that deliver acceleration.

**Performance of First-Order Methods for Smooth Convex Minimization: A Novel Approach** (2014)
- *Authors:* Y. Drori et al.
- *Connection:* Drori–Teboulle’s worst-case analysis framework emphasizes optimizing algorithm parameters (e.g., stepsizes) to minimize convergence factors; analogously, this paper derives block stepsizes that minimize the asymptotic rate (spectral radius) for two-block least-squares.

### 🔍 Gap Identification

**On the Convergence of Block Coordinate Descent Type Methods** (2013)
- *Authors:* A. Beck et al.
- *Connection:* Beck and Tetruashvili’s deterministic rates for cyclic BCD with Lipschitz-based stepsizes have worse constants than full GD, a limitation explicitly motivating this paper’s search for optimal block stepsizes that provably close (and surpass) that gap in least-squares.

### 📊 Baseline

**A Coordinate Gradient Descent Method for Nonsmooth Separable Minimization** (2009)
- *Authors:* P. Tseng et al.
- *Connection:* This paper formalized coordinate/block gradient descent with per-block Lipschitz stepsizes (1/L_i); the present work directly revisits and optimizes this stepsize rule for least-squares, yielding closed-form block stepsizes that outperform the vanilla 1/L_i choice.

### 🔗 Related Problem

**Iteration Complexity of Randomized Block-Coordinate Descent Methods for Minimizing a Composite Function** (2014)
- *Authors:* P. Richtárik et al.
- *Connection:* This work analyzes randomized BCD using block Lipschitz constants and highlights rate constants tied to block smoothness; the present paper provides a deterministic counterpart showing that tailored, optimal block steps can yield superior asymptotic factors in least-squares.

---

## Synthesis

The core of this paper is to overturn the long-standing default stepsize rule for block gradient descent—1 over the block-wise Lipschitz constant—by exhibiting the truly optimal block stepsizes for least-squares in a clean two-block, orthogonal design. The coordinate/block gradient paradigm and its canonical stepsize trace directly to Tseng–Yun (CGD) and Nesterov’s coordinate-descent framework, which established per-block Lipschitz scaling and its complexity implications. However, deterministic analyses such as Beck–Tetruashvili—and related randomized analyses like Richtárik–Takáč—revealed that with these default stepsizes, BCD’s convergence constants are often worse than full gradient descent, leaving the empirical superiority of block methods theoretically unexplained. This gap motivates a re-examination of stepsize choice as the lever for acceleration. The inspiration comes from two lines: Barzilai–Borwein showed decades ago that stepsize design alone can substantially accelerate gradient methods on quadratic (least-squares) problems without resorting to momentum; and Drori–Teboulle’s performance-estimation view formalized optimizing algorithm parameters to minimize worst-case rates. Building on these, the present work targets the specific least-squares/two-block/orthogonal setting to derive closed-form optimal block stepsizes that minimize the asymptotic convergence factor. The result is a momentum-free, principled acceleration of block gradient descent that directly addresses the prior constant-gap, finally providing a theoretical explanation for the observed advantage of block updates over standard GD in this regime.

---
*Generated: 2026-01-06T23:09:26.398998*

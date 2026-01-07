# Prior Work Analysis Report

## Target Paper
**Title:** Hk2fFm7W8c
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Cubic regularization of Newton method and its global performance** (2006)
- *Authors:* Yurii Nesterov and Boris T. Polyak
- *Connection:* The paper’s global convergence to a second-order stationary point with cubic regularization is a direct extension of Nesterov–Polyak’s cubic-regularized Newton framework to the setting where the Hessian is deliberately not refreshed every iteration.

**Inexact Newton methods** (1982)
- *Authors:* R. S. Dembo et al.
- *Connection:* The paper’s local superlinear-rate justification for convex problems with quadratic regularization leverages the inexact-Newton viewpoint, interpreting stale Hessians as structured inexactness and verifying conditions under which superlinear convergence still holds.

### 💡 Inspiration

**A modification of Newton’s method** (1967)
- *Authors:* N. V. Shamanskii
- *Connection:* Shamanskii introduced periodic Jacobian/Hessian updates—reusing the same curvature across several steps—which is the precise ‘lazy Hessian’ idea this paper formalizes and endows with modern nonconvex complexity guarantees via (cubic/quadratic) regularization.

### 🔍 Gap Identification

**Sub-sampled Newton methods I: Global convergence** (2016)
- *Authors:* Farbod Roosta-Khorasani and Michael W. Mahoney
- *Connection:* Subsampled Newton methods highlight the iteration-by-iteration curvature cost and propose stochastic approximations; this paper addresses that gap by proving that exact Hessians need not be recomputed each iteration—optimally only every d steps—yielding provable arithmetic savings.

### 📊 Baseline

**Adaptive cubic regularisation methods for unconstrained optimization. Part II: worst-case global evaluation complexity** (2011)
- *Authors:* Coralia Cartis et al.
- *Connection:* ARC provides the baseline second-order method whose per-iteration Hessian updates this work makes lazy; the new analysis preserves ARC’s SOSP guarantees while provably reducing total arithmetic complexity by updating curvature only once every d iterations.

### 🔗 Related Problem

**Newton Sketch: A near-linear-time optimization method** (2015)
- *Authors:* Mert Pilanci and Martin J. Wainwright
- *Connection:* Newton Sketch reduces Hessian costs by sketching curvature each iteration; the present work tackles the same bottleneck by showing one can avoid any per-iteration recomputation, reusing an exact Hessian for multiple steps while retaining strong guarantees.

---

## Synthesis

The core of “Second-Order Optimization with Lazy Hessians” marries a classical but under-theorized idea—periodically reusing curvature—with the modern theory of cubic-regularized Newton methods. Nesterov and Polyak established cubic regularization as a robust globalization device ensuring convergence to second-order stationary points for nonconvex problems. Building on this foundation, Cartis, Gould, and Toint’s ARC framework set the prevailing baseline and worst-case evaluation complexity for cubic-regularized second-order methods, but implicitly assumes new curvature each iteration. Shamanskii’s modified Newton method supplied the key operational idea: compute a Jacobian/Hessian intermittently and reuse it across several steps. The present paper lifts Shamanskii’s intuition into the nonconvex optimization era, showing that with cubic regularization one can rigorously guarantee SOSP convergence even when the Hessian is kept ‘lazy’ for many iterations, and it quantifies an optimal refresh rate of once every d steps. For convex problems, the local superlinear convergence of the proposed quadratic-regularized variant can be understood through the inexact Newton lens of Dembo, Eisenstat, and Steihaug by treating the stale Hessian as structured inexactness. Finally, the work positions itself against contemporary attempts to lower curvature cost—such as Newton Sketch and subsampled Newton—that approximate Hessians every iteration; instead, it demonstrates that exact curvature can be amortized across iterations with provable complexity gains, improving the total arithmetic cost by a factor √d while preserving strong convergence guarantees.

---
*Generated: 2026-01-06T23:09:26.533946*

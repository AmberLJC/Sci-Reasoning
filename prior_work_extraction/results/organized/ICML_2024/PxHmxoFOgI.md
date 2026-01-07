# Prior Work Analysis Report

## Target Paper
**Title:** PxHmxoFOgI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Gradient methods for minimizing composite functions** (2013)
- *Authors:* Yurii Nesterov
- *Connection:* The paper’s generalized gradient mapping for constrained, nonsmooth objectives explicitly extends Nesterov’s composite-gradient mapping framework, and the proposed approximate stationarity notions reduce to his classical measure in the smooth/composite special cases.

**Stochastic First- and Zeroth-Order Methods for Nonconvex Stochastic Programming** (2013)
- *Authors:* Saeed Ghadimi et al.
- *Connection:* The zeroth-order stochastic gradient estimators and non-asymptotic stationarity analysis for unconstrained nonconvex problems in Ghadimi–Lan are adapted and extended here to constrained, nonsmooth objectives with new stationarity criteria.

**Random gradient-free minimization of convex functions** (2017)
- *Authors:* Yurii Nesterov et al.
- *Connection:* The two-point Gaussian smoothing and its bias–variance characterization underpin the paper’s zeroth-order algorithms and convergence proofs in the constrained nonsmooth nonconvex regime.

**Online Convex Optimization in the Bandit Setting** (2005)
- *Authors:* Abraham D. Flaxman et al.
- *Connection:* The one-point smoothing/gradient-estimation paradigm from bandit optimization motivates the black-box (zeroth-order) oracle model and smoothing techniques that this paper leverages for constrained problems.

### 💡 Inspiration

**Proximally Guided Stochastic Subgradient Method for Nonsmooth Nonconvex Optimization** (2019)
- *Authors:* Damek Davis et al.
- *Connection:* The notion of approximate stationarity via Moreau-envelope/gradient-mapping for nonsmooth nonconvex objectives in this line of work inspires the paper’s generalized stationarity definitions and their non-asymptotic stochastic analysis under constraints.

### 🔧 Extension

**Convergence rate of Frank–Wolfe for non-convex objectives** (2016)
- *Authors:* Simon Lacoste-Julien
- *Connection:* The authors directly generalize Lacoste-Julien’s Frank–Wolfe gap—used as a stationarity measure in smooth nonconvex constrained problems—to the nonsmooth setting and build their non-asymptotic guarantees around this generalized FW gap.

### 🔗 Related Problem

**Proximal Stochastic Methods for Nonsmooth Nonconvex Finite-Sum Optimization** (2016)
- *Authors:* Sashank J. Reddi et al.
- *Connection:* Their non-asymptotic analysis for proximal stochastic methods on nonsmooth nonconvex objectives (unconstrained/composite) provides the proximal/gradient-mapping stationarity template that this work adapts to constrained, zeroth-order settings.

---

## Synthesis

The core innovations of this ICML 2024 work—generalizing gradient mapping and the Frank–Wolfe (FW) gap to the nonsmooth constrained setting, defining corresponding approximate stationarity, and delivering non-asymptotic guarantees for stochastic zeroth-order methods—sit at the intersection of three lines of prior art. First, the stationarity framework builds on the composite optimization literature: Nesterov’s gradient mapping for composite minimization established the canonical projected/prox-based stationarity measure that the authors generalize to nonsmooth constrained problems; Reddi et al. and the proximally guided stochastic subgradient line (Davis et al.) showed how such measures yield non-asymptotic rates for nonsmooth nonconvex objectives, motivating the paper’s nonsmooth notions and proof techniques. Second, on the projection-free side, Lacoste-Julien formalized the FW gap as a stationarity certificate for smooth nonconvex constrained optimization; this paper extends that certificate to nonsmooth objectives, enabling a unified constrained nonsmooth stationarity notion. Third, the zeroth-order algorithmic toolkit descends from bandit/DFO smoothing: Flaxman et al. introduced one-point smoothing and Nesterov–Spokoiny established rigorous two-point Gaussian-smoothing estimators; Ghadimi–Lan translated these estimators into non-asymptotic guarantees for unconstrained nonconvex stochastic programs. Liu et al. synthesize and extend these ideas by (i) crafting nonsmooth constrained stationarity surrogates (generalized gradient mapping and FW gap) and (ii) proving non-asymptotic convergence of stochastic zeroth-order methods to these targets, thereby closing the gap where prior constrained approaches largely offered only asymptotic guarantees.

---
*Generated: 2026-01-06T23:09:26.478495*

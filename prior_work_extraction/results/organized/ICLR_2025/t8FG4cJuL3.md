# Prior Work Analysis Report

## Target Paper

**Title:** Classic but Everlasting: Traditional Gradient-Based Algorithms Converge Fast Even in Time-Varying Multi-Player Games

**Conference:** ICLR 2025 (oral)

**Authors:** Yanzheng Chen, Jun Yu

**Keywords:** time-varying games, Nash equilibrium, extra gradient algorithm, optimistic gradient algorithm

**Abstract:** 
> Last-iterate convergence behaviours of well-known algorithms are intensively investigated in various games, such as two-player bilinear zero-sum games.
However, most known last-iterate convergence properties rely on strict settings where the underlying games must have time-invariant payoffs.
Besides, the limited known attempts on the games with time-varying payoffs are in two-player bilinear time-varying zero-sum games and strictly monotone games. By contrast, in other time-varying games, the la...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The extragradient method for finding saddle points and other problems** (1976)
- *Authors:* G. M. Korpelevich
- *Direct Connection:* This work introduces the Extra-Gradient (EG) algorithm whose last-iterate behavior the current paper analyzes and extends from time-invariant settings to time-varying multi-player games.

**Finite-Dimensional Variational Inequalities and Complementarity Problems** (2003)
- *Authors:* F. Facchinei and J.-S. Pang
- *Direct Connection:* The monograph establishes the VI framework for Nash equilibria and residual-based stationarity metrics (including natural/tangent-cone residuals) that underpin the paper’s use of the recently proposed tangent residual and its modification.

### 💡 Inspiration

**Training GANs with Optimism** (2018)
- *Authors:* C. Daskalakis et al.
- *Direct Connection:* It popularized Optimistic Gradient Descent-Ascent (OGDA) and established last-iterate convergence in fixed bilinear zero-sum games, directly motivating the paper’s extension of OG to time-varying and multi-player regimes.

### 🔍 Gap Identification

**Online Learning in Time-Varying Games** (2021)
- *Authors:* P. Mertikopoulos et al.
- *Direct Connection:* This line of work formalizes time-varying games and provides tracking/regret guarantees but leaves open last-iterate convergence and rates of EG/OG beyond special cases, a gap directly addressed by the current paper.

### 📊 Baseline

**Tight Last-Iterate Convergence of Optimistic Gradient Descent-Ascent in Bilinear Games** (2020)
- *Authors:* C. Azizian et al.
- *Direct Connection:* It delivers sharp last-iterate rates for OGDA (and EG) in two-player bilinear zero-sum games with static payoffs, forming the primary benchmark that the present paper generalizes to time-varying payoffs and multi-player settings.

### 🔧 Extension

**A Variational Inequality Perspective on Generative Adversarial Networks** (2019)
- *Authors:* G. Gidel et al.
- *Direct Connection:* By casting games as variational inequalities and analyzing EG/OG under monotonicity/coherence with gap/residual measures, this work provides the operator framework and diagnostic metrics that the paper builds on via the (modified) tangent residual in time-varying games.

---

## Synthesis: How Prior Work Led to This Paper

The extragradient method introduced by Korpelevich provided the prototypical two-step lookahead scheme for monotone variational inequalities and saddle-point problems, forming the baseline algorithm whose behavior has been most thoroughly understood in time-invariant games. Training GANs with Optimism by Daskalakis et al. brought optimism into game dynamics via OGDA, showing last-iterate convergence in fixed bilinear zero-sum settings and making optimism a central tool for stabilizing game learning. Gidel et al. then reframed GANs and broader differentiable games as variational inequalities, connecting EG/OG to operator monotonicity/coherence and gap/residual diagnostics, thereby sharpening the analytical lens used to certify convergence. Azizian et al. established tight last-iterate rates for OGDA (and EG) in static bilinear games, setting quantitative benchmarks for classical dynamics under fixed payoffs. Meanwhile, the online learning in time-varying games literature of Mertikopoulos and collaborators formalized drifting payoffs and analyzed tracking/regret, but without last-iterate convergence guarantees for EG/OG beyond special cases. Finally, Facchinei and Pang’s VI foundations codified residual-based stationarity, including tangent-cone-based residuals that have recently been adopted in differentiable games.
Collectively, these works expose a gap: classical EG/OG enjoy sharp last-iterate behavior in static or strictly monotone regimes, and time-variation is understood mainly via regret, not last iterates. Bridging these, the current paper leverages VI residual tools—specifically a (modified) tangent residual—to extend last-iterate convergence and rates of EG/OG from fixed, two-player bilinear or strictly monotone cases to general time-varying, multi-player games under convergent perturbations.

---

*Analysis generated on: 2026-01-06T15:17:29.233602*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

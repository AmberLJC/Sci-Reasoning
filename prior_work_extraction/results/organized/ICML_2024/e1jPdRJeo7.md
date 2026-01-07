# Prior Work Analysis Report

## Target Paper
**Title:** e1jPdRJeo7
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Online Convex Optimization in the Bandit Setting** (2005)
- *Authors:* Flaxman et al.
- *Connection:* This paper introduced randomized smoothing–based gradient estimators from function values (bandit/zeroth-order feedback), which underpins the random-direction gradient oracle that ZPDVR averages to tame coordinate-wise variance.

**Random Gradient-Free Minimization of Convex Functions** (2017)
- *Authors:* Nesterov and Spokoiny
- *Connection:* It formalized the two-point Gaussian/spherical smoothing estimator and its bias/variance properties; ZPDVR builds directly on this estimator and designs a direction-averaging scheme to further reduce its variance.

**A Proximal Stochastic Gradient Method with Progressive Variance Reduction** (2014)
- *Authors:* Xiao and Zhang
- *Connection:* Prox-SVRG established the control-variate framework for composite (proximal) optimization, which ZPDVR adapts in zeroth-order form as the first layer that reduces sampling variance.

### 📊 Baseline

**Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization** (2018)
- *Authors:* Liu et al.
- *Connection:* This work first married variance reduction with zeroth-order gradients and highlighted that random-direction estimators suffer a large coordinate-wise variance—leading prior methods to use O(d) coordinate-wise finite differences—precisely the gap ZPDVR closes by reducing that variance via averaging without O(d) queries.

### 🔧 Extension

**SPIDER: Near-Optimal Nonconvex Optimization via Stochastic Path-Integrated Differential Estimator** (2018)
- *Authors:* Fang et al.
- *Connection:* ZPDVR leverages SPIDER-style recursive estimators to reduce sampling variance efficiently in the proximal setting, and then augments them with a new averaging trick to also suppress coordinate-wise variance.

### 🔗 Related Problem

**SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient** (2017)
- *Authors:* Nguyen et al.
- *Connection:* The recursive variance-reduction idea of SARAH informs ZPDVR’s sampling-variance control in finite-sum/stochastic settings before adding the second (direction) averaging layer.

---

## Synthesis

ZPDVR’s core idea—double variance reduction—stands on two pillars: classical randomized smoothing for zeroth-order gradients and modern control-variate recursion for sampling variance. The randomized smoothing lineage starts with Flaxman–Kalai–McMahan’s bandit formulation, which showed how to turn function evaluations into gradient surrogates, and is concretized by Nesterov–Spokoiny’s two-point Gaussian/spherical smoothing estimator whose variance properties guide ZPDVR’s direction-averaging design. On the sampling side, Prox-SVRG introduced the proximal variance-reduction architecture for composite optimization, while SARAH and SPIDER refined recursion to achieve strong sampling-variance control with minimal full-gradient costs—structures ZPDVR adapts in its proximal, zeroth-order inner loops. The immediate catalyst is Liu et al.’s ZO-SVRG, which revealed a critical limitation: random-direction estimators induce a large coordinate-wise variance term that slows convergence unless one switches to O(d) coordinate-wise finite differences, effectively approximating first-order information and incurring prohibitive query complexity in high dimensions. ZPDVR directly targets this bottleneck. It keeps the efficient recursive control-variate machinery (for sampling variance) from SVRG/SARAH/SPIDER, but replaces the O(d) coordinate-wise estimator with a principled averaging of random-direction gradients that shrinks the coordinate-wise variance sufficiently—achieving the benefits of variance reduction without first-order surrogates or dimension-dependent query inflation.

---
*Generated: 2026-01-06T23:09:26.415919*

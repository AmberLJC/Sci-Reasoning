# Prior Work Analysis Report

## Target Paper

**Title:** Quasi-Monte Carlo for 3D Sliced Wasserstein

**Conference:** ICLR 2024 (spotlight)

**Authors:** Khai Nguyen, Nicola Bariletto, Nhat Ho

**Keywords:** Sliced Wasserstein, Monte Carlo Methods, Point-Cloud, Quasi-Monte Carlo, Optimal Transport

**Abstract:** 
> Monte Carlo (MC) integration has been employed as the standard approximation method for the Sliced Wasserstein (SW) distance, whose analytical expression involves an intractable expectation. However, MC integration is not optimal in terms of absolute approximation error. To provide a better class of empirical SW, we propose quasi-sliced Wasserstein (QSW) approximations that rely on Quasi-Monte Carlo (QMC) methods. For a comprehensive investigation of QMC for SW, we focus on the 3D setting, speci...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Sliced and Radon Wasserstein barycenters of measures** (2015)
- *Authors:* Bonneel et al.
- *Direct Connection:* This work formalized the Sliced Wasserstein distance as an expectation over random directions on the unit sphere and approximated it via Monte Carlo sampling, which is precisely the integral estimator that QSW replaces with QMC point sets.

**Scrambled net variance for integrals of smooth functions** (1997)
- *Authors:* Owen
- *Direct Connection:* Owen’s randomized QMC theory guarantees unbiasedness and reduced variance via scrambling, directly enabling the paper’s Randomized Quasi-Sliced Wasserstein (RQSW) estimator for stochastic optimization.

### 🔍 Gap Identification

**Max-Sliced Wasserstein Distance and Its Use for Distribution Learning** (2019)
- *Authors:* Deshpande et al.
- *Direct Connection:* By showing that randomly sampled directions can be sample-inefficient and advocating deterministic, optimized projections, this paper highlights the core limitation of MC-based SW that QSW addresses with low-discrepancy (QMC) direction sets.

### 📊 Baseline

**Generalized Sliced Wasserstein Distances** (2019)
- *Authors:* Kolouri et al.
- *Direct Connection:* GSW operationalizes SW-type objectives in practice by sampling a finite set of random projections (MC), providing the standard empirical SW approximation that QSW/RQSW targets to improve in absolute error.

### 🔧 Extension

**QMC designs: Optimal order quasi-Monte Carlo integration on the sphere** (2014)
- *Authors:* Brauchart et al.
- *Direct Connection:* This work develops low-discrepancy point sets and optimal-order error results for QMC integration on S^2, providing the theoretical and constructive blueprint for the sphere-based QMC direction sets evaluated in QSW.

**Spherical Fibonacci Point Sets for Illumination Integrals** (2015)
- *Authors:* Keinert et al.
- *Direct Connection:* It introduces generalized spiral/Fibonacci constructions on the sphere with excellent uniformity, one of the deterministic QMC-style direction families empirically assessed for 3D SW in this paper.

**Minimal Discrete Energy on the Sphere** (1994)
- *Authors:* Rakhmanov et al.
- *Direct Connection:* This paper’s energy-minimization framework underpins the discrepancy-energy optimization strategy for near-uniform spherical point sets, a construction the authors adopt to build QMC directions for QSW.

---

## Synthesis: How Prior Work Led to This Paper

Sliced Wasserstein distances were defined as expectations of one-dimensional Wasserstein distances over directions on the unit sphere, with practical approximation via Monte Carlo sampling of random projections, as established by Bonneel et al. Later, Kolouri et al. operationalized such SW-type objectives broadly, standardizing the use of finite random directions as the empirical SW estimator in applications. However, Deshpande et al. revealed that randomly chosen projections are often sample-inefficient, motivating deterministic selection of directions to reduce variance—signaling that the projection set itself is a bottleneck. In parallel, Owen’s randomized QMC theory showed that scrambling low-discrepancy sets yields unbiased estimators with markedly lower variance for smooth integrands, thereby reconciling variance reduction with the unbiasedness required in stochastic optimization. On the spherical domain specifically, Brauchart et al. developed QMC designs achieving optimal-order error for integration on S^2 and provided constructions based on discrepancy/energy principles. Complementing this, Keinert et al. introduced spherical Fibonacci (generalized spiral) point sets with excellent uniformity, while Rakhmanov et al. grounded energy-based optimization of spherical point sets through minimal Riesz-type energy formulations. Together, these works exposed MC sampling as a suboptimal approximation of the SW integral and supplied concrete QMC constructions on S^2 as well as randomized QMC machinery for unbiasedness. The current paper naturally synthesizes these strands by replacing MC directions with low-discrepancy spherical designs (including spiral and energy-optimized sets) for 3D SW and by deploying scrambling to create an unbiased randomized QSW estimator suitable for stochastic optimization, yielding lower absolute approximation error without changing the SW objective.

---

*Analysis generated on: 2026-01-06T16:46:58.641285*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

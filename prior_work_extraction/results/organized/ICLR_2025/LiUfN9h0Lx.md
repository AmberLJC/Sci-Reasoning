# Prior Work Analysis Report

## Target Paper

**Title:** Efficient and Accurate Explanation Estimation with Distribution Compression

**Conference:** ICLR 2025 (spotlight)

**Authors:** Hubert Baniecki, Giuseppe Casalicchio, Bernd Bischl, Przemyslaw Biecek

**Keywords:** explainable ai, feature attributions, feature importance, sampling, kernel thinning

**Abstract:** 
> We discover a theoretical connection between explanation estimation and distribution compression that significantly improves the approximation of feature attributions, importance, and effects. While the exact computation of various machine learning explanations requires numerous model inferences and becomes impractical, the computational cost of approximation increases with an ever-increasing size of data and model parameters. We show that the standard i.i.d. sampling used in a broad spectrum of...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**An Efficient Explanation of Individual Classifications using Game Theory** (2010)
- *Authors:* Strumbelj and Kononenko
- *Direct Connection:* This work introduces Monte Carlo Shapley sampling for local explanations, whose high-variance i.i.d. coalition sampling is the precise bottleneck CTE addresses by compressing the input distribution before estimation.

**Greedy Function Approximation: A Gradient Boosting Machine** (2001)
- *Authors:* Friedman
- *Direct Connection:* Partial Dependence relies on marginal expectations approximated with sample averages, and CTE targets this integration step by replacing raw i.i.d. samples with a kernel-thinned subset that better matches the data marginal.

**Visualizing the Effects of Predictor Variables in Black Box Supervised Learning Models** (2020)
- *Authors:* Apley and Zhu
- *Direct Connection:* ALE estimates effects via local integrals over the empirical distribution, and CTE improves these estimates by pre-compressing data with kernel thinning to reduce sampling error without extra runtime.

### 💡 Inspiration

**Stein Thinning: Selecting Representative Samples from Markov Chain Simulations** (2020)
- *Authors:* Riabiz et al.
- *Direct Connection:* Stein Thinning formalizes selecting a small, representative subset by minimizing a kernel-based discrepancy, and CTE adopts this distribution-compression principle to pre-compress background data used in explanation estimation.

**Support Points** (2018)
- *Authors:* Mak and Joseph
- *Direct Connection:* Support Points show that optimizing a discrepancy objective yields small subsets that reduce Monte Carlo integration error, directly motivating CTE’s use of kernel-based compression before computing explanations.

### 📊 Baseline

**A Unified Approach to Interpreting Model Predictions** (2017)
- *Authors:* Lundberg and Lee
- *Direct Connection:* KernelSHAP and related SHAP estimators rely on i.i.d. background sampling over feature coalitions, and CTE directly replaces this i.i.d. step with kernel-thinned compression to reduce Monte Carlo error and stabilize SHAP attributions.

**Understanding Global Feature Importance with SAGE** (2020)
- *Authors:* Covert et al.
- *Direct Connection:* SAGE estimates global Shapley-based importance via Monte Carlo over feature subsets and background draws, and CTE injects distribution compression to improve the accuracy and efficiency of these estimates at low sample budgets.

---

## Synthesis: How Prior Work Led to This Paper

Shapley-based explainers emerged from Monte Carlo coalition sampling for local explanations, with Strumbelj and Kononenko demonstrating practical Shapley estimation via i.i.d. draws over feature subsets. Lundberg and Lee’s SHAP unified local attribution with KernelSHAP’s weighted sampling over coalitions and background data, operationalizing Shapley estimation but inheriting the variance and scaling issues of i.i.d. sampling. For global importance, SAGE computes Shapley-based aggregations through Monte Carlo over subsets and background draws, again depending critically on the quality of i.i.d. samples. Partial Dependence defined feature effects as marginal expectations over the data distribution, and ALE refined this with local accumulation; both ultimately approximate integrals over empirical marginals via sampling. In parallel, distribution compression methods showed that carefully chosen subsets can dramatically reduce integration error: Support Points minimize an energy-distance objective to obtain representative samples, while Stein Thinning selects subsets by minimizing a kernel-based discrepancy, offering deterministic, sample-efficient alternatives to i.i.d. Monte Carlo.
Together, these strands reveal a clear gap: explanation algorithms hinge on i.i.d. sampling to approximate expectations over data marginals and coalitions, yet distribution compression can provably deliver better finite-sample approximations. The natural synthesis is to pre-compress the background distribution before explanation—replacing i.i.d. draws with a small, representative set selected by a kernel-based discrepancy criterion. Building on these insights, the current work connects explanation estimation to distribution compression and instantiates this connection via kernel thinning, yielding more accurate and stable feature attributions, importance, and effects with negligible overhead.

---

*Analysis generated on: 2026-01-06T15:28:39.255958*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

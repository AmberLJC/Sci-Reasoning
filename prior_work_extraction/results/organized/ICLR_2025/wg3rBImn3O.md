# Prior Work Analysis Report

## Target Paper
**Title:** wg3rBImn3O
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**A Value for n-Person Games** (1953)
- *Authors:* Lloyd S. Shapley
- *Connection:* Defines the Shapley value—the target quantity that Leverage SHAP provably estimates—establishing the core cooperative game-theoretic attribution objective used throughout.

**Explaining prediction models and individual predictions with feature contributions** (2014)
- *Authors:* Erik Strumbelj et al.
- *Connection:* Introduces model-agnostic Shapley-value-based explanations via sampling over coalitions, establishing the coalition-evaluation framework that Kernel SHAP and the proposed leverage-based estimator operate within.

**Fast least squares regression via randomized sampling** (2011)
- *Authors:* Petros Drineas et al.
- *Connection:* Provides the core guarantee that sampling rows proportional to (approximate) leverage scores yields an ε-accurate least-squares solution with O(d log d/ε^2) samples—instantiated here with the Kernel SHAP design matrix (d ≈ n) to derive O(n log n) model evaluations.

### 💡 Inspiration

**Fast Approximation of Matrix Coherence and Statistical Leverage Scores** (2012)
- *Authors:* Petros Drineas et al.
- *Connection:* Develops the concept and efficient approximation of statistical leverage scores, directly enabling the sampling distribution over coalitions used by Leverage SHAP.

### 🔧 Extension

**A Unified Approach to Interpreting Model Predictions** (2017)
- *Authors:* Scott M. Lundberg et al.
- *Connection:* Kernel SHAP casts Shapley estimation as a weighted least squares problem with the Shapley kernel, and Leverage SHAP is a light-weight modification that changes the sampling strategy to leverage-score sampling to obtain non-asymptotic O(n log n) guarantees.

### 🔗 Related Problem

**Leveraged volume sampling for linear regression** (2018)
- *Authors:* Michał Dereziński et al.
- *Connection:* Shows that actively selecting regression rows via leverage/volume sampling yields unbiased, high-accuracy estimators with near-minimal sample budgets, motivating the paper’s agnostic active regression lens for Shapley estimation.

**Low-rank approximation and regression in input sparsity time** (2013)
- *Authors:* Kenneth L. Clarkson et al.
- *Connection:* Establishes non-asymptotic guarantees for approximate least-squares via randomized sketching, reinforcing the principle that O(d log d)-scale samples suffice to recover regression solutions—an idea transferred to the Kernel SHAP design to yield provable sample complexity.

---

## Synthesis

Leverage SHAP’s core innovation—provable O(n log n) sample complexity for estimating Shapley values—arises by recasting Kernel SHAP’s weighted least squares formulation through the lens of agnostic active regression and then importing leverage-score sampling guarantees from randomized linear algebra. The target of estimation is the Shapley value, defined by Shapley (1953), and the coalition-based, model-agnostic evaluation framework stems from Strumbelj and Kononenko (2014). Lundberg and Lee (2017) then made the decisive step of formulating Shapley estimation as a weighted linear regression (Kernel SHAP), which works well empirically but lacks non-asymptotic accuracy/sample-complexity guarantees. The present work directly modifies that method by changing only the sampling strategy: instead of Kernel SHAP’s heuristic kernel-weighted sampling, it uses leverage-score sampling. This modification is theoretically powered by results from Drineas et al. (2011), who showed that sampling rows proportional to leverage scores yields ε-accurate least-squares solutions with O(d log d/ε^2) samples, and by Drineas et al. (2012), who developed practical methods to approximate leverage scores. Complementary lines on randomized regression (Clarkson & Woodruff, 2013) bolster the principle that near-linear-in-d sample sizes suffice for accurate regression recovery. Finally, leveraged volume sampling for linear regression (Dereziński & Warmuth, 2018) provides a closely related active regression perspective, reinforcing the idea that judicious, leverage-informed query selection can deliver unbiased, high-accuracy estimators with minimal budgets—precisely the paradigm Leverage SHAP instantiates for Shapley value estimation.

---
*Generated: 2026-01-06T23:09:26.612219*

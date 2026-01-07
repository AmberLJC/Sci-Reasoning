# Prior Work Analysis Report

## Target Paper
**Title:** m3zrHhiCCj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Natural Gradient Works Efficiently in Learning** (1998)
- *Authors:* Amari et al.
- *Connection:* Established the Fisher Information Matrix as a principled, parameterization-invariant measure of parameter sensitivity, providing the conceptual target whose diagonal Squisher seeks to approximate.

### 💡 Inspiration

**Dissecting Adam: The Sign, Magnitude and Variance of Stochastic Gradients** (2018)
- *Authors:* Balles et al.
- *Connection:* Analyzed what Adam’s second-moment estimate actually tracks (the second raw moment/variance of stochastic gradients), directly motivating the idea that this accumulator can stand in for the empirical Fisher’s diagonal.

### 🔍 Gap Identification

**Limitations of the empirical Fisher approximation for neural network optimization** (2019)
- *Authors:* Kunstner et al.
- *Connection:* Showed that the empirical Fisher (average of squared per-example gradients) can diverge from the true Fisher/Hessian, motivating Squisher’s careful empirical validation that the optimizer accumulator is an adequate Fisher proxy across applications.

### 📊 Baseline

**Overcoming catastrophic forgetting in neural networks** (2017)
- *Authors:* Kirkpatrick et al.
- *Connection:* EWC relies on a post-hoc diagonal Fisher estimate to define parameter importance; Squisher replaces this costly computation by substituting the already-computed squared-gradient accumulator.

**Merging Models with Fisher-Weighted Averaging** (2022)
- *Authors:* Matena et al.
- *Connection:* Uses diagonal Fisher to weight model parameters when merging; Squisher keeps the method but removes the expensive Fisher pass by reusing the optimizer’s second-moment statistics.

### 🔧 Extension

**Adam: A Method for Stochastic Optimization** (2015)
- *Authors:* Kingma et al.
- *Connection:* Introduced the moving average of squared gradients (the second-moment accumulator v_t) that Squisher directly repurposes as a 'for free' surrogate for the diagonal Fisher.

### 🔗 Related Problem

**Optimizing Neural Networks with Kronecker-factored Approximate Curvature** (2015)
- *Authors:* Martens et al.
- *Connection:* Demonstrated that practical Fisher approximations can be built from training-time statistics (K-FAC), inspiring Squisher’s premise of reusing readily available quantities—in this case Adam’s squared-gradient accumulator—to approximate Fisher cheaply.

---

## Synthesis

The paper’s core idea—recycling the optimizer’s squared-gradient accumulator to approximate the diagonal Fisher—rests on the Fisher’s role as a principled sensitivity metric (Amari, 1998), which many downstream methods operationalize via a diagonal approximation. Two prominent exemplars, EWC (Kirkpatrick et al., 2017) and Fisher-weighted model merging (Matena & Raffel, 2022), depend on computing a diagonal Fisher post hoc, creating a tangible computational bottleneck the present work targets. The enabling mechanism comes from adaptive optimizers: Adam (Kingma & Ba, 2015) maintains a second-moment accumulator of gradients, and an in-depth analysis (Balles et al., 2018) clarifies that this statistic tracks the second raw moment/variance of stochastic gradients—the very quantity underlying the empirical Fisher’s diagonal. At the same time, methodological caution from Kunstner et al. (2019) about discrepancies between empirical Fisher and true Fisher/Hessian motivates the paper’s broad empirical validation across diverse Fisher uses. Finally, K-FAC (Martens & Grosse, 2015) provides a precedent that practical Fisher approximations can be obtained by reusing training-time statistics, conceptually aligning with Squisher’s strategy but at a diagonal, near-zero-cost extreme. Together, these works define the Fisher-based problem formulation, expose the computational gap in standard practice, and supply both the statistical interpretation and the concrete machinery (Adam’s v_t) that make the paper’s “Fishers for free” approximation possible.

---
*Generated: 2026-01-06T23:07:19.568122*

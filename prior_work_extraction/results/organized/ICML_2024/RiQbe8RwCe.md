# Prior Work Analysis Report

## Target Paper
**Title:** RiQbe8RwCe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Stochastic Gradient Descent as Approximate Bayesian Inference** (2017)
- *Authors:* Stephan Mandt et al.
- *Connection:* By modeling SGD as a stochastic process whose noise (set by learning rate and batch size) induces implicit regularization, this paper provides the core theoretical lens that the current work tests and ultimately finds insignificant in the online regime.

**A Bayesian Perspective on Generalization and Stochastic Gradient Descent** (2018)
- *Authors:* Samuel L. Smith et al.
- *Connection:* This paper’s SDE/‘temperature’ view links batch size and learning rate to an implicit bias mechanism; the current work builds on this formulation to design online-learning experiments that isolate noise effects and show they do not yield generalization gains.

**The Implicit Bias of Gradient Descent on Separable Data** (2018)
- *Authors:* Daniel Soudry et al.
- *Connection:* Establishing deterministic GD’s implicit bias (e.g., max-margin), this paper provides the theoretical anchor for the current work’s ‘golden path’ hypothesis that online SGD takes noisy steps near the noiseless GD trajectory.

### 💡 Inspiration

**An Empirical Model of Large-Batch Training** (2018)
- *Authors:* Sam McCandlish et al.
- *Connection:* By quantifying the gradient noise scale and compute–batch-size trade-offs, this work motivates the paper’s central claim that in online training small batches confer strictly computational (not implicit-bias) benefits.

### 🔍 Gap Identification

**On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima** (2017)
- *Authors:* Nitish S. Keskar et al.
- *Connection:* This work argued that small-batch SGD’s noise steers training away from sharp minima to improve generalization; the present paper directly revisits this claim in the single-epoch (online) regime and shows that the purported implicit-bias benefit of small batches disappears there.

### 🔧 Extension

**Three Factors Influencing Minima in SGD** (2017)
- *Authors:* Stanislaw Jastrzebski et al.
- *Connection:* Their noise-scale characterization (learning rate–to–batch-size ratio) is directly used and extended to the online single-pass setting, where the authors demonstrate that varying noise scale does not alter implicit bias, contrary to the offline story.

### 🔗 Related Problem

**Train longer, generalize better: closing the generalization gap in large-batch training of neural networks** (2017)
- *Authors:* Elad Hoffer et al.
- *Connection:* Showing that generalization gaps can vanish when matching the number of updates, this work informs the present paper’s design and interpretation that, in single-epoch training, batch-size effects are about compute (update counts), not bias.

---

## Synthesis

The paper challenges the prevailing view that the stochasticity of small-batch SGD provides a beneficial implicit bias, arguing that in online (single-epoch) learning, this noise is insignificant for generalization and is only computationally useful. This conclusion is framed against foundational stochastic-process accounts of SGD’s implicit regularization (Mandt et al.; Smith et al.) and empirical claims that small batches find flatter, better-generalizing minima (Keskar et al.). The authors directly operationalize the noise-scale framework from Jastrzebski et al. and Smith et al., varying batch size and learning rate to hold the effective noise constant while controlling compute, and find that in single-pass training the expected implicit-bias advantages do not materialize. Instead, insights from compute-centric studies of batch scaling (McCandlish et al.) and from the observation that large-batch ‘gaps’ shrink when matching update counts (Hoffer et al.) point to a purely computational role for small batches in online regimes—cheaper steps and more updates per unit compute. To explain the dynamics, the paper adopts GD’s established implicit-bias perspective (Soudry et al.) as a reference trajectory, presenting evidence that online SGD behaves like noisy steps taken along this ‘golden path’ of noiseless gradient descent in both loss and function space. Together, these works directly motivate the problem, provide the theoretical and empirical baselines the authors test, and supply the compute-aware lens that underpins the paper’s central finding: in online learning, SGD noise does not confer implicit-bias benefits.

---
*Generated: 2026-01-06T23:09:26.450888*

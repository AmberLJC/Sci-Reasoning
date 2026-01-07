# Prior Work Analysis Report

## Target Paper

**Title:** What does automatic differentiation compute for neural networks?

**Conference:** ICLR 2024 (spotlight)

**Authors:** Sejun Park, Sanghyuk Chun, Wonyeol Lee

**Keywords:** automatic differentiation, correctness, neural networks, clarke subdifferential

**Abstract:** 
> Forward- or reverse-mode automatic differentiation (AD) is a popular algorithm for computing the derivative of a function expressed by a program. AD always outputs the correct derivative if a program does not use any non-differentiable functions and control flows; however, it may return an arbitrary value otherwise. In this work, we investigate what AD computes for neural networks that may contain non-differentiable functions such as ReLU and maxpools. We first prove that AD always returns a gen...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Optimization and Nonsmooth Analysis** (1983)
- *Authors:* F. H. Clarke
- *Direct Connection:* This monograph defines the Clarke subdifferential and establishes chain rules for Lipschitz compositions, providing the generalized derivative notion the paper proves AD selects in ReLU/maxpool networks.

**Variational Analysis** (1998)
- *Authors:* R. T. Rockafellar and R. J.-B. Wets
- *Direct Connection:* Its calculus for Clarke subdifferentials—especially for sums and pointwise maxima—underpins the analysis of minibatch aggregation and maxpool, including the strict-inclusion phenomena (∂C(f+g) ⊊ ∂Cf + ∂Cg) that motivate counterexamples and sufficient conditions.

**On the number of linear regions of deep neural networks** (2014)
- *Authors:* Guido F. Montúfar et al.
- *Direct Connection:* By formalizing ReLU networks as piecewise-linear, locally Lipschitz maps with region-dependent affine representations, this work provides the structural premise used to link backprop’s output to Clarke subgradients.

**Clarke subgradients of stratifiable functions** (2007)
- *Authors:* Jerome Bolte, Aris Daniilidis, Adrian Lewis, and Masahiro Shiota
- *Direct Connection:* Their subdifferential calculus for stratifiable (e.g., semi-algebraic) functions supplies the chain-rule machinery that justifies propagating Clarke selections through layered ReLU/max compositions.

### 💡 Inspiration

**Complexity of linear regions of deep neural networks** (2019)
- *Authors:* Boris Hanin and David Rolnick
- *Direct Connection:* Their generic-position arguments (e.g., distinct biases preventing ties) directly motivate the paper’s distinct-bias assumption ensuring unique active sets so AD matches a valid Clarke selection.

### 🔍 Gap Identification

**Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation (2nd ed.)** (2008)
- *Authors:* Andreas Griewank and Andrea Walther
- *Direct Connection:* This book explicitly notes that AD on programs with branches or non-differentiable primitives can return arbitrary values, directly motivating a precise characterization of what AD actually computes in nonsmooth neural networks.

### 🔗 Related Problem

**A Spline Theory of Deep Learning** (2021)
- *Authors:* Anthony Balestriero and Richard G. Baraniuk
- *Direct Connection:* Casting ReLU/maxpool networks as max-affine spline operators provides explicit active-affine and argmax descriptions that inform the paper’s treatment of maxpool layers and tie cases in the AD–Clarke correspondence.

---

## Synthesis: How Prior Work Led to This Paper

Clarke introduced the generalized gradient for locally Lipschitz functions along with a chain rule for compositions, establishing the Clarke subdifferential calculus that enables principled reasoning about nonsmooth derivatives. Rockafellar and Wets systematized this calculus, detailing how Clarke subdifferentials behave under sums and pointwise maxima, including when inclusions are strict—facts crucial for analyzing minibatch aggregation and max-type primitives. Griewank and Walther’s treatment of algorithmic differentiation emphasized that programs with branches and nonsmooth primitives can cause AD to return arbitrary values, highlighting a gap in understanding AD’s semantics beyond smooth settings. Montúfar and colleagues showed that ReLU networks are piecewise-linear and locally Lipschitz, i.e., stratified by affine regions, which is precisely the structural context where Clarke calculus applies. Bolte, Daniilidis, Lewis, and Shiota developed subdifferential rules for stratifiable functions, providing the formal machinery to propagate Clarke selections through layered compositions typical of neural networks. Hanin and Rolnick’s generic-position results underscore that distinct biases preclude ties and yield stable active sets. Finally, Balestriero and Baraniuk’s spline viewpoint renders ReLU/maxpool networks as max-affine splines, making explicit the role of argmax sets and tie handling. Taken together, these works expose a natural opportunity: characterize the precise Clarke selection that AD computes on stratified, piecewise-linear networks, and identify when sum- and max-operations (minibatching, maxpool) can break this identification. Synthesizing Clarke calculus with structural properties of ReLU networks and AD’s branch-wise behavior leads to sharp conditions—such as single-sample batches and distinct biases—under which backprop equals a Clarke subderivative, along with counterexamples and sufficient conditions beyond this regime.

---

*Analysis generated on: 2026-01-06T19:32:56.095025*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

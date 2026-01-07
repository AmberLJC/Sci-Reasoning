# Prior Work Analysis Report

## Target Paper

**Title:** Nesterov acceleration in benignly non-convex landscapes

**Conference:** ICLR 2025 (spotlight)

**Authors:** Kanan Gupta, Stephan Wojtowytsch

**Keywords:** Nonconvex optimization, stochastic optimization, stochastic acceleration, smooth convex optimization, deep learning, accelerated gradient descent

**Abstract:** 
> While momentum-based optimization algorithms are commonly used in the notoriously non-convex optimization problems of deep learning, their analysis has historically been restricted to the convex and strongly convex setting. In this article, we partially close this gap between theory and practice and demonstrate that virtually identical guarantees can be obtained in optimization problems with a 'benign' non-convexity. We show that these weaker geometric assumptions are well justified in overparam...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Introductory Lectures on Convex Optimization: A Basic Course** (2004)
- *Authors:* Yurii Nesterov
- *Direct Connection:* This monograph formalized Nesterov’s accelerated gradient (NAG) and its optimal rates under convex/strongly convex assumptions—the exact algorithm and guarantees that the current work extends to benignly non-convex settings.

**Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak–Łojasiewicz Condition** (2016)
- *Authors:* Hamed Karimi et al.
- *Direct Connection:* This paper established the PL (gradient dominance) condition as a benign non-convex geometry yielding strong convergence guarantees, which the current work leverages to obtain accelerated-style rates for NAG.

**Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (2018)
- *Authors:* Arthur Jacot et al.
- *Direct Connection:* The NTK regime’s local linearization implies PL/strongly-convex-like behavior in overparameterized networks, directly supporting the paper’s claim that benign non-convex assumptions hold in deep learning.

**Gradient Descent Finds Global Minima of Deep Neural Networks** (2019)
- *Authors:* Simon S. Du et al.
- *Direct Connection:* By proving global convergence of gradient methods in overparameterized nets via favorable curvature/error-bound properties, this work justifies the practical relevance of the benign landscape assumptions used to analyze NAG.

### 💡 Inspiration

**A Variational Perspective on Accelerated Methods** (2016)
- *Authors:* Wilson et al.
- *Direct Connection:* The Bregman-Lagrangian/Lyapunov framework provided here informs the energy-based analyses that the current work tailors to non-convex but PL/benign landscapes for both continuous and discrete NAG.

### 🔍 Gap Identification

**Accelerated Gradient Methods for Nonconvex Nonlinear and Stochastic Programming** (2016)
- *Authors:* Saeed Ghadimi et al.
- *Direct Connection:* By highlighting that classical acceleration results largely require convexity and offering limited nonconvex guarantees, this work frames the gap the current paper closes by proving NAG guarantees under structured nonconvexity.

### 🔧 Extension

**A Differential Equation for Modeling Nesterov’s Accelerated Gradient: Theory and Insights** (2016)
- *Authors:* Weijie Su et al.
- *Direct Connection:* Their continuous-time ODE model for NAG is the template the current paper adapts to analyze accelerated dynamics under benign non-convex geometry and in the presence of stochastic noise.

---

## Synthesis: How Prior Work Led to This Paper

Nesterov introduced the accelerated gradient method and its optimal rates for convex and strongly convex objectives, establishing the algorithmic template and guarantees that define acceleration. Su, Boyd, and Candès recast Nesterov’s method as a second-order differential equation, enabling Lyapunov- and energy-based analyses of acceleration in continuous time. Wibisono, Wilson, and Jordan broadened this picture through a Bregman-Lagrangian framework, systematizing Lyapunov constructions that can be tailored to different geometries. Karimi, Nutini, and Schmidt identified the Polyak–Łojasiewicz (PL) condition as a benign non-convex structure under which gradient methods enjoy linear convergence without convexity—pinpointing a precise weakening of convexity that still yields strong rates. Ghadimi and Lan cataloged what acceleration can and cannot guarantee beyond convexity, underscoring that classical proofs largely rely on convex geometry and leaving a gap for nonconvex acceleration theory. In parallel, Jacot, Gabriel, and Hongler’s NTK analysis and Du et al.’s overparameterization results showed that deep networks operate in regimes with locally linearized or curvature-controlled dynamics, implying PL-like behavior and error bounds. Together, these works suggested a path: import the ODE/Lyapunov machinery of accelerated methods into a PL/benignly non-convex setting that is empirically relevant for deep learning, and extend the analysis to discrete iterations and stochastic gradients. The current paper follows this trajectory, proving NAG-style guarantees under benign non-convexity and validating the assumptions via overparameterized neural network theory, thereby closing the convexity-to-practice gap.

---

*Analysis generated on: 2026-01-06T09:29:39.007916*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

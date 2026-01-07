# Prior Work Analysis Report

## Target Paper

**Title:** Feedback Schrödinger Bridge Matching

**Conference:** ICLR 2025 (oral)

**Authors:** Panagiotis Theodoropoulos, Nikolaos Komianos, Vincent Pacelli, Guan-Horng Liu, Evangelos Theodorou

**Keywords:** Diffusion models, Schrödinger bridge, Distribution matching, Semi-Supervised Learning

**Abstract:** 
> Recent advancements in diffusion bridges for distribution transport problems have heavily relied on matching frameworks, yet existing methods often face a trade-off between scalability and access to optimal pairings during training. 
Fully unsupervised methods make minimal assumptions but incur high computational costs, limiting their practicality. On the other hand, imposing full supervision of the matching process with optimal pairings improves scalability, however, it can be infeasible in mos...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Sinkhorn Distances: Lightspeed Computation of Optimal Transport** (2013)
- *Authors:* Marco Cuturi
- *Direct Connection:* FSBM formulates a static entropic OT objective with an additional feedback term, directly relying on the Sinkhorn-regularized EOT framework introduced by Cuturi for tractable training.

**On the relation between optimal transport and Schrödinger bridges: a stochastic control viewpoint** (2016)
- *Authors:* Yongxin Chen, Tryphon T. Georgiou, Michele Pavon
- *Direct Connection:* By casting Schrödinger bridges as stochastic optimal control with state-feedback drifts, this work supplies the control-theoretic foundation that FSBM leverages to interpret pre-aligned pairs as state feedback guiding the learned transport.

### 🔍 Gap Identification

**Conditional Flow Matching: Training Continuous Normalizing Flows without Score Estimation** (2023)
- *Authors:* Tongzhou Wang et al.
- *Direct Connection:* Conditional Flow Matching showed how to remove pair supervision by matching conditional velocities but at a significant computational cost, and FSBM explicitly addresses this limitation by reintroducing minimal pair supervision as feedback to retain scalability.

### 📊 Baseline

**Flow Matching for Generative Modeling** (2023)
- *Authors:* Yaron Lipman et al.
- *Direct Connection:* Flow Matching introduced the modern matching paradigm for training transport maps via path interpolants using paired data, which FSBM directly generalizes by injecting a small set of pre-aligned pairs as feedback while keeping the overall bridge-based matching framework.

**Schrödinger Bridge Sampling** (2021)
- *Authors:* Guillaume De Bortoli et al.
- *Direct Connection:* Schrödinger Bridge Sampling established the practical SB/EOT route for bridging empirical marginals without pairings, providing the fully unsupervised baseline whose high cost motivates FSBM’s semi-supervised, feedback-guided alternative.

### 🔧 Extension

**Optimal Transport for Domain Adaptation** (2014)
- *Authors:* Nicolas Courty et al.
- *Direct Connection:* This paper demonstrated how side information (e.g., labels) can regularize the OT coupling, an idea FSBM extends by using a small set of known pairings to regularize the EOT objective and steer uncoupled samples during bridge matching.

---

## Synthesis: How Prior Work Led to This Paper

Flow Matching introduced the idea of training transport maps by matching vector fields along chosen interpolants, showing that paired correspondences can yield scalable training for generative flows. Conditional Flow Matching removed the need for explicit pairings by matching conditional velocities, but the cost and complexity of sampling and estimating these conditionals made the approach computationally heavy in large-scale settings. Schrödinger Bridge Sampling established a practical, fully unsupervised bridge-based route between distributions using the Schrödinger problem and entropic OT, but it inherits high computational burden due to repeated coupling or score estimation without supervision. The Sinkhorn-regularized entropic OT framework made static optimal transport tractable and differentiable, enabling learnable couplings via efficient matrix scaling. From a control-theoretic lens, Schrödinger bridges are stochastic optimal control problems with state-feedback drifts, suggesting that external information can be injected as feedback to steer transport. Finally, optimal transport for domain adaptation showed that side information (labels or partial correspondences) can be incorporated as regularization to bias couplings toward desired alignments.
Bringing these strands together created a natural opportunity: retain the scalability of paired matching while avoiding the impracticality of fully supervised pairings, and cut the cost of fully unsupervised SB. FSBM synthesizes this by casting bridge learning as a static EOT with a targeted feedback term derived from a small set of pre-aligned pairs and interpreting this as state feedback in the SB control view. This semi-supervised coupling guides non-coupled samples, preserving efficiency while requiring only minimal supervision.

---

*Analysis generated on: 2026-01-06T14:04:34.236147*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** $\texttt{NAISR}$: A 3D Neural Additive Model for Interpretable Shape Representation

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yining Jiao, Carlton Jude ZDANSKI, Julia S Kimbell, Andrew Prince, Cameron P Worden, Samuel Kirse, Christopher Rutter, Benjamin Shields, William Alexander Dunn, Jisan Mahmud, Marc Niethammer

**Keywords:** Shape Modeling, Medical Shape Analysis, Interpretable Representation, AI4Science

**Abstract:** 
> Deep implicit functions (DIFs) have emerged as a powerful paradigm for many computer vision tasks such as 3D shape reconstruction, generation, registration, completion, editing, and understanding. However, given a set of 3D shapes with associated covariates there is at present no shape representation method which allows to precisely represent the shapes while capturing the individual dependencies on each covariate. Such a method would be of high utility to researchers to discover knowledge hidde...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Computing Large Deformation Metric Mappings via Geodesic Flows of Diffeomorphisms** (2005)
- *Authors:* Beg et al.
- *Direct Connection:* NAISR’s atlas-based description of population shape variation follows the LDDMM paradigm of modeling shapes via deformations of a template, but learns these deformations as neural fields additively tied to covariates.

**Geodesic Regression on Riemannian Manifolds** (2013)
- *Authors:* Fletcher et al.
- *Direct Connection:* NAISR builds on the problem formulation of regressing shapes on covariates introduced by geodesic regression, but replaces single-trajectory/geodesic assumptions with additive, covariate-specific neural deformation components.

### 💡 Inspiration

**Neural Additive Models: Interpretable Machine Learning with Neural Nets** (2021)
- *Authors:* Agarwal et al.
- *Direct Connection:* NAISR directly transfers the NAM principle of feature-wise subnetworks whose outputs sum to a prediction into 3D shape space by learning per-covariate deformation fields that additively compose into an interpretable atlas deformation.

### 📊 Baseline

**Gaussian Process Morphable Models** (2018)
- *Authors:* Gerig et al.
- *Direct Connection:* As a standard interpretable statistical shape model, GPMMs provide the primary baseline NAISR improves upon by replacing linear, correspondence-dependent Gaussian priors with nonlinear, implicit, covariate-disentangled additive deformations.

### 🔧 Extension

**DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation** (2019)
- *Authors:* Park et al.
- *Direct Connection:* NAISR adopts DeepSDF’s continuous SDF-based implicit shape representation and extends it by conditioning deformations of a learned atlas via an additive composition of covariate-specific subnetworks for interpretability.

### 🔗 Related Problem

**Occupancy Networks: Learning 3D Reconstruction in Function Space** (2019)
- *Authors:* Mescheder et al.
- *Direct Connection:* Occupancy Networks established neural implicit fields for high-fidelity 3D shape modeling, which NAISR leverages conceptually while focusing on interpretable, covariate-additive atlas deformations rather than reconstruction alone.

---

## Synthesis: How Prior Work Led to This Paper

Continuous neural implicit fields made high-fidelity 3D shape representations practical: DeepSDF showed that signed distance functions can be learned as continuous fields conditioned on a code, enabling precise, watertight surfaces, while Occupancy Networks framed learning shapes directly in function space to capture detailed geometry. In population modeling, Gaussian Process Morphable Models provided interpretable, probabilistic shape spaces supporting analysis with covariates, but relied on linear, correspondence-based assumptions that limit expressiveness. Atlas-based computational anatomy, grounded in LDDMM, established that population variability can be described as deformations of a template via diffeomorphic flows, furnishing a principled geometric scaffold for population trends. Complementing this, geodesic regression formalized the regression of shapes on covariates within Riemannian geometry, typically modeling effects along geodesic trajectories and supporting hypothesis testing, yet not designed for disentangled, multi-feature interpretability in complex, nonlinear regimes. Neural Additive Models, in parallel, introduced an interpretable deep-learning recipe: feature-wise subnetworks whose outputs sum to a prediction, preserving additivity and attribution per feature. Together these works exposed a clear opportunity: marry the geometric interpretability of atlas-based and regression-based shape analysis with the fidelity of neural implicit fields, while importing NAM-style additivity to disentangle covariate effects. NAISR is the natural synthesis—learning an implicit atlas and per-covariate deformation fields that add linearly in shape space, thus preserving interpretability, enabling patient-specific counterfactuals and shape transfer, and overcoming the linearity and correspondence constraints of classical statistical shape models.

---

*Analysis generated on: 2026-01-06T17:03:36.491441*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

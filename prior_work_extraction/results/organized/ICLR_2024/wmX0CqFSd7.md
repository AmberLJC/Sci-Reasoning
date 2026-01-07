# Prior Work Analysis Report

## Target Paper

**Title:** Compositional Generative Inverse Design

**Conference:** ICLR 2024 (spotlight)

**Authors:** Tailin Wu, Takashi Maruyama, Long Wei, Tao Zhang, Yilun Du, Gianluca Iaccarino, Jure Leskovec

**Keywords:** inverse design, generative design, PDE, physical simulation, compositional

**Abstract:** 
> Inverse design, where we seek to design input variables in order to optimize an underlying objective function, is an important problem that arises across fields such as mechanical engineering to aerospace engineering. Inverse design is typically formulated as an optimization problem, with recent works leveraging optimization across learned dynamics models. However, as models are optimized they tend to fall into adversarial modes, preventing effective sampling. We illustrate that by instead optim...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Score-Based Generative Modeling through Stochastic Differential Equations** (2021)
- *Authors:* Yang Song et al.
- *Direct Connection:* Treating the diffusion score as the gradient of a learned energy (log-density) underpins the paper’s core move to optimize over diffusion-model energies rather than over learned dynamics.

### 💡 Inspiration

**Classifier-Free Diffusion Guidance** (2022)
- *Authors:* Jonathan Ho et al.
- *Direct Connection:* The guidance mechanism that combines conditional and unconditional scores—and scales them to trade off constraints—inspires the paper’s weighted combination of component energies during compositional design.

### 🔍 Gap Identification

**Learning to Simulate Complex Physics with Graph Networks** (2020)
- *Authors:* Alvaro Sanchez-Gonzalez et al.
- *Direct Connection:* Graph-network physics simulators exemplify learned dynamics models that, when optimized over for design (e.g., N-body), can be adversarially exploited—precisely the failure mode this paper seeks to avoid.

### 📊 Baseline

**Fourier Neural Operator for Parametric Partial Differential Equations** (2021)
- *Authors:* Zongyi Li et al.
- *Direct Connection:* FNO-based surrogates are a primary baseline for PDE-governed inverse design whose direct optimization is shown to induce adversarial designs, motivating the shift to diffusion energy optimization.

### 🔧 Extension

**Compositional Visual Generation with Composable Diffusion Models** (2022)
- *Authors:* Yilun Du et al.
- *Direct Connection:* The paper directly extends the product-of-experts/sum-of-scores idea from composable diffusion to combine multiple diffusion models for different subcomponents into a single compositional inverse-design objective.

**Diffusion Posterior Sampling for General Noisy Inverse Problems** (2023)
- *Authors:* Hyungjin Chung et al.
- *Direct Connection:* This work’s sum-of-scores formulation that combines a diffusion prior with constraint/likelihood gradients is generalized here to compose multiple learned diffusion priors for multi-component inverse design.

### 🔗 Related Problem

**Diffuser: Diffusion Models for Sequential Decision Making** (2022)
- *Authors:* Michael Janner et al.
- *Direct Connection:* Using diffusion models as energy-shaped priors for planning informs the paper’s insight that optimizing over diffusion energies can avoid adversarial exploitation seen when directly optimizing learned dynamics.

---

## Synthesis: How Prior Work Led to This Paper

Score-based diffusion establishes that the score function is the gradient of a learned log-density, giving a principled energy interpretation and enabling gradient-based shaping of sampling trajectories. Building on this, composable diffusion demonstrates that multiple conditional generative factors can be composed by summing their scores (a product-of-experts view), yielding images that simultaneously satisfy several constraints. Classifier-free guidance refines this by showing how unconditional and conditional scores can be combined and scaled to trade off fidelity versus constraint satisfaction. In sequential decision-making, Diffuser leverages diffusion as an energy-shaped trajectory prior, guiding sampling with reward signals rather than directly optimizing a brittle learned dynamics model. For inverse problems, Diffusion Posterior Sampling formalizes combining a learned diffusion prior with measurement-consistency terms via score addition, unifying priors and constraints within one sampling procedure. In parallel, Fourier Neural Operators and graph-network simulators provide fast learned surrogates for PDEs and physical dynamics but exhibit vulnerability when used as optimization objectives, where gradient-based search often exploits model imperfections to produce adversarial designs. Together, these works suggest replacing direct optimization over learned forward models with optimization in the space of diffusion energies, and composing multiple design requirements by summing scores. The present paper synthesizes these insights by training diffusion models for design subcomponents and optimizing their combined energy landscape, achieving compositional inverse design that resists adversarial failure modes typical of surrogate-based optimization while naturally accommodating multi-constraint PDE-governed systems.

---

*Analysis generated on: 2026-01-06T19:29:12.460303*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

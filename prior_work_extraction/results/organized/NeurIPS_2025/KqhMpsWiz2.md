# Prior Work Analysis Report

## Target Paper
**Title:** KqhMpsWiz2
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Amortized Variational Transdimensional Inference fuses ideas from transdimensional Bayesian computation, amortized variational learning, and flow architectures to produce a single variational density that spans a union of model-specific parameter spaces. Green’s Reversible Jump MCMC established the canonical setup and challenges of dimension-changing inference, while Carlin–Chib’s product-space formulation suggested a unifying super-parameterization with padded inactive components—an idea CoSMIC operationalizes by identity-mapping nonactive parameters within one shared flow. On the optimization side, VAEs introduced amortized variational inference and the reparameterization trick, setting the stage for learning a single inference network across many conditionals; Rezende–Mohamed extended this to normalizing flows, enabling expressive variational families trained with stochastic gradients. CoSMIC specifically leverages masked, conditional flow designs: MAF contributes an autoregressive, mask-driven parameterization that readily accepts contextual inputs, and RealNVP contributes the architectural notion of identity-mapped subsets via coupling, which CoSMIC generalizes by conditioning the mask on the model index to realize transdimensionality. Finally, optimizing over discrete model indices requires Monte Carlo gradient estimators; Gumbel-Softmax provides a practical, low-variance relaxation that informs CoSMIC’s training strategy alongside standard pathwise and score-function estimators. Together, these works directly enable CoSMIC’s contextually-specified masking and its stochastic variational transdimensional training procedure, bridging classical multi-model Bayesian inference with modern amortized flow-based VI.

---
*Generated: 2026-01-07T00:21:32.310592*

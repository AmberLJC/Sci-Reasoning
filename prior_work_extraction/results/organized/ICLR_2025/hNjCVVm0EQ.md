# Prior Work Analysis Report

## Target Paper

**Title:** MamKO: Mamba-based Koopman operator for modeling and predictive control

**Conference:** ICLR 2025 (spotlight)

**Authors:** ZHAOYANG LI, Minghao Han, Xunyuan Yin

**Keywords:** Mamba; Koopman operator; model predictive control; nonlinear systems

**Abstract:** 
> The Koopman theory, which enables the transformation of nonlinear systems into linear representations, is a powerful and efficient tool to model and control nonlinear systems. However, the ability of the Koopman operator to model complex systems, particularly time-varying systems, is limited by the fixed linear state-space representation. To address the limitation, the large language model, Mamba, is considered a promising strategy for enhancing modeling capabilities while preserving the linear ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**A Data–Driven Approximation of the Koopman Operator: Extended Dynamic Mode Decomposition** (2015)
- *Authors:* Matthew O. Williams et al.
- *Direct Connection:* MamKO builds on EDMD’s core idea of learning a finite-dimensional linear predictor in a lifted space, but replaces the fixed Koopman matrix with a data-conditioned, time-varying operator generated online.

**Dynamic Mode Decomposition with Control** (2016)
- *Authors:* Joshua L. Proctor et al.
- *Direct Connection:* MamKO inherits the formalism of incorporating control inputs into Koopman/linear predictors from DMDc, while advancing it by letting the Koopman operator adapt to online data rather than remain constant.

### 💡 Inspiration

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2023)
- *Authors:* Albert Gu et al.
- *Direct Connection:* MamKO borrows Mamba’s selective state-space mechanism to condition the linear dynamics on the current input/context, using it to generate Koopman operators online without abandoning the linear state-space form.

### 🔍 Gap Identification

**Deep learning for universal linear embeddings of nonlinear dynamics** (2018)
- *Authors:* Brandon J. Lusch et al.
- *Direct Connection:* MamKO addresses the key limitation in deep Koopman autoencoders—using a fixed latent linear operator—by generating Koopman operators online to handle evolving dynamics.

**Learning Koopman Invariant Subspaces for Dynamic Mode Decomposition** (2017)
- *Authors:* Kenji Takeishi et al.
- *Direct Connection:* MamKO responds to the constraint in learning Koopman-invariant subspaces with a static linear evolution by enabling a data-driven, time-varying operator that preserves the linear structure while adapting over time.

### 📊 Baseline

**Linear predictors for nonlinear dynamical systems: Koopman meets model predictive control** (2018)
- *Authors:* Milan Korda et al.
- *Direct Connection:* MamKO directly extends the Koopman-MPC pipeline introduced by Korda and Mezić by substituting their constant Koopman operator with a Mamba-generated, time-varying operator to improve prediction and control on time-varying systems.

---

## Synthesis: How Prior Work Led to This Paper

Extended Dynamic Mode Decomposition (EDMD) established that nonlinear dynamics can be forecast via a learned linear operator acting on lifted observables, but this operator is fixed once trained. Dynamic Mode Decomposition with Control (DMDc) incorporated exogenous inputs into that linear predictor, preserving tractable linear structure for control. Deep Koopman models—via autoencoders—demonstrated that the lifting can itself be learned, again enforcing linear evolution in the latent space but still relying on a constant operator. Learning Koopman-invariant subspaces further codified the invariant linear-latent formulation, exhibiting strong modeling power yet sharing the same stationarity assumption on the linear operator. Meanwhile, the Koopman-MPC framework showed how these linear predictors could be embedded into model predictive control to regulate nonlinear systems efficiently, but real-world performance often degraded on time-varying dynamics due to the frozen operator. In parallel, Mamba introduced selective state space models that adapt their linear state-space evolution to the stream of inputs, providing a principled, efficient pathway to data-conditioned linear dynamics.
Taken together, these works illuminated both the power and the brittleness of Koopman methods with constant operators: linear structure enables MPC and efficient prediction, yet fixed operators struggle on time-varying systems. The selective SSM idea from Mamba offered exactly the missing mechanism to make the linear operator adaptive without discarding the linear state-space form. MamKO naturally synthesizes these threads by generating Koopman operators online via a Mamba-style selective state space, preserving Koopman-MPC tractability while improving modeling and control of evolving nonlinear dynamics.

---

*Analysis generated on: 2026-01-06T09:57:54.500559*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

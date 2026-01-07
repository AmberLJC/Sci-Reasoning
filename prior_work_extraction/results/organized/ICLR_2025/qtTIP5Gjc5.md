# Prior Work Analysis Report

## Target Paper

**Title:** Demystifying the Token Dynamics of Deep Selective State Space Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Thieu Vo, Duy-Tung Pham, Xin T. Tong, Tan Minh Nguyen

**Keywords:** Selective state-space model, continuous-time limit, dynamical system, asymptotic behavior, token reordering

**Abstract:** 
> Selective state space models (SSM), such as Mamba, have gained prominence for their effectiveness in modeling sequential data. Despite their outstanding empirical performance, a comprehensive theoretical understanding of deep selective SSM remains elusive, hindering their further development and adoption for applications that need high fidelity. In this paper, we investigate the dynamical properties of tokens in a pre-trained Mamba model. In particular, we derive the dynamical system governing t...

---

## Key Prior Works (5 papers with direct influence)

### 🏗️ Foundation

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2024)
- *Authors:* Albert Gu et al.
- *Direct Connection:* This paper introduces the selective state-space architecture and selective-scan recurrence that the current work explicitly takes to a continuous-time limit and analyzes for token-level asymptotic dynamics.

**Efficiently Modeling Long Sequences with Structured State Spaces** (2021)
- *Authors:* Albert Gu et al.
- *Direct Connection:* S4 formalizes continuous-time state-space dynamics and their discretizations for sequence modeling, providing the SSM mathematical framework and parameterization that the present analysis uses to derive Mamba’s depth-wise continuous-time dynamical system.

**HiPPO: Recurrent Memory with Optimal Polynomial Projections** (2020)
- *Authors:* Albert Gu et al.
- *Direct Connection:* HiPPO supplies the structured state matrices and memory formalism underlying modern SSM layers, whose spectral properties inform the parameter-based criteria this paper derives for token trajectories to converge or diverge.

### 💡 Inspiration

**Neural Ordinary Differential Equations** (2018)
- *Authors:* Ricky T. Q. Chen et al.
- *Direct Connection:* The neural-ODE viewpoint motivates taking the continuous-depth limit of layered sequence models, a methodological move this work applies to selective SSM stacks to obtain an ODE governing token dynamics.

### 🔗 Related Problem

**Liquid Time-constant Networks** (2021)
- *Authors:* Ramin Hasani et al.
- *Direct Connection:* LTC establishes analysis tools for input-dependent (gated) continuous-time recurrent dynamics, which this paper extends to selective SSM gating to characterize stability and asymptotic behavior (vanishing vs. exploding tokens).

---

## Synthesis: How Prior Work Led to This Paper

Selective state space models emerged from state-space sequence modeling, where S4 cast sequence processing as a discretization of continuous-time linear dynamics with structured parameterizations that enable long-range memory. The HiPPO framework clarified how specific structured state matrices encode recent history, making spectral properties of the state operator central to memory behavior. Building on these ideas, Mamba introduced selective scan: an input-dependent gating mechanism that modulates SSM parameters on the fly, yielding linear-time recurrence while substantially changing the effective dynamics across tokens. In parallel, the neural-ODE perspective established that deep networks can be meaningfully analyzed via their continuous-depth limits, providing a principled route to derive governing ODEs for stacked layers. Liquid Time-constant Networks showed how input-dependent, gated continuous-time systems can be analyzed for stability and asymptotics, highlighting that gating turns the dynamics into a controlled system whose long-term behavior depends on parameterized modulations. Together, these works set the stage for a precise dynamical study of selective SSMs. The combination of SSM formalism (S4/HiPPO), selective gating (Mamba), and continuous-depth analysis (Neural ODEs/LTC) reveals a gap: despite strong empirical performance, there is no principled characterization of token trajectories in deep selective SSMs. The current paper fills this by deriving the continuous-time limit of Mamba’s stacked selective SSM, then using spectral and gating-driven criteria to prove a sharp dichotomy in 1D—tokens either vanish or blow up—linking these regimes to performance and explaining observed token-mixing/reordering behavior.

---

*Analysis generated on: 2026-01-06T18:16:00.962651*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

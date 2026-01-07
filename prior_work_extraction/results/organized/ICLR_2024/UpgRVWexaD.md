# Prior Work Analysis Report

## Target Paper

**Title:** Accelerating Data Generation for Neural Operators via Krylov Subspace Recycling

**Conference:** ICLR 2024 (spotlight)

**Authors:** Hong Wang, Zhongkai Hao, Jie Wang, Zijie Geng, Zhen Wang, Bin Li, Feng Wu

**Keywords:** AI4PDE; Neural Operator; Data Generation; Krylov Subspace

**Abstract:** 
> Learning neural operators for solving partial differential equations (PDEs) has attracted great attention due to its high inference efficiency.
However, training such operators requires generating a substantial amount of labeled data, i.e., PDE problems together with their solutions.
The data generation process is exceptionally time-consuming, as it involves solving numerous systems of linear equations to obtain numerical solutions to the PDEs.
Many existing methods solve these systems independe...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Fourier Neural Operator for Parametric Partial Differential Equations** (2021)
- *Authors:* Zongyi Li et al.
- *Direct Connection:* By framing operator learning as supervised mapping between function spaces, FNO established the need to generate large numbers of PDE solutions via linear solves, creating precisely the data-generation bottleneck this work targets.

**Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators** (2021)
- *Authors:* Lu Lu et al.
- *Direct Connection:* DeepONet similarly relies on extensive labeled PDE solutions for training, solidifying the supervised operator-learning setup whose cost is dominated by repeatedly solving large linear systems.

### 💡 Inspiration

**GMRES with Deflated Restarting** (2002)
- *Authors:* Ronald B. Morgan
- *Direct Connection:* The deflated-restart idea of preserving approximate invariant subspaces across restarts directly inspires the recycled subspace mechanism that is adapted here to heterogeneous PDE-induced sequences.

### 📊 Baseline

**Recycling Krylov Subspaces for Sequences of Linear Systems** (2006)
- *Authors:* Michael L. Parks et al.
- *Direct Connection:* GCRO-DR introduced a practical framework to recycle Krylov subspaces across sequences of related systems, which this work uses as the inner workhorse and augments with an explicit similarity-driven sorting policy to maximize reuse.

### 🔗 Related Problem

**Block Krylov subspace methods for linear systems with multiple right-hand sides** (2003)
- *Authors:* Said El Guennouni et al.
- *Direct Connection:* Block GMRES shows how shared Krylov information can accelerate multiple RHS solves, providing a contrasting baseline that this work matches via sequential solves by ordering problems and recycling subspaces without block memory overhead.

**Krylov Subspace Recycling for Sequences of Shifted Linear Systems** (2014)
- *Authors:* Karl M. Soodhalter et al.
- *Direct Connection:* Results on shifted systems demonstrated that modest matrix variations still benefit from recycled subspaces, underpinning the assumption that parametric PDE sweeps can be sped up by reuse and motivating similarity-aware sequencing.

---

## Synthesis: How Prior Work Led to This Paper

Fourier Neural Operator formulated operator learning as supervised mapping between function spaces and showed that training requires many PDE solutions, each obtained by solving large linear systems; DeepONet reinforced this supervised paradigm, further highlighting that the data pipeline is dominated by repeated PDE solves. In numerical linear algebra, GMRES with Deflated Restarting introduced the mechanism of carrying approximate invariant subspaces across restarts to accelerate convergence, crystallizing the key technical idea of reusing spectral information. Building on this, Recycling Krylov Subspaces for Sequences of Linear Systems (GCRO-DR) extended reuse from within a single system to sequences of related systems, providing a practical algorithmic framework to maintain and apply a recycled subspace across solves. Block Krylov methods for multiple right-hand sides demonstrated that shared Krylov information can reduce work when several systems are solved together, albeit with higher memory and synchronization costs. Complementarily, recycling for shifted linear systems showed that even when matrices vary in a structured way, reusing subspaces remains effective, suggesting broader applicability to parametric PDE contexts. Together these works reveal a gap: operator learning demands long sequences of related but heterogeneous linear systems, yet existing recycling methods assume a given order and block methods require simultaneous solves. The natural next step is to couple recycled-Krylov solvers like GCRO-DR with an explicit, similarity-aware ordering of problems so that consecutive systems maximally benefit from the current recycled subspace, delivering end-to-end acceleration of data generation for neural operator training.

---

*Analysis generated on: 2026-01-06T08:48:30.380842*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Reinforcement Learning for Control of Non-Markovian Cellular Population Dynamics

**Conference:** ICLR 2025 (spotlight)

**Authors:** Josiah C Kratz, Jacob Adamczyk

**Keywords:** optimal drug dosing, fractional differential equations, reinforcement learning, control theory

**Abstract:** 
> Many organisms and cell types, from bacteria to cancer cells, exhibit a remarkable ability to adapt to fluctuating environments. Additionally, cells can leverage memory of past environments to better survive previously-encountered stressors. From a control perspective, this adaptability poses significant challenges in driving cell populations toward extinction, and is thus an open question with great clinical significance. In this work, we focus on drug dosing in cell populations exhibiting phen...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Phenotypic diversity, population growth, and information in fluctuating environments** (2005)
- *Authors:* O. Kussell et al.
- *Direct Connection:* Provided the canonical two-phenotype switching growth framework (with exact growth-rate solutions under environmental switching) that this work uses as the Markovian special case it generalizes to unknown parameters and memory.

**Stochastic state transitions give rise to phenotypic equilibrium in cancer cell populations** (2011)
- *Authors:* P. B. Gupta et al.
- *Direct Connection:* Established the resistant–sensitive (and intermediate) phenotypic plasticity model with stochastic switching that directly defines the control target and state structure addressed here.

**The random walk’s guide to anomalous diffusion: a fractional dynamics approach** (2000)
- *Authors:* R. Metzler et al.
- *Direct Connection:* Introduced the fractional-derivative formalism for encoding power-law memory kernels, which underlies the paper’s non-Markovian cellular population models via fractional differential equations.

### 💡 Inspiration

**Fractional Poisson process** (2003)
- *Authors:* N. Laskin
- *Direct Connection:* Showed how heavy-tailed residence times lead to fractional master equations, motivating the paper’s use of fractional switching dynamics to capture cellular memory in phenotype transitions.

**The Artificial Intelligence Clinician learns optimal treatment strategies for sepsis** (2018)
- *Authors:* W. Komorowski et al.
- *Direct Connection:* Demonstrated that model-free deep reinforcement learning can discover effective dosing policies under unknown physiological dynamics, directly motivating the application of RL to drug dosing in complex biological systems here.

### 📊 Baseline

**Integrating evolutionary dynamics into treatment of metastatic castrate-resistant prostate cancer** (2017)
- *Authors:* J. Zhang et al.
- *Direct Connection:* Proposed adaptive therapy as a feedback dosing heuristic in two-phenotype resistance models, providing the primary control baseline whose heuristic limitations this work seeks to surpass under non-Markovian and uncertain dynamics.

### 🔧 Extension

**Deep Recurrent Q-Learning for Partially Observable MDPs** (2015)
- *Authors:* M. Hausknecht et al.
- *Direct Connection:* Showed that recurrent networks endow RL agents with memory to handle non-Markovian dynamics, a capability this work extends to learn dosing policies for memory-based cellular dynamics.

---

## Synthesis: How Prior Work Led to This Paper

A body of work on phenotypic switching and evolutionary control established the mathematical and biological backdrop for dosing under resistance. Kussell and Leibler formulated the two-phenotype switching framework and derived exact growth-rate expressions under fluctuating environments, defining the tractable Markovian special case. In oncology, Gupta and colleagues showed that cancer cells undergo stochastic state transitions among sensitive and resistant phenotypes, grounding the specific state structure targeted by control policies. To represent genuine memory effects in kinetics, Metzler and Klafter introduced fractional-derivative operators to encode power-law memory kernels, while Laskin’s fractional Poisson process connected heavy-tailed residence times to fractional master equations—together providing a principled route to non-Markovian switching dynamics. On the control side, Komorowski et al. demonstrated that model-free deep reinforcement learning can uncover dosing policies without explicit models of patient dynamics, and Hausknecht and Stone showed that recurrent RL agents can cope with non-Markovian dynamics by retaining history. Clinically, Zhang et al. proposed adaptive therapy—simple feedback heuristics within two-phenotype models—as a practical baseline for managing resistance. Taken together, these works reveal a gap: analytic optimal control exists for Markovian, parameter-known switching, while clinical heuristics and standard RL assume Markovian dynamics. Fractional calculus offers a principled way to encode cellular memory, but control remains intractable. Bridging these threads, the current work naturally arises by leveraging recurrent, model-free deep RL to learn dosing strategies directly in non-Markovian, fractional-order phenotype-switching systems with unknown parameters, aiming to outperform heuristic adaptive therapy and extend beyond the exact-solvable Markovian regime.

---

*Analysis generated on: 2026-01-06T08:59:01.511156*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

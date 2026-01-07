# Prior Work Analysis Report

## Target Paper

**Title:** ASID: Active Exploration for System Identification in Robotic Manipulation

**Conference:** ICLR 2024 (oral)

**Authors:** Marius Memmel, Andrew Wagenmaker, Chuning Zhu, Dieter Fox, Abhishek Gupta

**Keywords:** sim2real, system identification, exploration

**Abstract:** 
> Model-free control strategies such as reinforcement learning have shown the ability to learn control strategies without requiring an accurate model or simulator of the world. While this is appealing due to the lack of modeling requirements, such methods can be sample inefficient, making them impractical in many real-world domains. On the other hand, model-based control techniques leveraging accurate simulators can circumvent these challenges and use a large amount of cheap simulation data to lea...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Sim-to-Real Transfer of Robotic Control with Dynamics Randomization** (2018)
- *Authors:* Xue Bin Peng et al.
- *Direct Connection:* ASID builds on the dynamics randomization and online system identification formulation introduced here by providing a principled way to actively gather trajectories that disambiguate the latent physical parameters those approaches aim to infer.

**BayesSim: Likelihood-Free Inference for Simulation-based System Identification** (2019)
- *Authors:* Fabio Ramos et al.
- *Direct Connection:* ASID adopts the core idea of inferring a posterior over simulator parameters from real trajectories, but augments it with actively selected, maximally informative interactions instead of relying on passively collected data.

### 💡 Inspiration

**Plan2Explore: Planning to Explore via Self-Supervised World Models** (2020)
- *Authors:* Ramanan Sekar et al.
- *Direct Connection:* ASID adapts Plan2Explore’s principle of planning for information gain—originally applied to latent world models—to the specific goal of reducing uncertainty over physics parameters in a simulator.

### 🔍 Gap Identification

**Data-Efficient Domain Randomization with Bayesian Optimization** (2021)
- *Authors:* Marco Muratore et al.
- *Direct Connection:* ASID explicitly addresses this work’s limitation of tuning parameter distributions from task returns by instead optimizing exploration actions to reduce parameter uncertainty before policy learning or planning.

### 📊 Baseline

**Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience** (2019)
- *Authors:* Yevgen Chebotar et al.
- *Direct Connection:* ASID directly improves on SimOpt by replacing its passive, task-driven rollouts and BO-based parameter tuning with an explicitly information-seeking exploration policy and posterior update targeted at identifying simulator parameters.

### 🔗 Related Problem

**Active Information Acquisition with Mobile Robots** (2014)
- *Authors:* Nikolay Atanasov et al.
- *Direct Connection:* ASID instantiates the mutual-information-based experimental design ideas from active perception to plan manipulation interactions that maximize identifiability of dynamics parameters.

---

## Synthesis: How Prior Work Led to This Paper

SimOpt showed that the gap between simulation and reality can be reduced by iteratively adapting domain randomization distributions using real-world feedback, but its data collection remained task-driven and passive, depending on Bayesian optimization over parameter distributions matched to task outcomes. Dynamics randomization work demonstrated that robust control and online system identification could be achieved by conditioning policies on latent dynamics and inferring them from rollouts, formalizing the goal of estimating hidden physical parameters for transfer. BayesSim introduced likelihood-free inference to recover posteriors over simulator parameters from real trajectories, establishing a general recipe for simulator parameter identification without requiring analytic likelihoods. Data-efficient domain randomization with Bayesian optimization further emphasized tuning parameter distributions from limited real trials, yet it also relied on passively obtained task executions rather than explicitly informative experiments. Plan2Explore advanced the idea of planning to reduce model uncertainty—using disagreement or information-theoretic objectives—showing the power of targeted exploration when the objective is epistemic uncertainty reduction. Active information acquisition framed mutual-information objectives for experiment design in robotics, offering formal criteria for selecting actions that maximally reduce parameter uncertainty.
Together, these works revealed a gap: while parameter inference and distribution adaptation were feasible, the data used to do so was not purposefully chosen to identify dynamics. The natural next step was to fuse posterior-based system identification with information-theoretic planning, yielding an exploration policy that selects manipulation interactions explicitly to disambiguate simulator parameters, thereby enabling more accurate sim refinement and stronger sim-to-real transfer from a small amount of real data.

---

*Analysis generated on: 2026-01-06T16:32:14.737086*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

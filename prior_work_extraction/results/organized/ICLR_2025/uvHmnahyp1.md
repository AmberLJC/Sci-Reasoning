# Prior Work Analysis Report

## Target Paper

**Title:** SynFlowNet: Design of Diverse and Novel Molecules with Synthesis Constraints

**Conference:** ICLR 2025 (spotlight)

**Authors:** Miruna Cretu, Charles Harris, Ilia Igashov, Arne Schneuing, Marwin Segler, Bruno Correia, Julien Roy, Emmanuel Bengio, Pietro Lio

**Keywords:** GFlowNets, de novo molecular generation, synthesizable molecular design

**Abstract:** 
> Generative models see increasing use in computer-aided drug design. However, while performing well at capturing distributions of molecular motifs, they often produce synthetically inaccessible molecules. To address this, we introduce SynFlowNet, a GFlowNet model whose action space uses chemical reactions and buyable reactants to sequentially build new molecules. By incorporating forward synthesis as an explicit constraint of the generative mechanism, we aim at bridging the gap between in silico ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**GFlowNet Foundations** (2021)
- *Authors:* Yoshua Bengio et al.
- *Direct Connection:* This work established the GFlowNet framework for sampling proportional to unnormalized rewards over sequential construction MDPs, which SynFlowNet adopts to generate diverse molecules while optimizing synthesizability-aware rewards.

**Planning Chemical Syntheses with Deep Neural Networks and Symbolic AI** (2018)
- *Authors:* Marwin Segler et al.
- *Direct Connection:* By formalizing route search over reaction templates and buyable starting materials, this work provided the reaction-template paradigm and practical motivation for constraining generation to forward-synthesis steps used in SynFlowNet’s action space.

### 💡 Inspiration

**Equivariant 3D-Conditional GFlowNets for Molecular Generation** (2022)
- *Authors:* Ilia Igashov et al.
- *Direct Connection:* This paper demonstrated that GFlowNets produce substantially more diverse molecular candidates under property-driven rewards, motivating SynFlowNet’s choice of GFlowNets to preserve diversity while imposing synthesis constraints.

### 🔍 Gap Identification

**Molecular De-novo Design through Deep Reinforcement Learning (REINVENT)** (2017)
- *Authors:* Marcus Olivecrona et al.
- *Direct Connection:* REINVENT optimized SMILES with heuristic synthesizability terms but did not enforce forward-synthesis feasibility, a limitation SynFlowNet addresses by making executable reactions the generative actions.

**Junction Tree Variational Autoencoder for Molecular Graph Generation** (2018)
- *Authors:* Wengong Jin et al.
- *Direct Connection:* JT-VAE improved validity via substructure assembly but lacked explicit synthesis constraints, highlighting the broader gap of generative models producing non-synthesizable molecules that SynFlowNet closes with reaction-constrained generation.

### 📊 Baseline

**Lib-INVENT: Reaction-Based Generative Scaffold Decoration Using Reinforcement Learning** (2020)
- *Authors:* Thomas Blaschke et al.
- *Direct Connection:* Lib-INVENT introduced building molecules via specified reaction filters and purchasable building blocks; SynFlowNet directly builds on this reaction-as-action idea but replaces RL with GFlowNets to achieve mode-covering diversity and stronger synthesis guarantees.

### 🔧 Extension

**Trajectory Balance: Improved Training for Generative Flow Networks** (2022)
- *Authors:* Nikolai Malkin et al.
- *Direct Connection:* SynFlowNet trains its reaction-based policy using the Trajectory Balance objective introduced here, directly extending TB to a reaction-application action space to stabilize learning over long synthesis trajectories.

---

## Synthesis: How Prior Work Led to This Paper

Generative Flow Networks were introduced to sample from unnormalized reward distributions over sequential construction processes, providing a principled way to generate diverse sets of high-reward objects rather than collapsing to a few modes. Trajectory Balance subsequently gave a stable, path-consistent training objective for GFlowNets, enabling learning over long horizons with many alternative construction paths. In molecular design, equivariant 3D-conditional GFlowNets showed that this framework yields markedly higher diversity while optimizing property-driven objectives, establishing GFlowNets as a strong fit for chemistry search spaces. In parallel, synthesis planning work formalized the use of reaction templates with buyable starting materials to define practically actionable chemical routes, anchoring the notion that generation constrained by executable reactions can bridge in silico proposals and lab feasibility. Reaction-based generative design, exemplified by Lib-INVENT, operationalized this by building molecules through reaction filters and catalog reagents, but trained with RL that often forfeits diversity. Earlier SMILES/RL and graph VAEs improved validity or property scores but relied on heuristic synthesizability terms or none at all, frequently yielding non-synthesizable outputs.
Together these strands point to a natural opportunity: marry the practical guarantees of reaction-constrained construction with the mode-covering sampling of GFlowNets. By treating forward reaction applications on purchasable reactants as actions and training with Trajectory Balance, the current work synthesizes these insights to produce diverse, property-optimized molecules that are executable by construction, while also confronting reaction-encoding issues that arise when navigating the resulting MDP.

---

*Analysis generated on: 2026-01-06T17:28:53.213333*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

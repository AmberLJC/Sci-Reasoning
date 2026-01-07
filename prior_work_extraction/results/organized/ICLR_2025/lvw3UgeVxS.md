# Prior Work Analysis Report

## Target Paper

**Title:** gRNAde: Geometric Deep Learning for 3D RNA inverse design

**Conference:** ICLR 2025 (spotlight)

**Authors:** Chaitanya K. Joshi, Arian Rokkum Jamasb, Ramon Viñas Torné, Charles Harris, Simon V Mathis, Alex Morehead, Rishabh Anand, Pietro Lio

**Keywords:** RNA Structure, RNA Design, Geometric Deep Learning, Graph Neural Networks

**Abstract:** 
> Computational RNA design tasks are often posed as inverse problems, where sequences are designed based on adopting a single desired secondary structure without considering 3D conformational diversity. We introduce gRNAde, a geometric RNA design pipeline operating on 3D RNA backbones to design sequences that explicitly account for structure and dynamics. gRNAde uses a multi-state Graph Neural Network and autoregressive decoding to generates candidate RNA sequences conditioned on one or more 3D ba...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Atomic accuracy in predicting and designing noncanonical RNA structure** (2010)
- *Authors:* Das et al.
- *Direct Connection:* This paper established the fixed-backbone RNA redesign benchmark of 14 PDB structures and framed 3D-aware RNA design within Rosetta, directly defining the problem setting and evaluation protocol gRNAde targets and extends.

**NUPACK: Analysis and design of nucleic acid systems** (2011)
- *Authors:* Zadeh et al.
- *Direct Connection:* NUPACK formalized RNA inverse design as satisfying target secondary structures (including multi-state targets) but operates in 2D, providing both the canonical formulation and the 3D/dynamics gap gRNAde addresses.

### 💡 Inspiration

**Generative Models for Graph-Based Protein Design** (2019)
- *Authors:* Ingraham et al.
- *Direct Connection:* This work introduced autoregressive graph neural generation conditioned on 3D backbones for sequence design, a key idea that gRNAde adapts from proteins to RNA with nucleotide-specific features.

### 🔍 Gap Identification

**LEARNA: Reinforcement learning for RNA design** (2018)
- *Authors:* Runge et al.
- *Direct Connection:* LEARNA demonstrated modern ML can solve RNA inverse folding but optimizes only secondary-structure constraints, highlighting the limitation to 2D objectives that motivated gRNAde’s 3D, multi-state conditioning.

### 📊 Baseline

**FARFAR2: Improved de novo RNA structure prediction** (2020)
- *Authors:* Watkins et al.
- *Direct Connection:* As the Rosetta-based state-of-the-art for 3D RNA modeling and redesign used on the Das 2010 set, FARFAR2 provides the primary energy-based baseline whose slower, hand-crafted scoring and lower recovery rates gRNAde explicitly surpasses.

### 🔧 Extension

**Robust deep learning–based protein sequence design using ProteinMPNN** (2022)
- *Authors:* Dauparas et al.
- *Direct Connection:* ProteinMPNN’s locality-focused message passing on kNN backbone graphs and order-agnostic decoding directly informed gRNAde’s backbone-conditioned GNN design, which it extends to RNA and to multi-state conditioning over conformational ensembles.

---

## Synthesis: How Prior Work Led to This Paper

NUPACK formalized RNA inverse design as selecting sequences that realize prescribed secondary structures, even across multiple targets, but its objective and energy model are strictly 2D and agnostic to 3D geometry and conformational variability. LEARNA showed that machine learning can automate inverse folding with strong performance, yet it too optimizes only secondary-structure satisfaction, reinforcing the community’s focus on 2D targets. In contrast, Das and colleagues assembled a fixed-backbone RNA redesign benchmark from PDB structures and embedded the task within a 3D Rosetta framework, establishing a geometric, atomistic setting for evaluating sequence recovery. FARFAR2 further advanced Rosetta’s 3D modeling and redesign pipeline on this benchmark, but its energy-based optimization is computationally heavy and limited by hand-tuned scoring. On the protein side, Ingraham et al. introduced autoregressive graph-based generation conditioned on 3D backbones, proving that local geometric message passing enables accurate, fast sequence design. ProteinMPNN crystallized this insight with a simple locality-biased kNN graph and order-agnostic decoding that achieved state-of-the-art protein recovery with remarkable speed. Together these works exposed a clear opportunity: RNA design needed to move beyond 2D objectives to 3D backbone-conditioning, while inheriting the speed and accuracy of protein-structure-conditioned generative GNNs. By transplanting and extending backbone-conditioned message passing and autoregressive decoding from protein design to RNA—and by aggregating information across multiple backbone conformations—gRNAde naturally fills the gap between 2D inverse folding tools and slow energy-based 3D pipelines, enabling fast, accurate, and explicitly multi-state RNA sequence design.

---

*Analysis generated on: 2026-01-06T11:50:06.963966*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

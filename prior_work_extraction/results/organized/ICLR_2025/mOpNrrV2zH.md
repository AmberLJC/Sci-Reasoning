# Prior Work Analysis Report

## Target Paper

**Title:** CBGBench: Fill in the Blank of Protein-Molecule Complex Binding Graph

**Conference:** ICLR 2025 (spotlight)

**Authors:** Haitao Lin, Guojiang Zhao, Odin Zhang, Yufei Huang, Lirong Wu, Cheng Tan, Zicheng Liu, Zhifeng Gao, Stan Z. Li

**Keywords:** Molecule Generation Benchmark, Target-Aware Drug Design, Generative Model

**Abstract:** 
> Structure-based drug design (SBDD) aims to generate potential drugs that can bind to a target protein and is greatly expedited by the aid of AI techniques in generative models. However, a lack of systematic understanding persists due to the diverse settings, complex implementation, difficult reproducibility, and task singularity. Firstly, the absence of standardization can lead to unfair comparisons and inconclusive insights. To address this dilemma, we propose CBGBench, a comprehensive benchmar...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The PDBbind Database: Collection of Binding Affinities for Protein–Ligand Complexes** (2004)
- *Authors:* Wang et al.
- *Direct Connection:* PDBbind provides the core protein–ligand complex structures and affinities that underpin SBDD training/evaluation, which CBGBench systematizes into consistent task definitions and splits.

**A Cross-Docked Dataset for Pose Selection and Binding Affinity** (2020)
- *Authors:* Francoeur et al.
- *Direct Connection:* CrossDocked2020 formalizes large-scale, pocket-centered complex data and rigorous splits for docking, which CBGBench leverages to standardize data protocols across its unified tasks.

### 💡 Inspiration

**GuacaMol: Benchmarking Models for de Novo Molecular Design** (2019)
- *Authors:* Brown et al.
- *Direct Connection:* GuacaMol showed the value of standardized, modular benchmarks and clear metrics for molecule generation, directly motivating CBGBench’s standardized, extensible benchmarking for structure-based, target-aware settings.

**Deep Generative Models for 3D Linker Design (DeLinker)** (2020)
- *Authors:* Imrie et al.
- *Direct Connection:* DeLinker’s formulation of molecular design as ‘fill-in-the-blank’ 3D graph completion between anchors inspires CBGBench’s central idea of casting SBDD as completion of a protein–ligand complex binding graph with the ligand as the blank.

### 📊 Baseline

**Pocket2Mol: Efficient molecular sampling based on pocket-conditioned graph generative models** (2021)
- *Authors:* Liu et al.
- *Direct Connection:* CBGBench adopts and reimplements Pocket2Mol as a key pocket-conditioned generator and reframes it under a unified complex-binding-graph completion interface to enable standardized comparisons.

### 🔗 Related Problem

**DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking** (2023)
- *Authors:* Corso et al.
- *Direct Connection:* DiffDock’s diffusion-based, SE(3)-aware pose generation motivates treating docking/pose prediction as a sub-task of complex binding graph completion and serves as a primary baseline within the unified framework.

**EquiBind: Geometric Deep Learning for Drug Binding Structure Prediction** (2022)
- *Authors:* Stärk et al.
- *Direct Connection:* EquiBind’s geometric matching over protein–ligand interaction graphs reinforces the interaction-graph view that CBGBench generalizes into a fill-in-the-blank complex completion paradigm and provides a contrasting baseline for pose tasks.

---

## Synthesis: How Prior Work Led to This Paper

Pocket-conditioned generative modeling emerged with methods like Pocket2Mol, which directly synthesize ligands using graph-based generation constrained by the 3D geometry and chemistry of a protein pocket, but with bespoke data handling and metrics. In parallel, pose-prediction methods such as DiffDock and EquiBind framed protein–ligand complexes geometrically, using SE(3)-aware diffusion or geometric matching on interaction graphs to place ligands in pockets; these works reinforced treating complexes as structured graphs that span protein and ligand components. Benchmarking in molecular generation was professionalized by GuacaMol, which demonstrated how standardized tasks, metrics, and modular implementations yield fair, reproducible comparisons—though its scope excluded protein-structure conditioning. Foundational datasets like PDBbind provided curated protein–ligand complexes with binding affinities, while CrossDocked2020 scaled pocket-centered complex data and rigorous splits for docking and pose tasks. Independently, DeLinker established a concrete “fill-in-the-blank” generative paradigm by completing missing molecular segments in 3D, proving that graph completion can be a natural generative interface. Together, these works expose a gap: SBDD methods operate on similar protein–ligand graphs yet remain fragmented across tasks, datasets, and implementations, hampering comparability. The natural next step is to unify them by casting target-aware drug design as complex binding graph completion, standardizing data protocols from PDBbind/CrossDocked, and integrating pocket-conditioned generation (Pocket2Mol) and pose baselines (DiffDock/EquiBind) within a modular, extensible benchmark that spans multiple sub-tasks.

---

*Analysis generated on: 2026-01-06T12:35:52.384688*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

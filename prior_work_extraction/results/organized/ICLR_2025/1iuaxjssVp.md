# Prior Work Analysis Report

## Target Paper
**Title:** 1iuaxjssVp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Direct-coupling analysis of residue coevolution captures native contacts across many protein families** (2011)
- *Authors:* Morcos et al.
- *Connection:* InvMSAFold explicitly adopts the Potts-model (pairwise Markov random field) formulation introduced by DCA to represent a sequence distribution with residue–residue couplings, and aims to predict those parameters directly from structure.

**Generative Models for Graph-Based Protein Design** (2019)
- *Authors:* Ingraham et al.
- *Connection:* This work formalized inverse folding as learning from backbone geometry to sequences with graph neural networks, a setup InvMSAFold extends by predicting a global pairwise distribution (Potts parameters) rather than independent per-position probabilities.

### 🔍 Gap Identification

**Disease variant prediction with deep generative models of evolutionary sequence variation (EVE)** (2021)
- *Authors:* Frazer et al.
- *Connection:* EVE underscored the power but also the limitation of MSA-based generative models—they require deep MSAs and are slow to deploy for novel or orphan folds—directly motivating InvMSAFold to generate MSA-like pairwise distributions from a single structure.

### 📊 Baseline

**Robust deep learning–based protein sequence design using ProteinMPNN** (2022)
- *Authors:* Dauparas et al.
- *Connection:* ProteinMPNN is the principal structure-conditioned design baseline that InvMSAFold improves upon by replacing autoregressive, single-sequence sampling with a predicted pairwise distribution enabling much faster sampling and substantially higher diversity.

### 🔧 Extension

**Improved contact prediction in proteins: Using pseudolikelihoods to infer Potts model parameters** (2013)
- *Authors:* Ekeberg et al.
- *Connection:* The plmDCA work established the standard parameterization (fields h and couplings J) and practical inference target that InvMSAFold emulates—predicting these Potts parameters without an MSA by conditioning on structure.

**Mutation effects predicted from sequence co-variation** (2017)
- *Authors:* Hopf et al.
- *Connection:* EVmutation demonstrated that Potts energies learned from MSAs capture functional constraints and enable sequence sampling with realistic epistasis, motivating InvMSAFold to recover MSA-like covariances from structure to achieve diverse, functional designs.

### 🔗 Related Problem

**Deep generative models of genetic variation capture mutation effects** (2018)
- *Authors:* Riesselman et al.
- *Connection:* DeepSequence showed that modeling a full sequence distribution from an MSA yields accurate fitness priors and epistatic structure; InvMSAFold keeps this “model-a-distribution then sample” paradigm but replaces the MSA with structure-conditioned parameter generation.

---

## Synthesis

InvMSAFold fuses two historically separate lines of work: MSA-based Potts modeling of protein sequence landscapes and structure-conditioned inverse folding. The DCA framework (Morcos et al.) and its practical pseudolikelihood inference (Ekeberg et al.) established the pairwise Markov random field with fields and couplings as a faithful model of coevolutionary constraints. EVmutation (Hopf et al.) further showed that these Potts energies capture epistasis relevant to function and that sampling from them yields plausible variant repertoires, clarifying the utility of a distributional, pairwise model for design. In parallel, DeepSequence and EVE demonstrated that generative models trained on MSAs provide strong priors over sequences but are bottlenecked by the need for deep alignments and are slow to deploy for novel folds—precisely the limitations InvMSAFold targets by predicting MSA-like pairwise statistics directly from structure. The inverse folding literature (Ingraham et al.; ProteinMPNN) defined effective structure-to-sequence learning but largely outputs per-position probabilities and samples sequences autoregressively, which hampers diversity and speed. InvMSAFold synthesizes these strands by using structural input to generate Potts parameters that mimic MSA covariances, enabling immediate, parallel sampling of highly diverse sequences while preserving structural and functional constraints. In effect, it replaces the MSA with structure as the source of epistatic signal and replaces autoregressive decoding with fast sampling from a learned pairwise distribution.

---
*Generated: 2026-01-06T23:09:26.594291*

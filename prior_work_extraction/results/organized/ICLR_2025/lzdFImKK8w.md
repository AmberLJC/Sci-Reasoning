# Prior Work Analysis Report

## Target Paper
**Title:** lzdFImKK8w
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**SKEMPI 2.0: an updated benchmark of changes in protein–protein binding energy, kinetics and thermodynamics upon mutation** (2019)
- *Authors:* Jankauskaitė et al.
- *Connection:* Defines the standard PPI ΔΔG prediction task and supplies the core benchmark used to evaluate methods under severe data scarcity, a key motivation for transferring knowledge from pretraining.

**Generative models for graph-based protein design** (2019)
- *Authors:* Ingraham et al.
- *Connection:* Established modeling p(sequence|structure) for inverse folding and interpreting negative log-likelihood as a statistical energy; this paper leverages that quantity and, via Bayes plus Boltzmann, aligns it to physical binding free energy changes.

### 💡 Inspiration

**Deep generative models of genetic variation capture the effects of mutations** (2018)
- *Authors:* Riesselman et al.
- *Connection:* Introduces the idea that log-likelihood differences from unsupervised generative models can approximate mutational effects via a statistical-energy view, directly inspiring this paper’s use of model log-likelihoods to estimate ΔΔG.

### 🔍 Gap Identification

**SAAMBE-3D: Predicting the effect of mutations on protein–protein interactions** (2020)
- *Authors:* Pahari et al.
- *Connection:* Representative supervised ΔΔG predictor relying on hand-crafted/physics-derived features; its limited generalization and data dependence motivate a principled alignment of pretrained inverse-folding knowledge to ΔΔG.

### 📊 Baseline

**Flex ddG: Rosetta ensemble-based estimation of changes in protein–protein binding affinity upon mutation** (2018)
- *Authors:* Barlow et al.
- *Connection:* Provides a primary physics-based baseline grounded in the thermodynamic cycle for PPI ΔΔG; the present work starts from the same thermodynamic definition but replaces costly conformational sampling with Boltzmann-aligned use of learned inverse-folding likelihoods.

### 🔧 Extension

**ProteinMPNN: Protein sequence design by learning probabilistic models of sequences conditioned on backbone** (2022)
- *Authors:* Dauparas et al.
- *Connection:* Provides a state-of-the-art inverse folding model whose log-likelihoods are directly used and explicitly aligned to ΔΔG in this work, improving over prior ad hoc use of raw likelihood differences.

**ESM-IF1: Inverse folding with a sequence–structure transformer** (2022)
- *Authors:* Hsu et al.
- *Connection:* Supplies a powerful structure-conditioned sequence likelihood that this paper repurposes; the Boltzmann Alignment formalism calibrates ESM-IF1 log-likelihoods to binding free-energy differences.

---

## Synthesis

The paper’s core idea—Boltzmann Alignment of inverse-folding log-likelihoods to predict ΔΔG for protein–protein interactions—arises from unifying thermodynamic principles with advances in structure-conditioned generative modeling. SKEMPI 2.0 formalized the PPI ΔΔG task and, by highlighting data scarcity, motivated leveraging pretrained models rather than purely supervised training. Physics-based methods such as Rosetta Flex ddG grounded ΔΔG prediction in the thermodynamic cycle, but their reliance on explicit conformational sampling is computationally intensive. DeepSequence provided the conceptual bridge that differences in model log-likelihoods can act as statistical energies reflecting mutational impact, suggesting a route to energy prediction without direct simulation. In parallel, inverse folding was established by Ingraham et al., who modeled p(sequence|structure) and interpreted negative log-likelihood as a sequence ‘energy’ for a given backbone; subsequent high-capacity models such as ProteinMPNN and ESM-IF1 delivered strong, calibrated log-likelihoods conditioned on structure. Prior uses of these scores for mutation assessment, however, lacked a principled thermodynamic alignment to binding free energy and did not account for conformational ensembles. The present work combines the Boltzmann distribution with Bayes’ theorem to re-express intractable p(structure|sequence) ratios in terms of accessible p(sequence|structure) likelihoods from inverse folding, thereby directly aligning statistical energies to ΔΔG. This addresses limitations of feature-engineered predictors like SAAMBE-3D and computationally heavy physics methods, yielding a data-efficient, thermodynamically grounded estimator of mutational effects on PPIs.

---
*Generated: 2026-01-06T23:09:26.598788*

# Prior Work Analysis Report

## Target Paper

**Title:** Gene Regulatory Network Inference in the Presence of Dropouts: a Causal View

**Conference:** ICLR 2024 (oral)

**Authors:** Haoyue Dai, Ignavier Ng, Gongxu Luo, Peter Spirtes, Petar Stojanov, Kun Zhang

**Keywords:** Gene regulatory network, Single-cell RNA-sequencing, Dropout, Zero-inflated data, Causal model, Causal discovery, Nonparametric

**Abstract:** 
> Gene regulatory network inference (GRNI) is a challenging problem, particularly owing to the presence of zeros in single-cell RNA sequencing data: some are biological zeros representing no gene expression, while some others are technical zeros arising from the sequencing procedure (aka dropouts), which may bias GRNI by distorting the joint distribution of the measured gene expressions. Existing approaches typically handle dropout error via imputation, which may introduce spurious relations as th...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Causality: Models, Reasoning, and Inference (2nd ed.)** (2009)
- *Authors:* Judea Pearl
- *Direct Connection:* Provides the causal-graph and selection-bias framework (selection diagrams, d-separation under selection) that the paper leverages to argue why conditional independences are preserved when cases are deleted based only on variables in the conditioning set.

**Bayesian approach to single-cell differential expression analysis** (2014)
- *Authors:* Peter V. Kharchenko et al.
- *Direct Connection:* Models scRNA-seq dropouts as a probabilistic function of true expression levels (SCDE), a mechanistic assumption the paper formalizes causally to justify how technical zeros arise and can be handled without imputation.

**Causation, Prediction, and Search (2nd ed.)** (2000)
- *Authors:* Peter Spirtes et al.
- *Direct Connection:* Establishes the constraint-based causal discovery paradigm that relies on conditional independences, which the paper’s main theorem is designed to preserve in zero-inflated data via principled case deletion.

### 💡 Inspiration

**Graphical Models for Processing Missing Data** (2013)
- *Authors:* Karthika Mohan et al.
- *Direct Connection:* Introduces missingness graphs (m-graphs) that explicitly model the data-generation and missingness mechanisms causally, which directly inspires the paper’s Causal Dropout Model that treats zeros as outcomes of a causal measurement process rather than naive missingness.

### 🔍 Gap Identification

**scImpute: accurate and robust imputation for single-cell RNA-seq data** (2018)
- *Authors:* Wei Vivian Li et al.
- *Direct Connection:* Represents the dominant imputation paradigm for handling scRNA-seq zeros, whose tendency to alter the joint distribution is explicitly identified by the paper as the bias it avoids through its CI-preserving deletion strategy.

**Recovering gene interactions from single-cell data using data diffusion (MAGIC)** (2018)
- *Authors:* David van Dijk et al.
- *Direct Connection:* Proposes diffusion-based imputation that smooths scRNA-seq data but can inflate spurious associations, a limitation the paper targets by proving CI recovery without any imputation.

### 🔧 Extension

**Recovering from Selection Bias in Causal and Statistical Inference** (2014)
- *Authors:* Elias Bareinboim et al.
- *Direct Connection:* Provides recoverability conditions under selection that the paper extends to the zero-inflation setting, underpinning the result that deleting samples with zeros in conditioned variables leaves the target conditional independences intact.

---

## Synthesis: How Prior Work Led to This Paper

Pearl’s treatment of selection bias formalizes how conditioning on or selecting by certain variables can preserve or distort conditional independences, offering graphical criteria to reason about when CI relations remain valid after case deletion. Mohan, Pearl, and Tian’s missingness graphs crystalize the idea that one should model the measurement/missingness mechanism causally, with explicit response indicators that determine whether values are observed, thereby enabling identification arguments about statistical relationships under missingness. Bareinboim, Tian, and Pearl provide recoverability conditions under selection, clarifying when target quantities (including independence relations) are preserved despite biased sampling. In parallel, Kharchenko et al. (SCDE) introduced a mechanistic view of scRNA-seq dropouts where the probability of observing a zero depends on the unobserved true expression, establishing a concrete, biologically motivated dropout mechanism. On the practice side, scImpute and MAGIC typify the prevailing imputation-first responses to zeros in single-cell data, replacing missing/zero entries with model-based estimates or diffusion-smoothed values, which can alter the joint distribution and inflate spurious dependencies.
Synthesizing these threads, the opportunity emerges to treat scRNA-seq zeros as outcomes of a causal measurement process and to reason about their impact on CI via selection/missingness graphs rather than imputation. By viewing deletion of samples with zeros in conditioned variables as a specific selection operation sanctioned by the graphical criteria of Pearl and Bareinboim, and grounding the dropout mechanism in SCDE-style assumptions, the paper shows that the true CIs are recoverable without imputation. This directly enables constraint-based causal/GRN discovery to proceed on zero-inflated single-cell data with nonparametric CI tests, aligning with the CPS framework while avoiding the joint-distribution distortions of imputation.

---

*Analysis generated on: 2026-01-06T23:51:14.926475*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

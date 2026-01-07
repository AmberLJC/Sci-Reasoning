# Prior Work Analysis Report

## Target Paper
**Title:** qgsXsqahMq
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Connection:* GETS adopts the core MoE idea of input-dependent expert selection, instantiating a sparsely-gated expert mixture as a post-hoc calibrator that routes each graph node to the most relevant calibration experts.

### 💡 Inspiration

**Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles** (2017)
- *Authors:* Balaji Lakshminarayanan et al.
- *Connection:* GETS explicitly leverages the uncertainty benefits of model ensembles proposed by Deep Ensembles and calibrates the aggregated ensemble outputs jointly through its expert gating mechanism.

**Do Transformers Really Perform Bad on Graphs? (Graphormer)** (2021)
- *Authors:* Chengxuan Ying et al.
- *Connection:* GETS draws on Graphormer’s centrality/degree encoding to incorporate degree embeddings as structural inputs to its gate, injecting graph topology into the calibration decision.

### 🔍 Gap Identification

**Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift** (2019)
- *Authors:* Yarin Ovadia et al.
- *Connection:* Ovadia et al. demonstrate that both single-model and post-hoc calibrated predictors often degrade under shift, motivating GETS’s combined use of model ensembles and input-aware calibration to improve robustness on graphs.

### 📊 Baseline

**On Calibration of Modern Neural Networks** (2017)
- *Authors:* Chuan Guo et al.
- *Connection:* GETS directly generalizes Guo et al.’s temperature scaling by replacing a single global temperature on logits with a node-wise, input-conditioned mixture of temperature experts that also exploits graph information.

**Beyond Temperature Scaling: Obtaining Well-Calibrated Multiclass Probabilities with Dirichlet Calibration** (2019)
- *Authors:* Marnik Kull et al.
- *Connection:* Dirichlet calibration is a principal post-hoc baseline that enriches TS with a more expressive mapping, and GETS advances this line by using a graph-aware mixture-of-experts as the richer calibrator instead of a fixed parametric transform.

---

## Synthesis

GETS builds squarely on post-hoc calibration while addressing its key shortcomings for graph learning. Temperature scaling by Guo et al. established the dominant baseline but uses a single global temperature on logits, ignoring input- and structure-specific variation. Dirichlet calibration pushed beyond a scalar temperature with a richer mapping, yet remains feature-agnostic and non-graph-aware. GETS advances this lineage by replacing a fixed calibrator with a graph-aware mixture-of-experts that conditions on logits, node features, and degree embeddings, thereby adapting the calibration rule per node. The architectural mechanism enabling this step is the sparsely-gated Mixture-of-Experts of Shazeer et al., which GETS repurposes as a post-hoc calibrator that routes each node to the most suitable temperature (or expert) components. On the uncertainty side, Deep Ensembles by Lakshminarayanan et al. showed that aggregating multiple models yields stronger, more reliable uncertainty; GETS explicitly integrates the ensemble signal into its calibration pipeline and learns to calibrate ensemble predictions jointly. For injecting topology, GETS is inspired by Graphormer’s centrality/degree encoding, using degree embeddings as lightweight but informative structural cues for the calibrator’s gate. Finally, evidence from Ovadia et al. that calibration often breaks under distribution shift motivates GETS’s combined input- and model-ensemble strategy, which is especially pertinent in graph domains where heterophily, sparsity, and structural variability demand node-wise, structure-aware calibration.

---
*Generated: 2026-01-06T23:09:26.640732*

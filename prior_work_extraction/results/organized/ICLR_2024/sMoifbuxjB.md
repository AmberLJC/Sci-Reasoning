# Prior Work Analysis Report

## Target Paper

**Title:** Towards Meta-Pruning via Optimal Transport

**Conference:** ICLR 2024 (spotlight)

**Authors:** Alexander Theus, Olin Geimer, Friedrich Wicke, Thomas Hofmann, Sotiris Anagnostidis, Sidak Pal Singh

**Keywords:** Pruning, Fusion

**Abstract:** 
> Structural pruning of neural networks conventionally relies on identifying and discarding less important neurons, a practice often resulting in significant accuracy loss that necessitates subsequent fine-tuning efforts. This paper introduces a novel approach named Intra-Fusion, challenging this prevailing pruning paradigm.
Unlike existing methods that focus on designing meaningful neuron importance metrics, Intra-Fusion redefines the overlying pruning procedure.
Through utilizing the concepts of...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Computational Optimal Transport** (2019)
- *Authors:* Peyré and Cuturi
- *Direct Connection:* Provides the optimal transport formulations and regularized solvers that underpin the paper’s construction of many-to-one neuron transport plans for fusion-based pruning.

### 💡 Inspiration

**Probabilistic Federated Neural Matching** (2019)
- *Authors:* Yurochkin et al.
- *Direct Connection:* This paper frames model aggregation as neuron matching with transport-style couplings, directly inspiring the use of transport plans to merge neurons rather than delete them in the pruning setting.

**Model Soup: Averaging Weights of Multiple Fine-Tuned Models Improves Accuracy Without Increasing Inference Time** (2022)
- *Authors:* Wortsman et al.
- *Direct Connection:* By demonstrating that weight-space averaging can recover or improve accuracy, this work motivates using fusion/averaging as a post-pruning recovery mechanism rather than heavy fine-tuning.

### 🔍 Gap Identification

**SNIP: Single-shot Network Pruning Based on Connection Sensitivity** (2019)
- *Authors:* Lee et al.
- *Direct Connection:* SNIP highlights that one-shot structural pruning based on importance scores incurs accuracy drops without fine-tuning, a limitation the paper addresses by using fusion to recover accuracy without costly retraining.

### 📊 Baseline

**Learning Efficient Convolutional Networks through Network Slimming** (2017)
- *Authors:* Liu et al.
- *Direct Connection:* This influential channel-pruning method uses BN-scale magnitudes as importance scores, which the paper treats as agnostic inputs and then replaces hard removal with optimal-transport-based fusion into retained channels.

### 🔧 Extension

**Git Re-Basin: Merging Models modulo Permutation Symmetries** (2023)
- *Authors:* Ainsworth et al.
- *Direct Connection:* By showing that neuron alignment via an assignment problem enables effective weight-space fusion, this work provides the matching machinery that the paper generalizes to many-to-one couplings for intra-layer neuron fusion during pruning.

### 🔗 Related Problem

**Federated Learning with Matched Averaging (FedMA)** (2020)
- *Authors:* Wang et al.
- *Direct Connection:* FedMA’s layer-wise neuron matching and averaging across models informs the paper’s strategy of matching low-importance units to survivors and fusing their weights instead of discarding them.

---

## Synthesis: How Prior Work Led to This Paper

Permutation symmetries in neural networks make naive weight averaging ineffective, and Git Re-Basin showed that solving a neuron alignment problem yields well-behaved weight-space fusion through assignment-based matching. In federated settings, Probabilistic Federated Neural Matching cast aggregation as constructing transport-like couplings between client neurons, while FedMA operationalized layer-wise neuron matching and averaging to form a coherent global model. Model Soup further established that weight-space averaging can recover or improve accuracy without changing inference cost when models are suitably aligned. In contrast, mainstream structural pruning approaches like Network Slimming rely on importance scores (e.g., BN scales) to delete channels outright, and SNIP’s single-shot pruning with sensitivity scores revealed that such deletion typically causes accuracy drops unless followed by expensive fine-tuning. The mathematical toolkit for these matching and fusion procedures is grounded in Computational Optimal Transport, which provides objectives and solvers to compute transport plans and their regularized variants. Bringing these threads together reveals a clear opportunity: instead of deleting low-importance neurons and relying on heavy fine-tuning to repair damage, match them to surviving neurons and fuse their parameters to preserve function. The paper synthesizes alignment from model-fusion work with importance scores from pruning, formulating pruning as many-to-one optimal transport that maps pruned units onto keepers. This OT-driven fusion recovers accuracy in a single shot and can be integrated into the pruning process during training to reduce training time while retaining competitive performance.

---

*Analysis generated on: 2026-01-06T12:29:00.694945*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Multisize Dataset Condensation

**Conference:** ICLR 2024 (oral)

**Authors:** Yang He, Lingao Xiao, Joey Tianyi Zhou, Ivor Tsang

**Keywords:** Dataset Condensation, Dataset Distillation, Image Classification

**Abstract:** 
> While dataset condensation effectively enhances training efficiency, its application in on-device scenarios brings unique challenges. 1) Due to the fluctuating computational resources of these devices, there's a demand for a flexible dataset size that diverges from a predefined size. 2) The limited computational power on devices often prevents additional condensation operations. These two challenges connect to the "subset degradation problem" in traditional dataset condensation: a subset from a ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Dataset Distillation** (2018)
- *Authors:* Tongzhou Wang et al.
- *Direct Connection:* This work established the core formulation of optimizing a small synthetic dataset so that training a model on it achieves high downstream accuracy, which MDC inherits as the basic condensation setup that its new adaptive subset loss augments.

### 💡 Inspiration

**Once for All: Train One Network and Specialize It for Efficient Deployment** (2020)
- *Authors:* Han Cai et al.
- *Direct Connection:* The ‘train-once, serve-many-budgets’ paradigm in Once-for-All directly motivates MDC’s idea of compressing N size-specific condensation processes into a single training via a subset-consistency objective.

### 📊 Baseline

**Matching Training Trajectories for Data Condensation** (2022)
- *Authors:* George Cazenavette et al.
- *Direct Connection:* MTT is a primary strong baseline that optimizes synthetic data for a fixed target size; MDC explicitly addresses MTT’s limitation of requiring separate condensation per size and the observed degradation when subsetting larger synthetic sets.

**Dataset Distillation with Kernel Methods (KIP)** (2021)
- *Authors:* Tuan Anh Nguyen et al.
- *Direct Connection:* KIP exemplifies fixed-budget condensation that must be rerun for each target size and whose subsets are not guaranteed to be representative; MDC targets this rigidity by training once to support many sizes.

### 🔧 Extension

**Dataset Condensation with Gradient Matching** (2021)
- *Authors:* Bo Zhao et al.
- *Direct Connection:* MDC builds directly on gradient-matching style condensation objectives and adds an adaptive subset loss so that any sampled subset of the synthesized data remains representative, collapsing multiple size-specific gradient-matching runs into a single training.

**Dataset Condensation with Distribution Matching** (2023)
- *Authors:* Bo Zhao et al.
- *Direct Connection:* MDC augments distribution-matching condensation by introducing a subset-consistency term on top of the base loss, enabling a single optimization to yield high-quality synthetic datasets across multiple sizes.

---

## Synthesis: How Prior Work Led to This Paper

Dataset distillation introduced the objective of optimizing a compact synthetic set so that training on it from scratch yields competitive performance, grounding later condensation methods in a meta-optimization over data rather than model weights. Gradient matching then provided a practical surrogate loss by directly aligning synthetic and real gradients, making synthetic sets tuned for a chosen budget (e.g., images per class). Matching training trajectories pushed fidelity further by aligning entire optimization paths, producing strong synthetic datasets but still targeting a single, fixed size. Distribution matching reframed condensation as aligning distributions of features/gradients between real and synthetic mini-batches, again yielding state-of-the-art results for a pre-specified dataset size. Kernel-based KIP demonstrated a distinct, fixed-budget route via inducing points in kernel space, similarly lacking guarantees that subsets of a larger synthetic set remain representative. Outside condensation, Once-for-All showed that a single training procedure can be structured to support many deployment budgets by enforcing consistency across sub-configurations.
Together these works crystallize a gap: leading condensation objectives (gradient/trajectory/distribution matching and kernel methods) optimize for one size at a time, and subsets of larger synthetic sets often degrade compared to sets distilled directly for the smaller size. Inspired by the Once-for-All paradigm, the new approach synthesizes these insights by augmenting standard condensation losses with a subset-consistency objective, effectively compressing multiple size-specific optimizations into one. This makes condensed data flexible for on-device deployment across fluctuating compute budgets while preserving representativeness at every target size.

---

*Analysis generated on: 2026-01-06T23:35:49.497367*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** SWAP-NAS: Sample-Wise Activation Patterns for Ultra-fast NAS

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yameng Peng, Andy Song, Haytham M. Fayek, Vic Ciesielski, Xiaojun Chang

**Keywords:** Neural Architecture Search, Network evaluation, Training-free metric, Deep neural networks

**Abstract:** 
> Training-free metrics (a.k.a. zero-cost proxies) are widely used to avoid resource-intensive neural network training, especially in Neural Architecture Search (NAS). Recent studies show that existing training-free metrics have several limitations, such as limited correlation and poor generalisation across different search spaces and tasks. Hence, we propose Sample-Wise Activation Patterns and its derivative, SWAP-Score, a novel high-performance training-free metric. It measures the expressivity ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Zero-Cost Proxies for Lightweight NAS** (2021)
- *Authors:* Abdelfattah et al.
- *Direct Connection:* This paper formalized training-free proxies for NAS and benchmarked metrics such as SNIP, GraSP, SynFlow, GradNorm, and Jacobian-based scores, whose limited and inconsistent cross-space correlations constitute the explicit gap SWAP-Score targets and the baselines it surpasses.

**On the number of linear regions of deep neural networks** (2014)
- *Authors:* Montúfar et al.
- *Direct Connection:* This work established that the diversity of activation regions (activation patterns) governs network expressivity, providing the theoretical basis for SWAP’s focus on aggregating sample-wise activation patterns as a performance predictor.

### 🔍 Gap Identification

**TE-NAS: Training-Free Evolution for Neural Architecture Search** (2021)
- *Authors:* Chen et al.
- *Direct Connection:* TE-NAS showed that no single zero-cost metric is reliably predictive across tasks and instead learned task-specific combinations, motivating SWAP’s design of a single, high-correlation metric that generalizes across search spaces without per-task weighting.

### 📊 Baseline

**Zen-NAS: A Zero-Shot NAS** (2021)
- *Authors:* Lin et al.
- *Direct Connection:* Zen-NAS proposed the Zen-Score, a training-free indicator based on BatchNorm and gradient responses that serves as a strong zero-shot baseline; SWAP is positioned to outperform such metrics while avoiding dataset-specific calibration.

### 🔧 Extension

**Neural Architecture Search Without Training** (2021)
- *Authors:* Mellor et al.
- *Direct Connection:* NASWOT introduced an activation-pattern-based separability proxy built from ReLU sign patterns over a batch, and SWAP directly generalizes this idea to sample-wise activation pattern expressivity with a formulation and regularization that improve robustness and cross-space generalization.

### 🔗 Related Problem

**Pruning neural networks without any data** (2020)
- *Authors:* Tanaka et al.
- *Direct Connection:* SynFlow introduced a data-agnostic saliency signal that seeded many training-free scores later repurposed for NAS, and SWAP departs from weight-saliency toward activation-pattern expressivity while benchmarking against SynFlow as a canonical zero-cost baseline.

---

## Synthesis: How Prior Work Led to This Paper

Research on training-free evaluation for NAS coalesced around zero-cost proxies that could predict performance without optimization. Abdelfattah et al. systematized this space by benchmarking SNIP, GraSP, SynFlow, Jacobian-based, and other instantaneous signals, revealing that correlations with final accuracy were often weak and inconsistent across search spaces and tasks. Mellor et al. (NASWOT) took a different tack, showing that the structure of ReLU activation sign patterns across a minibatch encodes separability and can predict accuracy without training, grounding a practical route to activation-pattern–based proxies. Chen et al. (TE-NAS) reported that no single proxy generalizes reliably; instead they learned task-dependent combinations of heterogeneous signals to drive evolution, improving results but at the cost of per-task tuning. Lin et al. (Zen-NAS) proposed Zen-Score, a zero-shot indicator built from BatchNorm and input-gradient responses, providing a strong single-metric baseline yet still showing sensitivity to dataset and search space. In parallel, Tanaka et al. (SynFlow) demonstrated robust, data-agnostic saliency for pruning at initialization, which was later reused as a NAS proxy but remained weight-centric. The theoretical backdrop from Montúfar et al. connected the diversity of activation regions to expressivity, justifying activation-pattern counting as a meaningful capacity measure. Together, these works suggest that activation-pattern–based expressivity is promising, but existing instantiations either lack robustness (single proxies) or require task-specific combinations. Building on the sign-pattern insight of NASWOT and the expressivity theory of linear regions, the next step is to measure sample-wise activation pattern structure over a batch and regularize it to decouple size effects, yielding a single, training-free metric with stable cross-space and cross-task correlation.

---

*Analysis generated on: 2026-01-06T12:43:25.558971*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

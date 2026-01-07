# Prior Work Analysis Report

## Target Paper
**Title:** ZV7CLf0RHK
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning** (2020)
- *Authors:* Armen Aghajanyan et al.
- *Connection:* By showing fine-tuning primarily moves models within a low-dimensional subspace, this work underpins both low-rank PEFT and NoRM’s premise that most useful signal concentrates in a small set of principal directions that can be retained while discarding noise.

### 💡 Inspiration

**Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time** (2022)
- *Authors:* Mitchell Wortsman et al.
- *Connection:* Model soups demonstrated that consolidating stable signal across models/checkpoints reduces overfitting without inference overhead; NoRM internalizes this idea by retaining the majority (stable) subspace of a LoRA update prior to merge, achieving a single-model, zero-latency denoising effect.

### 🔍 Gap Identification

**AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning** (2023)
- *Authors:* Chen et al.
- *Connection:* AdaLoRA exposed that many LoRA directions are redundant and used SVD-based importance to allocate rank; NoRM addresses the same redundancy issue but targets noise/hallucination by post-hoc decomposing the LoRA update and reserving the majority (stable) components before merging.

### 📊 Baseline

**LoRA: Low-Rank Adaptation of Large Language Models** (2021)
- *Authors:* Edward J. Hu et al.
- *Connection:* This work adopts the LoRA fine-tuning scheme and directly operates on the learned LoRA updates, proposing to reduce redundancies in these low-rank parameters before merging them back—explicitly improving upon LoRA’s behavior at higher ranks.

### 🔗 Related Problem

**DoRA: Weight-Decomposed Low-Rank Adaptation for Large Language Models** (2024)
- *Authors:* Liu et al.
- *Connection:* DoRA showed that decomposing parameters (magnitude/direction) in PEFT can improve stability and quality; NoRM similarly leverages structured decomposition of LoRA updates but focuses on denoising—keeping the major components and suppressing noise to curb hallucinations.

**Editing Models with Task Arithmetic** (2023)
- *Authors:* Gabriel Ilharco et al.
- *Connection:* Task Arithmetic treats fine-tuning as a weight-space delta that can be analyzed and manipulated; NoRM operates directly on the LoRA delta, decomposing it and preserving dominant directions, echoing the task-vector perspective that meaningful signal resides in a structured subspace.

---

## Synthesis

The core of NoRM is to study redundancy in LoRA parameters and then explicitly denoise the LoRA update before merging it into the base model, preserving a majority (stable) subspace while suppressing noisy components that exacerbate hallucinations. This idea sits squarely on top of LoRA’s formulation (Hu et al.), which provides the low-rank parameterization whose updates NoRM analyzes and modifies. Evidence that fine-tuning lives in a low-dimensional subspace (Aghajanyan et al.) motivates both LoRA and NoRM’s assumption that the useful adaptation signal concentrates in a compact set of directions. AdaLoRA directly surfaced the redundancy problem in LoRA by ranking singular directions and reallocating rank, revealing a gap: high-rank LoRA can carry superfluous or low-importance directions. NoRM addresses this by a post-hoc decomposition of the learned LoRA delta and retention of the dominant components, targeting noise reduction and hallucination control rather than budget allocation.
DoRA further influenced the design space by showing that careful decomposition of PEFT parameters can improve stability and quality, reinforcing that structure-aware operations on the adaptation weights are beneficial. From the perspective of model consolidation, Model Soups provided the intuition that aggregating stable signals can reduce overfitting without inference overhead; NoRM internalizes a similar principle within a single fine-tuning run by keeping the majority subspace of the LoRA update. Finally, Task Arithmetic frames fine-tuning as a manipulable delta in weight space; NoRM concretizes this by operating directly on the LoRA delta, projecting onto dominant directions to retain capacity while suppressing hallucination-inducing noise.

---
*Generated: 2026-01-06T23:09:26.630783*

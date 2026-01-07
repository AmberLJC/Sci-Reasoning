# Prior Work Analysis Report

## Target Paper

**Title:** HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models

**Conference:** ICLR 2025 (oral)

**Authors:** Qiushi Huang, Tom Ko, Zhan Zhuang, Lilian Tang, Yu Zhang

**Keywords:** Parametric-efficient fine-tuning, Large Language Model

**Abstract:** 
> We propose Hadamard High-Rank Adaptation (HiRA), a parameter-efficient fine-tuning (PEFT) method that enhances the adaptability of Large Language Models (LLMs). While Low-rank Adaptation (LoRA) is widely used to reduce resource demands, its low-rank updates may limit its expressiveness for new tasks. HiRA addresses this by using a Hadamard product to retain high-rank update parameters, improving the model capacity. Empirically, HiRA outperforms LoRA and its variants on several tasks, with extens...

---

## Key Prior Works (5 papers with direct influence)

### 💡 Inspiration

**Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning (IA3)** (2022)
- *Authors:* Liu et al.
- *Direct Connection:* IA3 introduces learned element-wise multiplicative scaling (Hadamard gating) within Transformer layers, inspiring HiRA’s use of an element-wise (Hadamard) mechanism to modulate weights so that the resulting updates can be high-rank while staying parameter-efficient.

**Compacter: Efficient Low-Rank Adaptation via Parameterized Hypercomplex Multiplication** (2021)
- *Authors:* Mahabadi et al.
- *Direct Connection:* Compacter demonstrates that structured parameterizations using composition operations (e.g., PHM-based factorization) can yield expressive, effectively full-rank adapter transforms with few parameters, a principle HiRA echoes using a Hadamard product to realize high-rank updates efficiently.

### 🔍 Gap Identification

**AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning** (2023)
- *Authors:* Zhang et al.
- *Direct Connection:* AdaLoRA highlights that fixed-rank LoRA can be under-expressive and proposes dynamic rank allocation, a limitation HiRA resolves more directly by enabling inherently high-rank updates via a Hadamard product without relying on rank scheduling.

### 📊 Baseline

**LoRA: Low-Rank Adaptation of Large Language Models** (2022)
- *Authors:* Hu et al.
- *Direct Connection:* HiRA directly addresses LoRA’s core limitation—updates constrained to a fixed low rank—by replacing the BA low-rank update with a Hadamard-based parameterization that preserves high-rank update capacity under a similar parameter budget.

### 🔗 Related Problem

**DoRA: Weight-Decomposed Low-Rank Adaptation** (2024)
- *Authors:* Liu et al.
- *Direct Connection:* By decomposing weight direction and magnitude to improve LoRA’s expressiveness, DoRA motivates HiRA’s alternative route to boosting capacity—achieving high-rank weight updates through element-wise (Hadamard) modulation rather than only reparameterizing low-rank factors.

---

## Synthesis: How Prior Work Led to This Paper

Low-Rank Adaptation (LoRA) established the dominant PEFT formulation by expressing update matrices as BA with small rank, greatly reducing trainable parameters but necessarily constraining the update’s rank and expressiveness. AdaLoRA exposed the brittleness of a fixed rank by allocating budget adaptively across layers and steps, indicating that capacity bottlenecks—not just parameter count—limit downstream performance. DoRA further probed LoRA’s capacity issue by decomposing weight magnitude and direction, showing that reparameterizing how updates are represented can recover substantial accuracy under similar budgets. IA3 introduced learned element-wise multiplicative scaling within Transformer components, validating that Hadamard-style modulation is a lightweight yet powerful means to steer model behavior without large parameter overhead. Compacter, via PHM-style structured parameterization, showed that carefully designed compositions can synthesize expressive, effectively high-rank adapter transformations while remaining compact.
Together, these works reveal a clear opportunity: LoRA’s low-rank constraint systematically limits update expressiveness, while element-wise multiplicative modulation and structured parameterizations can unlock far higher capacity without abandoning parameter efficiency. Building on these insights, the current work synthesizes the benefits by using a Hadamard product to parameterize updates so they remain high-rank under a modest parameter budget, sidestepping rank tuning and complementing prior reparameterizations like DoRA while retaining LoRA’s practical simplicity.

---

*Analysis generated on: 2026-01-06T18:17:47.794415*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

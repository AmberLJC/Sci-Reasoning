# Prior Work Analysis Report

## Target Paper

**Title:** DARE the Extreme: Revisiting Delta-Parameter Pruning For Fine-Tuned Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Wenlong Deng, Yize Zhao, Vala Vakilian, Minghui Chen, Xiaoxiao Li, Christos Thrampoulidis

**Keywords:** Delta parameter pruning, Efficiency, Large Language Models

**Abstract:** 
> Storing open-source fine-tuned models separately introduces redundancy and increases response times in applications utilizing multiple models. Delta-parameter pruning (DPP), particularly the random drop and rescale (DARE) method proposed by Yu et al., addresses this by pruning the majority of delta parameters—the differences between fine-tuned and pre-trained model weights—while typically maintaining minimal performance loss. However, DARE fails when either the pruning rate or the magnitude of t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**BitFit: Simple Parameter-Efficient Fine-Tuning for Transformer-based Masked Language Models** (2021)
- *Authors:* Ben Zaken et al.
- *Direct Connection:* By showing that only a small subset of parameters (biases) need to change during fine-tuning, BitFit provides empirical grounding that many delta parameters are dispensable, motivating aggressive delta pruning refined by DAREx.

### 💡 Inspiration

**Dropout: A Simple Way to Prevent Neural Networks from Overfitting** (2014)
- *Authors:* Nitish Srivastava et al.
- *Direct Connection:* DARE’s use of 1/(1-p) rescaling after random dropping is inherited from dropout’s expectation-preserving principle, which DAREx rethinks to avoid variance blow-up at extreme pruning.

**Regularization of Neural Networks using DropConnect** (2013)
- *Authors:* Li Wan et al.
- *Direct Connection:* DARE’s mechanism of randomly zeroing weights (here, delta-weights) with rescaling is a direct analogue of DropConnect’s weight-level stochastic masking that DAREx retains but rescales more robustly.

### 🔧 Extension

**DARE: Drop-and-Rescale for Delta-Parameter Pruning** (2024)
- *Authors:* Yu et al.
- *Direct Connection:* DAREx directly modifies DARE’s core random drop-and-rescale scheme by replacing its expectation-preserving scaling (which explodes at high pruning rates) and correcting for biased, high-variance delta distributions that DARE assumes away.

### 🔗 Related Problem

**Movement Pruning: Adaptive Sparsity by Fine-Tuning** (2020)
- *Authors:* Victor Sanh et al.
- *Direct Connection:* Movement pruning demonstrates that sparsity can be introduced during fine-tuning with minimal loss, informing DAREx’s premise that large fractions of fine-tuning deltas can be removed if scaling/statistics are handled correctly.

**Editing Models with Task Arithmetic** (2022)
- *Authors:* Gabrielle Ilharco et al.
- *Direct Connection:* Task arithmetic shows that scaling and combining weight deltas (task vectors) critically affects behavior, directly motivating DAREx’s attention to delta mean/variance and principled rescaling for stable performance.

---

## Synthesis: How Prior Work Led to This Paper

Randomized drop-and-rescale has a long lineage: dropout established the expectation-preserving 1/(1−p) rule for activation masking, and DropConnect ported the idea to weight-level stochastic masking. DARE applies this exact principle to delta-weights—the differences between fine-tuned and base parameters—pruning a random subset of deltas and rescaling the survivors to keep the expected update unchanged. Independent evidence from parameter-efficient fine-tuning reinforced the feasibility of removing many updates: BitFit showed that modifying only biases can often suffice, and movement pruning demonstrated that sparsity introduced during fine-tuning preserves accuracy if chosen carefully. Complementary work on task vectors revealed that the magnitude and statistics of weight deltas strongly influence model behavior; scaling those deltas changes downstream performance in predictable ways, implying that both the rescaling rule and the distributional properties (mean and variance) of deltas matter.
Collectively, these works exposed an opportunity: while random delta pruning can work surprisingly well, the dropout-style rescaling inherited by DARE becomes unstable under extreme pruning, and real-world delta distributions are not zero-mean with benign variance. The natural next step was to keep the simplicity and speed of random delta masking but replace brittle expectation-only scaling with a robust scheme and to actively correct delta statistics. DAREx operationalizes this by introducing a modified rescaling (DAREx-q) that avoids large-factor blowups and by normalizing/centering high-mean, high-variance deltas to push pruning into the extreme regime with minimal loss.

---

*Analysis generated on: 2026-01-06T13:03:33.883890*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

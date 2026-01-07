# Prior Work Analysis Report

## Target Paper
**Title:** hlvKd7Vdxm
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Sparse Communication for Distributed Gradient Descent** (2017)
- *Authors:* Alham Fikri Aji et al.
- *Connection:* This work established the top-k/sparsification principle that most updates are redundant, which ExCP applies temporally by sparsifying residuals between adjacent checkpoints.

**Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding** (2016)
- *Authors:* Song Han et al.
- *Connection:* Deep Compression demonstrated near-lossless accuracy after aggressive parameter pruning, directly underpinning ExCP’s premise that many parameters (here, residuals across checkpoints) can be discarded while retaining performance.

### 💡 Inspiration

**Deep Gradient Compression: Reducing the Communication Bandwidth for Distributed Training** (2018)
- *Authors:* Yujun Lin et al.
- *Connection:* DGC showed that small updates can be safely dropped when momentum is used to preserve their effect, directly motivating ExCP’s weight–momentum joint criterion for safely discarding many parameters at checkpoint time.

**RigL: Pruning and Growing Sparse Neural Networks** (2020)
- *Authors:* Utku Evci et al.
- *Connection:* RigL uses momentum-informed signals to decide which connections to keep or regrow; ExCP adopts the same insight—using momentum magnitude as an importance signal—to decide which residual parameters must be preserved in compressed checkpoints.

**LoRA: Low-Rank Adaptation of Large Language Models** (2021)
- *Authors:* Edward J. Hu et al.
- *Connection:* LoRA popularized representing training progress as compact parameter deltas to a base model; ExCP similarly stores changes rather than full weights by computing and sparsifying residuals between adjacent checkpoints.

### 🔍 Gap Identification

**8-bit Optimizers via Block-wise Quantization** (2022)
- *Authors:* Tim Dettmers et al.
- *Connection:* 8-bit optimizers compress optimizer states but do not exploit them to guide what to store; ExCP addresses this gap by explicitly using momentum information to decide which parameters can be discarded from checkpoints.

---

## Synthesis

ExCP’s core idea has two pillars: store only the information that changes between checkpoints, and let optimizer momentum tell you which changes truly matter. The first pillar is rooted in the sparsification literature. Aji and Heafield (2017) established that most updates are redundant, while Han et al. (2016) showed that large-scale pruning can be near-lossless—together legitimizing ExCP’s aggressive pruning of checkpoint deltas. LoRA (Hu et al., 2021) further popularized representing training as compact deltas to a base model; ExCP transposes this notion temporally by computing residuals between adjacent checkpoints and sparsifying them instead of saving full states.

The second pillar—weight–momentum joint shrinking—builds on momentum-aware sparsification ideas. Deep Gradient Compression (Lin et al., 2018) demonstrated that momentum can preserve the effect of dropped small updates, providing a clear mechanism for safely discarding many entries. RigL (Evci et al., 2020) reinforced momentum as a powerful importance signal for deciding which connections to keep. ExCP synthesizes these insights by jointly considering weight residual magnitude and momentum to retain only critical parameters when saving checkpoints.

Finally, while 8-bit optimizers (Dettmers et al., 2022) shrink optimizer states, they do not use optimizer statistics to guide storage. ExCP explicitly leverages momentum to decide what to keep, achieving extreme checkpoint compression with negligible loss—bridging sparsification theory, delta-based storage, and momentum-informed selection into a single checkpoint-centric framework.

---
*Generated: 2026-01-06T23:09:26.420002*

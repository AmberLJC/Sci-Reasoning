# Prior Work Analysis Report

## Target Paper
**Title:** eFGQ97z5Cd
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Connection:* Introduced MoE layers and the learned router with softmax gating probabilities—the exact routing weights (RWs) this paper repurposes as semantic embeddings.

**Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks** (2019)
- *Authors:* Nils Reimers et al.
- *Connection:* Established the sentence-embedding problem formulation and evaluation protocols that this work targets, providing the benchmark setting where RW-based embeddings are assessed.

### 🔍 Gap Identification

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Connection:* Standardized simple top-1 routing where gating scores are used solely for dispatch and balancing; this paper explicitly addresses that overlooked gap by using those router scores as off-the-shelf embeddings.

**SimCSE: Simple Contrastive Learning of Sentence Embeddings** (2021)
- *Authors:* Tianyu Gao et al.
- *Connection:* Showed that strong embeddings typically require (contrastive) finetuning; the present work addresses this limitation by achieving competitive performance without finetuning via MoE routing weights and their combination with hidden states.

### 🔧 Extension

**GShard: Scaling Giant Neural Networks with Conditional Computation and Automatic Sharding** (2020)
- *Authors:* Dmitry Lepikhin et al.
- *Connection:* Extended MoE to Transformer LMs with top-2 gating and load-balancing losses, defining the practical RW signals (pre-top-k soft routing) that the current work extracts and analyzes.

**GLaM: Efficient Scaling of Language Models with Mixture-of-Experts** (2022)
- *Authors:* Nan Du et al.
- *Connection:* Demonstrated large-scale MoE LLMs and router behavior across layers; the proposed method directly leverages these GLaM-style router distributions as representation vectors.

---

## Synthesis

The paper’s core insight—that the router in sparse Mixture-of-Experts LLMs already computes a rich, task-agnostic representation—traces directly to the invention and scaling of MoE routing. Shazeer et al. (2017) introduced sparsely-gated MoE layers and the learned router whose softmax gating probabilities define the routing weights; these are precisely the signals the present work repurposes as embeddings. GShard (Lepikhin et al., 2020) adapted MoE to Transformers with top-k gating and balancing losses, making router scores a stable, ubiquitous byproduct across layers that can be extracted without modifying training. Switch Transformers (Fedus et al., 2021) popularized simple top-1 routing for trillion-parameter models, but treated router outputs purely as a dispatch mechanism—an implicit gap this paper exploits by reframing those scores as robust semantic embeddings. GLaM (Du et al., 2022) further validated the scalability and behavior of MoE routers in large LLMs, providing the exact architectural context whose routing distributions the authors analyze.
In parallel, the sentence-embedding literature defined both the problem and its prevailing assumption that finetuning is necessary. Sentence-BERT (Reimers & Gurevych, 2019) established standard evaluation, while SimCSE (Gao et al., 2021) demonstrated that contrastive finetuning is key for strong performance. The current work challenges this premise by showing MoE routing weights—complementary to hidden states—yield strong, prompt-robust embeddings without any finetuning, and by combining RW and HS (MoEE) to surpass either alone.

---
*Generated: 2026-01-06T23:09:26.636549*

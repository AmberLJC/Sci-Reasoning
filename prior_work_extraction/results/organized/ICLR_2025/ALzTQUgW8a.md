# Prior Work Analysis Report

## Target Paper

**Title:** MagicPIG: LSH Sampling for Efficient LLM Generation

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zhuoming Chen, Ranajoy Sadhukhan, Zihao Ye, Yang Zhou, Jianyu Zhang, Niklas Nolte, Yuandong Tian, Matthijs Douze, Leon Bottou, Zhihao Jia, Beidi Chen

**Keywords:** locality sensitive hashing, randomized algorithms, llm inference, kv cache

**Abstract:** 
> Large language models (LLMs) with long context windows have gained significant attention. However, the KV cache, stored to avoid re-computation, becomes a bottleneck. Various dynamic sparse or TopK-based attention approximation methods have been proposed to leverage the common insight that attention is sparse. In this paper, we first show that TopK attention itself suffers from quality degradation in certain downstream tasks because attention is not always as sparse as expected. Rather than sele...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Similarity Estimation Techniques from Rounding Algorithms** (2002)
- *Authors:* Moses Charikar
- *Direct Connection:* MagicPIG relies on Charikar’s sign random projection LSH for angular similarity to construct hash tables whose collision probabilities track query–key cosine similarity, enabling provably good sampling of high-contribution keys.

**Asymmetric LSH (ALSH) for Maximum Inner Product Search (MIPS)** (2014)
- *Authors:* Anshumali Shrivastava et al.
- *Direct Connection:* Because attention is governed by dot products, MagicPIG draws on ALSH’s transformation for MIPS so that LSH buckets preferentially retrieve large inner-product keys, aligning the sampler with the attention scoring function.

### 💡 Inspiration

**SLIDE: In Defense of Smart Algorithms over Hardware Acceleration for Large-Scale Deep Learning Systems** (2020)
- *Authors:* Beidi Chen et al.
- *Direct Connection:* MagicPIG adopts SLIDE’s heterogeneous design—maintaining LSH hash tables on CPU to cheaply select a small candidate set that is then processed on GPU—adapting it from sparse MLP training to LLM attention inference.

### 🔍 Gap Identification

**Big Bird: Transformers for Longer Sequences** (2020)
- *Authors:* Manzil Zaheer et al.
- *Direct Connection:* BigBird shows fixed sparse patterns can approximate attention but implicitly assume sparsity, a limitation that MagicPIG addresses by demonstrating quality drops when attention is dense and replacing hard sparsity with unbiased LSH-based sampling.

### 🔧 Extension

**Reformer: The Efficient Transformer** (2020)
- *Authors:* Nikita Kitaev et al.
- *Direct Connection:* MagicPIG repurposes Reformer’s LSH-based bucketing of queries/keys, but instead of restricting attention within buckets, it uses the buckets to importance-sample KV pairs during decoding, yielding an unbiased estimator of attention with far lower runtime.

### 🔗 Related Problem

**Rethinking Attention with Performers** (2021)
- *Authors:* Krzysztof Choromanski et al.
- *Direct Connection:* Performer’s unbiased, theoretically grounded approximation of softmax attention motivates MagicPIG’s shift from deterministic TopK selection to a provably justified stochastic estimator, though MagicPIG uses data-dependent LSH sampling rather than random features.

---

## Synthesis: How Prior Work Led to This Paper

Charikar introduced sign random projection LSH for angular similarity, establishing that hash collisions probabilistically track cosine similarity; this makes it possible to retrieve vectors with high dot products using compact binary hashes. Shrivastava and Li extended this line to maximum inner product search via ALSH, mapping inner-product neighbors to LSH-retrievable space so that large dot-product items are found efficiently. Reformer carried LSH into the Transformer itself, hashing queries and keys so attention is computed within buckets, reducing complexity by exploiting locality in representation space. Performer reframed approximate attention as a statistically principled estimation problem, using unbiased random feature expansions to approximate softmax attention with theoretical guarantees. BigBird demonstrated that sparse patterns can preserve long-range modeling with theoretical coverage, but these patterns still hinge on attention being sparse. SLIDE showed that hashing can power a heterogeneous system: maintain cheap hash tables on CPU to shortlist high-value candidates and push only those to accelerators for heavy compute. These threads collectively reveal that (1) attention relevance aligns with dot-product neighbors recoverable by LSH, (2) unbiased estimators can replace brittle TopK heuristics, and (3) hashing-driven candidate selection maps naturally to CPU–GPU pipelines. The natural next step is to replace deterministic TopK or fixed sparsity with LSH-guided, theoretically grounded sampling of keys and values during decoding, and to operationalize it in a heterogeneous system that builds and queries hash tables efficiently while preserving attention quality when sparsity assumptions fail.

---

*Analysis generated on: 2026-01-06T17:37:05.387461*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

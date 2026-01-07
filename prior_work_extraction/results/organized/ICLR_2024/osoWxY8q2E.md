# Prior Work Analysis Report

## Target Paper

**Title:** ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models

**Conference:** ICLR 2024 (oral)

**Authors:** Seyed Iman Mirzadeh, Keivan Alizadeh-Vahid, Sachin Mehta, Carlo C del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar

**Keywords:** Large Language Models, Sparsity, Activation Function, ReLU Activation Function

**Abstract:** 
> Large Language Models (LLMs) with billions of parameters have drastically transformed AI applications. However, their demanding computation during inference has raised significant challenges for deployment on resource-constrained devices. Despite recent trends favoring alternative activation functions such as GELU or SiLU, known for increased computation, this study strongly advocates for reinstating ReLU activation in LLMs. We demonstrate that using the ReLU activation function has a negligible...

---

## Key Prior Works (7 papers with direct influence)

### 💡 Inspiration

**Deep Sparse Rectifier Neural Networks** (2011)
- *Authors:* Xavier Glorot et al.
- *Direct Connection:* This work established that ReLU induces sparse, exactly-zero activations, a property the paper scales to LLMs and operationalizes with algorithms that skip inactive neurons and reuse activation masks across tokens.

### 🔍 Gap Identification

**SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot** (2023)
- *Authors:* Aleksandar Frantar et al.
- *Direct Connection:* While demonstrating high unstructured weight sparsity with minimal perplexity loss, this work highlights limited practical speedups on GPUs, motivating the paper’s shift to activation sparsity (via ReLU) that can be exploited at inference time for real runtime gains.

### 📊 Baseline

**GLU Variants Improve Transformer** (2020)
- *Authors:* Noam Shazeer et al.
- *Direct Connection:* SwiGLU from this work is the dominant LLM activation baseline that the paper replaces with ReLU to unlock exact channel-level zeros and enable neuron-skipping during inference.

**Gaussian Error Linear Units (GELUs)** (2016)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* GELU is the standard smooth activation used in many Transformers; the paper directly challenges this default by swapping GELU with ReLU to obtain activation sparsity without hurting convergence.

**Sigmoid-Weighted Linear Units for Deep Learning** (2018)
- *Authors:* Dongyoon Elfwing et al.
- *Direct Connection:* SiLU/Swish, widely adopted in LLM MLPs, serves as a primary baseline whose smooth nonlinearity lacks inherent zeros; the paper shows ReLU can match its accuracy while enabling zero-skipping and reduced weight transfer.

### 🔧 Extension

**DejaVu: Contextual Sparsity for Efficient LLM Inference** (2023)
- *Authors:* Liu et al.
- *Direct Connection:* By revealing temporal consistency and contextual sparsity of active neurons in LLMs, this work directly motivates the paper’s strategy to cache and reuse activated neuron sets across tokens, now amplified by ReLU’s exact zeros.

### 🔗 Related Problem

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* This paper’s conditional computation via top-k expert gating informs the idea that selective activation can cut FLOPs; the current work achieves a non-architectural, intra-layer analogue by leveraging ReLU-induced channel sparsity.

---

## Synthesis: How Prior Work Led to This Paper

GLU Variants Improve Transformer introduced SwiGLU, showing that gated smooth activations outperform plain ReLU in Transformers and becoming the default MLP nonlinearity in modern LLMs. GELU further cemented smooth activations as standard, and SiLU/Swish provided another widely adopted choice; however, all of these eliminate exact zeros, implicitly precluding straightforward zero-skipping at inference. Earlier, Deep Sparse Rectifier Neural Networks established that ReLU naturally yields sparse, exactly-zero activations, suggesting a compute-saving opportunity if such sparsity could be safely harnessed in large models. DejaVu then demonstrated contextual sparsity and temporal consistency of active neurons in LLMs, showing that small subsets of channels remain predictive across successive tokens, hinting that caching and reusing active sets could substantially reduce matmul cost. In parallel, SparseGPT revealed that although large weight sparsity is achievable post hoc, unstructured weight sparsity often fails to translate into real GPU speedups, pointing to the need for a more hardware-friendly sparsity source. Switch Transformers validated the principle that conditional computation—activating only a subset of capacity per token—can preserve quality while cutting FLOPs.
Together, these works exposed a promising but underutilized path: conditional computation at the channel level that is temporally stable and hardware-exploitable. By reinstating ReLU, the current paper recovers exact activation zeros, strengthens the temporal reuse signal observed by DejaVu, and translates it into practical inference-time algorithms that skip inactive neurons and reuse activation masks, achieving substantial compute and memory-traffic reductions without sacrificing convergence or accuracy.

---

*Analysis generated on: 2026-01-06T10:12:20.577278*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

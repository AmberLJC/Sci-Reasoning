# Prior Work Analysis Report

## Target Paper

**Title:** Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zeyuan Allen-Zhu, Yuanzhi Li

**Keywords:** scaling laws, knowledge capacity, language models

**Abstract:** 
> Scaling laws describe the relationship between the size of language models and their capabilities. Unlike prior studies that evaluate a model's capability via loss or benchmarks, we estimate information-theoretically the number of knowledge \emph{bits} a model stores. We focus on factual knowledge represented as tuples, such as (USA, capital, Washington D.C.) from a Wikipedia page. Through multiple controlled datasets, we establish that language models can and only can store \emph{2 bits of know...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Language Models as Knowledge Bases?** (2019)
- *Authors:* Fabio Petroni et al.
- *Direct Connection:* Petroni et al. formalized factual knowledge as subject–relation–object tuples and developed probing protocols, providing the exact problem formulation this paper uses to define and count “knowledge bits” stored by language models.

### 💡 Inspiration

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Direct Connection:* By showing that transformer feed-forward layers act as key–value memory that stores factual associations, this work directly motivates treating parameters as memory slots and underpins the paper’s per-parameter knowledge capacity estimate.

### 🔍 Gap Identification

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Jordan Hoffmann et al.
- *Direct Connection:* Hoffmann et al. refined loss-based, compute-optimal scaling, whose limitation—optimizing loss rather than parametric knowledge—explicitly motivates this paper’s shift to measuring knowledge capacity.

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* Carlini et al. quantified parametric memorization and extraction, highlighting that prior measures focused on verbatim data rather than structured factual knowledge—a gap this paper closes by counting extractable knowledge bits.

### 📊 Baseline

**Scaling Laws for Neural Language Models** (2020)
- *Authors:* Jared Kaplan et al.
- *Direct Connection:* Kaplan et al. introduced loss-based scaling laws that serve as the primary baseline the paper replaces with an information-theoretic scaling law over stored knowledge bits.

### 🔗 Related Problem

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* Switch Transformers introduced sparse MoE architectures where only a subset of parameters are active per token, directly prompting this paper’s analysis of how sparsity/MoE affects per-parameter knowledge storage capacity.

**LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale** (2022)
- *Authors:* Tim Dettmers et al.
- *Direct Connection:* Dettmers et al. showed that int8 quantization preserves model quality, motivating the paper’s test of whether knowledge capacity per parameter remains invariant under int8—culminating in the 2-bits-per-parameter result even when quantized.

---

## Synthesis: How Prior Work Led to This Paper

Petroni et al. established the practice of viewing factual knowledge in language models as subject–relation–object tuples and probing models for these associations, thereby setting a concrete, structured notion of what constitutes factual knowledge in parametric form. Geva et al. then argued that transformer feed-forward layers serve as key–value memories, directly tying parameters to stored factual associations and suggesting a memory-slot perspective on what parameters hold. Kaplan et al. demonstrated predictable power-law scaling of performance with model size, data, and compute but defined capability via loss, not explicit knowledge content. Hoffmann et al. refined these loss-based laws to compute-optimal regimes, further entrenching loss as the dominant metric for “capability.” In parallel, Fedus et al. introduced sparse Mixture-of-Experts, complicating the relationship between total parameters and active capacity by activating only a fraction of parameters per token. Carlini et al. quantified parametric memorization and extraction, but focused on verbatim training data rather than structured factual knowledge. Dettmers et al. showed that int8 quantization can preserve downstream quality, raising the question of how discretization affects what and how much knowledge is actually stored. Together, these works revealed a gap: while models scale predictably in loss and maintain quality under sparsity and quantization, there was no direct, information-theoretic account of how many discrete units of factual knowledge are stored per parameter. Building on tuple-based probing and the memory view of transformer parameters, the paper replaces loss with an information-centric metric, constructs controlled datasets of facts, and derives a robust scaling law—about two bits of factual knowledge per parameter—that remains stable across training duration, architecture (including MoE), and quantization, providing a unified, actionable measure of knowledge capacity.

---

*Analysis generated on: 2026-01-06T06:34:37.288191*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

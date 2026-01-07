# Prior Work Analysis Report

## Target Paper
**Title:** IfD2MKTmWv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Memory Mosaics at scale fuses classical associative memory theory with modern large-scale language modeling practice. Hopfield’s original energy-based formulation and Kanerva’s Sparse Distributed Memory supply the core principle: content-addressable, distributed storage that can be composed across many cells. Building on this, modern continuous Hopfield work (Ramsauer et al.) formalizes the tight link between associative dynamics and attention, making associative layers compatible with transformer-era optimization and providing a natural path to LLM-scale architectures.

From the neural memory systems lineage, Neural Turing Machines contribute differentiable read/write access and training recipes for modular memory components, strongly informing Memory Mosaics’ v2 architectural choices for robust new-knowledge insertion without catastrophic interference. Retrieval-augmented LMs such as RETRO show that separating parametric knowledge from non-parametric memory can yield large inference-time gains; this directly motivates the paper’s evaluation axes—training-knowledge storage versus new-knowledge storage—and its claim that inference-time augmentation is a superior route to rapid knowledge acquisition.

Finally, GPT-3 establishes in-context learning as a central competency and provides the canonical evaluation setting that Memory Mosaics v2 seeks to outperform. Chinchilla-style scaling laws guide the 10B-parameter, trillion-token training regime used as a fair comparison point and ground the paper’s assertion that simply scaling data for transformers does not recover the benefits of an explicitly associative, memory-centric design. Together, these works converge on the key insight: networks of associative memories can be engineered to retain transformer-level pretraining performance while substantially improving inference-time learning and compositionality at LLM scale.

---
*Generated: 2026-01-06T23:42:48.149454*

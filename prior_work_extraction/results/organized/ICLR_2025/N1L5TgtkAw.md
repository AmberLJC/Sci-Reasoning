# Prior Work Analysis Report

## Target Paper

**Title:** Multi-Draft Speculative Sampling: Canonical Decomposition and Theoretical Limits

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ashish J Khisti, MohammadReza Ebrahimi, Hassan Dbouk, Arash Behboodi, Roland Memisevic, Christos Louizos

**Keywords:** speculative decoding, multi draft speculative sampling, large language models, weighted importance sampling, optimal transport

**Abstract:** 
> We consider multi-draft speculative sampling, where the proposal sequences are sampled independently from different draft models.  At each step, a  token-level draft selection scheme takes a list of valid tokens as input and produces an output token whose distribution matches that of the target model. Previous works have demonstrated that the optimal scheme (which maximizes the probability of accepting one of the input tokens) can be cast as a solution to a linear program. In this work we show t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Blockwise Parallel Decoding for Deep Autoregressive Models** (2018)
- *Authors:* Mitchell Stern et al.
- *Direct Connection:* Introduced the draft-and-verify paradigm that underlies token-list verification, the core procedural template that speculative sampling builds upon and that this paper refines for multi-draft settings.

**Fast Inference from Transformers via Speculative Decoding** (2023)
- *Authors:* Yair Leviathan et al.
- *Direct Connection:* Established single-draft speculative sampling with an accept/reject rule guaranteeing exact target distribution, which this work uses as the second stage of its canonical two-step decomposition.

**Optimally Combining Sampling Techniques for Monte Carlo Rendering** (1995)
- *Authors:* Eric Veach and Leonidas J. Guibas
- *Direct Connection:* Introduced multiple importance sampling for combining independent proposal distributions, directly informing the paper’s first-stage weighted-IS selection across multiple draft models.

### 🔍 Gap Identification

**On the Acceptance Rate and Exactness of Speculative Decoding** (2024)
- *Authors:* Sun et al.
- *Direct Connection:* Analyzed acceptance probability and exactness conditions for single-draft speculative decoding, motivating this paper’s derivation of necessary and sufficient conditions and explicit expressions in the multi-draft (two identical drafts) case.

### 📊 Baseline

**Optimal Multi‑Draft Speculative Sampling via Linear Programming** (2024)
- *Authors:* Zhang et al.
- *Direct Connection:* Formulated the optimal token-level selection in multi-draft speculative sampling as a linear program maximizing acceptance, which this paper decomposes into an IS-based intermediate selection followed by single-draft speculation.

### 🔧 Extension

**Speculative Decoding as Optimal Transport** (2024)
- *Authors:* Liu et al.
- *Direct Connection:* Showed the equivalence between optimal token assignment and an optimal-transport coupling, providing the structural LP view that this paper leverages to derive a canonical two-step factorization and limits.

---

## Synthesis: How Prior Work Led to This Paper

Blockwise Parallel Decoding formalized the draft-and-verify pattern that allows proposing multiple tokens and conditionally verifying them against a stronger model, establishing the procedural backbone for token-list acceptance schemes. Building on that, Fast Inference from Transformers via Speculative Decoding laid out a single-draft accept/reject mechanism that preserves the target model’s distribution, specifying the exact correctness criterion and acceptance rules now standard in speculative sampling. Subsequent work cast multi-draft token selection as a linear program that maximizes the probability of accepting one of several proposals, revealing an optimal policy over token lists under multiple independent drafts. A complementary strand connected this LP to optimal transport, showing the token-assignment structure is a coupling between proposal and target distributions. Orthogonally, multiple importance sampling provided the principled way to combine several independent proposals into an unbiased selection through appropriately weighted draws. Finally, theoretical analyses of acceptance rates characterized exactness and tight bounds in the single-draft case, clarifying when perfect acceptance is attainable and where bottlenecks arise. Taken together, these works exposed both the structural LP/OT nature of optimal multi-draft selection and the statistical principle for combining proposals via importance weights. The present paper synthesizes these insights by proving a canonical two-step factorization—an IS-style intermediate selection followed by single-draft speculation—and by tightening theory with necessary and sufficient conditions and explicit acceptance expressions for two identical drafts, thereby pinpointing the fundamental limits of multi-draft speculative sampling.

---

*Analysis generated on: 2026-01-06T13:34:38.131205*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

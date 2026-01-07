# Prior Work Analysis Report

## Target Paper

**Title:** Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness

**Conference:** ICLR 2024 (oral)

**Authors:** Bohang Zhang, Jingchu Gai, Yiheng Du, Qiwei Ye, Di He, Liwei Wang

**Keywords:** Graph Neural Networks, Expressive Power, Homomorphism, Subgraph Counting, Weisfeiler-Lehman

**Abstract:** 
> Designing expressive Graph Neural Networks (GNNs) is a fundamental topic in the graph learning community. So far, GNN expressiveness has been primarily assessed via the Weisfeiler-Lehman (WL) hierarchy. However, such an expressivity measure has notable limitations: it is inherently coarse, qualitative, and may not well reflect practical requirements (e.g., the ability to encode substructures). In this paper, we introduce a novel framework for quantitatively studying the expressiveness of GNN arc...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**How Powerful are Graph Neural Networks?** (2019)
- *Authors:* Keyulu Xu et al.
- *Direct Connection:* By establishing the Weisfeiler–Lehman (WL) test as the de facto benchmark for GNN expressiveness and tying MPNNs to 1-WL, this work set the qualitative, WL-centric yardstick that the present paper replaces with a quantitative homomorphism-based measure.

**Weisfeiler and Leman Go Neural: Higher-Order Graph Neural Networks** (2019)
- *Authors:* Christopher Morris et al.
- *Direct Connection:* By aligning higher-order GNN architectures with the k-WL hierarchy, this paper entrenched WL as the organizing principle for expressiveness, motivating the need for a unified quantitative framework that can compare such models beyond coarse WL levels.

**Large Networks and Graph Limits** (2012)
- *Authors:* László Lovász
- *Direct Connection:* Lovász’s results that homomorphism count vectors form complete graph invariants provide the mathematical backbone for defining homomorphism expressivity and proving its completeness for comparing GNN models.

### 💡 Inspiration

**The Logical Expressive Power of Graph Neural Networks** (2020)
- *Authors:* Pablo Barceló et al.
- *Direct Connection:* Their characterization of GNNs via first-order logic with counting highlighted counting as the core mechanism of GNN expressivity, directly inspiring the shift to a homomorphism-count–based expressivity measure.

**Expressive Power of Invariant and Equivariant Graph Neural Networks** (2021)
- *Authors:* Alireza Azizian and Marc Lelarge
- *Direct Connection:* By connecting invariant/equivariant GNNs to polynomial graph invariants tightly linked to subgraph and homomorphism counts, this work motivates treating homomorphism counting as a principled, quantitative yardstick for GNN expressiveness.

### 🔍 Gap Identification

**Improving Graph Neural Networks with Learnable Structural and Positional Representations** (2020)
- *Authors:* Georgios Bouritsas et al.
- *Direct Connection:* By explicitly targeting motif/subgraph counting as a missing practical capability in standard GNNs, this work exposes the concrete need—quantifying substructure-counting power—that the homomorphism expressivity metric directly addresses.

### 📊 Baseline

**Provably Powerful Graph Networks** (2019)
- *Authors:* Haggai Maron et al.
- *Direct Connection:* These tensor-power architectures exemplify beyond-1-WL expressiveness via higher-order invariants, serving as a primary model class that the new homomorphism expressivity framework evaluates and compares quantitatively.

---

## Synthesis: How Prior Work Led to This Paper

Xu et al. formalized GNN expressiveness through the lens of the 1-WL test and popularized WL as the field’s benchmark, while Morris et al. extended this alignment to higher-order GNNs via k-WL, cementing a qualitative, WL-centric hierarchy of expressiveness. Barceló et al. then provided a logic-with-counting characterization of GNNs, revealing that counting is the operative mechanism underlying the distinctions WL captures. Lovász’s theory established that homomorphism count vectors constitute complete graph invariants, offering a principled quantitative basis to compare graphs through counts. Azizian and Lelarge connected invariant/equivariant GNNs to polynomial invariants intimately tied to subgraph and homomorphism counts, suggesting a natural bridge from neural architectures to count-based measures. Maron et al. introduced tensor-power architectures achieving beyond-1-WL power via higher-order invariants, providing concrete models whose strengths should be compared quantitatively. In parallel, Bouritsas et al. highlighted practical needs around motif and subgraph counting, underscoring the limitations of purely WL-based assessments for real tasks. Together, these works expose that WL offers only a coarse, qualitative scale, while theory and practice increasingly revolve around counting. The current paper synthesizes these insights by proposing homomorphism expressivity—a complete, quantitative measure grounded in homomorphism counts—that spans model families like MPNNs, higher-order/tensor GNNs, and subgraph-aware designs. This framework naturally follows from Lovász’s completeness, the logic-of-counting view, and the community’s emphasis on subgraph counting, yielding a unified tool that compares models’ expressivity and concretely interprets abilities such as subgraph counting.

---

*Analysis generated on: 2026-01-06T09:20:54.824936*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

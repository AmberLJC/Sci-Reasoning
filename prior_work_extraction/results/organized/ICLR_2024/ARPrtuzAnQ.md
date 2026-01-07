# Prior Work Analysis Report

## Target Paper

**Title:** On the hardness of learning under symmetries

**Conference:** ICLR 2024 (spotlight)

**Authors:** Bobak Kiani, Thien Le, Hannah Lawrence, Stefanie Jegelka, Melanie Weber

**Keywords:** Equivariance, statistical query, lower bound, computational hardness, invariance, symmetry, neural networks

**Abstract:** 
> We study the problem of learning equivariant neural networks via gradient descent. The incorporation of known  symmetries ("equivariance") into neural nets has empirically improved the performance of learning pipelines, in domains ranging from biology to computer vision. However, a rich yet separate line of learning theoretic research has demonstrated that actually learning shallow, fully-connected (i.e. non-symmetric) networks has exponential complexity in the correlational statistical query (C...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Efficient noise-tolerant learning from statistical queries** (1998)
- *Authors:* Michael Kearns
- *Direct Connection:* Introduces the Statistical Query (SQ) framework that underpins the correlational SQ (CSQ) model used to formalize the gradient-descent–encompassing hardness results in this paper.

**Group Equivariant Convolutional Networks** (2016)
- *Authors:* Taco S. Cohen and Max Welling
- *Direct Connection:* Introduces the group-equivariant CNN paradigm that this paper targets, with CSQ lower bounds showing that learning shallow instances of such equivariant CNNs remains hard despite built-in symmetry.

**Deep Sets** (2017)
- *Authors:* Manzil Zaheer et al.
- *Direct Connection:* Provides the canonical permutation-invariant architecture (sum/mean pooling over sets) that underlies the permutation-invariant networks analyzed here via CSQ lower bounds (including frame-averaged constructions).

**Invariant and Equivariant Graph Networks** (2019)
- *Authors:* Haggai Maron et al.
- *Direct Connection:* Develops invariant polynomial/tensor constructions for permutation groups, which this work directly targets by proving CSQ hardness for learning such invariant polynomial networks.

**Equivariance Through Parameter-Sharing** (2017)
- *Authors:* Siamak Ravanbakhsh et al.
- *Direct Connection:* Formalizes enforcing group symmetries via parameter-sharing and averaging, the exact frame-averaged mechanism whose CSQ learning hardness is established for permutation subgroups in this paper.

### 🔍 Gap Identification

**The Complexity of Learning Neural Networks via Statistical Queries** (2017)
- *Authors:* Amit Daniely
- *Direct Connection:* Establishes exponential CSQ lower bounds for learning shallow fully-connected networks, directly motivating this paper’s central question of whether symmetry (e.g., parameter sharing/group actions) can circumvent such SQ barriers.

### 🔧 Extension

**A general characterization of the statistical query complexity** (2012)
- *Authors:* Vitaly Feldman
- *Direct Connection:* Provides the modern SQ/CSQ lower-bound machinery and indistinguishability tools that this paper instantiates within symmetry-constrained hypothesis classes to derive superpolynomial and exponential lower bounds.

---

## Synthesis: How Prior Work Led to This Paper

The statistical query paradigm of Kearns formalized algorithms that access data through expectations rather than individual examples, laying the groundwork for correlational SQ analyses. Feldman’s characterization supplied the modern lower-bound machinery—based on indistinguishability of carefully crafted distributions in the CSQ model—that has become the standard way to argue that whole families of learning procedures, including gradient-based ones, cannot succeed under certain regimes. Building on this, Daniely demonstrated exponential CSQ lower bounds for learning shallow fully-connected neural networks, crystallizing a precise computational barrier for gradient-descent–like learners. In parallel, Cohen and Welling introduced group-equivariant convolutional networks, showing how group structure can be embedded via weight tying and group convolution; Zaheer and colleagues proposed Deep Sets, the canonical architecture for permutation-invariant learning; and Maron and collaborators developed invariant and equivariant graph networks using polynomial/tensor representations of permutation groups. Ravanbakhsh et al. unified these themes through parameter sharing and explicit group-averaging constructions to guarantee equivariance.
These strands collectively posed a natural question: might symmetry-aware architectures evade CSQ hardness known for non-symmetric shallow networks? By combining Feldman’s CSQ lower-bound toolkit with the concrete symmetry mechanisms from equivariant CNNs, Deep Sets, invariant polynomials, and parameter-sharing/frame averaging, the present work shows that symmetry does not lift the barrier—proving superpolynomial or exponential CSQ lower bounds for learning shallow GNNs, CNNs, invariant polynomial networks, and frame-averaged models for permutation subgroups. Thus, the synthesis of CSQ hardness techniques with precise equivariant constructions reveals an inherent computational limitation persisting even under known symmetries.

---

*Analysis generated on: 2026-01-06T16:56:23.660654*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

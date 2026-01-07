# Prior Work Analysis Report

## Target Paper

**Title:** Homomorphism Expressivity of Spectral Invariant Graph Neural Networks

**Conference:** ICLR 2025 (oral)

**Authors:** Jingchu Gai, Yiheng Du, Bohang Zhang, Haggai Maron, Liwei Wang

**Keywords:** Graph Neural Network, Expressive Power, Spectral Invariant, Graph Homomorphism, Weisfeiler-Lehman

**Abstract:** 
> Graph spectra are an important class of structural features on graphs that have shown promising results in enhancing Graph Neural Networks (GNNs). Despite their widespread practical use, the theoretical understanding of the power of spectral invariants --- particularly their contribution to GNNs --- remains incomplete. In this paper, we address this fundamental question through the lens of homomorphism expressivity, providing a comprehensive and quantitative analysis of the expressive power of s...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**How Powerful are Graph Neural Networks?** (2019)
- *Authors:* Keyulu Xu et al.
- *Direct Connection:* This work formalized MPNN expressivity via 1-WL, providing the baseline framework that the paper quantitatively refines by showing how spectral invariants change homomorphism-counting power beyond the 1-WL regime.

**Universal Invariant and Equivariant Graph Neural Networks** (2019)
- *Authors:* Mathieu Keriven et al.
- *Direct Connection:* Their characterization of invariant graph functions as (limits of) polynomial functions of adjacency/Laplacian underpins the paper’s use of spectral moments to derive precise homomorphism-counting capabilities.

**Spectra of Graphs** (2011)
- *Authors:* Andries E. Brouwer et al.
- *Direct Connection:* Classical spectral moment identities (e.g., sums of eigenvalue powers equaling closed-walk counts) provide the mathematical bridge the paper exploits to connect spectral invariants to exact homomorphism counts for specific tree-like templates.

### 💡 Inspiration

**Provably Powerful Graph Networks** (2019)
- *Authors:* Haggai Maron et al.
- *Direct Connection:* This work showed invariant/equivariant networks can implement explicit homomorphism counts of small templates, directly inspiring the present paper’s homomorphism-based proof technique to identify exactly-countable tree-like patterns with spectral invariants.

### 🔍 Gap Identification

**The Logical Expressiveness of Graph Neural Networks** (2021)
- *Authors:* Pablo Barceló et al.
- *Direct Connection:* By pinning MPNNs to C2 and exposing their inability to count many subgraphs, this paper motivates addressing that gap, which the current work fills by proving what additional homomorphism counts become exact when spectral invariants are used.

### 🔗 Related Problem

**Weisfeiler and Leman Go Neural: Higher-Order Graph Neural Networks** (2019)
- *Authors:* Christopher Morris et al.
- *Direct Connection:* By linking higher-order GNNs to k-WL and substructure counting, this paper established the homomorphism-counting lens for expressivity that is extended here to characterize what spectral-invariant architectures can exactly count.

---

## Synthesis: How Prior Work Led to This Paper

Xu et al. established that message-passing GNNs are bounded by 1-WL, motivating expressivity analyses in terms of structures these networks can or cannot distinguish. Morris et al. connected higher-order GNNs to k-WL and substructure counting, crystallizing a homomorphism-counting perspective for expressivity: certain architectures are exactly characterized by the graph templates whose homomorphisms they can count. Maron et al. demonstrated that invariant/equivariant architectures can implement explicit homomorphism polynomials, making homomorphism counts a constructive tool rather than just a characterization. Keriven and Peyré showed invariant graph functions arise as polynomial functions of adjacency/Laplacian, tying invariance to traces and spectral moments that encode structured walk counts. Barceló et al. formalized the logical limits of MPNNs in C2, highlighting their inability to count many subgraphs and calling for principled ways to surpass these limits. Finally, Brouwer and Haemers provided the spectral moment equalities linking eigenvalue power sums to closed-walk counts, the key algebraic identities connecting spectra to combinatorial counts.
Bringing these threads together, a natural opportunity emerges: use the polynomial/spectral viewpoint to translate spectral invariants into precise homomorphism-counting capabilities and quantify how this extends WL-bounded MPNNs. By leveraging spectral moment identities within the homomorphism-count framework pioneered for higher-order and invariant networks, the paper pinpoints a concrete, exactly-countable family—parallel trees—and derives a hierarchy across spectral-invariant architectural variants and depths. This synthesis turns the abstract promise of spectra into a rigorous, quantitative expressivity statement about what subgraphs spectral-invariant GNNs can exactly count.

---

*Analysis generated on: 2026-01-06T09:39:11.473210*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

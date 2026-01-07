# Prior Work Analysis Report

## Target Paper
**Title:** oQ4igHyh3N
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

TokenFormer’s key contribution—replacing all linear projections with attention between input tokens and a bank of learned parameter tokens—sits at the intersection of three mature ideas: decoupling weights from computation, cross-attention to learned latents, and token-dependent parameter selection. HyperNetworks first showed that a model’s parameters need not be fixed matrices tied to architecture; TokenFormer takes this further by making parameters persistent, addressable tokens rather than generated weights. Set Transformer and Perceiver introduced cross-attention to learned latent arrays/inducing points, decoupling input size from internal compute; TokenFormer repurposes this mechanism so every projection layer queries a shared parameter-token memory, enabling dimension-agnostic scaling and architectural changes without full retraining. Theoretical work on fast weight programmers reframed attention as dynamic weight access, providing the conceptual bridge for treating parameters as memory retrieved by queries. Product Key Memory demonstrated scalable, content-addressable parameter banks in Transformer LMs; TokenFormer generalizes this from auxiliary memory to the universal substrate replacing linear layers. Finally, MoE (Switch Transformer) established that tokens can be routed to subsets of parameters for scalable capacity, a principle TokenFormer adopts through differentiable attention rather than hard gating. Together with evidence from prefix/soft prompting that learned token vectors can act as effective parametric knobs, these works crystallize into TokenFormer’s parameter-as-tokens paradigm for native architectural scalability.

---
*Generated: 2026-01-06T23:42:48.094845*

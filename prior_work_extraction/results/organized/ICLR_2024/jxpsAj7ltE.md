# Prior Work Analysis Report

## Target Paper

**Title:** From Sparse to Soft Mixtures of Experts

**Conference:** ICLR 2024 (spotlight)

**Authors:** Joan Puigcerver, Carlos Riquelme Ruiz, Basil Mustafa, Neil Houlsby

**Keywords:** transformers, mixtures of experts, computer vision

**Abstract:** 
> Sparse mixture of expert architectures (MoEs) scale model capacity without significant increases in training or inference costs.
Despite their success, MoEs suffer from a number of issues: training instability, token dropping, inability to scale the number of experts, or ineffective finetuning.
In this work, we propose Soft MoE, a fully-differentiable sparse Transformer that addresses these challenges, while maintaining the benefits of MoEs.
Soft MoE performs an implicit soft assignment by passi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Direct Connection:* This work introduced sparse MoE layers with discrete top-k token-to-expert routing and load-balancing losses, the core framework that Soft MoE keeps in spirit while replacing non-differentiable routing with a soft, fully differentiable assignment to avoid token dropping and instability.

### 💡 Inspiration

**DSelect-k: Differentiable Selection in the Mixture-of-Experts Model** (2021)
- *Authors:* Yassine Hazimeh et al.
- *Direct Connection:* DSelect-k proposed a continuous relaxation for expert selection, directly inspiring Soft MoE’s pursuit of fully differentiable sparse routing but leading Soft MoE to a different mechanism—soft token mixing to experts—to avoid brittle relaxed top-k selection.

### 🔍 Gap Identification

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* Switch’s top-1 token-choice routing exposed key limitations—training instability, expert overload, and token dropping due to capacity—that Soft MoE explicitly targets with its soft routing and differentiable sparse design.

### 📊 Baseline

**Scaling Vision with Sparse Mixture of Experts** (2021)
- *Authors:* Carlos Riquelme et al.
- *Direct Connection:* V-MoE brought token-choice MoE to ViTs and introduced router z-loss for stability, providing the principal vision baseline and revealing finetuning fragility and token-drop issues that Soft MoE resolves with its soft token-to-expert mixing.

**Mixture-of-Experts with Expert Choice Routing** (2022)
- *Authors:* Barret Zoph et al.
- *Direct Connection:* Expert-Choice routing showed that letting experts select tokens can scale the number of experts, a key comparator that Soft MoE surpasses by using soft token mixtures per expert to remove hard assignments while keeping sparsity.

### 🔗 Related Problem

**GLaM: Efficient Scaling of Language Models with Mixture-of-Experts** (2022)
- *Authors:* Nan Du et al.
- *Direct Connection:* GLaM’s large-scale top-2 token routing demonstrated MoE’s capacity benefits but retained discrete routing and capacity-based token drops, motivating Soft MoE’s fully differentiable sparse routing that scales experts without dropping tokens.

---

## Synthesis: How Prior Work Led to This Paper

Sparsely-Gated Mixture-of-Experts established the core recipe of conditional computation with discrete top-k token-to-expert routing and balancing losses, enabling massive capacity without proportional compute but introducing non-differentiable decisions and capacity-driven token drops. Switch Transformers simplified routing to top-1 and scaled MoEs impressively, yet surfaced instability, expert overload, and dropped tokens, revealing brittleness in discrete routing under load constraints. In vision, V-MoE adapted token-choice MoE to ViTs, adding router z-loss to stabilize routing while still relying on hard capacity limits that hinder fine-tuning and cause token dropping. GLaM demonstrated the benefits of top-2 token routing at extreme scale, but maintained the same discrete mechanisms and capacity truncation, constraining expert count scalability. Expert-Choice routing inverted the assignment by allowing experts to select tokens, improving scalability to many experts but still using hard, non-differentiable selections. In parallel, DSelect-k introduced a differentiable relaxation for expert selection, pointing toward end-to-end trainable routers yet tied to relaxed top-k choices that can be brittle. Taken together, these works defined the sparse MoE paradigm, exposed its discrete routing pathologies, and explored scalability via token- or expert-centric assignments. The natural next step is a fully differentiable sparse router that preserves MoE’s conditional compute while eliminating hard selection and token dropping; by softly mixing tokens per expert and maintaining sparse expert computation, Soft MoE synthesizes these insights to stabilize training, scale expert counts, and improve fine-tuning in vision.

---

*Analysis generated on: 2026-01-06T15:14:06.782612*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy

**Conference:** ICLR 2024 (spotlight)

**Authors:** Pingzhi Li, Zhenyu Zhang, Prateek Yadav, Yi-Lin Sung, Yu Cheng, Mohit Bansal, Tianlong Chen

**Keywords:** Sparse Mixture-of-Experts, Efficiency, Merging, Compression

**Abstract:** 
> Sparsely activated Mixture-of-Experts (SMoE) has shown promise to scale up the learning capacity of neural networks, however, they have issues like: ($a$) $\textit{High Memory Usage,}$ due to duplication of the network layers into multiple copies as experts; and ($b$) $\textit{Redundancy in Experts,}$ as common learning-based routing policies suffer from representational collapse. Therefore, vanilla SMoE models are memory inefficient and non-scalable, especially for resource-constrained downstre...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Direct Connection:* This work introduced the SMoE formulation with learned routing and load-balancing, establishing the duplicated-experts architecture and routing signals that the current method consolidates via expert merging.

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* Switch’s practical routing (top-1) and stabilization techniques exposed routing-driven expert redundancy and collapse, motivating the use of router probabilities as actionable signals to guide which experts to merge and how much to compress.

### 💡 Inspiration

**The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks** (2022)
- *Authors:* Mohammad Reza Entezari et al.
- *Direct Connection:* This paper’s insight that permutation symmetry underlies successful model interpolation directly motivates performing neuron alignment prior to fusing experts so that merged experts land in a compatible mode.

**TIES-Merging: Resolving Interference When Merging Models** (2023)
- *Authors:* Prateek Yadav et al.
- *Direct Connection:* The idea of masking/sparsifying unimportant parameter differences to prevent interference when merging models directly informs the proposed redundancy-aware scheme that prevents dominant experts from overshadowing critical ones during expert fusion.

### 📊 Baseline

**Merging Models with Fisher-Weighted Averaging** (2022)
- *Authors:* Michael Matena et al.
- *Direct Connection:* Fisher-weighted averaging serves as a primary merging baseline that the authors find ineffective for SMoE expert consolidation, motivating their routing-aware and permutation-aligned merging strategy.

### 🔧 Extension

**Git Re-Basin: Merging Models modulo Permutation Symmetry** (2023)
- *Authors:* Samuel Ainsworth et al.
- *Direct Connection:* The current method extends Git Re-Basin’s neuron permutation alignment by applying weight matching within each expert and across experts, now guided by router-derived affinities, before merging to avoid destructive averaging.

### 🔗 Related Problem

**DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training** (2022)
- *Authors:* Samyam Rajbhandari et al.
- *Direct Connection:* By formalizing and instrumenting routing policies (e.g., Expert-Choice) with per-expert loads and balancing losses, this work provides the measurable routing statistics that are repurposed as hints for grouping and prioritizing experts during merging.

---

## Synthesis: How Prior Work Led to This Paper

Sparsely-gated Mixture-of-Experts was established by Shazeer et al., which paired learned routing with load balancing to scale capacity but at the cost of duplicating expert parameters and incurring memory overhead; crucially, this setup yields router probabilities and per-expert loads as observable signals. Switch Transformers demonstrated a practical, top-1 routing variant and stabilization tricks, yet also revealed that learned routing can induce expert redundancy and collapse, highlighting that routing statistics reflect which experts truly carry distinct knowledge. DeepSpeed-MoE further systematized routing with Expert-Choice and exposed per-expert traffic and balancing metrics, making routing behavior measurable at scale. In parallel, the model-merging literature showed both potential and pitfalls: Git Re-Basin introduced neuron permutation alignment to enable effective weight fusion by matching units across networks, while Entezari et al. explained why permutation alignment is necessary for mode-compatible merging. Fisher-weighted averaging provided a principled but permutation-agnostic baseline that often fails when representations are misaligned. TIES-Merging showed that sparsifying or masking unimportant differences reduces interference during fusion, preventing dominant updates from swamping critical parameters. Together, these works expose a gap: SMoE has rich routing signals that identify expert importance and similarity, but naïve merging fails without permutation alignment and interference control. The natural next step is to merge experts using router-derived affinities to group and weight experts, apply neuron-level permutation matching before fusion, and incorporate redundancy-aware masking; this yields compact, knowledgeable experts that can then be safely compressed.

---

*Analysis generated on: 2026-01-06T09:22:41.793515*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

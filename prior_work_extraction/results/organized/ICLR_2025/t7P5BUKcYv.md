# Prior Work Analysis Report

## Target Paper

**Title:** MoE++: Accelerating Mixture-of-Experts Methods with Zero-Computation Experts

**Conference:** ICLR 2025 (oral)

**Authors:** Peng Jin, Bo Zhu, Li Yuan, Shuicheng YAN

**Keywords:** Mixture of Experts, Large Language Models, Efficient Foundation Models

**Abstract:** 
> In this work, we aim to simultaneously enhance the effectiveness and efficiency of Mixture-of-Experts (MoE) methods. To achieve this, we propose MoE++, a general and heterogeneous MoE framework that integrates both Feed-Forward Network (FFN) and zero-computation experts. Specifically, we introduce three types of zero-computation experts: the zero expert, copy expert, and constant expert, which correspond to discard, skip, and replace operations, respectively. This design offers three key advanta...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Direct Connection:* MoE++ directly extends the sparsely-gated MoE formulation by augmenting the expert set with zero-computation options and permitting tokens to effectively choose k=0 (skip) under the same routing framework.

### 💡 Inspiration

**ST-MoE: Designing Stable and Transferable Mixture-of-Experts** (2022)
- *Authors:* Barret Zoph et al.
- *Direct Connection:* ST-MoE’s exploration of routing design to better allocate expert capacity inspires MoE++ to go further by allowing routers to choose non-FFN actions (skip/replace) so true FFN experts focus on challenging tokens.

**Universal Transformers** (2019)
- *Authors:* Mostafa Dehghani et al.
- *Direct Connection:* The ACT-style per-token halting in Universal Transformers motivates MoE++’s zero expert and cheap paths (copy/constant), bringing adaptive, token-wise computation to the MoE layer.

### 🔍 Gap Identification

**BASE Layers: Simplifying Training of Large, Sparse Models** (2021)
- *Authors:* Mike Lewis et al.
- *Direct Connection:* By highlighting routing imbalance and capacity contention in MoE, BASE motivates MoE++’s approach of expanding the routing action space with zero-compute experts to reduce contention rather than only rebalance assignments.

### 📊 Baseline

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* MoE++ addresses Switch’s limitation of uniform per-token FFN usage and capacity-induced token dropping by letting routers assign easy tokens to zero/copy/constant experts so FFN capacity is concentrated on hard tokens.

**GLaM: Efficient Scaling of Language Models with Mixture-of-Experts** (2022)
- *Authors:* Nan Du et al.
- *Direct Connection:* While GLaM improves quality with top-2 routing, it still enforces fixed FFN compute per token; MoE++ directly relaxes this by learning a variable number of FFN calls—including zero—to allocate computation adaptively.

### 🔧 Extension

**GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding** (2020)
- *Authors:* Igor Lepikhin et al.
- *Direct Connection:* MoE++ builds on the GShard integration of MoE into Transformer FFN sublayers by generalizing the expert space from pure FFNs to heterogeneous experts (zero, copy, constant) within the same routed sublayer.

---

## Synthesis: How Prior Work Led to This Paper

Sparsely-gated mixtures of experts established token-wise conditional computation through a router that selects a small set of experts, grounding the idea that not all tokens need the same processing depth. GShard embedded this mechanism concretely into Transformer FFN sublayers, operationalizing routed FFN computation at scale. Switch Transformers demonstrated that top-1 routing yields large efficiency gains but revealed practical issues—uniform per-token FFN compute and token drops under capacity pressure. GLaM showed that using more than one expert per token improves quality-per-compute, yet still adheres to a fixed number of FFN evaluations per token. BASE Layers exposed how routing imbalance and capacity contention degrade utilization, proposing reassignment strategies to mitigate these effects. ST-MoE further refined routing choices to improve stability and capacity allocation across experts. In parallel, Universal Transformers introduced per-token halting via adaptive computation time, establishing that learned skip/early-exit decisions can judiciously reduce compute for easy inputs.
Together, these works suggested a clear opportunity: marry MoE routing with learned, token-level decisions about whether to compute at all. The natural synthesis is to expand the expert set beyond FFNs to include zero-computation actions—explicit skip (copy), discard (zero), or cheap replace (constant)—so routers can steer easy tokens away from scarce FFN capacity. This creates truly heterogeneous, input-adaptive compute within the MoE layer, concentrating expensive expert computation on hard tokens while preserving or improving overall performance and deployment efficiency.

---

*Analysis generated on: 2026-01-06T20:12:51.675472*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

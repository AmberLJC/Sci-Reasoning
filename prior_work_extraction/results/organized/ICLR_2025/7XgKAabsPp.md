# Prior Work Analysis Report

## Target Paper

**Title:** Theory on Mixture-of-Experts in Continual Learning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Hongbo Li, Sen Lin, Lingjie Duan, Yingbin Liang, Ness Shroff

**Keywords:** continual learning, mixture-of-experts, catastrophic forgetting, generalization error

**Abstract:** 
> Continual learning (CL) has garnered significant attention because of its ability to adapt to new tasks that arrive over time. Catastrophic forgetting (of old tasks) has been identified as a major issue in CL, as the model adapts to new tasks. The Mixture-of-Experts (MoE) model has recently been shown to effectively mitigate catastrophic forgetting in CL, by employing a gating network to sparsify and distribute diverse tasks among multiple experts. However, there is a lack of theoretical analysi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** (2017)
- *Authors:* Noam Shazeer et al.
- *Direct Connection:* Introduces the sparsely-gated MoE with a learned router and load-balancing auxiliary losses—the exact architectural mechanism whose expert specialization and routing behavior this work theoretically analyzes under continual learning.

**Surprises in High-Dimensional Ridgeless Least Squares: Double Descent and More** (2019)
- *Authors:* Trevor Hastie et al.
- *Direct Connection:* Provides the high-dimensional generalization framework for overparameterized linear regression and minimum-norm solutions that underpins the analytical lens used to derive MoE generalization and forgetting guarantees.

### 💡 Inspiration

**Expert Gate: Lifelong Learning with a Network of Experts** (2017)
- *Authors:* Rahaf Aljundi et al.
- *Direct Connection:* Demonstrates that gating inputs among task-specialized experts mitigates catastrophic forgetting in continual learning, providing the empirical mechanism that this work models and proves beneficial via expert diversification and routing.

### 🔍 Gap Identification

**Overcoming catastrophic forgetting in neural networks** (2017)
- *Authors:* James Kirkpatrick et al.
- *Direct Connection:* Identifies catastrophic forgetting and proposes parameter-importance regularization (EWC), whose limitations in mitigating cross-task interference motivate analyzing capacity-partitioning via MoE as a principled alternative.

### 🔧 Extension

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Direct Connection:* Formalizes top‑1 routing with an explicit load-balancing objective, directly motivating the analysis here of how a router both picks the correct expert per task and balances traffic across experts in a continual setting.

### 🔗 Related Problem

**Routing Networks: Adaptive Selection of Non-linear Functions for Multi-Task Learning** (2018)
- *Authors:* Clemens Rosenbaum et al.
- *Direct Connection:* Proposes a controller that adaptively selects experts per input/task, directly informing the router abstraction and specialization notion that are analyzed theoretically in the continual, overparameterized linear setting.

---

## Synthesis: How Prior Work Led to This Paper

Sparsely gated mixture-of-experts (MoE) introduced a learned router that activates a small subset of experts and includes explicit load-balancing terms, establishing a concrete mechanism for conditional computation and specialization (Shazeer et al.). Switch Transformers simplified this to top‑1 routing and sharpened the role of auxiliary load-balancing losses, clarifying how routing and balanced capacity usage emerge in practice (Fedus et al.). In continual learning, Expert Gate showed that allocating inputs to task-specific experts via a gate can prevent interference and reduce forgetting, offering an empirical template for expert specialization across tasks (Aljundi et al.). Routing Networks further generalized the idea of a controller selecting computation paths conditioned on inputs or tasks, emphasizing adaptive selection as the driver of specialization (Rosenbaum et al.). Parallelly, high-dimensional theory for ridgeless least squares characterized generalization in overparameterized linear regression via minimum-norm solutions, providing tools to analyze test error precisely (Hastie et al.). Finally, EWC framed catastrophic forgetting and highlighted the limits of regularization-based stability in the face of task interference (Kirkpatrick et al.). Together, these works reveal a gap: while gated experts appear to mitigate forgetting by specializing capacity and balancing usage, there was no theoretical account of how routing and diversification translate into generalization gains under task sequences. By marrying MoE routing/balancing insights with the precise overparameterized linear regression framework, the present work naturally emerges—proving that experts diversify to tasks, the router selects appropriately while balancing loads, and that this mechanism outperforms a single expert in continual learning.

---

*Analysis generated on: 2026-01-06T18:44:21.023171*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

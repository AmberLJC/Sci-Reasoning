# Prior Work Analysis Report

## Target Paper

**Title:** Knowledge Localization: Mission Not Accomplished? Enter Query Localization!

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yuheng Chen, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao

**Keywords:** Knowledge Neruon Thesis, Knowledge Localization, Query Localization

**Abstract:** 
> Large language models (LLMs) store extensive factual knowledge, but the mechanisms behind how they store and express this knowledge remain unclear.
The Knowledge Neuron (KN) thesis is a prominent theory for explaining these mechanisms. This theory is based on the **Knowledge Localization (KL)** assumption, which suggests that a fact can be localized to a few knowledge storage units, namely knowledge neurons.
 However, this assumption has two limitations: first, it may be too rigid  regarding kno...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Knowledge Neurons in Pretrained Transformers** (2022)
- *Authors:* Zhang et al.
- *Direct Connection:* This work formalized the Knowledge Localization assumption by proposing that specific facts are stored in a small set of "knowledge neurons," which the current paper re-examines and generalizes into the Query Localization assumption.

### 💡 Inspiration

**Transformer Feed-Forward Layers Are Key-Value Memories** (2021)
- *Authors:* Mor Geva et al.
- *Direct Connection:* By showing MLP layers implement key–value memories retrieved by inputs acting as queries, this paper provided the key mechanism that motivates reframing knowledge expression around query localization rather than neuron localization.

### 🔍 Gap Identification

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* By demonstrating that features are often stored in superposition across neurons, this work undermines strict neuron-level localization and motivates the paper’s finding that knowledge storage is more distributed than the KL assumption allows.

### 📊 Baseline

**Locating and Editing Factual Associations in GPT (ROME)** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* ROME operationalized localization by pinpointing and editing factual associations in specific MLP layers, a neuron/weight-centric premise that the present paper critiques as too rigid and incomplete without accounting for attention-driven expression.

**MEMIT: Mass-Editing Memory in a Transformer** (2023)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* MEMIT scaled localized fact editing across many facts under the same localization premise, providing a primary baseline whose limitations the new work addresses by shifting from storage localization to query-dependent expression.

### 🔗 Related Problem

**In-context Learning and Induction Heads** (2022)
- *Authors:* Catherine Olsson et al.
- *Direct Connection:* This study uncovered attention-head circuits where query–key interactions gate downstream computation, directly informing the claim that attention modules crucially control how stored knowledge is expressed.

---

## Synthesis: How Prior Work Led to This Paper

One line of research posited that facts can be pinpointed to a sparse set of internal units: Knowledge Neurons in Pretrained Transformers introduced a procedure and thesis that facts reside in small neuron sets, enabling causal interventions at the neuron level. Locating and Editing Factual Associations in GPT (ROME) made this actionable by identifying mid-layer MLP sites that store subject–relation associations and editing weights to alter specific facts. MEMIT extended this paradigm to large-scale, multi-fact editing, reinforcing the premise that localized parametric sites encode factual content. In contrast, Transformer Feed-Forward Layers Are Key-Value Memories showed that MLPs behave as key–value stores whose retrieval depends on input-derived queries, suggesting expression hinges on routing rather than purely on where facts are stored. Complementarily, In-context Learning and Induction Heads revealed attention circuits where query–key interactions gate downstream computations, highlighting attention’s central role in activating or suppressing stored content. Toy Models of Superposition further argued that features often inhabit superposed, distributed representations, challenging neuron-level exclusivity.
Together these works reveal a tension: neuron/weight localization methods succeed but assume rigid storage and overlook attention-mediated routing, while mechanistic studies emphasize query-driven retrieval and distributed storage. The current paper synthesizes these insights by reframing the core assumption from knowledge localization to query localization, presenting evidence that storage is more distributed than previously assumed and that attention (via queries) governs expression, thus explaining both the strengths and the failure modes of neuron- and layer-centric localization/editing approaches.

---

*Analysis generated on: 2026-01-06T18:30:18.946671*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

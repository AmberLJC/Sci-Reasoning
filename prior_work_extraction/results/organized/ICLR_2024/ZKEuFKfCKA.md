# Prior Work Analysis Report

## Target Paper

**Title:** A Lightweight Method for Tackling Unknown Participation Statistics in Federated Averaging

**Conference:** ICLR 2024 (spotlight)

**Authors:** Shiqiang Wang, Mingyue Ji

**Keywords:** federated learning, partial client participation, adaptation, aggregation weights

**Abstract:** 
> In federated learning (FL), clients usually have diverse participation statistics that are unknown a priori, which can significantly harm the performance of FL if not handled properly. Existing works aiming at addressing this problem are usually based on global variance reduction, which requires a substantial amount of additional memory in a multiplicative factor equal to the total number of clients. An important open problem is to find a lightweight method for FL in the presence of clients with...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Agnostic Federated Learning** (2019)
- *Authors:* Mehryar Mohri et al.
- *Direct Connection:* By formalizing client-weighted federated objectives and treating aggregation weights as optimization variables, AFL provides the conceptual foundation that aggregation weights determine the target objective—an insight this paper uses to seek ‘optimal’ weights under non-uniform participation.

### 🔍 Gap Identification

**SCAFFOLD: Stochastic Controlled Averaging for On-Device Federated Learning** (2020)
- *Authors:* Sai Praneeth Karimireddy et al.
- *Direct Connection:* SCAFFOLD addresses client-drift via global variance reduction using per-client control variates that require O(N) client-state memory at the server, a heavy footprint this paper explicitly avoids while targeting the same participation-induced bias.

**Federated Learning Based on Dynamic Regularization (FedDyn)** (2021)
- *Authors:* Dimitris A. Acar et al.
- *Direct Connection:* FedDyn mitigates drift by maintaining per-client dynamic regularizers stored at the server, and its O(N) auxiliary state motivates the paper’s lightweight alternative based on adaptive aggregation weights instead of global variance-reduction memory.

### 📊 Baseline

**Communication-Efficient Learning of Deep Networks from Decentralized Data** (2017)
- *Authors:* H. Brendan McMahan et al.
- *Direct Connection:* The proposed method directly modifies FedAvg’s aggregation step by replacing its fixed data-size weights with participation-history–adapted weights to prevent objective drift under heterogeneous client availability.

### 🔗 Related Problem

**Fair Resource Allocation in Federated Learning (q-FFL)** (2020)
- *Authors:* Tian Li et al.
- *Direct Connection:* q-FFL operationalizes client reweighting in aggregation to achieve a desired objective (fairness), demonstrating that principled, goal-driven aggregation weights can be designed—an idea paralleled here for correcting participation-induced bias.

**Asynchronous Federated Optimization** (2019)
- *Authors:* Chenliang Xie et al.
- *Direct Connection:* Asynchronous FL weights client updates by staleness using simple history-based rules to counter sampling/recency bias, directly informing the paper’s use of participation history to compute debiasing aggregation weights.

---

## Synthesis: How Prior Work Led to This Paper

FedAvg introduced the canonical partial-participation training loop with data-size–proportional aggregation, implicitly defining how client sampling and aggregation interact in practice. SCAFFOLD later showed that client-drift from intermittent participation and non-IID data can be countered by global variance reduction using client-specific control variates, but at the cost of maintaining an O(N) set of client states. FedDyn pursued the same drift-mitigation goal by storing per-client dynamic regularizers on the server, again incurring O(N) memory. Agnostic Federated Learning established that the choice of aggregation weights defines the effective optimization objective and can be treated as an explicit decision variable. q-FFL further demonstrated that reweighting clients in the aggregation step can deliberately bias optimization toward a target (fairness), providing a concrete recipe for designing weights to achieve a specified objective. In parallel, asynchronous FL showed that simple history-based server weights (e.g., staleness-aware) can effectively correct sampling-induced biases without heavy auxiliary state.
Together, these works reveal a gap: strong drift-correction via global variance reduction exists but is memory-heavy, while weight-design frameworks and history-based debiasing show that aggregation weights can realign training objectives at low cost. The present paper synthesizes these insights by proving that heterogeneous participation skews FedAvg away from the original objective and then using participation history to estimate sampling probabilities and adapt aggregation weights accordingly. This yields a lightweight, memory-efficient alternative that preserves the intended federated objective under unknown, non-uniform client availability.

---

*Analysis generated on: 2026-01-06T13:20:11.071655*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

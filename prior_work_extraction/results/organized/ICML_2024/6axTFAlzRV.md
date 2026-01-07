# Prior Work Analysis Report

## Target Paper
**Title:** 6axTFAlzRV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Communication-Efficient Learning of Deep Networks from Decentralized Data** (2017)
- *Authors:* H. Brendan McMahan et al.
- *Connection:* FedLESAM is built on the standard FedAvg federated learning protocol (multi-step local updates followed by global averaging), and its global-perturbation estimate is computed from consecutive global models produced by FedAvg-style aggregation.

**Averaging Weights Leads to Wider Optima in Deep Learning** (2018)
- *Authors:* Pavel Izmailov et al.
- *Connection:* This work established the generalization benefits of flatter minima, providing the flatness motivation that SAM operationalizes and that FedLESAM seeks to target specifically at the global (not merely local) loss landscape in FL.

### 💡 Inspiration

**Adaptive Federated Optimization** (2021)
- *Authors:* Sashank J. Reddi et al.
- *Connection:* FedLESAM’s key idea—using differences between consecutive global models as a proxy for a global descent signal—echoes FedAdam’s use of aggregated model deltas to approximate global gradients, motivating FedLESAM’s use of global-model differences to steer perturbations.

### 🔍 Gap Identification

**Federated Optimization in Heterogeneous Networks (FedProx)** (2020)
- *Authors:* Tian Li et al.
- *Connection:* FedProx formalized the objective inconsistency caused by client heterogeneity, a core limitation that underlies why locally computed SAM perturbations can misalign with the global landscape—precisely the mismatch FedLESAM addresses.

### 🔧 Extension

**Sharpness-Aware Minimization for Efficiently Improving Generalization** (2021)
- *Authors:* Pierre Foret et al.
- *Connection:* FedLESAM directly modifies SAM’s perturb-then-descend procedure by replacing the locally computed perturbation direction with a locally estimated global direction, preserving SAM’s min–max objective while altering how the perturbation vector is obtained.

### 🔗 Related Problem

**SCAFFOLD: Stochastic Controlled Averaging for Federated Learning** (2020)
- *Authors:* Sai Praneeth Karimireddy et al.
- *Connection:* SCAFFOLD’s control variates explicitly correct client drift by injecting an estimate of the global-gradient signal into local updates; FedLESAM applies the same principle to the SAM perturbation step by aligning perturbations with an estimated global direction.

---

## Synthesis

FedLESAM sits at the intersection of federated optimization and sharpness-aware training. The conceptual motivation for pursuing flat minima comes from the flatness–generalization link demonstrated by Averaging Weights Leads to Wider Optima, which SAM later operationalized via perturb-then-descend updates. However, standard federated learning is conducted under the FedAvg paradigm, whose multi-step local updates and aggregation create a global model sequence; under heterogeneity, this induces objective inconsistency, a gap formalized by FedProx. That gap explains why naively applying SAM locally can be misaligned: local sharpness need not reflect the global landscape relevant to the aggregated model. Prior algorithms such as SCAFFOLD showed that injecting an estimate of the global gradient into local updates can correct drift, highlighting the value of aligning local computation with global signals. Adaptive Federated Optimization (FedAdam/FedYogi) provided a concrete mechanism: treat consecutive global model differences as a proxy for the global gradient. FedLESAM fuses these threads by modifying SAM’s perturbation step—replacing the locally computed direction with a client-side estimate of the global perturbation direction computed from consecutive global models. This directly targets global flatness, mitigating heterogeneity-induced misalignment, and, by fixing the perturbation direction, reduces SAM’s two-backprop overhead to a single backprop per iteration.

---
*Generated: 2026-01-06T23:09:26.486565*

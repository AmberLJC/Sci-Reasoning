# Prior Work Analysis Report

## Target Paper
**Title:** h1iMVi2iEM
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

A-FedPD’s core contribution is to diagnose and fix a previously underexplored failure mode in federated primal-dual learning: dual drift caused by partial client participation. Foundationally, FedAvg established the partial participation setting and revealed how infrequent client engagement leads to stale states and drift. Follow-up stabilization methods such as FedProx and SCAFFOLD demonstrated that maintaining auxiliary correction mechanisms (proximal regularization and control variates) can effectively counter client drift, providing a template for how corrective state can be maintained across rounds. In parallel, primal-dual frameworks like ADMM and the CoCoA family grounded the consensus formulation of distributed learning in Lagrangian terms, with explicit dual variables coordinating local models to a shared global solution. These works clarify the central role of dual variables in enforcing consensus and the sensitivity of convergence to the currency of those dual updates. Analyses of local updates under sparse communication, such as Local SGD, sharpened the understanding of how staleness accumulates between synchronizations. Drift-correction techniques like FedDyn then reinforced that drift can be mitigated by algorithmically maintaining alignment even when participation is intermittent. A-FedPD synthesizes these strands by moving the correction mechanism to the dual layer: it constructs virtual dual updates that keep inactive clients’ dual variables aligned with the global consensus, thereby eliminating dual hysteresis without requiring their participation. This principled dual-space alignment closes a key gap left by prior primal-only stabilization approaches.

---
*Generated: 2026-01-06T23:33:35.560930*

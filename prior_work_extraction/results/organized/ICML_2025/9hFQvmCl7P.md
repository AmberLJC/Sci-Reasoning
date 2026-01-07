# Prior Work Analysis Report

## Target Paper
**Title:** 9hFQvmCl7P
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

FedSSI’s core contribution—rehearsal-free continual federated learning that remains robust under non-IID client distributions—emerges at the intersection of rehearsal-free continual learning and heterogeneity-aware federated optimization. Synaptic Intelligence (Zenke et al., 2017) is the central intellectual foundation, providing a path-integral estimate of parameter importance to regularize updates without storing past samples. Elastic Weight Consolidation (Kirkpatrick et al., 2017) and Memory Aware Synapses (Aljundi et al., 2018) establish the broader regularization paradigm that protects important parameters across tasks, and they serve as key points of comparison when adapting such methods to the federated setting. Learning without Forgetting (Li & Hoiem, 2016) reinforces the rehearsal-free objective—preserving prior knowledge without caching data—aligning with privacy and memory constraints in CFL.
On the federated side, FedAvg (McMahan et al., 2017) provides the basic aggregation mechanism and practical substrate on which FedSSI operates. However, the principal challenge addressed by FedSSI is non-IID heterogeneity, where standard SI degrades. FedProx (Li et al., 2020) and SCAFFOLD (Karimireddy et al., 2020) contribute essential insights into stabilizing local training and mitigating client drift. FedSSI synthesizes these lines by making synaptic-importance estimates compatible with federated aggregation and by using them to constrain local updates in a heterogeneity-aware manner. This synergy preserves past knowledge across evolving client streams without rehearsal, achieving continual learning goals while respecting FL’s privacy and resource constraints.

---
*Generated: 2026-01-07T00:21:32.401986*

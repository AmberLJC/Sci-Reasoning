# Prior Work Analysis Report

## Target Paper

**Title:** A Mutual Information Perspective on Federated Contrastive Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Christos Louizos, Matthias Reisser, Denis Korzhenkov

**Keywords:** federated learning, contrastive learning, self-supervised, semi-supervised, mutual information

**Abstract:** 
> We investigate contrastive learning in the federated setting through the lens of Sim- CLR and multi-view mutual information maximization. In doing so, we uncover a connection between contrastive representation learning and user verification; by adding a user verification loss to each client’s local SimCLR loss we recover a lower bound to the global multi-view mutual information. To accommodate for the case of when some labelled data are available at the clients, we extend our SimCLR variant to t...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Representation Learning with Contrastive Predictive Coding** (2018)
- *Authors:* Aaron van den Oord et al.
- *Direct Connection:* CPC’s InfoNCE objective provides the mutual-information lower bound framework that the paper leverages to formally connect the augmented SimCLR + user-verification loss to a bound on global multi-view mutual information.

**On Variational Bounds of Mutual Information** (2019)
- *Authors:* Ben Poole et al.
- *Direct Connection:* This work’s unifying treatment of MI lower bounds (including InfoNCE) underpins the paper’s derivation that combining local contrastive terms with user verification recovers a valid global multi-view MI bound.

**Communication-Efficient Learning of Deep Networks from Decentralized Data** (2017)
- *Authors:* H. Brendan McMahan et al.
- *Direct Connection:* This work defines the federated learning setup and aggregation protocol on which the paper’s federated SimCLR and user-verification objectives are instantiated and evaluated.

### 💡 Inspiration

**Contrastive Multiview Coding** (2020)
- *Authors:* Yonglong Tian et al.
- *Direct Connection:* CMC’s view that contrastive learning maximizes mutual information across multiple views directly motivates framing federated clients/views under a global multi-view MI objective.

### 🔍 Gap Identification

**Model-Contrastive Federated Learning** (2021)
- *Authors:* Qinbin Li et al.
- *Direct Connection:* MOON’s observation that non-i.i.d. data degrades federated contrastive learning motivates the paper’s MI-based objective and analysis, replacing heuristic model-level contrast with a principled global MI perspective.

### 📊 Baseline

**A Simple Framework for Contrastive Learning of Visual Representations** (2020)
- *Authors:* Ting Chen et al.
- *Direct Connection:* The paper adopts SimCLR’s instance-discrimination contrastive loss as the local client objective and then augments it with a user-verification term, showing this combination yields a lower bound to a global multi-view mutual information.

### 🔧 Extension

**Supervised Contrastive Learning** (2020)
- *Authors:* Prannay Khosla et al.
- *Direct Connection:* The paper extends SimCLR to the federated semi-supervised setting by adopting SupCon’s key idea—treat same-label samples as positives—and by adding an auxiliary label-prediction head.

---

## Synthesis: How Prior Work Led to This Paper

SimCLR showed that instance-discrimination with augmentations and a temperature-scaled softmax contrastive loss can learn strong representations, establishing a practical contrastive objective widely adopted in vision. Contrastive Predictive Coding formalized the InfoNCE objective as a tractable lower bound on mutual information, casting contrastive learning as MI maximization via a noise-contrastive classification task. Poole et al. unified variational MI bounds, clarifying when InfoNCE-type objectives constitute valid MI lower bounds and how combining or reweighting terms affects bound properties. Contrastive Multiview Coding emphasized that maximizing mutual information across multiple views is key to representation quality, framing contrast as multiview MI maximization rather than mere instance pairing. Supervised Contrastive Learning demonstrated that using same-label examples as positives and coupling contrastive learning with a classification head yields stronger supervised/semi-supervised representations. Federated learning, formalized by FedAvg, enables decentralized training under client heterogeneity, while MOON highlighted that non-i.i.d. data induces representational drift and proposed a contrastive alignment between local and global models to mitigate it.
Building on these insights, a clear gap emerged: federated contrastive methods lacked a principled connection between local objectives and a global representation criterion under client heterogeneity. By viewing clients as views and leveraging InfoNCE/variational MI theory, it becomes natural to add a user-verification objective that ties client identity to representations, thereby recovering a lower bound to global multiview mutual information. The supervised contrastive recipe provides a direct path to a federated semi-supervised variant via same-label positives and an auxiliary label head, while MOON’s non-i.i.d. findings motivate analyzing how heterogeneity impacts global MI. Within the FedAvg framework, this synthesis yields a theoretically grounded, federated SimCLR extension.

---

*Analysis generated on: 2026-01-06T15:33:24.783612*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** CLAP: Collaborative Adaptation for Patchwork Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Sen Cui, Abudukelimu Wuerkaixi, Weishen Pan, Jian Liang, Lei Fang, Changshui Zhang, Fei Wang

**Keywords:** Patchwork learning, robustness

**Abstract:** 
> In this paper, we investigate a new practical learning scenario, where the data distributed in different sources/clients are typically generated with various modalities. Existing research on learning from multi-source data mostly assume that each client owns the data of all modalities, which may largely limit its practicability. In light of the expensiveness and sparsity of multimodal data, we propose patchwork learning to jointly learn from fragmented multimodal data in distributed clients. Con...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Communication-Efficient Learning of Deep Networks from Decentralized Data** (2017)
- *Authors:* McMahan et al.
- *Direct Connection:* CLAP operates under the privacy-preserving federated learning setup introduced by FedAvg and builds its collaborative adaptation and imputation protocol atop the standard federated aggregation loop.

**Multimodal Generative Models for Scalable Weakly-Supervised Learning** (2018)
- *Authors:* Wu et al.
- *Direct Connection:* CLAP’s cross-modal imputation mechanism is grounded in the MVAE/Product-of-Experts idea from Wu & Goodman, using observed modalities to infer missing ones via a shared latent space.

### 💡 Inspiration

**Federated Learning with Personalization Layers** (2019)
- *Authors:* Arivazhagan et al.
- *Direct Connection:* CLAP adopts the parameter decoupling principle of FedPer—separating shared global parameters from client-specific adapters—to enable collaborative adaptation of multimodal imputation across heterogeneous modality combinations.

### 🔍 Gap Identification

**Federated Optimization in Heterogeneous Networks (FedProx)** (2020)
- *Authors:* Li et al.
- *Direct Connection:* CLAP addresses the client-drift under non-i.i.d. data highlighted by FedProx, but does so by aligning cross-client conditional dependencies for multimodal imputation rather than relying solely on a proximal regularizer.

**Model-Contrastive Federated Learning** (2021)
- *Authors:* Li et al.
- *Direct Connection:* CLAP borrows the core insight of representation alignment from MOON to combat heterogeneity, re-purposing it to collaboratively align multimodal imputation models across clients with different modality mixes.

**FedBN: Federated Learning on Non-IID Features via Local Batch Normalization** (2021)
- *Authors:* Li et al.
- *Direct Connection:* CLAP leverages FedBN’s insight that client-specific statistics should be preserved by keeping client-specific components when fusing imputation models, mitigating feature-distribution shifts across clients.

### 📊 Baseline

**Generalized Multimodal ELBO** (2021)
- *Authors:* Sutter et al.
- *Direct Connection:* CLAP directly extends MoPoE-VAE’s arbitrary-subset inference by coordinating modality experts across clients and tackling modality-combination heterogeneity that MoPoE handles only in a centralized, i.i.d. setting.

---

## Synthesis: How Prior Work Led to This Paper

Federated learning formalized a privacy-preserving collaboration protocol in which clients improve a shared model without exposing raw data, establishing the aggregation loop later methods refine. In parallel, multimodal generative modeling advanced practical imputation: MVAE introduced product-of-experts inference to reconstruct missing modalities from observed ones via a shared latent space, and MoPoE-VAE generalized the evidence bound to support arbitrary subsets of modalities, making cross-modal completion scalable and flexible in centralized settings. Yet, federated deployments face severe heterogeneity; FedProx exposed how client drift degrades aggregation under non-i.i.d. data, while MOON showed that aligning representations across local and global models can stabilize learning. FedBN further demonstrated the value of preserving client-specific normalization statistics to handle feature shifts. Finally, FedPer proposed splitting models into global and personalized parts, showing that decoupling shared knowledge from client-specific adaptations can better accommodate heterogeneity. Together, these threads revealed an opportunity: centralized multimodal imputation methods effectively handle missing modalities but assume i.i.d. data and unified training, whereas federated optimization methods address heterogeneity but do not transfer cross-modal dependencies. The natural next step is to synthesize arbitrary-subset multimodal inference with federated personalization and alignment: coordinate modality experts across clients, preserve client-specific components where distributions differ, and explicitly align conditional dependencies to combat drift. CLAP crystallizes this by extending PoE-style imputation into a collaborative federated regime with decoupled shared/personalized parameters and alignment mechanisms tailored to modality-combination heterogeneity.

---

*Analysis generated on: 2026-01-07T00:23:10.269824*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

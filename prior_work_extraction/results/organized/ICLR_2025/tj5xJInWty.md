# Prior Work Analysis Report

## Target Paper

**Title:** Temporal Heterogeneous Graph Generation with Privacy, Utility, and Efficiency

**Conference:** ICLR 2025 (spotlight)

**Authors:** Xinyu He, Dongqi Fu, Hanghang Tong, Ross Maciejewski, Jingrui He

**Keywords:** Temporal Graph, Heterogeneous Graph, Graph Generation

**Abstract:** 
> Nowadays, temporal heterogeneous graphs attract much research and industrial attention for building the next-generation Relational Deep Learning models and applications, due to their informative structures and features. While providing timely and precise services like personalized recommendations and question answering, this rich information also introduces extra exposure risk for each node in the graph. The distinctive local topology, the abundant heterogeneous features, and the time dimension ...

---

## Key Prior Works (8 papers with direct influence)

### 🏗️ Foundation

**DyRep: Learning Representations over Dynamic Graphs** (2019)
- *Authors:* Rakshit Trivedi et al.
- *Direct Connection:* DyRep’s continuous-time relational event modeling (via conditional intensities for typed interactions) underpins the temporal edge-generation mechanism that THePUff adapts to synthesize time-stamped, relation-typed edges.

**PrivBayes: Private Data Release via Bayesian Networks** (2014)
- *Authors:* Jun Zhang et al.
- *Direct Connection:* PrivBayes established the perturb-then-synthesize pipeline for DP data generation, which THePUff generalizes from tabular Bayesian networks to temporal heterogeneous graph synthesis.

**Differentially Private Exponential Random Graph Estimation** (2016)
- *Authors:* Krishna Karwa and Aleksandra B. Slavković
- *Direct Connection:* This work formalized edge-level randomized response mechanisms for networks, which THePUff extends to a DP perturbation tailored to time-stamped, relation-typed edges with temporal composition.

**Mining Heterogeneous Information Networks: Principles and Methodologies** (2012)
- *Authors:* Yizhou Sun and Jiawei Han
- *Direct Connection:* This monograph defined the heterogeneous information network formalism (typed nodes/edges and meta-relations) that THePUff adopts as the core problem setting for heterogeneous temporal graph generation.

### 💡 Inspiration

**PATE-GAN: Generating Synthetic Data with Differential Privacy** (2018)
- *Authors:* Graham J. G. Jordon et al.
- *Direct Connection:* PATE-GAN’s idea of combining a privatized view with limited guidance derived from original data motivates THePUff’s use of both a differentially perturbed graph and original signals to boost utility under DP.

### 📊 Baseline

**GraphRNN: Generating Realistic Graphs with Deep Auto-regressive Models** (2018)
- *Authors:* Jiaxuan You et al.
- *Direct Connection:* This work is the main static graph-generation baseline whose sequential structure modeling THePUff must outperform and generalize beyond to handle temporal, heterogeneous graphs efficiently.

**NetGAN: Generating Graphs via Random Walks** (2018)
- *Authors:* Aleksandar Bojchevski et al.
- *Direct Connection:* NetGAN’s random-walk-based synthesis is a primary comparator that THePUff directly improves upon by moving from static homogeneous generation to privacy-preserving temporal heterogeneous graph generation.

### 🔗 Related Problem

**Temporal Graph Networks for Deep Learning on Dynamic Graphs** (2020)
- *Authors:* Emanuele Rossi et al.
- *Direct Connection:* TGN introduced history-aware temporal message passing that THePUff leverages conceptually to encode temporal contexts when parameterizing its generative process for dynamic, typed interactions.

---

## Synthesis: How Prior Work Led to This Paper

Autoregressive graph generators like GraphRNN demonstrated how to synthesize realistic structures by sequentially adding nodes and edges, while NetGAN showed that random-walk distributions can drive plausible edge sampling, establishing strong but static, homogeneous baselines. DyRep introduced continuous-time relational event modeling with conditional intensities over node embeddings to capture when and which typed interactions occur, and Temporal Graph Networks contributed history-aware message passing with temporal memory to encode evolving contexts for dynamic edges. In the privacy domain, PrivBayes pioneered a perturb-then-synthesize pipeline that achieves differential privacy by first privatizing sufficient statistics before training a generator, and PATE-GAN revealed how privatized supervision can be combined with limited information from original data through teacher–student transfer to reclaim utility under DP. For graph-specific privacy, Karwa and Slavković formalized network-relevant randomized response and edge-DP machinery, while the heterogeneous information network framework of Sun and Han established the schema-level formalism for typed nodes, edges, and meta-relations.
Bringing these strands together reveals a gap: existing generators lack temporality and heterogeneity, DP graph methods target static homogeneous settings, and DP synthetic data techniques don’t capture relational-temporal dependencies. The natural next step is a DP mechanism that perturbs time-stamped, relation-typed edges with proper temporal composition, coupled with a continuous-time, history-aware generator that models typed interactions. By combining a privatized graph view with carefully constrained original-data guidance, one can recover utility and scalability, yielding an efficient, privacy-preserving generator for temporal heterogeneous graphs.

---

*Analysis generated on: 2026-01-06T11:34:59.893689*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

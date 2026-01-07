# Prior Work Analysis Report

## Target Paper
**Title:** fCPB0qRJT2
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**GraphNAS: Graph Neural Architecture Search with Reinforcement Learning** (2020)
- *Authors:* Gao et al.
- *Connection:* GraphNAS established the problem and mechanisms of neural architecture search tailored to GNNs; AutoGFM extends this line by bringing GNAS into the foundation-model setting and across multiple domains/tasks.

**GPT-GNN: Generative Pre-Training of Graph Neural Networks** (2020)
- *Authors:* Hu et al.
- *Connection:* GPT-GNN introduced large-scale pretraining for graphs (a precursor to GFMs) but relied on fixed backbones; AutoGFM inherits the pretraining paradigm while replacing hand-crafted, fixed architectures with automated, adaptive ones.

### 💡 Inspiration

**Invariant Risk Minimization** (2020)
- *Authors:* Arjovsky et al.
- *Connection:* IRM’s principle of learning invariant mechanisms across environments inspires AutoGFM’s discovery of an invariant graph–architecture relationship shared across diverse domains and tasks.

### 🔍 Gap Identification

**Design Space for Graph Neural Networks** (2020)
- *Authors:* You et al.
- *Connection:* This work systematically showed that the best-performing GNN design choices vary widely across datasets and tasks, directly motivating AutoGFM’s focus on resolving architecture inconsistency across domains.

### 📊 Baseline

**GraphMAE: Masked Autoencoders for Graphs** (2022)
- *Authors:* Hou et al.
- *Connection:* GraphMAE is a strong pretraining baseline built on a fixed GNN backbone; AutoGFM targets the core limitation by searching and customizing the backbone architecture per domain/task to surpass fixed-design GFMs.

### 🔧 Extension

**FairNAS: Rethinking Evaluation Fairness of Weight Sharing Neural Architecture Search** (2021)
- *Authors:* Chu et al.
- *Connection:* FairNAS identified and mitigated training bias in weight-sharing NAS; AutoGFM adapts fairness-aware sampling/optimization ideas to counter the data domination phenomenon during multi-domain architecture search.

### 🔗 Related Problem

**Graph Prompt Learning for Node Classification** (2023)
- *Authors:* Liu et al.
- *Connection:* Prompt-based graph adaptation keeps the backbone fixed; AutoGFM complements and goes beyond this by adapting the architecture itself, addressing cases where prompts alone cannot resolve backbone mismatch across domains.

---

## Synthesis

AutoGFM’s central idea—automatically customizing graph backbones for a graph foundation model across diverse domains—sits at the intersection of GNN design, pretraining, and architecture search. The evidence for the need to adapt architectures comes from You et al., who demonstrated that optimal GNN design choices vary markedly across datasets, revealing the architecture inconsistency that AutoGFM targets. On the mechanism side, GraphNAS established GNN-specific NAS, which AutoGFM advances by scaling NAS into a foundation-model setting that must serve many domains and tasks. The GFM/pretraining lineage is anchored by GPT-GNN and strong pretraining baselines like GraphMAE: both validate the efficacy of large-scale graph pretraining yet rely on fixed, hand-crafted backbones—exactly the constraint that AutoGFM removes via automated, task/domain-aware customization. While prompt-based adaptation methods (e.g., Graph Prompt Learning) show that non-architectural adaptation can transfer knowledge across tasks, their fixed backbones leave performance on mismatched domains capped; AutoGFM complements this by adapting the architecture itself. To make adaptation stable across domains, AutoGFM draws inspiration from IRM, seeking invariant graph–architecture relations that generalize across environments. Finally, because weight-sharing NAS can be biased, FairNAS’s fairness-aware training informs AutoGFM’s strategy to mitigate data domination during multi-domain supernet training, ensuring balanced optimization of candidate architectures.

---
*Generated: 2026-01-06T23:07:19.638606*

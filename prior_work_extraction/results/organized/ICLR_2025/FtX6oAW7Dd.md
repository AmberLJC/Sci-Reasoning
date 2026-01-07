# Prior Work Analysis Report

## Target Paper

**Title:** Realistic Evaluation of Deep Partial-Label Learning Algorithms

**Conference:** ICLR 2025 (spotlight)

**Authors:** Wei Wang, Dong-Dong Wu, Jindong Wang, Gang Niu, Min-Ling Zhang, Masashi Sugiyama

**Keywords:** Partial-label learning, weakly supervised learning, benchmark.

**Abstract:** 
> Partial-label learning (PLL) is a weakly supervised learning problem in which
each example is associated with multiple candidate labels and only one is the
true label. In recent years, many deep PLL algorithms have been developed to
improve model performance. However, we find that some early developed
algorithms are often underestimated and can outperform many later algorithms
with complicated designs. In this paper, we delve into the empirical
perspective of PLL and identify several critical bu...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning from Partial Labels** (2011)
- *Authors:* T. Cour et al.
- *Direct Connection:* This work formalized the partial-label learning setting (each instance has a candidate set with a single unknown true label), providing the core problem formulation and evaluation paradigm that PLENCH standardizes and stress-tests.

**Solving the Partial Label Learning Problem: An Instance-based Approach** (2015)
- *Authors:* Min-Ling Zhang et al.
- *Direct Connection:* This classic instance-based disambiguation line established widely used protocols and real-world PLL datasets/practices that later deep works inherited—limitations of which (small, outdated images and ad-hoc evaluation) PLENCH explicitly revisits.

**Risk-consistent Partial-Label Learning** (2020)
- *Authors:* Y. Feng et al.
- *Direct Connection:* By introducing risk-consistent objectives for PLL and highlighting sensitivity to learning choices, this paper exposed evaluation and tuning ambiguities that PLENCH systematizes with unified metrics and selection criteria.

### 🔍 Gap Identification

**Self-Paced Partial-Label Learning** (2020)
- *Authors:* J. Feng et al.
- *Direct Connection:* This method’s curriculum-style disambiguation relied on ad-hoc early stopping and tuning under partial labels, illustrating the non-trivial model selection issue that PLENCH isolates and addresses with a principled selection strategy.

### 📊 Baseline

**PRODEN: Progressive Identification of True Labels for Partial-Label Learning** (2020)
- *Authors:* X. Yi et al.
- *Direct Connection:* As a seminal deep PLL method that iteratively refines soft label assignments, PRODEN is a primary baseline whose reported performance varied across papers due to inconsistent setups, directly motivating PLENCH’s standardized training and model-selection protocol.

**PiCO: Contrastive Label Disambiguation for Partial Label Learning** (2021)
- *Authors:* H. Wang et al.
- *Direct Connection:* PiCO’s contrastive representation and pseudo-labeling pipeline became a flagship deep PLL baseline whose training tricks, synthetic-label protocols, and validation heuristics vary across works—precisely the inconsistencies PLENCH controls for.

---

## Synthesis: How Prior Work Led to This Paper

Partial-label learning was crystallized by Cour et al., who defined the setting where each example comes with multiple candidate labels but only one is correct; their formulation and evaluation approach underpins all subsequent work. Zhang et al. advanced instance-based disambiguation and popularized practical PLL datasets and protocols, but these early resources were small and not aligned with modern deep models. With deep learning, PRODEN introduced progressive soft-label refinement, becoming a central baseline but also revealing that performance is sensitive to training details. Risk-consistent PLL formalized principled objectives, underscoring how choices in losses and optimizers impact validity, yet it left open how to compare methods fairly across heterogeneous setups. PiCO integrated contrastive learning with label disambiguation, adding stronger representation learning but with diverse training tricks and synthetic candidate-generation schemes across papers. Self-Paced PLL demonstrated curriculum strategies for resolving ambiguity but depended on heuristic model selection and early stopping under weak supervision.
Together these works established both the modern algorithmic toolkit and the pain points: heterogeneous synthetic protocols, legacy real-world datasets ill-suited to deep backbones, and ad-hoc model selection that confounds comparisons. PLENCH emerges naturally from this landscape by standardizing candidate-label generation, assembling real-world image datasets compatible with contemporary architectures, and instituting a principled, unified model-selection and evaluation protocol—thereby revealing true relative performance (including the strength of earlier methods) under realistic, controlled conditions.

---

*Analysis generated on: 2026-01-06T18:37:12.672668*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

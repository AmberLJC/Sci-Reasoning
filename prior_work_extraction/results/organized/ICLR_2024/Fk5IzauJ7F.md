# Prior Work Analysis Report

## Target Paper

**Title:** Candidate Label Set Pruning: A Data-centric Perspective for Deep Partial-label Learning

**Conference:** ICLR 2024 (oral)

**Authors:** Shuo He, Chaojie Wang, Guowu Yang, Lei Feng

**Keywords:** partial label learning, label disambiguation, candidate label set pruning

**Abstract:** 
> Partial-label learning (PLL) allows each training example to be equipped with a set of candidate labels. Existing deep PLL research focuses on a \emph{learning-centric} perspective to design various training strategies for label disambiguation i.e., identifying the concealed true label from the candidate label set, for model training. However, when the size of the candidate label set becomes excessively large, these learning-centric strategies would be unable to find the true label for model tra...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Learning from Partial Labels** (2011)
- *Authors:* Cour et al.
- *Direct Connection:* This work formalized the partial-label learning setting where each instance has a candidate label set, providing the problem formulation that CLSP explicitly operates on by pruning candidate labels.

### 💡 Inspiration

**PiCO: Contrastive Label Disambiguation for Partial Label Learning** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* PiCO’s core insight that representation-space neighborhood structure encodes label information directly inspires CLSP’s training-free use of representation–candidate set consistency to filter implausible candidate labels.

**Confident Learning: Estimating Uncertainty in Dataset Labels** (2021)
- *Authors:* Northcutt et al.
- *Direct Connection:* This data-centric approach to identify and prune label errors directly inspires CLSP’s training-free philosophy, adapting label error detection to the PLL setting at the candidate-label level using feature–label inconsistency.

### 🔍 Gap Identification

**Provably Consistent Partial-Label Learning** (2020)
- *Authors:* Feng et al.
- *Direct Connection:* By formalizing identifiability conditions and showing learning-centric PLL can fail when ambiguity is high, this work motivates CLSP’s data-centric pruning to reduce ambiguity before learning.

### 📊 Baseline

**Progressive Identification of True Labels for Partial-Label Learning (PRODEN)** (2020)
- *Authors:* Lv et al.
- *Direct Connection:* As a leading deep PLL method that progressively disambiguates labels during training, it serves as a principal baseline whose performance degrades with large candidate sets—exactly the failure mode CLSP is designed to mitigate via pre-training pruning.

### 🔧 Extension

**IDGP: Instance-Dependent Graph Propagation for Deep Partial-Label Learning** (2021)
- *Authors:* Feng et al.
- *Direct Connection:* IDGP leverages instance-similarity graphs to propagate label confidences, and CLSP extends this neighbor-consistency principle by converting it into a training-free criterion for pruning candidate labels instead of learning weights.

---

## Synthesis: How Prior Work Led to This Paper

Partial-label learning was formalized by Cour et al., who introduced the setting where each instance is associated with a candidate label set that contains the true class, anchoring subsequent methods to reason over candidate labels. PRODEN advanced deep PLL by progressively identifying true labels through iterative risk minimization and pseudo-label refinement, but its reliance on training-time disambiguation makes it sensitive to large candidate sets. PiCO revealed that representation-space neighborhoods provide strong supervisory signals: contrastive learning can cluster same-class instances and help disambiguate candidates via feature similarity. IDGP encoded this neighbor-agreement prior explicitly using an instance-similarity graph to propagate label confidences, showing that graph-based representation consistency can refine ambiguous labels. Feng et al. further provided identifiability guarantees and clarified when learning-centric strategies break down under heavy ambiguity, delineating the limits of disambiguation-only pipelines. In parallel, Confident Learning demonstrated a data-centric, training-free paradigm to detect and prune label errors by exploiting prediction-driven label–data inconsistencies.
Together, these works expose a gap: when candidate sets are large, learning-centric disambiguation struggles, yet representation neighborhoods and data-centric cleaning offer reliable signals. The current paper synthesizes these insights by introducing candidate label set pruning as a training-free pre-processing step that measures inconsistency between representation space and candidate label space, filtering implausible candidates to reduce ambiguity and bolster downstream deep PLL methods like PRODEN and PiCO.

---

*Analysis generated on: 2026-01-06T17:30:04.582356*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

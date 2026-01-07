# Prior Work Analysis Report

## Target Paper
**Title:** sBJNokmYuV
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Learning Transferable Visual Models From Natural Language Supervision** (2021)
- *Authors:* Alec Radford et al.
- *Connection:* CPL builds directly on CLIP’s zero-shot formulation—using class-name prompts and image–text similarity scores as a confidence score matrix from which its intra-/inter-instance candidate pseudolabels are generated.

**Learning to Prompt for Vision-Language Models** (2022)
- *Authors:* Kaiyang Zhou et al.
- *Connection:* CPL adopts the CoOp-style learnable prompt parameterization for CLIP and replaces supervised targets with unlabeled, candidate pseudolabel–based supervision to drive prompt tuning.

**Pseudo-Label: The Simple and Efficient Semi-Supervised Learning Method for Deep Neural Networks** (2013)
- *Authors:* Dong-Hyun Lee
- *Connection:* CPL generalizes the classic pseudolabeling idea by moving from a single hard label to a dynamically refined candidate label set to mitigate early-stage pseudolabel errors.

### 💡 Inspiration

**ReMixMatch: Semi-Supervised Learning with Distribution Alignment and Augmentation Anchoring** (2020)
- *Authors:* David Berthelot et al.
- *Connection:* CPL’s inter-instance selection explicitly seeks class-balanced instance selection across unlabeled data, echoing ReMixMatch’s distribution alignment idea and adapting it to VLM prompt tuning via a global confidence matrix.

### 📊 Baseline

**FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence** (2020)
- *Authors:* Kihyuk Sohn et al.
- *Connection:* CPL targets the well-known failure mode of hard, confidence-thresholded pseudolabels used in FixMatch-like pipelines, replacing them with progressively refined candidate sets to remain reliable when zero-shot accuracy is low.

### 🔧 Extension

**Progressive Identification of True Labels for Partial-Label Learning (PRODEN)** (2020)
- *Authors:* Jiaqi Lv et al.
- *Connection:* CPL extends PRODEN’s progressive disambiguation principle to the VLM setting by iteratively refining candidate pseudolabel sets based on CLIP-derived confidences with both intra- and inter-instance selection.

---

## Synthesis

CPL sits at the intersection of vision–language prompt tuning and semi/weakly supervised learning. Its foundation is the CLIP framework, which provides zero-shot, prompt-based class scores that CPL aggregates into a global confidence score matrix; without CLIP’s text–image matching formulation, CPL’s candidate pseudolabel construction would not be defined. CoOp contributes the concrete mechanism for learnable prompts that CPL fine-tunes—CPL keeps the CoOp parameterization but swaps supervised labels for unlabeled supervision via candidate pseudolabels. The intellectual spark comes from the pseudolabeling lineage: Lee’s Pseudo-Label and FixMatch popularized confidence-thresholded hard pseudolabels, but also exposed a key gap—when initial predictions are weak, hard labels are error-prone and destabilize training. CPL addresses this by generalizing the target from a single label to a progressively refined candidate set, improving true-label inclusion while avoiding premature commitment. Its inter-instance selection is informed by distribution alignment ideas in ReMixMatch, using the global score matrix to promote class-balanced instance selection. Finally, CPL’s progressive refinement mechanism draws on partial-label learning, particularly PRODEN’s principle of iteratively identifying the true label from a candidate set; CPL adapts this to the VLM context by leveraging CLIP confidences and combining intra-/inter-instance selection so that standard losses can be applied over candidate pseudolabels.

---
*Generated: 2026-01-06T23:09:26.463639*

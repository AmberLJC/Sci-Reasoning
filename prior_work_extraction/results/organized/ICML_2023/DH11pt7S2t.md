# Prior Work Analysis Report

## Target Paper
**Title:** DH11pt7S2t
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Controlling the false discovery rate: a practical and powerful approach to multiple testing** (1995)
- *Authors:* Yoav Benjamini et al.
- *Connection:* The proposed adaptive frame-rate procedure is built around applying the Benjamini–Hochberg step-up rule to decide when video-level inference is reliable, directly using FDR control as its single governing hyperparameter.

**Sequential Tests of Statistical Hypotheses** (1945)
- *Authors:* Abraham Wald
- *Connection:* The paper adopts Wald’s core idea of stopping as soon as sufficient evidence is accumulated, recasting it for video FER by replacing SPRT thresholds with an FDR-controlled multiple testing criterion.

### 💡 Inspiration

**Adaptive Computation Time for Recurrent Neural Networks** (2016)
- *Authors:* Alex Graves
- *Connection:* ACT’s idea of input-adaptive halting in sequential processing directly inspires treating frames as a sequence and deciding when to stop, with this paper replacing learned halting with BH-based FDR guarantees.

### 🔍 Gap Identification

**AdaFrame: Adaptive Frame Selection for Fast Video Recognition** (2019)
- *Authors:* Wu et al.
- *Connection:* AdaFrame established that adaptive frame selection yields large compute savings in video tasks but requires training a policy network; the current paper addresses this gap with a plug-and-play, training-free, statistically principled stopping rule.

### 📊 Baseline

**Temporal Segment Networks: Towards Good Practices for Deep Action Recognition** (2016)
- *Authors:* Limin Wang et al.
- *Connection:* TSN popularized fixed-rate, uniform frame sampling with simple aggregation; the proposed method directly improves on this fixed-sampling baseline by adaptively selecting how many frames to process per clip.

### 🔧 Extension

**Online rules for control of false discovery rate** (2018)
- *Authors:* Adel Javanmard et al.
- *Connection:* This work’s perspective on sequential/online FDR control informs the paper’s framing of per-frame evidence accumulation as a sequential multiple testing problem, guiding how error is controlled while frames arrive over time.

### 🔗 Related Problem

**BranchyNet: Fast Inference via Early Exiting from Deep Networks** (2016)
- *Authors:* Suradech Teerapittayanon et al.
- *Connection:* BranchyNet showed compute can be reduced via confidence-based early exits; this paper advances that notion by providing a statistically grounded (FDR-controlled) exit criterion without modifying the backbone.

---

## Synthesis

The core contribution—adaptive frame-rate selection for video facial expression recognition with a single, interpretable error parameter—emerges from unifying sequential decision-making with multiple testing control. At its heart lies Benjamini and Hochberg’s false discovery rate (FDR) procedure, which the paper directly operationalizes as the stopping rule to declare a reliable video-level prediction. Wald’s sequential hypothesis testing provides the foundational paradigm of halting once evidence suffices, while modern online FDR work (e.g., Javanmard and Montanari) motivates viewing arriving frames as a sequential multiple testing stream where error must be controlled as evidence accumulates. On the video efficiency side, AdaFrame demonstrated the practical value of adaptive frame selection but required training a policy and integrating it into a particular architecture; the present work fills that gap with a training-free, plug-in mechanism applicable to arbitrary feature extractors. Similarly, ideas from Adaptive Computation Time and early-exit networks like BranchyNet crystallized the benefit of input-adaptive halting, but relied on learned or heuristic confidence thresholds; this paper replaces those with a principled BH-based criterion that exposes a single hyperparameter: the target false acceptance rate. Finally, against common fixed-sampling practices exemplified by Temporal Segment Networks, the method contributes a statistically grounded, compute-aware alternative that processes fewer frames for easy clips and more for difficult ones while maintaining error control.

---
*Generated: 2026-01-06T23:09:26.547447*

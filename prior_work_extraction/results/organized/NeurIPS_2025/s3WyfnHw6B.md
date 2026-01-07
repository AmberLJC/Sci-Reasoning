# Prior Work Analysis Report

## Target Paper
**Title:** s3WyfnHw6B
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central insight—that optimizer choice can systematically influence group fairness—emerges from converging lines of prior work in fairness, optimization dynamics, and adaptive methods. Foundational fairness studies (Hardt et al., 2016) formalized group fairness criteria, while Hashimoto et al. (2018) and Sagawa et al. (2020) showed that ERM under imbalance can harm minorities and that reweighting or distributional robustness can improve worst-group performance. Rather than altering the objective, the present work examines the training dynamics themselves, building on evidence that optimizers impose distinct inductive biases (Wilson et al., 2017). To analyze these dynamics, the paper adopts the diffusion/SDE lens introduced by Mandt et al. (2017), which links stochastic optimization to continuous-time dynamics whose noise geometry and preconditioning shape convergence to different regions of the loss landscape. Within this framework, adaptive methods—rooted in AdaGrad’s per-coordinate normalization (Duchi et al., 2011) and instantiated by RMSProp (Tieleman & Hinton, 2012)—naturally rescale updates using historical gradient magnitudes. Under severe group imbalance, this rescaling can amplify minority gradients relative to majority ones, tilting updates toward fairer minima. The paper formalizes this by proving single-step and update-level guarantees in which RMSProp, compared to SGD, more evenly allocates learning across groups and improves fairness under appropriate conditions. Empirically, the theory is validated on CelebA, FairFace, and MS-COCO, positioning optimizer choice as an orthogonal, theoretically grounded lever complementing Group-DRO-style objective modifications for improving group fairness.

---
*Generated: 2026-01-07T00:05:12.531078*

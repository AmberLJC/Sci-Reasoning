# Prior Work Analysis Report

## Target Paper

**Title:** Confidential-DPproof: Confidential Proof of Differentially Private Training

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ali Shahin Shamsabadi, Gefei Tan, Tudor Ioan Cebere, Aurélien Bellet, Hamed Haddadi, Nicolas Papernot, Xiao Wang, Adrian Weller

**Keywords:** privacy auditing, zero knowledge proof, differentially private training

**Abstract:** 
> Post hoc privacy auditing techniques can be used to test the privacy guarantees of a model, but come with several limitations: (i) they can only establish lower bounds on the privacy loss, (ii) the intermediate model updates and some data must be shared with the auditor to get a better approximation of the privacy loss, and (iii) the auditor typically faces a steep computational cost to run a large number of attacks. In this paper, we propose to proactively generate a cryptographic certificate o...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Deep Learning with Differential Privacy** (2016)
- *Authors:* Martin Abadi et al.
- *Direct Connection:* The certificate proves that each DP-SGD step—per-example gradient clipping and addition of Gaussian noise—was performed as in Abadi et al.’s DP-SGD, and the claimed (ε, δ) guarantee refers to this training procedure.

**Rényi Differential Privacy** (2017)
- *Authors:* Ilya Mironov
- *Direct Connection:* The privacy accounting in the certificate composes per-iteration losses using Rényi Differential Privacy, directly adopting Mironov’s framework to compute an overall (ε, δ).

**Improving the Gaussian Mechanism for Differential Privacy: Analytical Calibration** (2018)
- *Authors:* Borja Balle et al.
- *Direct Connection:* Noise calibration in the certified training (i.e., the σ required for a target (ε, δ)) relies on the analytic characterization of the Gaussian mechanism from this work, which the proof system references when attesting correct noise addition.

### 💡 Inspiration

**Proof of Learning: Definitions and Practice** (2021)
- *Authors:* Fangzhou Jia et al.
- *Direct Connection:* The idea of producing a cryptographic proof tied to the training process is adapted here to certify DP-specific predicates, extending PoL’s training-time attestations to a zero-knowledge setting that proves privacy rather than data provenance.

### 🔍 Gap Identification

**Membership Inference Attacks From First Principles** (2022)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* This work formalizes the optimal likelihood-ratio membership audit that underpins post hoc DP auditing, whose intrinsic lower-bound nature and high computational cost are the explicit limitations replaced by proactive zero-knowledge certification.

### 🔧 Extension

**Subsampled Rényi Differential Privacy** (2019)
- *Authors:* Yu-Xiang Wang et al.
- *Direct Connection:* The epsilon reported by the certificate is computed under the subsampled Gaussian mechanism used by DP-SGD, following the RDP analysis for subsampling introduced by Wang, Balle, and Kasiviswanathan.

**Bulletproofs: Short Proofs for Confidential Transactions and More** (2018)
- *Authors:* Benedikt Bünz et al.
- *Direct Connection:* The customized zero-knowledge protocol builds on Bulletproof-style inner-product and range arguments to efficiently prove linear relations and norm/clipping constraints on gradients without revealing the underlying values.

---

## Synthesis: How Prior Work Led to This Paper

Differentially private training as practiced in modern deep learning follows DP-SGD, where each step clips per-example gradients and injects Gaussian noise; the method and its moments accountant originate in Abadi et al. Rényi Differential Privacy, introduced by Mironov, provides a tight and composable accounting framework, while the subsampled RDP analysis of Wang, Balle, and Kasiviswanathan specifies how privacy accumulates under mini-batch sampling, the regime DP-SGD operates in. The analytic calibration of the Gaussian mechanism by Balle and Wang precisely links target (ε, δ) to the noise scale σ, giving a principled basis for certifying that the injected noise suffices for the claimed guarantee. In parallel, Proof of Learning (Jia et al.) showed how to bind a training run to cryptographic evidence by producing proofs tied to training steps, but without confidentiality or privacy semantics. Membership inference work from first principles (Carlini et al.) established optimal auditing tests widely used to post hoc estimate privacy loss, highlighting that such audits only yield lower bounds and can be computationally intensive. Finally, Bulletproofs furnished efficient zero-knowledge inner-product and range arguments, enabling succinct proofs of linear relations and norm bounds over hidden values. Together, these works exposed a gap: auditing-based checks are weak and costly, while training-time attestations lacked privacy objectives. The natural synthesis is a confidential proof system that, during DP-SGD, proves per-step clipping and correctly sampled Gaussian noise, composes privacy via (subsampled) RDP, and outputs a verifiable (ε, δ) certificate—leveraging Bulletproof-style arguments for efficiency and adopting DP accounting results for correctness.

---

*Analysis generated on: 2026-01-06T07:33:48.627995*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

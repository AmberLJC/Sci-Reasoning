# Prior Work Analysis Report

## Target Paper

**Title:** Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues

**Conference:** ICLR 2025 (oral)

**Authors:** Riccardo Grazzi, Julien Siems, Arber Zela, Jörg K.H. Franke, Frank Hutter, Massimiliano Pontil

**Keywords:** State Tracking, State Space, Mamba, Linear RNN, Linear Attention, GLA, DeltaNet, Formal Languages, Products of Householders

**Abstract:** 
> Linear Recurrent Neural Networks (LRNNs) such as Mamba, RWKV, GLA, mLSTM, and DeltaNet have emerged as efficient alternatives to Transformers for long sequences. However, both Transformers and LRNNs struggle to perform state-tracking, which may impair performance in tasks such as code evaluation. In one forward pass, current architectures are unable to solve even parity, the simplest state-tracking task, which non-linear RNNs can handle effectively. Recently, Sarrof et al. (2024) demonstrated th...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention** (2020)
- *Authors:* Angelos Katharopoulos et al.
- *Direct Connection:* By reformulating attention as a linear recurrence with nonnegative kernel features, this work implicitly constrains effective transition spectra to be positive, a structural limitation our analysis identifies as fatal for state-tracking.

### 💡 Inspiration

**On parity failures in linear RNNs and the role of negative decays** (2024)
- *Authors:* Sarrof et al.
- *Direct Connection:* They showed for diagonal LRNNs (e.g., Mamba) that restricting the transition to [0,1] blocks parity while introducing negative values fixes it; we generalize and formalize this insight to non-diagonal LRNNs via an eigenvalue-based criterion and show non-triangularity is needed for modulo-3 counting.

### 🔍 Gap Identification

**Theoretical Limitations of Self-Attention in Neural Sequence Models** (2020)
- *Authors:* Michael Hahn
- *Direct Connection:* This result that standard Transformers cannot reliably track certain formal-language states in one forward pass motivates our focus on LRNNs’ state-tracking limitations and the search for architectural spectral remedies.

### 📊 Baseline

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2024)
- *Authors:* Albert Gu and Tri Dao
- *Direct Connection:* Mamba’s diagonal state-transition with nonnegative decays is the canonical LRNN setting our theory targets, and its observed failure on parity is explained by our positive-eigenvalue impossibility and remedied by allowing negative eigenvalues.

**Retentive Network: A Successor to Transformer for Large Language Models** (2023)
- *Authors:* Zhiqing Sun et al.
- *Direct Connection:* RetNet’s gated linear attention (GLA) implements retention through positive decays, providing a primary LRNN class to which our impossibility results directly apply and motivating our spectral fix via negative eigenvalues.

**RWKV: Reinventing RNNs for the Transformer Era** (2023)
- *Authors:* Bo Peng et al.
- *Direct Connection:* RWKV’s per-channel exponential time-mix with decays in (0,1) exemplifies the positive-eigenvalue regime we prove cannot implement parity at finite precision, motivating the need for sign-changing dynamics.

### 🔧 Extension

**Full-Capacity Unitary Recurrent Neural Networks** (2017)
- *Authors:* Li Jing et al.
- *Direct Connection:* We adapt the product-of-Householder parametrization from this work to construct learnable, non-triangular transition matrices with controllable (including negative) eigenvalues required by our theory.

---

## Synthesis: How Prior Work Led to This Paper

Selective state-space LRNNs popularized by Mamba leverage diagonal state transitions with nonnegative decays for linear-time sequence modeling, a structural choice shared by RWKV’s exponential time-mixing and RetNet’s gated linear attention retention mechanism—each effectively constraining the transition spectrum to positive values. Linear attention’s kernel reformulation further entrenches nonnegativity through positive feature maps that bias effective dynamics toward positive spectra. In a distinct line, unitary/orthogonal RNNs introduced products of Householder reflections as a practical way to learn expressive, non-triangular transition operators with controlled spectra. Concurrently, theoretical analyses of self-attention have highlighted one-pass failures on formal-language state-tracking tasks, sharpening interest in architectural conditions that permit exact counting and toggling behavior. Most decisively, recent work by Sarrof et al. pinpointed that diagonal LRNNs fail on parity precisely because their transitions are restricted to [0,1], and demonstrated that introducing negative values restores the ability to solve parity.
Taken together, these works surfaced a clear opportunity: dominant LRNNs inherit positivity-biased transitions that preclude basic state-tracking, while diagonal-only fixes are insufficient for richer counters and non-diagonal architectures. Building on Sarrof’s negative-value insight, it is natural to elevate the condition from entries to spectra, proving that positive eigenvalues forbid parity at finite precision and that non-triangular structure is required for modulo-3 counting. Householder-based parametrizations then become a principled vehicle to realize learnable, non-triangular transitions with negative eigenvalues, enabling LRNNs that provably recover state-tracking while retaining efficiency.

---

*Analysis generated on: 2026-01-06T10:26:13.521259*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

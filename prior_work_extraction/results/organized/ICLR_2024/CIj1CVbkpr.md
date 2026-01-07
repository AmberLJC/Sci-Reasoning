# Prior Work Analysis Report

## Target Paper

**Title:** Online Stabilization of Spiking Neural Networks

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yaoyu Zhu, Jianhao Ding, Tiejun Huang, Xiaodong Xie, Zhaofei Yu

**Keywords:** spiking neural networks, online training

**Abstract:** 
> Spiking neural networks (SNNs), attributed to the binary, event-driven nature of spikes, possess heightened biological plausibility and enhanced energy efficiency on neuromorphic hardware compared to analog neural networks (ANNs). Mainstream SNN training schemes apply backpropagation-through-time (BPTT) with surrogate gradients to replace the non-differentiable spike emitting process during backpropagation. While achieving competitive performance, the requirement for storing intermediate informa...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**A solution to the learning dilemma for recurrent networks of spiking neurons** (2020)
- *Authors:* Guillaume Bellec et al.
- *Direct Connection:* E-prop provides the core online credit-assignment framework that the paper stabilizes, addressing e-prop’s sensitivity to unnormalized, time-varying spiking statistics by adding causal normalization.

### 💡 Inspiration

**Batch Renormalization: Towards Reducing Mini-Batch Dependence in Batch-Normalized Models** (2017)
- *Authors:* Sergey Ioffe
- *Direct Connection:* The renormalization correction (r, d) for aligning per-batch and running statistics directly inspires the paper’s causal, future-free normalization that stabilizes spiking activations in online settings.

**Online Normalization for Training Neural Networks** (2019)
- *Authors:* Julian Chiley et al.
- *Direct Connection:* Streaming, causally updated normalization statistics motivate the paper’s design of an online, temporally causal normalization scheme for spiking dynamics without batch access.

### 🔍 Gap Identification

**Recurrent Batch Normalization** (2016)
- *Authors:* Tim Cooijmans et al.
- *Direct Connection:* Its per-time-step BN for RNNs requires sequence-wide statistics, highlighting the core limitation—dependence on future timesteps—that the paper explicitly removes for SNNs with an online, causal alternative.

### 📊 Baseline

**BNTT: Batch Normalization Through Time for Training Spiking Neural Networks** (2021)
- *Authors:* Hyoungseok Kim and Priyadarshini Panda
- *Direct Connection:* By applying BN separately at each timestep to stabilize SNNs, BNTT serves as the principal normalization baseline whose need for future timesteps the paper overcomes with online spiking renormalization.

### 🔗 Related Problem

**Direct Training for Spiking Neural Networks: Faster, Larger, Better** (2019)
- *Authors:* Yujie Wu et al.
- *Direct Connection:* Its NeuNorm-style spiking-specific normalization demonstrates that stabilizing spike dynamics is crucial, which the paper extends by formulating a normalization that works under strict online constraints.

---

## Synthesis: How Prior Work Led to This Paper

Batch Renormalization introduced explicit correction factors that reconcile noisy mini-batch statistics with running estimates, mapping out a practical path to stable normalization when reliable batch statistics are unavailable. Recurrent Batch Normalization showed the benefit of time-step-specific normalization for recurrent dynamics, but crucially depended on full-sequence access, making it incompatible with strictly causal, online training. Online Normalization established that streaming, causal estimators of mean and variance can replace batch-dependent normalization and still stabilize deep learning in non-i.i.d. or low-batch regimes. In spiking networks, Direct Training for Spiking Neural Networks demonstrated that SNN-specific normalization (e.g., NeuNorm) is essential to control membrane potential scales and firing rates, underscoring the centrality of normalization to trainability and accuracy. BNTT extended this idea to time-resolved normalization in SNNs, stabilizing dynamics by applying BN per timestep but at the cost of requiring future information. Finally, e-prop provided a biologically plausible, memory-efficient online credit-assignment mechanism using eligibility traces, yet it remained vulnerable to instability from unnormalized, time-varying spiking activity. Together, these works expose a gap: SNNs trained online need normalization that is both time-aware and strictly causal. The paper synthesizes the renormalization insight (correction toward running stats), streaming normalization updates, and SNN-specific temporal normalization into an online spiking renormalization module that plugs into e-prop-style training, delivering BN-like stabilization without future timesteps—making online, memory-efficient SNN training both stable and accurate.

---

*Analysis generated on: 2026-01-07T00:26:39.295242*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

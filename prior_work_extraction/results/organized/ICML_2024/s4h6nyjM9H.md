# Prior Work Analysis Report

## Target Paper
**Title:** s4h6nyjM9H
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**The Reversible Residual Network: Backpropagation Without Storing Activations** (2017)
- *Authors:* Aidan Gomez et al.
- *Connection:* T-RevSNN adapts RevNet’s invertible residual-block principle to reconstruct forward states during backprop, enabling O(L) training memory without checkpointing.

**Spatio-Temporal Backpropagation for Training High-Performance Spiking Neural Networks** (2018)
- *Authors:* Yujie Wu et al.
- *Connection:* STBP formalized surrogate-gradient BPTT for SNNs and its O(LT) memory footprint, defining the training bottleneck that T-RevSNN fixes via reversible temporal computation.

### 💡 Inspiration

**Reversible Recurrent Neural Networks** (2018)
- *Authors:* MacKay et al.
- *Connection:* The idea of making temporal updates invertible to avoid storing per-timestep activations directly inspired T-RevSNN’s temporal reversible interactions at turn-on spiking neurons.

**DIET-SNN: Direct Input Encoding With Trainable Membrane Time Constant for Low-Latency Spiking Neural Networks** (2020)
- *Authors:* Nitin Rathi et al.
- *Connection:* Evidence that direct input encoding reduces time steps and energy informed T-RevSNN’s redesigned input encoding, which—combined with reversibility—achieves O(1) inference energy cost.

### 🔍 Gap Identification

**Conversion of Continuous-Valued Deep Networks to Efficient Event-Driven Networks for Image Classification** (2017)
- *Authors:* Bodo Rueckauer et al.
- *Connection:* Rate-coded ANN-to-SNN conversion attains accuracy but requires long simulations and high inference energy, a key limitation T-RevSNN overcomes with constant-cost inference.

### 🔧 Extension

**Deep Residual Learning in Spiking Neural Networks** (2021)
- *Authors:* Wei Fang et al.
- *Connection:* T-RevSNN modifies SEW-ResNet-style spiking residual blocks and internal units to make residual pathways compatible with sparse, reversible temporal information flow.

### 🔗 Related Problem

**A solution to the learning dilemma in spiking neural networks** (2020)
- *Authors:* Guillaume Bellec et al.
- *Connection:* e-prop reduces training memory via local rules but departs from exact backprop and does not lower inference cost; T-RevSNN instead uses temporal reversibility to keep global gradients with O(L) memory and O(1) inference energy.

---

## Synthesis

The core of T-RevSNN is to make SNN time evolution reversible at carefully chosen “temporal turn-on” points so that training needs only O(L) memory and inference consumes O(1) energy. This directly builds on reversible neural computation: RevNet (Gomez et al.) established that invertible residual blocks allow reconstructing activations during backprop, eliminating activation storage, while Reversible RNNs (MacKay et al.) showed how temporal updates can be made invertible to cut BPTT memory. These ideas motivate T-RevSNN’s multi-level temporal reversible interactions and the decision to turn off neuron dynamics most timesteps to preserve invertibility and stability. The training bottleneck T-RevSNN targets is defined by STBP (Wu et al.), which popularized surrogate-gradient BPTT for SNNs but incurs O(LT) memory by storing time sequences. On the architectural side, T-RevSNN refines spiking residual blocks along the lines of SEW-ResNet (Fang et al.), adjusting residual pathways and internal neuron units so sparse temporal information remains effective under reversible constraints. The inference-energy dilemma is crystallized by ANN-to-SNN conversion (Rueckauer et al.), where long rate-coded simulations drive energy costs high; DIET-SNN (Rathi et al.) demonstrated that direct input encoding can drastically cut timesteps, a cue T-RevSNN leverages and couples with reversibility to reach O(1) inference energy. Finally, while e-prop (Bellec et al.) reduces training memory via local learning, it does not provide the exact, global-gradient training with simultaneous inference savings that T-RevSNN achieves by redesigning the forward dynamics themselves.

---
*Generated: 2026-01-06T23:09:26.498401*

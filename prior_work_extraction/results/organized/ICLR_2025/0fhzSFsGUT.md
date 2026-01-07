# Prior Work Analysis Report

## Target Paper

**Title:** PETRA: Parallel End-to-end Training with Reversible Architectures

**Conference:** ICLR 2025 (spotlight)

**Authors:** Stephane Rivaud, Louis Fournier, Thomas Pumir, Eugene Belilovsky, Michael Eickenberg, Edouard Oyallon

**Keywords:** Model parallelism, Delayed gradient, Reversible architectures

**Abstract:** 
> Reversible architectures have been shown to be capable of performing on par with their non-reversible architectures, being applied in deep learning for memory savings and generative modeling. In this work, we show how reversible architectures can solve challenges in parallelizing deep model training. We introduce PETRA, a novel alternative to backpropagation for parallelizing gradient computations. PETRA facilitates effective model parallelism by enabling stages (i.e., a set of layers) to comput...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**The Reversible Residual Network: Backpropagation Without Storing Activations** (2017)
- *Authors:* Aidan N. Gomez et al.
- *Direct Connection:* PETRA directly relies on RevNet’s invertible residual blocks to reconstruct activations during backward passes, enabling exact gradients while decoupling stage computations without storing activations.

**GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism** (2019)
- *Authors:* Yanping Huang et al.
- *Direct Connection:* GPipe formalized stage-based pipeline parallelism with micro-batches, a setup PETRA adopts but re-engineers by using reversibility to allow independent stage execution and minimal activation/gradient communication.

### 💡 Inspiration

**i-RevNet: Deep Invertible Networks** (2018)
- *Authors:* Julius Jacobsen et al.
- *Direct Connection:* By showing that fully invertible architectures can match non-invertible CNNs on classification, i-RevNet provided the empirical justification that PETRA’s reliance on reversible layers would not sacrifice accuracy.

### 🔍 Gap Identification

**PipeDream-2BW: Balancing Pipeline Parallelism for DNN Training** (2021)
- *Authors:* Deepak Narayanan et al.
- *Direct Connection:* The two-weight-version scheme in PipeDream-2BW reduces staleness at the cost of extra memory, a limitation PETRA addresses by eliminating weight stashing entirely while preserving correctness via reversibility-based gradient routing.

**Decoupled Neural Interfaces using Synthetic Gradients** (2016)
- *Authors:* Max Jaderberg et al.
- *Direct Connection:* DNI sought to decouple layers with synthetic (approximate) gradients but suffered stability/accuracy issues, motivating PETRA’s use of reversibility to achieve similar decoupling with exact but delayed gradients.

### 📊 Baseline

**PipeDream: Generalized Pipeline Parallelism for DNN Training** (2019)
- *Authors:* Deepak Narayanan et al.
- *Direct Connection:* PipeDream’s weight-stashing mechanism to handle inconsistent weights across pipeline stages serves as PETRA’s principal baseline, which PETRA replaces by keeping a single weight version enabled by reversible reconstruction and delayed exact gradients.

---

## Synthesis: How Prior Work Led to This Paper

Reversible residual networks established that invertible blocks can reconstruct activations exactly, enabling backpropagation without storing intermediate states; this property is crucial when gradients must be computed without retaining forward caches. Building on that, i-RevNet demonstrated that fully invertible CNNs can achieve competitive accuracy on standard vision tasks, alleviating concerns that reversibility undermines representational power. In parallel, GPipe formalized stage-based pipeline parallelism with micro-batching, clarifying how models can be partitioned across devices but still requiring stored activations and tightly coupled forward/backward scheduling. PipeDream pushed pipeline parallelism further with asynchronous execution, introducing weight stashing to maintain per-microbatch consistency under staleness, while PipeDream-2BW reduced staleness by keeping two weight versions—both approaches trading memory for correctness. A different thread, Decoupled Neural Interfaces, attempted to break the forward-backward dependency with synthetic gradients, exposing the promise of stage independence but revealing instability from inexact gradient signals. Together, these works suggested that practical pipeline parallelism needed exact gradients, minimal activation storage, and no multi-version weights. PETRA synthesizes these insights by using reversibility to reconstruct activations at stage boundaries, enabling independent stage computations that exchange only activations and true (but delayed) gradients; this removes weight stashing entirely and preserves a single parameter version, delivering a parallel, autograd-like training procedure that retains accuracy while addressing the core memory and consistency limitations of prior pipeline methods.

---

*Analysis generated on: 2026-01-06T16:31:38.563049*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Improving the Sparse Structure Learning of Spiking Neural Networks from the View of Compression Efficiency

**Conference:** ICLR 2025 (spotlight)

**Authors:** Jiangrong Shen, Qi Xu, Gang Pan, Badong Chen

**Keywords:** spiking neural networks

**Abstract:** 
> The human brain utilizes spikes for information transmission and dynamically reorganizes its network structure to boost energy efficiency and cognitive capabilities throughout its lifespan. Drawing inspiration from this spike-based computation, Spiking Neural Networks (SNNs) have been developed to construct event-driven models that emulate this efficiency. Despite these advances, deep SNNs continue to suffer from over-parameterization during training and inference, a stark contrast to the brain’...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks** (2019)
- *Authors:* Jonathan Frankle and Michael Carbin
- *Direct Connection:* The existence of ‘winning ticket’ sparse subnetworks motivates our first-stage evaluation of candidate sparse SNN subnetworks, which we operationalize via a PQ-based compressibility metric to preserve trainability while compressing.

**SNIP: Single-shot Network Pruning based on Connection Sensitivity** (2019)
- *Authors:* Namhoon Lee et al.
- *Direct Connection:* SNIP’s connection-sensitivity criterion for pruning at or near initialization informs our practice of assessing subnetwork viability during training, which we generalize to SNNs using a compression-efficiency–aware PQ index.

### 💡 Inspiration

**Deep Rewiring: Training very sparse deep neural networks** (2018)
- *Authors:* Guillaume Bellec et al.
- *Direct Connection:* Deep Rewiring introduced biologically inspired synaptic rewiring for sparse SNNs; we adopt the structural plasticity view but guide both rewiring and sparsity levels by measured compression efficiency.

**AMC: AutoML for Model Compression and Acceleration on Mobile Devices** (2018)
- *Authors:* Yihui He et al.
- *Direct Connection:* AMC formalized choosing per-layer pruning ratios by optimizing an accuracy–compression objective; we bring this compression-efficiency principle to SNN structural learning via a lightweight PQ index rather than RL search.

### 🔍 Gap Identification

**Sparse Evolutionary Training of Deep Neural Networks** (2018)
- *Authors:* Decebal C. Mocanu et al.
- *Direct Connection:* SET prunes and regrows connections with a fixed fraction each update, and this static pruning ratio is the exact limitation (under/over-pruning) our method replaces with a compressibility-driven, adaptive schedule for sparse SNN training.

### 📊 Baseline

**Rigging the Lottery: Making All Tickets Winners** (2020)
- *Authors:* Utku Evci et al.
- *Direct Connection:* RigL’s gradient-based connection growth under a fixed global sparsity is our main dynamic-sparsity baseline, over which we introduce compressibility-aware adjustment of the pruning level tailored to SNNs.

### 🔗 Related Problem

**Parameter Efficient Training of Deep CNNs by Dynamic Sparse Reparameterization** (2019)
- *Authors:* Hussein Mostafa and Xin Wang
- *Direct Connection:* Dynamic Sparse Reparameterization couples magnitude pruning with growth while enforcing a target sparsity; we extend this dynamic reallocation idea by learning the target via a compressibility (PQ) index rather than fixing it.

---

## Synthesis: How Prior Work Led to This Paper

Sparse Evolutionary Training (SET) showed that prune-and-grow can maintain trainability in sparse networks but relies on a fixed pruning fraction at every update, making sparsity control insensitive to training dynamics. RigL advanced dynamic sparse training by growing connections using gradient signals while keeping a fixed global sparsity target, and Dynamic Sparse Reparameterization similarly coupled magnitude pruning with growth under a preset sparsity budget. The Lottery Ticket Hypothesis established that trainable sparse subnetworks exist and can match dense performance when appropriately selected, encouraging principled evaluation of subnetwork viability. SNIP demonstrated that connection-sensitivity can identify viable sparse subnetworks at or near initialization, pointing to saliency-style criteria for early or mid-training assessment. In the SNN context, Deep Rewiring introduced biologically inspired synaptic rewiring, emphasizing structural plasticity as an effective mechanism for sparse SNNs. Complementarily, AMC cast pruning as an explicit accuracy–compression optimization, showing that pruning ratios should be chosen by compression efficiency rather than set heuristically.
Together, these works reveal a gap: dynamic sparse methods reallocate connections but freeze the sparsity level, while compression-aware methods choose ratios but lack spike-based structural plasticity. The natural next step is a two-stage SNN structure learning procedure that (i) evaluates the compressibility of current sparse subnetworks—preserving winning-ticket–like trainability via a PQ-style efficiency metric—and (ii) adaptively adjusts the pruning ratio to avoid under/over-pruning, thereby aligning synaptic rewiring with compression efficiency throughout training.

---

*Analysis generated on: 2026-01-06T06:03:41.456936*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

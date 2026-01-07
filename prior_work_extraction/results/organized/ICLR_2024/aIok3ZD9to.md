# Prior Work Analysis Report

## Target Paper

**Title:** LLMCarbon: Modeling the End-to-End Carbon Footprint of Large Language Models

**Conference:** ICLR 2024 (oral)

**Authors:** Ahmad Faiz, Sotaro Kaneda, Ruhan Wang, Rita Chukwunyere Osi, Prateek Sharma, Fan Chen, Lei Jiang

**Keywords:** carbon footprint modeling, large lanaguage models

**Abstract:** 
> The carbon footprint associated with large language models (LLMs) is a significant concern, encompassing emissions from their training, inference, experimentation, and storage processes, including operational and embodied carbon emissions. An essential aspect is accurately estimating the carbon impact of emerging LLMs even before their training, which heavily relies on GPU usage. Existing studies have reported the carbon footprint of LLM training, but only one tool, mlco2, can predict the carbon...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Energy and Policy Considerations for Deep Learning in NLP** (2019)
- *Authors:* Strubell et al.
- *Direct Connection:* LLMCarbon builds on Strubell et al.’s carbon accounting formulation—energy multiplied by datacenter PUE and regional grid carbon intensity—as the base emissions model it expands to an end-to-end lifecycle.

**Training Compute-Optimal Large Language Models** (2022)
- *Authors:* Hoffmann et al.
- *Direct Connection:* LLMCarbon leverages Hoffmann et al.’s compute-optimal scaling laws and FLOP/token estimates to map LLM architectural parameters and dataset size to training compute, enabling accurate pre-training carbon prediction.

### 💡 Inspiration

**The Carbon Footprint of Machine Learning Training Will Plateau, Then Shrink** (2022)
- *Authors:* Patterson et al.
- *Direct Connection:* LLMCarbon adopts Patterson et al.’s key insight to include embodied hardware emissions and datacenter efficiency factors in ML carbon estimates, extending these ideas to GPU-centric LLM projections and lifecycle phases beyond training.

### 📊 Baseline

**Quantifying the Carbon Emissions of Machine Learning** (2019)
- *Authors:* Lacoste et al.
- *Direct Connection:* LLMCarbon directly generalizes mlco2’s pre-training emissions prediction by making it architecture-aware (dense and MoE), adding multi-phase coverage (training, inference, experimentation, storage), and incorporating embodied-carbon accounting that mlco2 lacks.

### 🔧 Extension

**DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale** (2022)
- *Authors:* Rajbhandari et al.
- *Direct Connection:* LLMCarbon extends DeepSpeed-MoE’s practical metrics (top-k routing, capacity factor, expert/communication overhead) to parameterize MoE training and inference energy and carbon within its projection model.

### 🔗 Related Problem

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* Fedus et al.
- *Direct Connection:* LLMCarbon uses Switch Transformers’ characterization of MoE routing (e.g., top-1 expert activation and per-token compute) to model the sparsity-driven reduction in FLOPs and energy for MoE LLMs.

---

## Synthesis: How Prior Work Led to This Paper

Quantifying the Carbon Emissions of Machine Learning introduced the first widely used predictor (mlco2) that estimates emissions via hardware choice, location, and runtime, cementing the carbon-accounting template based on energy, PUE, and grid carbon intensity. Energy and Policy Considerations for Deep Learning in NLP formalized this accounting, tying emissions to datacenter PUE and regional carbon intensity and establishing transparent reporting for training workloads. The Carbon Footprint of Machine Learning Training Will Plateau, Then Shrink argued that embodied hardware emissions and datacenter efficiency must be included alongside operational energy, and provided a methodology to factor hardware manufacturing impacts. Training Compute-Optimal Large Language Models provided compute scaling laws and FLOP-per-token estimates linking LLM architecture and dataset size to required compute—a bridge from model design to energy demand. Switch Transformers characterized MoE sparsity with top-1 routing and per-token compute, quantifying how only a subset of parameters are active per token. DeepSpeed-MoE detailed practical MoE training/inference behavior—capacity factors, top-k routing, and communication overhead—giving actionable parameters for system-level cost modeling.

Together, these works revealed the opportunity for an architecture-aware, end-to-end predictor that covers dense and MoE LLMs, spans training, inference, experimentation, and storage, and includes both operational and embodied emissions. LLMCarbon synthesizes the carbon-accounting framework (energy × PUE × carbon intensity) with compute scaling laws for dense models and routing/overhead characterizations for MoE, and integrates Patterson’s embodied-emissions perspective, yielding a pre-training projection tool that connects LLM design choices directly to total lifecycle carbon.

---

*Analysis generated on: 2026-01-06T19:53:59.124439*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

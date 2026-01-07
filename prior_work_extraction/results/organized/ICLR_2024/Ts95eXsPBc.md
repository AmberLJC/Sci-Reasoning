# Prior Work Analysis Report

## Target Paper

**Title:** Spatially-Aware Transformers for Embodied Agents

**Conference:** ICLR 2024 (spotlight)

**Authors:** Junmo Cho, Jaesik Yoon, Sungjin Ahn

**Keywords:** Episodic Memory, Spatial Inference, Prediction, Generation, Reinforcement Learning

**Abstract:** 
> Episodic memory plays a crucial role in various cognitive processes, such as the ability to mentally recall past events. While cognitive science emphasizes the significance of spatial context in the formation and retrieval of episodic memory, the current primary approach to implementing episodic memory in AI systems is through transformers that store temporally ordered experiences, which overlooks the spatial dimension. As a result, it is unclear how the underlying structure could be extended to...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Neural Map: Structured Memory for Deep Reinforcement Learning** (2018)
- *Authors:* Emilio Parisotto et al.
- *Direct Connection:* Neural Map introduced a 2D map-indexed external memory keyed by agent pose, providing the core place-centric abstraction that the current work integrates into transformer attention for episodic recall.

**Cognitive Mapping and Planning for Visual Navigation** (2017)
- *Authors:* Saurabh Gupta et al.
- *Direct Connection:* This paper formalized building and using allocentric spatial maps from egocentric observations, underpinning the notion of aggregating experiences by place that the current work fuses with transformer-based memory.

### 💡 Inspiration

**Unsupervised Predictive Memory in a Goal-Directed Agent (MERLIN)** (2018)
- *Authors:* Greg Wayne et al.
- *Direct Connection:* MERLIN demonstrated that predictive, place-aware episodic memory improves long-horizon behavior, motivating the current paper’s design of transformer memories that explicitly encode spatial context.

### 🔍 Gap Identification

**Decision Transformer: Reinforcement Learning via Sequence Modeling** (2021)
- *Authors:* Lili Chen et al.
- *Direct Connection:* By treating trajectories as temporally ordered sequences, this paper exemplifies the dominant temporal-only transformer approach whose lack of spatial grounding the current work directly addresses with place-centric memory.

### 📊 Baseline

**Stabilizing Transformers for Reinforcement Learning** (2020)
- *Authors:* Emilio Parisotto et al.
- *Direct Connection:* This work established transformer-based episodic memory for RL but organizes memory purely along temporal order, which the current paper takes as the main baseline and augments with explicit spatial structure.

### 🔗 Related Problem

**Semi-Parametric Topological Memory for Navigation** (2018)
- *Authors:* Nikolay Savinov et al.
- *Direct Connection:* SPTM’s topological, place-centric memory and retrieval showed the effectiveness of organizing experiences by location, an idea the current work adopts in a differentiable transformer to guide spatial recall.

---

## Synthesis: How Prior Work Led to This Paper

Transformers have been effectively used as episodic memories for reinforcement learning, as demonstrated by Gated Transformer-XL variants that stabilize long-context credit assignment but rely solely on temporal ordering of tokens. Sequence-modeling approaches like Decision Transformer similarly treat trajectories as time-ordered sequences without explicit spatial grounding. In contrast, a line of work on spatial memory in embodied agents showed the power of place-centric organization: Neural Map introduced an external 2D map indexed by agent pose for structured memory writes and reads; MERLIN provided predictive, place-aware episodic memory that improved long-horizon tasks by conditioning recall on spatial context; Semi-Parametric Topological Memory built nonparametric graph memories where nodes correspond to places and retrieval follows topological connectivity; and Cognitive Mapping and Planning established how egocentric observations can be accumulated into allocentric maps to support planning.
Combining these insights reveals a clear opportunity: temporal-only transformers excel at sequence modeling but are inefficient for place-centric recall, whereas spatial memory systems excel at locality and retrieval but lack the flexible content-based querying of transformers. The present work naturally emerges by embedding the place-centric organization of Neural Map/SPTM and the predictive, spatially contextualized recall of MERLIN within a transformer, augmenting attention with spatial indices so episodic memories are written, aggregated, and retrieved by place. This synthesis yields a spatially-aware transformer that preserves transformer flexibility while improving memory utilization and accuracy on spatial tasks.

---

*Analysis generated on: 2026-01-06T09:12:51.381049*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

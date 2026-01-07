# Prior Work Analysis Report

## Target Paper

**Title:** Quality Measures for Dynamic Graph Generative Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Ryien Hosseini, Filippo Simini, Venkatram Vishwanath, Rebecca Willett, Henry Hoffmann

**Keywords:** generative models, dynamic graphs, evaluation metrics

**Abstract:** 
> Deep generative models have recently achieved significant success in modeling graph data, including dynamic graphs, where topology and features evolve over time. However, unlike in vision and natural language domains, evaluating generative models for dynamic graphs is challenging due to the difficulty of visualizing their output, making quantitative metrics essential. In this work, we develop a new quality metric for evaluating generative models of dynamic graphs. Current metrics for dynamic gra...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A Relational Event Framework for Social Action** (2008)
- *Authors:* Carter T. Butts et al.
- *Direct Connection:* By formalizing dynamic networks as relational event point processes, this work provides the event-level representation that the proposed metric compares directly instead of snapshotting.

### 💡 Inspiration

**DyRep: Learning Representations over Dynamic Graphs** (2019)
- *Authors:* Rakshit Trivedi et al.
- *Direct Connection:* DyRep’s continuous-time, marked-event modeling of dynamic graphs directly motivates treating temporal dependence as intrinsic to the metric rather than evaluating i.i.d. snapshots.

### 🔍 Gap Identification

**GraphRNN: Generating Realistic Graphs with Deep Auto-regressive Models** (2018)
- *Authors:* Jiaxuan You et al.
- *Direct Connection:* GraphRNN popularized the multi-statistic MMD evaluation protocol for graph generators, whose lack of a unified scalar score we address in the dynamic-graph setting.

**Temporal Networks** (2012)
- *Authors:* Petter Holme et al.
- *Direct Connection:* This survey pinpoints how aggregating or coarse snapshotting erases non-uniform temporal dynamics, the exact failure mode our metric is designed to avoid.

### 📊 Baseline

**NetLSD: Hearing the Shape of a Graph** (2018)
- *Authors:* Maksim Tsitsulin et al.
- *Direct Connection:* NetLSD’s heat-trace signatures are a primary snapshot-based similarity our work replaces, highlighting the limits of per-slice comparisons that ignore event timing and dependence.

**DeltaCon: A Principled Massive-Graph Similarity Function** (2013)
- *Authors:* Danai Koutra et al.
- *Direct Connection:* DeltaCon is a widely used scalar graph-similarity baseline for generative evaluation, whose snapshot application to dynamic graphs our metric supersedes by preserving temporal dependencies.

### 🔧 Extension

**Fused Gromov–Wasserstein Distances for Structured Objects** (2019)
- *Authors:* Titouan Vayer et al.
- *Direct Connection:* We extend the fused Gromov–Wasserstein principle of jointly aligning structure and attributes to yield a single scalar discrepancy that couples topology with features across time.

---

## Synthesis: How Prior Work Led to This Paper

Relational event modeling established that dynamic networks are best represented as sequences of timestamped interactions, where order and inter-event times carry essential information about the process generating edges and features. Building on this, continuous-time deep models like DyRep framed dynamic graphs as marked temporal point processes, demonstrating that temporality must be modeled explicitly rather than through independent snapshots. In parallel, optimal transport advances introduced fused Gromov–Wasserstein distances, which produce a single scalar by jointly aligning structural relations and node/edge attributes, showing a principled path to unify topology and features in one measure. Snapshot-based similarity tools such as NetLSD compress each static graph into a spectral heat-trace signature to enable efficient comparisons, and DeltaCon offers a fast scalar similarity sensitive to local structural changes; both have been adopted for evaluating generated graphs slice-by-slice. Finally, GraphRNN popularized a de facto evaluation suite built on multiple MMDs over handcrafted statistics, encoding practice but also fragmentation of quality assessment, while the temporal network literature highlighted that coarse discretization obscures non-uniform evolution.
Taken together, these works reveal a clear gap: evaluations that either rely on per-snapshot similarities or multi-metric reports fail to capture continuous-time dependencies and do not offer a unified scalar that is sensitive to both structure and attributes. The present metric synthesizes the event-based view from relational/point-process modeling with OT-based joint alignment of structure and features, yielding a single temporally aware quality score that avoids snapshot i.i.d. assumptions while remaining comparable and interpretable across models.

---

*Analysis generated on: 2026-01-06T07:14:10.865578*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

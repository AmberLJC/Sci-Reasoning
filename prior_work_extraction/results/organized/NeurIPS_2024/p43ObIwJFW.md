# Prior Work Analysis Report

## Target Paper
**Title:** p43ObIwJFW
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—solving QUBO in a one-shot classification manner with a graph-convolutional value extractor and a label-free training routine—emerges from three converging lines of prior work. First, the QUBO canon (Glover–Kochenberger–Du) formalized binary quadratic modeling and highlighted symmetry in Q, which the authors operationalize via a graph view and symmetry-aware feature extraction. Second, the learning-to-optimize literature largely adopted sequential decision paradigms: early sequence-to-sequence RL (Bello et al.) and high-performing autoregressive attention policies (Kool et al.) achieved strong quality but at substantial computational cost; graph-based RL (Dai–Khalil–Dilkina–Song) showed the effectiveness of GNNs for Max-Cut/QUBO but retained the sequential burden. These works set both the performance bar and the efficiency pain point that VCM targets by abandoning autoregression. Third, graph neural models for combinatorial optimization reframed solution construction as labeling and demonstrated label-free training by directly optimizing task objectives (Karalias & Loukas), while the broader semi-supervised literature established pseudo-label self-training (Lee). Building on these, VCM designs a GCN-based Depth Value Network to compress Q’s pairwise structure into value features and couples it with a Value Classification Network for direct assignment prediction. Its Greedy-guided Self Trainer instantiates pseudo-labeling tailored to QUBO: inexpensive greedy flips create evolving supervision without optimal labels. Together, these strands directly inform VCM’s classification reformulation, architectural choices, and efficient training regime.

---
*Generated: 2026-01-07T00:02:04.752274*

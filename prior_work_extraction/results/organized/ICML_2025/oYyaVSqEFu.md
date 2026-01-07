# Prior Work Analysis Report

## Target Paper
**Title:** oYyaVSqEFu
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s central contribution—a multimodal, latency-aware anomaly detector that marries an asynchronous event-stream GNN with an RGB CNN—emerges from three converging lines of prior work. First, neuromorphic sensing established the need and means for microsecond-latency perception. The DVS (Lichtsteiner et al., 2008) introduced event-driven vision, while DAVIS (Brandli et al., 2014) co-located events and frames, directly enabling practical event–RGB fusion. Event-native feature design (Sironi et al., 2018, HATS) then demonstrated that spatiotemporal neighborhoods around events yield robust, low-latency descriptors, a principle our method inherits by organizing events into local structures suitable for graph processing.
Second, the asynchronous processing mechanics of dynamic graphs (Xu et al., 2020, TGAT; Rossi et al., 2020, TGN) provided the algorithmic blueprint for continuous-time, event-wise message passing with lightweight memory updates. We adapt these ideas to event-camera data, enabling our GNN to update representations at event arrival times without expensive batching—crucial for millisecond response.
Third, multimodal synergy and application grounding in driving anomalies informed our fusion and evaluation choices. Events-to-Video (Rebecq et al., 2019) showed the complementarity of event temporal detail with frame-based spatial content, justifying our hybrid architecture. Street Scene (Ramachandra & Jones, 2020) clarified anomaly definitions and metrics in urban settings, which we extend to real-time constraints. Together, these works directly shaped our asynchronous graph design, event–RGB fusion strategy, and latency-first evaluation, culminating in a system that advances both accuracy and response time for safety-critical driving scenarios.

---
*Generated: 2026-01-07T00:04:09.146943*

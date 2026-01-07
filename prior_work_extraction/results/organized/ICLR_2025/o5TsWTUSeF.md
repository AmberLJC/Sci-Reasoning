# Prior Work Analysis Report

## Target Paper
**Title:** o5TsWTUSeF
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

ChartMoE’s core contribution—replacing the standard single linear projector with a Mixture-of-Experts (MoE) connector composed of diversely aligned experts—sits at the intersection of two influential threads. First, projector-based multimodal LLMs such as LLaVA and MiniGPT-4, and connector-centric designs like BLIP-2, crystallized the cross-modal ‘connector’ as a key bottleneck for visual-language grounding. Their successes and observed brittleness with a single mapping motivated ChartMoE to rethink the connector as a set of specialized experts, each initialized by distinct alignment tasks, rather than one-size-fits-all linear projection.

Second, advances in sparse MoE—Switch Transformers and ViT-MoE—demonstrated that routing to specialized experts improves capacity and domain specialization without prohibitive compute. ChartMoE strategically applies these MoE principles at the connector level, using a router to select among task-initialized experts, thereby bridging modality gaps more robustly for charts.

Finally, the chart-understanding literature shaped the specific alignment signals. ChartQA underscored the need for faithful, numerically grounded reasoning, while DePlot showed that converting chart images into structured tables boosts reliability. ChartMoE operationalizes these insights by curating ChartMoE-Align—a large-scale chart-table-JSON-code dataset—and by training separate connector experts on chart→table/JSON/code alignments. The resulting MoE connector, initialized from these specialized pre-alignments and refined with high-quality supervision, directly addresses the faithfulness and reliability challenges endemic to chart understanding.

---
*Generated: 2026-01-07T00:02:04.911818*

# Prior Work Analysis Report

## Target Paper

**Title:** Open-YOLO 3D: Towards Fast and Accurate Open-Vocabulary 3D Instance Segmentation

**Conference:** ICLR 2025 (oral)

**Authors:** Mohamed El Amine Boudjoghra, Angela Dai, Jean Lahoud, Hisham Cholakkal, Rao Muhammad Anwer, Salman Khan, Fahad Shahbaz Khan

**Keywords:** Open Vocabulary, 3D point cloud instance segmentation

**Abstract:** 
> Recent works on open-vocabulary 3D instance segmentation show strong promise but at the cost of slow inference speed and high computation requirements. This high computation cost is typically due to their heavy reliance on aggregated clip features from multi-view, which require computationally expensive 2D foundation models like Segment Anything (SAM) and CLIP. Consequently, this hampers their applicability in many real-world applications that require both fast and accurate predictions. To this ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**OpenScene: 3D Scene Understanding with Open Vocabularies** (2023)
- *Authors:* First author et al.
- *Direct Connection:* OpenScene introduced projecting 2D vision-language cues into 3D to obtain open-vocabulary semantics, a formulation that Open-YOLO 3D retains while substituting dense CLIP features with category distributions from 2D detectors.

**Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection** (2023)
- *Authors:* Shilong Liu et al.
- *Direct Connection:* Grounding DINO provides text-conditioned open-vocabulary 2D detections whose per-prompt scores serve as the view-wise semantic evidence that Open-YOLO 3D aggregates with its Multi-View Prompt Distribution (MVPDist).

### 💡 Inspiration

**YOLO-World: Real-Time Open-Vocabulary Object Detection** (2024)
- *Authors:* First author et al.
- *Direct Connection:* YOLO-World demonstrated that open-vocabulary detection can be made real-time, directly inspiring Open-YOLO 3D’s emphasis on a detector-only pipeline and YOLO-style efficiency for scalable 3D open-vocabulary instance segmentation.

### 🔍 Gap Identification

**OpenIns3D** (2024)
- *Authors:* First author et al.
- *Direct Connection:* OpenIns3D demonstrated that fusing per-view vision-language features and 2D masks yields accurate open-vocabulary 3D instances but incurs heavy computational cost, directly motivating Open-YOLO 3D’s detector-only design to achieve comparable accuracy at much higher speed.

### 📊 Baseline

**OpenMask3D: Open-Vocabulary 3D Instance Segmentation** (2024)
- *Authors:* First author et al.
- *Direct Connection:* OpenMask3D established the dominant pipeline of aggregating multi-view CLIP/SAM features to label 3D instance masks, which Open-YOLO 3D explicitly replaces with lightweight 2D open-vocabulary detections and a multi-view label fusion mechanism.

### 🔗 Related Problem

**ConceptFusion: Open-set Multimodal 3D Mapping** (2023)
- *Authors:* First author et al.
- *Direct Connection:* ConceptFusion showed that multi-view 2D VLM signals can be fused into 3D maps but relied on heavyweight per-pixel features, highlighting the opportunity that Open-YOLO 3D seizes by fusing only detection-level category scores across views.

**OWL-ViT: Open-Vocabulary Object Detection via Vision Transformers** (2023)
- *Authors:* Michael Minderer et al.
- *Direct Connection:* OWL-ViT established efficient text-queryable 2D detection, enabling the use of detector score distributions as semantic primitives that Open-YOLO 3D fuses across views to robustly label 3D instances.

---

## Synthesis: How Prior Work Led to This Paper

OpenMask3D showed that open-vocabulary 3D instance segmentation is achievable by projecting multi-view CLIP features and SAM-derived masks into 3D and classifying instances with language embeddings, albeit with a heavy per-view compute footprint. OpenIns3D likewise fused per-view vision-language features and segmentation to obtain strong 3D instance masks, but its reliance on dense 2D foundation models limited throughput. OpenScene established the general formulation of lifting 2D vision-language signals into 3D to endow point clouds with open-vocabulary semantics, validating the projection-and-fusion paradigm. ConceptFusion further demonstrated that multi-view 2D VLM cues can be consistently integrated in 3D mapping, reinforcing the utility of view aggregation while also revealing the computational burden of dense feature pipelines. In parallel, Grounding DINO introduced text-conditioned open-vocabulary detection that outputs phrase-aligned box scores, and OWL-ViT showed efficient transformer-based detectors can be directly queried with arbitrary vocabularies. YOLO-World then proved that open-vocabulary detection can be real-time, providing fast category-score evidence at scale.
Together, these works suggested a gap: prior 3D methods relied on dense multi-view CLIP/SAM features for semantics, while open-vocabulary detectors could deliver lightweight, text-queryable evidence but had not been fused into 3D at the instance level. Open-YOLO 3D synthesizes these insights by replacing dense features with detector score distributions and introducing a principled multi-view prompt distribution (MVPDist) that aggregates category evidence across views to counter single-view misclassifications, yielding fast yet accurate open-vocabulary 3D instance segmentation.

---

*Analysis generated on: 2026-01-06T19:31:26.634825*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

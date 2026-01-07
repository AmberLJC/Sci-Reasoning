# Prior Work Analysis Report

## Target Paper

**Title:** Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment

**Conference:** ICLR 2025 (spotlight)

**Authors:** Dongping Chen, Ruoxi Chen, Shu Pu, Zhaoyi Liu, Yanru Wu, Caixi Chen, Benlin Liu, Yue Huang, Yao Wan, Pan Zhou, Ranjay Krishna

**Keywords:** Interleaved Text-and-Image Generation, Generative Models, Multimodal Large Language Model, Scene Graphs, Automatic Evaluation, Benchmark

**Abstract:** 
> Many real-world user queries (e.g. *"How do to make egg fried rice?"*) could benefit from systems capable of generating responses with both textual steps with accompanying images, similar to a cookbook.
Models designed to generate interleaved text and images face challenges in ensuring consistency within and across these modalities.
To address these challenges, we present ISG, a comprehensive evaluation framework for interleaved text-and-image generation. ISG leverages a scene graph structure to...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations** (2017)
- *Authors:* Ranjay Krishna et al.
- *Direct Connection:* ISG adopts the Visual Genome scene graph formalism (objects, attributes, relations) as its core representation and extends it to link textual blocks with image regions across a response.

**Chameleon: Mixed-Modal Early-Fusion Foundation Models** (2024)
- *Authors:* Meta AI et al.
- *Direct Connection:* ISG targets the interleaved text-and-image generation capability exemplified by Chameleon, providing the missing evaluation protocol for assessing holistic and structural consistency of mixed-modality generations.

### 💡 Inspiration

**GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering** (2019)
- *Authors:* Drew A. Hudson et al.
- *Direct Connection:* ISG borrows GQA’s practice of deriving structured, compositional questions from scene graphs to produce interpretable question–answer feedback tied to specific graph nodes and relations.

### 🔍 Gap Identification

**T2I-CompBench: A Comprehensive Benchmark for Compositional Text-to-Image Generation** (2023)
- *Authors:* Xuanlin Li et al.
- *Direct Connection:* ISG overcomes T2I-CompBench’s image-only, detector-based checks of objects/attributes/relations by introducing graph-based cross-modal alignment and block-level coherence for interleaved outputs.

### 📊 Baseline

**TIFA: Text-to-Image Faithfulness Evaluation** (2023)
- *Authors:* Yushi Hu et al.
- *Direct Connection:* ISG addresses TIFA’s unstructured, image-only QA evaluation by replacing it with a structured interleaved scene graph that enables holistic, structural, block-level, and image-specific consistency checks.

### 🔧 Extension

**SPICE: Semantic Propositional Image Caption Evaluation** (2016)
- *Authors:* Peter Anderson et al.
- *Direct Connection:* ISG generalizes SPICE’s scene-graph-based semantic comparison from single-image caption evaluation to interleaved text–image sequences by introducing cross-modal nodes/edges and multi-level scoring.

### 🔗 Related Problem

**Emu2: Multimodal Pretraining for Interleaved Image–Text Generation** (2024)
- *Authors:* Chunyuan Li et al.
- *Direct Connection:* ISG is designed to evaluate models like Emu2 that natively generate interleaved sequences, filling the measurement gap left by image-only or text-only metrics.

---

## Synthesis: How Prior Work Led to This Paper

Scene-graph ideas matured through two strands that are directly relevant here. SPICE showed that converting captions into a scene-graph representation of objects, attributes, and relations enables semantics-aware evaluation beyond n-gram overlap, establishing graphs as a metric substrate. Visual Genome standardized this formalism with dense object–attribute–relation annotations, making graphs a lingua franca for connecting visual content and language. Building on this, GQA demonstrated how to derive compositional questions from scene graphs, producing interpretable QA that probes specific nodes and relations rather than holistic heuristics. In parallel, automatic evaluation of text-to-image models advanced with TIFA, which uses question answering to assess image–prompt faithfulness but remains image-only and unstructured; and with T2I-CompBench, which tests compositionality using detectors on objects, attributes, and relations but likewise focuses solely on images. Meanwhile, new generative models such as Chameleon and Emu2 began producing interleaved sequences of text and images, creating outputs that require alignment and coherence checks within and across modalities and blocks.
Together, these threads exposed a gap: existing metrics either model semantics via graphs but only for captions, or evaluate images via QA/detectors without cross-modal structure, while modern generators output interleaved multimodal content. ISG synthesizes SPICE’s graph-based semantics, Visual Genome’s object–relation schema, and GQA’s graph-derived QA with the problem setting introduced by Chameleon/Emu2, yielding an interleaved scene graph that supports holistic, structural, block-level, and image-specific evaluation with interpretable QA grounded in the graph.

---

*Analysis generated on: 2026-01-06T15:31:09.747495*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

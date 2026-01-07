# Prior Work Analysis Report

## Target Paper

**Title:** InstructScene: Instruction-Driven 3D Indoor Scene Synthesis with Semantic Graph Prior

**Conference:** ICLR 2024 (spotlight)

**Authors:** Chenguo Lin, Yadong MU

**Keywords:** 3D indoor scene synthesis, controllable generative models, graph diffusion models

**Abstract:** 
> Comprehending natural language instructions is a charming property for 3D indoor scene synthesis systems. Existing methods directly model object joint distributions and express object relations implicitly within a scene, thereby hindering the controllability of generation. We introduce InstructScene, a novel generative framework that integrates a semantic graph prior and a layout decoder to improve controllability and fidelity for 3D scene synthesis. The proposed semantic graph prior jointly lea...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**3D-FRONT: 3D Furnished Rooms with Layouts of Objects and Textures** (2021)
- *Authors:* Hao-Shu Fang Fu et al.
- *Direct Connection:* InstructScene trains and evaluates its semantic graph prior and layout decoding on 3D-FRONT’s large-scale indoor scenes, adopting its problem formulation and assets for joint appearance/layout learning.

### 💡 Inspiration

**GRAINS: Generative Recursive Autoencoders for Indoor Scenes** (2019)
- *Authors:* Zhengjie Wu et al.
- *Direct Connection:* GRAINS demonstrated that explicitly modeling inter-object relations improves indoor scene plausibility, motivating InstructScene’s shift to an explicit semantic graph prior rather than implicit relation learning.

### 📊 Baseline

**ATISS: Autoregressive Transformers for Indoor Scene Synthesis** (2021)
- *Authors:* Despoina Paschalidou et al.
- *Direct Connection:* ATISS models object placements via an implicit joint distribution, and InstructScene directly replaces this paradigm with an explicit semantic graph prior to achieve controllability over object relations.

**ControlRoom3D: Controllable Text-to-3D Room Generation** (2023)
- *Authors:* Zhengzhe Liu et al.
- *Direct Connection:* As a primary text-driven indoor scene baseline that maps text to scenes without explicit relation priors, ControlRoom3D’s limitations in fine-grained controllability motivate InstructScene’s semantic graph prior.

### 🔧 Extension

**DiGress: A Generative Model for Graphs via Discrete Denoising Diffusion** (2022)
- *Authors:* Thibaud Vignac et al.
- *Direct Connection:* InstructScene adapts discrete graph diffusion from DiGress to learn and sample instruction-conditioned semantic scene graphs as a controllable prior.

**Graph2Plan: Learning Floorplan Generation from Layout Graphs** (2021)
- *Authors:* Natsunori Minami Nauata et al.
- *Direct Connection:* By showing that graph-to-layout decoding is effective, Graph2Plan directly informs InstructScene’s layout decoder that maps semantic graphs to 3D object layouts.

---

## Synthesis: How Prior Work Led to This Paper

Autoregressive indoor scene generators such as ATISS model object arrangements by directly learning joint distributions over placements, yielding realistic layouts but encoding relations only implicitly, which hampers precise control. Earlier, GRAINS highlighted that explicit structural modeling of inter-object relations and hierarchies improves plausibility, suggesting a representational gap between implicit set modeling and relationally structured priors. Discrete diffusion on graphs, exemplified by DiGress, introduced a principled way to learn and sample complex discrete relational structures, providing a scalable generative mechanism for graphs. Graph2Plan demonstrated that conditioning a decoder on a relational graph to produce spatial layouts can disentangle semantics from geometry, enabling controllable layout synthesis. Concurrently, ControlRoom3D established text-to-3D room generation but largely mapped language to layouts without an explicit relational prior, limiting fine-grained, relation-aware control. Across these works, the 3D-FRONT dataset supplied standardized room categories, object assets, and typical co-occurrence/layout statistics to learn both appearance and spatial distributions.
Synthesizing these insights, the opportunity emerged to decouple scene semantics and relations from geometry: learn a language-conditioned semantic graph as a controllable prior, and then decode it into object layouts. InstructScene operationalizes this by adapting discrete graph diffusion to sample instruction-conditioned semantic graphs, addressing ATISS-style implicitness and ControlRoom3D’s coarse control. A graph-conditioned layout decoder, in the spirit of Graph2Plan, maps the semantic graph to 3D placements, leveraging 3D-FRONT’s distributions while extending GRAINS’ explicit relational modeling to a scalable, instruction-driven, zero-shot-capable framework.

---

*Analysis generated on: 2026-01-06T19:11:43.352671*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Can Large Language Models Understand Symbolic Graphics Programs?

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zeju Qiu, Weiyang Liu, Haiwen Feng, Zhen Liu, Tim Z. Xiao, Katherine M. Collins, Joshua B. Tenenbaum, Adrian Weller, Michael J. Black, Bernhard Schölkopf

**Keywords:** Large Language Models, Symbolic Graphics Programs

**Abstract:** 
> Against the backdrop of enthusiasm for large language models (LLMs), there is a growing need to scientifically assess their capabilities and shortcomings. This is nontrivial in part because it is difficult to find tasks which the models have not encountered during training. Utilizing symbolic graphics programs, we propose a domain well-suited to test multiple spatial-semantic reasoning skills of LLMs. Popular in computer graphics, these programs procedurally generate visual data. While LLMs exhi...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning** (2017)
- *Authors:* Johnson et al.
- *Direct Connection:* CLEVR introduced procedurally generated scenes and compositional question programs to precisely probe visual-semantic reasoning, a blueprint this work adopts but re-centers on executable graphics programs to eliminate the vision front end.

**CSGNet: Neural Shape Parser for Constructive Solid Geometry** (2018)
- *Authors:* Sharma et al.
- *Direct Connection:* CSGNet formalized 2D/3D shapes as executable CSG programs, providing the core notion that symbolic graphics programs carry precise geometric semantics that can be queried without images.

### 💡 Inspiration

**The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences From Natural Supervision** (2019)
- *Authors:* Mao et al.
- *Direct Connection:* NS-CL showed how executable symbolic programs can disentangle perception from reasoning, directly inspiring the idea to reason purely over the symbolic generative graphics program rather than rendered pixels.

### 🔍 Gap Identification

**SCAN: Simplifying and Testing Systematic Generalization in Sequence-to-Sequence Models** (2018)
- *Authors:* Lake and Baroni
- *Direct Connection:* SCAN exposed failures of sequence models on compositional generalization, motivating the use of graphics programs to craft systematic splits that stress LLMs’ compositional spatial-semantic reasoning.

**On the Measure of Intelligence (ARC)** (2019)
- *Authors:* Chollet
- *Direct Connection:* ARC argued for contamination-resistant, procedurally generated abstraction tests, motivating the choice of symbolic graphics programs as a controllable domain unlikely to appear verbatim in LLM pretraining.

### 🔗 Related Problem

**DreamCoder: Growing Generalizable, Interpretable Knowledge with Wake-Sleep Program Induction** (2021)
- *Authors:* Ellis et al.
- *Direct Connection:* DreamCoder demonstrated that graphics DSLs capture compositional structure enabling generalizable reasoning, informing the selection of vector/CSG-like primitives as a substrate for semantic querying.

---

## Synthesis: How Prior Work Led to This Paper

Procedurally generated worlds with compositional queries, as in CLEVR, established how to precisely probe visual-semantic reasoning using controllable scene generation and functional question programs. The neuro-symbolic concept learner (NS-CL) then showed that executable programs can cleanly separate perception from reasoning by operating over symbolic structures rather than raw pixels. SCAN revealed that sequence models struggle with systematic generalization, especially when compositional rules must be applied to novel combinations—an insight germane to constructing splits that target compositionality. ARC argued that robust intelligence evaluation demands procedurally generated, contamination-resistant tasks that rely on abstract reasoning rather than memorization, emphasizing careful domain design. From the graphics side, CSGNet formalized shapes as constructive solid geometry programs, making explicit that symbolic graphics programs encode exact geometric semantics. DreamCoder further demonstrated that graphics DSLs expose compositional regularities that support programmatic analysis and concept learning, underscoring the value of vector/CSG primitives for interpretable reasoning. Taken together, these works suggest a natural opportunity: use executable graphics programs themselves as the world model to test spatial-semantic reasoning without a vision encoder. By unifying CLEVR-style controlled compositional queries with ARC’s contamination-aware generation, leveraging NS-CL’s decoupling of perception and reasoning, and adopting CSG/DSL representations highlighted by CSGNet and DreamCoder, the present work formulates an evaluation where LLMs must “imagine” renderings from symbolic curve and stroke descriptions and answer semantics-rich questions, enabling targeted tests of compositional and spatial generalization.

---

*Analysis generated on: 2026-01-06T13:39:03.938605*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

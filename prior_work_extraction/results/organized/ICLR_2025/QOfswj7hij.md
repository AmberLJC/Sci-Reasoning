# Prior Work Analysis Report

## Target Paper

**Title:** VisualPredicator: Learning Abstract World Models with Neuro-Symbolic Predicates for Robot Planning

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yichao Liang, Nishanth Kumar, Hao Tang, Adrian Weller, Joshua B. Tenenbaum, Tom Silver, Joao F. Henriques, Kevin Ellis

**Keywords:** learning abstractions for planning, neuro-symbolic ai, concept learning

**Abstract:** 
> Broadly intelligent agents should form task-specific abstractions that selectively expose the essential elements of a task, while abstracting away the complexity of the raw sensorimotor space. In this work, we present Neuro-Symbolic Predicates, a first-order abstraction language that combines the strengths of symbolic and neural knowledge representations. We outline an online algorithm for inventing such predicates and learning abstract world models. We compare our approach to hierarchical reinf...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Classical Planning in Deep Latent Space** (2018)
- *Authors:* Asai et al.
- *Direct Connection:* This work showed that a planning-ready discrete representation can be learned directly from images, and the present paper generalizes that idea from propositional latent bits to learned first-order neuro-symbolic predicates with an abstract transition model for compositional generalization.

**An Object-Oriented Representation for Efficient Reinforcement Learning** (2008)
- *Authors:* Diuk et al.
- *Direct Connection:* This work formalized object- and relation-centric abstractions in RL, which is instantiated here by learning a first-order predicate language and dynamics over relational states from pixels to enable lifted planning.

### 💡 Inspiration

**From Skills to Symbols: Learning Symbolic Representations for Abstract, High-Level Planning** (2018)
- *Authors:* Konidaris et al.
- *Direct Connection:* It provided the key insight that task-specific symbols should be learned from interaction to support planning, which is extended here to relational, first-order predicate learning jointly with an abstract world model rather than assuming pre-specified skills.

**DreamCoder: Growing generalizable, interpretable knowledge with wake–sleep program learning** (2021)
- *Authors:* Ellis et al.
- *Direct Connection:* The paper adapts DreamCoder’s online library-learning (wake–sleep) mechanism for inventing reusable abstractions to the predicate-invention setting, consolidating a predicate vocabulary that composes into an abstract world model.

**The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences from Natural Supervision** (2019)
- *Authors:* Mao et al.
- *Direct Connection:* NS-CL’s idea of neural concept detectors functioning as symbolic predicates over objects directly informs the use of neural predicates here, repurposed for model-based planning with explicit transition dynamics.

### 🔍 Gap Identification

**Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan)** (2022)
- *Authors:* Ahn et al.
- *Direct Connection:* SayCan highlights that VLM-based planners lack internal causal world models and struggle with OOD generalization, motivating the move to learned, task-specific neuro-symbolic predicates and abstract models.

### 📊 Baseline

**Meta-Interpretive Learning of Higher-Order Logic Programs** (2015)
- *Authors:* Muggleton et al.
- *Direct Connection:* This ILP framework is a primary symbolic predicate-invention baseline whose reliance on discrete logic and search is addressed by grounding invented predicates neurally and learning them online for scalable robot planning.

---

## Synthesis: How Prior Work Led to This Paper

Object- and relation-centric formulations such as Object-Oriented MDPs established that first-order abstractions over entities and predicates enable efficient, lifted decision-making. LatPlan demonstrated that planning-ready discrete state can be learned directly from images, but did so at a propositional level that limits compositionality and relational generalization. NS-CL showed how neural concept detectors can be cast as symbolic predicates over objects and composed into programs, providing a recipe for grounding symbolic reasoning in perception. In symbolic learning, Meta-Interpretive Learning introduced predicate invention via logic-based search, but required fully symbolic input and struggled to scale in perceptual domains. DreamCoder advanced online abstraction invention with wake–sleep library learning, making it possible to grow a reusable vocabulary of high-level concepts over time. In robotics, “From Skills to Symbols” argued that task-specific symbols should be learned from interaction to support high-level planning, but relied on pre-specified skills and largely non-relational symbols. Meanwhile, SayCan exemplified VLM planning’s ability to sequence language-described skills while exposing its lack of an internal causal world model and weak OOD generalization. Taken together, these threads expose a clear opportunity: learn relational, task-specific symbols as neural predicates grounded in perception, invent them online as reusable abstractions, and couple them with an explicit abstract world model to enable lifted planning. The present work synthesizes these ideas by upgrading propositional latent planning to first-order neuro-symbolic predicates, importing online abstraction invention to grow the predicate vocabulary, and addressing VLM and ILP limitations through learned, interpretable dynamics that support sample-efficient, OOD-robust robot planning.

---

*Analysis generated on: 2026-01-06T13:32:28.055184*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** The Computational Complexity of Circuit Discovery for Inner Interpretability

**Conference:** ICLR 2025 (spotlight)

**Authors:** Federico Adolfi, Martina G. Vilas, Todd Wareham

**Keywords:** inner interpretability, mechanistic interpretability, circuit discovery, computational complexity, parameterized complexity

**Abstract:** 
> Many proposed applications of neural networks in machine learning, cognitive/brain science, and society hinge on the feasibility of inner interpretability via circuit discovery. This calls for empirical and theoretical explorations of viable algorithmic options. Despite advances in the design and testing of heuristics, there are concerns about their scalability and faithfulness at a time when we lack understanding of the complexity properties of the problems they are deployed to solve. To addres...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Zoom In: An Introduction to Circuits** (2020)
- *Authors:* Chris Olah et al.
- *Direct Connection:* Introduced the circuit discovery paradigm—identifying sparse subnetworks of neurons and connections that mediate specific behaviors—which is the exact object of study whose query variants this paper formalizes and analyzes for complexity.

### 💡 Inspiration

**A Mathematical Framework for Transformer Circuits** (2021)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* Provided concrete formal notions of paths, mediating components, and patch-based interventions in transformers that are abstracted here into general circuit-finding queries and the affordances of description, explanation, prediction, and control.

**Causal Abstraction for Faithful Model Explanation** (2023)
- *Authors:* Atticus Geiger et al.
- *Direct Connection:* Formalized intervention-based evaluation of mechanisms (distinguishing prediction vs. control) and fidelity criteria, which directly inform the intervention semantics and explanatory affordances used to define and analyze the circuit-discovery queries here.

### 🔍 Gap Identification

**Towards Automated Circuit Discovery** (2023)
- *Authors:* Benjamin Conmy et al.
- *Direct Connection:* Proposed heuristic search procedures (e.g., path/activation patching over nodes and edges) for finding circuits while noting scalability and faithfulness limitations, directly motivating this paper’s settling of the inherent computational complexity of the underlying queries.

**Toy Models of Superposition in Neural Networks** (2022)
- *Authors:* Nelson Elhage et al.
- *Direct Connection:* Showed that features are superposed across units rather than isolated, implying combinatorial selection across layers for circuit discovery—precisely the sparsity/depth parameters whose roles this paper makes explicit via parameterized complexity.

### 🔗 Related Problem

**Locating and Editing Factual Associations in GPT (ROME)** (2022)
- *Authors:* Kevin Meng et al.
- *Direct Connection:* Demonstrated locating small mediating subnetworks via causal tracing and then editing them to control outputs, a form of circuit-finding and control query whose tractability is formalized and classified in this paper’s complexity framework.

---

## Synthesis: How Prior Work Led to This Paper

The circuits line of work established that model behavior can be explained by sparse subnetworks of neurons and connections, with Zoom In detailing how such circuits mediate specific tasks through interconnected components rather than isolated units. Building on this, a mathematical framework for transformer circuits made precise the notions of paths, mediating components, and patch-based interventions, operationalizing how to trace and validate causal pathways in deep models. Heuristic efforts toward automated circuit discovery proposed practical search procedures using activation and path patching across nodes and edges to assemble candidate circuits, while explicitly flagging issues of scalability and faithfulness. Intervention-centric theory further clarified how to evaluate mechanisms by distinguishing predictive adequacy from control via causal interventions and fidelity criteria, grounding explanation in causal semantics. Empirically, locating and editing factual associations showed how small mediating subnetworks can be identified and surgically edited to control outputs, and toy models of superposition demonstrated that features distribute across units, hinting at inherently combinatorial search spaces.
Taken together, these works defined the objects (circuits as mediating subnetworks), the empirical procedures (patching and causal tracing), and the evaluative semantics (prediction vs. control) while surfacing practical failures (scalability, unfaithfulness, superposition). The natural next step was to abstract these concrete circuit-finding and intervention tasks into formal query families aligned with explanatory affordances and to determine their inherent difficulty. By doing so, the current paper synthesizes the circuit and causal-intervention insights into a unified complexity-theoretic framework that classifies which circuit-discovery goals are tractable and which are provably hard, including parameterized regimes keyed to sparsity, depth, and layer structure.

---

*Analysis generated on: 2026-01-06T11:42:15.175606*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Prediction without Preclusion: Recourse Verification with Reachable Sets

**Conference:** ICLR 2024 (spotlight)

**Authors:** Avni Kothari, Bogdan Kulynych, Tsui-Wei Weng, Berk Ustun

**Keywords:** algorithmic recourse, fairness, robustness, consumer finance, integer programming, trustworthy AI

**Abstract:** 
> Machine learning models are often used to decide who receives a loan, a job interview, or a public benefit. Models in such settings use features without considering their *actionability*. As a result, they can assign predictions that are \emph{fixed} -- meaning that individuals who are denied loans and interviews are, in fact, *precluded from access* to credit and employment. In this work, we introduce a procedure called *recourse verification* to test if a model assigns fixed predictions to its...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Actionable Recourse in Linear Classification** (2019)
- *Authors:* Berk Ustun et al.
- *Direct Connection:* This work formalized recourse with explicit actionability constraints and discrete, immutable features, directly informing the current paper’s construction of action-induced reachable sets and the notion of “fixed” predictions when no feasible change exists.

**Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR** (2017)
- *Authors:* Sandra Wachter et al.
- *Direct Connection:* This paper introduced the counterfactual-explanation objective that recourse builds on, whose lack of actionability constraints and feasibility guarantees motivated the present shift from finding a single counterfactual to verifying existence over a reachable set.

### 💡 Inspiration

**FACE: Feasible and Actionable Counterfactual Explanations** (2020)
- *Authors:* Lélio Poyiadzi et al.
- *Direct Connection:* FACE’s graph/path-based feasibility notion inspired treating feasible changes as a reachability problem, which the current work elevates from heuristic path search to certified coverage over an entire reachable set.

**Towards Fast Computation of Certified Robustness for ReLU Networks** (2018)
- *Authors:* Tsui-Wei Weng et al.
- *Direct Connection:* The certify-over-a-set paradigm from robustness verification—proving model properties hold for all inputs in a region—directly inspired framing recourse as verification over action-induced reachable input sets.

### 🔍 Gap Identification

**Towards Robust and Reliable Algorithmic Recourse** (2021)
- *Authors:* Sahil Upadhyay et al.
- *Direct Connection:* By showing that many recourse methods fail under realistic constraints and model perturbations, this work highlights the need for guarantees, motivating the present paper’s certified verification of whether recourse exists at all.

### 🔧 Extension

**Model-Agnostic Counterfactual Explanations for Consequential Decisions** (2020)
- *Authors:* Amir-Hossein Karimi et al.
- *Direct Connection:* By casting recourse as sequences of feasible interventions (via causal/structural constraints), this paper provides the intervention-semantics that the present work operationalizes as reachable sets for model-agnostic verification by querying predictions.

---

## Synthesis: How Prior Work Led to This Paper

Actionable recourse was first grounded by Ustun et al., who formalized feasible changes with immutable and discrete features, and encoded actionability via optimization constraints. Karimi et al. then framed recourse as sequences of feasible interventions, using structural constraints to define exactly which counterfactual states are attainable through actions. Poyiadzi et al. brought a path-based perspective, finding feasible counterfactuals along a graph built on observed data so that traversed steps correspond to plausible, incremental changes. Wachter et al. introduced the counterfactual objective itself for black-box models, prioritizing minimally different alternatives but without explicit feasibility or actionability guarantees. In parallel, robustness verification work by Weng et al. established the certify-over-a-set paradigm, proving properties for all inputs within a region rather than testing points one by one. Upadhyay et al. highlighted that many recourse procedures break under realistic constraints and perturbations, underscoring the need for guarantees rather than heuristic solutions. Together these strands expose a clear opportunity: use action semantics to define the set of states an individual can genuinely reach, and apply verification-style reasoning to certify whether any point in that set changes the model’s prediction. The current work synthesizes these insights by constructing reachable sets for discrete feature spaces and verifying, via model queries, whether recourse exists—shifting from counterfactual search to certifiable recourse verification and revealing when predictions are fixed (precluding access) in consequential domains.

---

*Analysis generated on: 2026-01-06T12:03:35.056119*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

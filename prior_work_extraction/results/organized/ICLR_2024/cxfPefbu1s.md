# Prior Work Analysis Report

## Target Paper

**Title:** Procedural Fairness Through Decoupling Objectionable Data Generating Components

**Conference:** ICLR 2024 (spotlight)

**Authors:** Zeyu Tang, Jialu Wang, Yang Liu, Peter Spirtes, Kun Zhang

**Keywords:** Procedural Fairness, Decouple Objectionable Component, Reference Point, Causal Fairness, Data Generating Process, Bias Mitigation

**Abstract:** 
> We reveal and address the frequently overlooked yet important issue of _disguised procedural unfairness_, namely, the potentially inadvertent alterations on the behavior of neutral (i.e., not problematic) aspects of data generating process, and/or the lack of procedural assurance of the greatest benefit of the least advantaged individuals. Inspired by John Rawls's advocacy for _pure procedural justice_ (Rawls, 1971; 2001), we view automated decision-making as a microcosm of social institutions, ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A Theory of Justice** (1971)
- *Authors:* John Rawls
- *Direct Connection:* Rawls’s notion of pure procedural justice and the difference principle provides the normative basis that this paper operationalizes via reference-point-based decoupling and procedural assurance for the least advantaged.

**Counterfactual Fairness** (2017)
- *Authors:* Matt J. Kusner et al.
- *Direct Connection:* This work supplies the counterfactual semantics—evaluating decisions under interventions on protected attributes—that the paper leverages when instantiating reference values to isolate objectionable components of the data-generating process.

**Identifiability of Path-Specific Effects** (2005)
- *Authors:* Carmel Avin, Ilya Shpitser, Judea Pearl
- *Direct Connection:* It introduces the path-specific effect formalism enabling baseline-setting along selected causal paths, the precise operation that undergirds the paper’s decoupling of objectionable versus neutral generative components.

### 💡 Inspiration

**Avoiding Discrimination through Causal Reasoning** (2017)
- *Authors:* M. Kilbertus et al.
- *Direct Connection:* By framing fairness as blocking inadmissible causal pathways from protected attributes to outcomes, this work directly motivates the paper’s admissible/objectionable component separation in the data-generating process.

### 🔍 Gap Identification

**Residual Unfairness in Fair Machine Learning from Preexisting Bias** (2018)
- *Authors:* Narayana P. Kallus, Angela Zhou
- *Direct Connection:* It shows that standard fairness adjustments can unintentionally preserve or worsen unfairness due to biased data generation, motivating the paper’s focus on preventing disguised procedural unfairness when intervening on models or data.

### 📊 Baseline

**Fair Inference on Outcomes** (2018)
- *Authors:* Razieh Nabi, Ilya Shpitser
- *Direct Connection:* It operationalizes fairness by nullifying disallowed path-specific effects via setting protected attributes to a reference level, which the paper extends with a reference-point/value-instantiation rule and procedural guarantees to prevent disguised unfairness.

### 🔧 Extension

**Path-Specific Counterfactual Fairness** (2019)
- *Authors:* Silvia Chiappa
- *Direct Connection:* This paper implements PSE-based fairness by specifying admissible vs. inadmissible paths and baseline instantiation, a strategy generalized here to entire generative components with procedural constraints.

---

## Synthesis: How Prior Work Led to This Paper

Rawls established pure procedural justice and the difference principle, emphasizing processes that ensure fair treatment and prioritization of the least advantaged even when outcomes are uncertain. In algorithmic contexts, counterfactual fairness formalized decisions’ invariance to interventions on protected attributes, grounding fairness in counterfactual semantics. The path-specific effect literature developed the formal machinery to isolate and manipulate causal influence along selected pathways by setting variables to baseline values, enabling fine-grained control over how protected attributes affect outcomes. Building on this, causal approaches to algorithmic fairness proposed identifying admissible versus inadmissible pathways and blocking discriminatory influence through causal graphs. Fair inference on outcomes then operationalized fairness by nullifying disallowed path-specific effects via reference-level interventions, and path-specific counterfactual fairness provided practical learning procedures that instantiate these baselines during training. Meanwhile, empirical critiques highlighted that naive fairness adjustments can entrench or exacerbate bias due to the underlying data-generating process, warning that interventions may inadvertently alter benign mechanisms or fail to aid the least advantaged. Together, these works reveal both the power and pitfalls of causal, counterfactual fairness: we can target specific influences, but interventions risk collateral changes to neutral components and insufficient benefit to those worst-off. The current paper synthesizes Rawlsian procedural commitments with path-specific causal interventions by formalizing reference points and a value-instantiation rule that explicitly decouple objectionable components from neutral ones, ensuring mitigation targets only problematic mechanisms and incorporates procedural assurance for maximizing the least advantaged individuals’ welfare—a natural next step given prior causal fairness tools and their documented limitations.

---

*Analysis generated on: 2026-01-07T00:18:22.797156*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper
**Title:** aTiMLVePXi
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—estimand-agnostic, practical do-SHAP with a scalable computation scheme—sits at the confluence of causal attribution, general causal identification, and efficient Shapley estimation. SHAP (Lundberg & Lee, 2017) provided the dominant Shapley-based attribution framework but largely relied on observational sampling assumptions; subsequent work showed these can be misleading when features interact causally. Causal perspectives on attribution (Janzing et al., 2019) and the formalization of Causal/do-Shapley values (Frye et al., 2020) reframed feature importance as an interventional notion on a causal graph—defining the semantics the present paper adopts. To make such explanations broadly applicable on complex graphs, the authors invoke the structural causal model and do-calculus foundations (Pearl, 2009) together with the ID algorithm’s general identification results (Shpitser & Pearl, 2006), enabling any identifiable interventional estimand to be computed from a single fitted causal model rather than bespoke estimators per query. Practically, this is realized by learning a generative causal model that supports arbitrary interventions, an idea operationalized in CGNN (Goudet et al., 2018) and related neural SCMs, which directly motivates the paper’s estimand-agnostic engine and its ability to explain inaccessible data-generating processes via surrogate SCMs. Finally, the proposed fast algorithm for do-SHAP is influenced by advances in efficient Shapley computation such as FastSHAP (Jethani et al., 2021), adapting amortized/structured computation principles to the interventional setting to achieve significant speed-ups at negligible accuracy cost.

---
*Generated: 2026-01-07T00:21:32.264363*

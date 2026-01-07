# Prior Work Analysis Report

## Target Paper
**Title:** 6vcgsrK6pN
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core innovation—a competitive-analysis framework for oracle-based model extraction with provably perfect-fidelity reconstruction of additive decision trees—sits at the intersection of threat modeling, explainability-driven oracles, and classic query-learning theory. Tramèr et al. (2016) crystallized the black-box model extraction threat and introduced fidelity and query-efficiency metrics, which this work elevates from empirical benchmarks to formal guarantees. Jagielski et al. (2020) demonstrated that high-fidelity extraction is practically achievable under constrained queries, motivating the paper’s emphasis on anytime performance and rigorous bounds.
Counterfactual explanations, introduced by Wachter et al. (2017) and formalized further by Karimi et al. (2021), provide the specific oracle signals that make explainability a double-edged sword. By mapping counterfactual-style queries to structured constraints on decision boundaries, the paper turns explanations into informative queries for exact reconstruction.
The theoretical backbone comes from Angluin’s (1988) query-learning model and Kushilevitz and Mansour’s (1991) exact tree-learning techniques, which show how membership/counterexample-style queries can identify tree structures. Building on these insights, the paper designs reconstruction algorithms tailored to additive tree ensembles (decision trees, random forests, gradient boosting) with provable fidelity and bounded query complexity. Finally, the evaluation lens is grounded in Borodin and El-Yaniv’s (1998) competitive analysis, enabling the authors to define and prove competitive ratios and anytime guarantees for extraction procedures. Together, these works directly shape the paper’s oracle formalization, algorithmic strategy for tree reconstruction, and the novel competitive-performance framework.

---
*Generated: 2026-01-07T00:21:32.325236*

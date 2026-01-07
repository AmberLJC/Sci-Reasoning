# Prior Work Analysis Report

## Target Paper
**Title:** eD534mPhAg
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s key contribution—a robustness-based, OOD-resistant evaluation of post-hoc GNN explanations—sits at the intersection of three strands of prior work: (1) subgraph-based GNN explainability and its evaluation practice, (2) adversarial robustness, especially on graphs, and (3) covariate-shift correction.

First, GNNExplainer established the dominant paradigm of extracting explanatory subgraphs and evaluating them by re-feeding masked inputs. While widely adopted, this procedure can push inputs off the data manifold, undermining faithfulness. In vision, ROAR revealed that deletion/insertion tests suffer from OOD artifacts and advocated distribution-aware evaluation via retraining—insight that directly motivates OAR’s OOD-aware design.

Second, adversarial robustness provides a principled, model-agnostic metric: measure the worst-case perturbation needed to change a prediction. Madry et al. formalized robustness-as-worst-case risk with PGD-style evaluation. On graphs, Dai et al., Nettack, and Metattack operationalized adversarial perturbations under realistic constraints (structure and features), supplying concrete attack spaces and optimization tools. OAR translates this robustness lens to explanations: an explanation is better if it is harder to adversarially subvert when restricted to its subgraph.

Third, to avoid the OOD trap during evaluation, OAR introduces importance-based reweighting grounded in covariate-shift correction (e.g., Kernel Mean Matching), keeping the assessment aligned with the original data distribution without expensive retraining. Together, these works enable OAR/SimOAR to deliver scalable, distribution-respecting, and adversarially grounded metrics for judging the quality of GNN post-hoc explanations.

---
*Generated: 2026-01-06T23:42:49.126438*

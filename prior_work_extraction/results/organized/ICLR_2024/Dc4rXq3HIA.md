# Prior Work Analysis Report

## Target Paper

**Title:** Improving Domain Generalization with Domain Relations

**Conference:** ICLR 2024 (spotlight)

**Authors:** Huaxiu Yao, Xinyu Yang, Xinyi Pan, Shengchao Liu, Pang Wei Koh, Chelsea Finn

**Keywords:** Domain Generalization; Domain Relations; Distribution Shift

**Abstract:** 
> Distribution shift presents a significant challenge in machine learning, where models often underperform during the test stage when faced with a different distribution than the one they were trained on. In this paper, we focus on domain shifts, which occur when the model is applied to new domains that are different from the ones it was trained on, and propose a new approach called DG. Unlike previous approaches that aim to learn a single model that is domain invariant, DG leverages domain simila...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**In Search of Lost Domain Generalization** (2021)
- *Authors:* Gulrajani et al.
- *Direct Connection:* DomainBed formalized the DG setup with multiple labeled source domains and standardized evaluations, establishing the problem setting in which domain relations between sources and a target domain can be exploited.

**WILDS: A Benchmark of in-the-Wild Distribution Shifts** (2021)
- *Authors:* Koh et al.
- *Direct Connection:* WILDS introduced real-world datasets with explicit domain metadata (e.g., hospital IDs, time), providing the kind of side information this paper uses to learn and apply domain relations for reweighting experts.

**Domain Adaptation with Multiple Sources** (2009)
- *Authors:* Mansour et al.
- *Direct Connection:* The theory that a target predictor can be expressed as a weighted mixture of source hypotheses underlies this work’s strategy of learning per-domain functions and reweighting them via domain similarity for out-of-domain generalization.

### 💡 Inspiration

**Task2Vec: Task Embedding for Meta-Learning** (2019)
- *Authors:* Achille et al.
- *Direct Connection:* Task2Vec showed that quantifying task/domain similarity enables selecting or weighting specialized experts, inspiring the use of metadata-derived domain relations to gate combinations of domain-specific functions.

**Model Soups: Averaging Weights of Multiple Fine-Tuned Models Improves Accuracy without Increasing Inference Time** (2022)
- *Authors:* Wortsman et al.
- *Direct Connection:* Model Soups demonstrated that aggregating specialized models yields better generalization, motivating this paper’s principled, metadata-informed reweighting of domain-specific models at test time rather than uniform averaging.

### 🔍 Gap Identification

**Invariant Risk Minimization** (2019)
- *Authors:* Arjovsky et al.
- *Direct Connection:* IRM’s pursuit of a single domain-invariant predictor highlighted the limitation that one model cannot exploit meaningful variation across domains, motivating this paper’s shift to domain-specific functions reweighted by domain relations.

### 📊 Baseline

**Distributionally Robust Neural Networks for Group Shifts** (2020)
- *Authors:* Sagawa et al.
- *Direct Connection:* GroupDRO reweights domains during training but still learns a single hypothesis, providing the primary baseline that this work advances by instead reweighting domain-specific predictors at test time using metadata-derived domain relations.

---

## Synthesis: How Prior Work Led to This Paper

Invariant Risk Minimization proposed learning a single predictor whose features are invariant across domains, a powerful but restrictive stance when domain-specific variation carries predictive signal. GroupDRO similarly optimized for worst-case domain performance yet maintained one shared hypothesis, relying on training-time reweighting to handle group shift. DomainBed established the modern domain generalization protocol with multiple labeled source domains and rigorous evaluation, revealing that many invariant methods underperform strong baselines and encouraging alternative formulations. WILDS introduced real-world distribution shifts accompanied by rich domain metadata (such as site, region, or time), making explicit the side information that can encode relationships among domains. Classic multi-source adaptation theory by Mansour, Mohri, and Rostamizadeh showed that a target predictor can be well-approximated by a weighted mixture of source hypotheses when weights reflect source–target relatedness. Task2Vec provided a practical route to compute task/domain similarity and leverage it for expert selection or weighting. Model Soups further showed that combining specialized models improves generalization, suggesting that ensembles of domain-specialized functions can outperform a single shared model.

Together, these works point to a gap: single-model invariance leaves performance on the table when domains are related but not identical, and ensembles should be guided by how the target relates to sources. The current paper synthesizes these insights by training source-domain-specific functions and, at test time, reweighting them using domain relations learned from metadata, aligning practice with multi-source theory and exploiting real-world metadata to compute principled mixture weights with provable generalization benefits.

---

*Analysis generated on: 2026-01-06T18:44:34.191484*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

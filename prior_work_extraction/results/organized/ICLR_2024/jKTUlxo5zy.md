# Prior Work Analysis Report

## Target Paper

**Title:** Less is More: Fewer Interpretable Region via Submodular Subset Selection

**Conference:** ICLR 2024 (oral)

**Authors:** Ruoyu Chen, Hua Zhang, Siyuan Liang, Jingzhi Li, Xiaochun Cao

**Keywords:** Interpretable AI, Submodular subset selection, Explainable AI, Image Attribution

**Abstract:** 
> Image attribution algorithms aim to identify important regions that are highly relevant to model decisions. Although existing attribution solutions can effectively assign importance to target elements, they still face the following challenges: 1) existing attribution methods generate inaccurate small regions thus misleading the direction of correct attribution, and 2) the model cannot produce good attribution results for samples with wrong predictions. To address the above challenges, this paper...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Why Should I Trust You? Explaining the Predictions of Any Classifier** (2016)
- *Authors:* Marco Tulio Ribeiro et al.
- *Direct Connection:* This work introduced superpixel-based interpretable components for image explanations and a submodular-pick principle for diverse, succinct explanations, which directly motivates framing region-level explanation as a subset selection problem over interpretable regions.

**Learning to Explain: An Information-Theoretic Perspective on Model Interpretation** (2018)
- *Authors:* Jianbo Chen et al.
- *Direct Connection:* L2X formalized explanations as selecting a fixed-size subset that is sufficient for the prediction, which the paper adapts from feature vectors to spatial regions via a submodular objective and selection.

**An analysis of approximations for maximizing submodular set functions** (1978)
- *Authors:* George L. Nemhauser et al.
- *Direct Connection:* The paper’s greedy selection algorithm and its near-optimality rely on Nemhauser et al.’s 1−1/e guarantee for monotone submodular maximization under cardinality constraints.

### 💡 Inspiration

**Anchors: High-Precision Model-Agnostic Explanations** (2018)
- *Authors:* Marco Tulio Ribeiro et al.
- *Direct Connection:* Anchors’ emphasis on high-precision (confidence) constraints for local explanations informs the paper’s confidence requirement that the selected regions alone sustain the model’s decision.

**Understanding Deep Networks via Meaningful Perturbations** (2017)
- *Authors:* Ruth Fong et al.
- *Direct Connection:* The idea of finding minimal-area evidence that preserves the class score directly inspires replacing continuous mask optimization with discrete selection of few accurate regions under a principled objective.

### 📊 Baseline

**Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization** (2017)
- *Authors:* Ramprasaath R. Selvaraju et al.
- *Direct Connection:* As a primary baseline, Grad-CAM’s tendency to produce coarse, imprecise small regions and unrevealing maps on misclassified samples motivates the paper’s focus on selecting fewer, more accurate regions.

### 🔧 Extension

**Explanations from Deep Networks via Extremal Perturbations** (2019)
- *Authors:* Ruth Fong et al.
- *Direct Connection:* Building on extremal perturbations’ area-constrained evidence masks, the paper generalizes from a single contiguous mask to multiple discrete regions and embeds additional constraints via a submodular framework.

---

## Synthesis: How Prior Work Led to This Paper

Superpixel-based image explanations established that human-interpretable components can be formed by grouping pixels into regions and selecting a succinct subset, and the submodular-pick idea showed that a principled subset objective can encourage diversity and coverage in what is shown. High-precision local rules demonstrated that explanations should satisfy an explicit confidence requirement, ensuring that the evidence alone is sufficient for the prediction. Information-theoretic instance-wise feature selection framed explanations as choosing a fixed-size subset that maximizes sufficiency, linking explanation quality to how much of the prediction can be retained from a few selected elements. Perturbation-based saliency advanced the notion of minimal-area evidence that preserves the class score, while extremal perturbations formalized area-constrained masks that isolate the most supportive region. At the same time, gradient-based localization became the de facto baseline but often produced coarse, blob-like maps that fail to pin down accurate small regions and tend to falter on misclassified samples. Classic results on submodular maximization provided an efficient, theoretically grounded way to optimize set-valued objectives under size constraints.
These strands collectively suggested selecting a small set of spatial regions that is sufficient and precise, guided by explicit confidence-like constraints, yet computed via a discrete procedure with guarantees. The paper synthesizes these insights by casting image attribution as submodular subset selection over interpretable regions, designing a submodular utility that targets accurate small-region evidence, and imposing constraints for confidence, effectiveness, consistency, and collaboration to work robustly even on mispredictions—an evolution from continuous mask optimization and coarse heatmaps to principled, few-region selection with theoretical support.

---

*Analysis generated on: 2026-01-06T18:39:31.080062*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

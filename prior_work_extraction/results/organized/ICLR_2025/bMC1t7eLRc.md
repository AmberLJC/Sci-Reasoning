# Prior Work Analysis Report

## Target Paper

**Title:** Harnessing Diversity for Important Data Selection in Pretraining Large Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Chi Zhang, Huaping Zhong, Kuan Zhang, Chengliang Chai, Rui Wang, Xinlin Zhuang, Tianyi Bai, Qiu Jiantao, Lei Cao, Ju Fan, Ye Yuan, Guoren Wang, Conghui He

**Keywords:** LLMs, data selection, influence function, diversity

**Abstract:** 
> Data selection is of great significance in  pretraining large language models, given the  variation in quality within the large-scale available training corpora. 
To achieve this, researchers are currently investigating the use of data influence to measure the importance of data instances, $i.e.,$ a high influence score indicates that incorporating this instance to the training set is likely to enhance the model performance. Consequently, they select the top-$k$ instances with the highest scores...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Understanding Black-box Predictions via Influence Functions** (2017)
- *Authors:* Koh et al.
- *Direct Connection:* This work introduced the influence-function formalism that Quad adopts to quantify each pretraining instance’s effect on downstream performance, forming the core "quality" (importance) signal in the method.

### 💡 Inspiration

**GLISTER: Generalization based Data Subset Selection for Efficient and Robust Learning** (2021)
- *Authors:* Killamsetty et al.
- *Direct Connection:* GLISTER’s bi-level, generalization-aware subset selection with submodular objectives inspired Quad’s paradigm of combining a quality signal with explicit diversity constraints, adapted here with influence-based scoring for LLM pretraining.

### 🔍 Gap Identification

**Deduplicating Training Data Makes Language Models Better** (2022)
- *Authors:* Lee et al.
- *Direct Connection:* By showing redundancy in pretraining corpora harms LLMs and that semantic de-dup improves results, this paper motivates Quad’s explicit diversity modeling rather than pure top-k importance selection.

### 📊 Baseline

**Beyond neural scaling laws: beating power law scaling via data pruning** (2022)
- *Authors:* Sorscher et al.
- *Direct Connection:* This paper established top-k per-example scoring (e.g., EL2N) as an effective pruning baseline but with no explicit diversity control, a limitation Quad targets by coupling importance with diversity-aware selection.

### 🔧 Extension

**Estimating Training Data Influence by Tracing Gradient Descent (TracIn)** (2020)
- *Authors:* Pruthi et al.
- *Direct Connection:* TracIn provided a scalable approximation to influence that Quad directly builds on and improves, addressing its computational cost/noise when applied to web-scale LLM pretraining.

### 🔗 Related Problem

**Coresets for Data-efficient Training of Neural Networks** (2020)
- *Authors:* Mirzasoleiman et al.
- *Direct Connection:* This work’s facility-location style, gradient-based subset selection for diverse coverage informs Quad’s diversity term and greedy selection strategy when marrying influence scores with diversity.

---

## Synthesis: How Prior Work Led to This Paper

Influence functions introduced a principled way to estimate how upweighting a single training example would change a model’s loss, turning per-example influence into a measurable notion of "quality" for data selection. TracIn then provided a practical approximation by accumulating gradient alignments across training checkpoints, making influence-based scoring feasible at larger scales while revealing accuracy–efficiency trade-offs. In parallel, data pruning work demonstrated that simple per-example scores such as EL2N can beat scaling laws by dropping low-utility data, but these top-k strategies operate purely on a scalar importance axis. Subset-selection methods like GLISTER formalized combining a generalization-driven quality signal with submodular selection to avoid redundancy, and CRAIG operationalized diversity using facility-location objectives over gradient features with fast greedy maximization, highlighting how coverage and representativeness mitigate overfitting to narrow modes. Finally, deduplication for LLMs showed empirically that semantic redundancy in corpora degrades pretraining and that enforcing diversity improves downstream generalization, underscoring the need to look beyond raw importance.

Together these threads expose a clear opportunity: retain the theoretical fidelity of influence-based importance while explicitly preventing redundancy that plagues pure top-k selection, and do so at web scale where naïve influence computation is prohibitive. Quad naturally synthesizes these insights by using influence as the quality signal and a diversity-aware objective (in the spirit of facility location/submodularity) to select subsets, while addressing TracIn-style computational burdens with a tailored, efficient influence estimator suited for LLM pretraining.

---

*Analysis generated on: 2026-01-06T10:42:39.853418*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

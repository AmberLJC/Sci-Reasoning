# Prior Work Analysis Report

## Target Paper

**Title:** Rethinking Reward Modeling in Preference-based Large Language Model Alignment

**Conference:** ICLR 2025 (oral)

**Authors:** Hao Sun, Yunyi Shen, Jean-Francois Ton

**Keywords:** Bradley-Terry Model, Reward Modeling, Large Language Models

**Abstract:** 
> The Bradley-Terry (BT) model is a common and successful practice in reward modeling for Large Language Model (LLM) alignment. However, it remains unclear *why* this model --- originally developed for multi-player stochastic game matching --- can be adopted to convert pairwise response comparisons to reward values and make predictions. Especially given the fact that only a limited number of prompt-response pairs are sparsely compared with others. 
In this paper, we first establish the convergence...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The use of ranks to avoid the assumption of normality implicit in the analysis of variance** (1952)
- *Authors:* R. A. Bradley and M. E. Terry
- *Direct Connection:* Introduced the Bradley–Terry probabilistic choice model that underlies the standard pairwise-preference likelihood used in reward modeling, which this paper analyzes theoretically and questions as a necessary assumption.

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Direct Connection:* Established the preference-based RLHF pipeline by training a reward model with a Bradley–Terry likelihood on human comparisons, providing the exact problem formulation this work re-examines and theoretically grounds.

### 💡 Inspiration

**Learning to rank using gradient descent** (2005)
- *Authors:* Christopher J. C. Burges et al.
- *Direct Connection:* Introduced pairwise logistic (BT-style) learning with neural scoring functions (RankNet), which this work leverages when analyzing convergence of BT reward models parameterized by deep embeddings.

### 🔍 Gap Identification

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Yura Rafailov et al.
- *Direct Connection:* Derived a direct policy objective by assuming the BT link between preference probabilities and reward differences, whose reliance on the BT form this paper identifies as unnecessary by formalizing order-consistent alternatives.

### 📊 Baseline

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* Adopted BT-based reward modeling as the core of InstructGPT alignment, serving as the primary BT paradigm that this paper both provides theoretical justification for and relaxes via order-consistency.

### 🔧 Extension

**Rank Centrality: Ranking from Pairwise Comparisons** (2012)
- *Authors:* S. Negahban, S. Oh, and D. Shah
- *Direct Connection:* Provided statistical consistency and finite-sample rates for BTL under sparse comparison graphs, which this work extends to BT reward models with neural embeddings in LLM alignment settings.

### 🔗 Related Problem

**Learning to summarize with human feedback** (2020)
- *Authors:* Nisan Stiennon et al.
- *Direct Connection:* Demonstrated BT-trained reward models in NLP with sparse pairwise comparisons, directly motivating this paper’s analysis of convergence under sparse comparison graphs and its focus on ranking-preserving objectives.

---

## Synthesis: How Prior Work Led to This Paper

Bradley and Terry introduced the probabilistic choice model that connects pairwise preferences to latent scores via a logistic link, establishing the statistical foundation for inferring utilities from comparisons. Christiano et al. later embedded this Bradley–Terry likelihood into the RLHF pipeline, training reward models directly from human pairwise judgments and using them for downstream policy optimization. In large-scale NLP, Stiennon et al. showed this approach works under sparse pairwise comparisons for summarization, underscoring the practical regime where only a small comparison graph is observed. Ouyang et al. operationalized this recipe for instruction-following LLMs, making BT-based reward modeling the de facto baseline for alignment. Complementing these applications, Burges et al.’s RankNet framed pairwise logistic learning with neural scoring functions, an architectural viewpoint that directly links BT likelihoods to deep embeddings. On the theory side, Negahban, Oh, and Shah established consistency and rates for BTL under sparse comparison graphs, providing finite-sample guarantees that motivate extending such analyses to neural parameterizations. Rafailov et al. then derived DPO by assuming the BT mapping from reward differences to preference probabilities, tying downstream policy optimization tightly to BT.
Together, these works revealed a mature but BT-centric ecosystem: practical success with sparse comparisons, neural scoring architectures, and even direct policy optimization all lean on the BT link. This convergence highlighted a gap: alignment pipelines primarily need correct orderings, not calibrated rewards. Building on the neural pairwise-loss view and BTL statistical guarantees, the present work formalizes convergence for BT with deep embeddings and then relaxes the necessity of the BT assumption by elevating order consistency as the essential criterion for reward models.

---

*Analysis generated on: 2026-01-06T14:23:48.158647*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

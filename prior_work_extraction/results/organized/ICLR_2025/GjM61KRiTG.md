# Prior Work Analysis Report

## Target Paper

**Title:** Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Wenxuan Zhang, Philip Torr, Mohamed Elhoseiny, Adel Bibi

**Keywords:** Large Language Models, RLHF, Safety

**Abstract:** 
> Fine-tuning large language models (LLMs)  on human preferences, typically through reinforcement learning from human feedback (RLHF), has proven successful in enhancing their capabilities.  However, ensuring the safety of LLMs during fine-tuning remains a critical concern, and mitigating the potential conflicts in  safety and helpfulness  is costly in RLHF.  To address this issue, we propose a supervised learning framework called Bi-Factorial Preference Optimization (BFPO), which re-parameterizes...

---

## Key Prior Works (5 papers with direct influence)

### 🏗️ Foundation

**Learning to summarize with human feedback** (2020)
- *Authors:* Stiennon et al.
- *Direct Connection:* This work established the preference-based RLHF formulation (pairwise comparisons trained via a reward model and optimized with KL-regularized policy updates) that BFPO explicitly re-parameterizes into a supervised objective across two factors.

### 🔍 Gap Identification

**Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback** (2022)
- *Authors:* Bai et al.
- *Direct Connection:* This paper explicitly surfaced the tension between helpfulness and harmlessness and the high cost of jointly optimizing them with RLHF, a limitation BFPO targets by unifying them in a low-cost supervised preference objective.

### 📊 Baseline

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Ouyang et al.
- *Direct Connection:* As the canonical RLHF baseline (KL-regularized PPO on a learned reward), this paper’s objective is the joint helpfulness/safety RL formulation that BFPO replaces with a single supervised objective via a labeling function.

### 🔧 Extension

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Rafailov et al.
- *Direct Connection:* DPO’s key idea of reparameterizing KL-regularized RLHF into a supervised preference loss directly inspires BFPO, which extends this paradigm from single-objective pairwise preferences to a bi-factor, globally ranked labeling objective.

### 🔗 Related Problem

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Bai et al.
- *Direct Connection:* By showing how to balance harmlessness and helpfulness via AI feedback and principles, this work motivates BFPO’s need to encode multi-faceted safety-helpfulness tradeoffs directly in a learning objective rather than separate multi-stage procedures.

---

## Synthesis: How Prior Work Led to This Paper

Preference-based alignment first took shape in work showing that pairwise human comparisons could train a reward model and, via KL-regularized policy optimization, steer generation toward preferred behavior; the formulation crystallized the now-standard RLHF pipeline and its reliance on comparisons and a reference policy. Instruction-following alignment then scaled this recipe to general-purpose language models, codifying KL-regularized RLHF as the de facto baseline objective for helpful behavior while introducing practical recipes for preference collection and policy optimization. Subsequent alignment efforts focused not only on being useful but also on being harmless, documenting that optimizing both properties with RLHF is costly and can create conflicts when refusal and helpfulness interact. A complementary strand demonstrated that principles and AI feedback can reliably elicit harmlessness without excessive human labor, highlighting the importance of explicitly encoding safety-helpfulness tradeoffs. In parallel, direct preference optimization showed that the KL-regularized RLHF objective can be reparameterized as a supervised preference loss, avoiding explicit reward modeling and RL while retaining the same target solution. Together, these works exposed a gap: multi-objective (safety plus helpfulness) alignment remained expensive and conflict-prone under RLHF, while supervised preference methods were largely single-objective and pairwise. The natural next step is to fuse the supervised reparameterization idea with a multi-factor preference formulation, using a labeling function to capture global rankings across safety and helpfulness and optimize them jointly without RL—precisely the niche BFPO fills.

---

*Analysis generated on: 2026-01-06T19:42:41.348454*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Confronting Reward Model Overoptimization with Constrained RLHF

**Conference:** ICLR 2024 (spotlight)

**Authors:** Ted Moskovitz, Aaditya K Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca Dragan, Stephen Marcus McAleer

**Keywords:** rlhf, overoptimization, constrained RL

**Abstract:** 
> Large language models are typically aligned with human preferences by optimizing reward models (RMs) fitted to human feedback. However, human preferences are multi-faceted, and it is increasingly common to derive reward from a composition of simpler reward models which each capture a different aspect of language quality. This itself presents a challenge, as it is difficult to appropriately weight these component RMs when combining them. Compounding this difficulty, because any RM is only a proxy...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul Christiano et al.
- *Direct Connection:* Introduced the core RL-from-preferences pipeline of fitting a learned reward model from human feedback and optimizing a policy against it, which this paper adopts as the base alignment framework that becomes vulnerable to overoptimization.

**Fine-Tuning Language Models from Human Preferences** (2019)
- *Authors:* Daniel M. Ziegler et al.
- *Direct Connection:* Established the LM RLHF training objective with PPO and a KL penalty to a reference policy, which the present work modifies by augmenting the objective with per-component constraints rather than relying solely on scalarized rewards.

**Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* Demonstrated practical composite objectives by combining separate helpfulness and harmlessness reward models via a weighted sum, the exact setup whose weight-tuning fragility this paper replaces with constraint-based control.

### 💡 Inspiration

**Categorizing Variants of Goodhart’s Law** (2019)
- *Authors:* David Manheim et al.
- *Direct Connection:* Identified regressional and extremal Goodhart effects where proxy–goal correlations determine failure modes, inspiring this paper’s empirical analysis of how correlations among component RMs shift overoptimization points.

### 🔍 Gap Identification

**The Inverse Reward Design Problem** (2017)
- *Authors:* Dylan Hadfield-Menell et al.
- *Direct Connection:* Explicitly showed that learned reward proxies can be mis-specified and lead to undesirable behavior when optimized, motivating this paper’s focus on curbing overoptimization of RM proxies.

### 📊 Baseline

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* Serves as the canonical PPO+RM baseline whose scalar reward optimization the current paper improves upon by preventing reward model overoptimization via explicit constraints.

### 🔧 Extension

**Constrained Policy Optimization** (2017)
- *Authors:* Joshua Achiam et al.
- *Direct Connection:* Provides the constrained MDP formulation and policy-gradient machinery that this paper extends to RLHF by enforcing per-reward-model-component constraints during LM policy optimization.

---

## Synthesis: How Prior Work Led to This Paper

Human-in-the-loop reinforcement learning matured with the insight that a policy can be aligned by learning a reward model from pairwise human preferences and optimizing the policy against it, establishing the core preference-learning and policy-optimization loop. In language modeling, PPO-based RLHF with a KL penalty to a reference policy operationalized this idea at scale, defining the practical objective many systems use today. As alignment objectives became multi-faceted, practitioners began training multiple reward models—for helpfulness and harmlessness—and combining them by a weighted sum, thereby turning alignment into a composition problem whose behavior depends acutely on the chosen weights. Theoretical work on reward misspecification cautioned that learned reward proxies can be systematically wrong in parts of the state space; and Goodhart’s taxonomy clarified that when proxies correlate imperfectly with the true objective, optimization can drive behavior into regions where the proxy breaks down, particularly under extremal optimization. Constrained policy optimization, in parallel, provided a principled way to optimize a primary objective while keeping auxiliary quantities within specified limits via a constrained MDP formulation.
Together, these strands reveal a gap: composite RM scalarization is brittle and prone to Goodhart-type overoptimization, especially as component correlations and optimization pressure interact, while constrained optimization offers a natural alternative to weight-tuning. The current work synthesizes these insights by diagnosing how component-RM correlations determine overoptimization thresholds and by recasting RLHF as a constrained optimization problem that enforces per-component limits during policy updates, thereby preserving human-rated quality while pursuing improvement.

---

*Analysis generated on: 2026-01-06T06:51:49.184732*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

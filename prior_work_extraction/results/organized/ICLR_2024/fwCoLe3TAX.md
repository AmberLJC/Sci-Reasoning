# Prior Work Analysis Report

## Target Paper

**Title:** Improving Generalization of Alignment with Human Preferences through Group Invariant Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Rui Zheng, Wei Shen, Yuan Hua, Wenbin Lai, Shihan Dou, Yuhao Zhou, Zhiheng Xi, Xiao Wang, Haoran Huang, Tao Gui, Qi Zhang, Xuanjing Huang

**Keywords:** alignment, language model, invariant learning

**Abstract:** 
> The success of AI assistants based on language models (LLMs) hinges crucially on Reinforcement Learning from Human Feedback (RLHF), which enables the generation of responses more aligned with human preferences. 
As universal AI assistants, there's a growing expectation for them to perform consistently across various domains. 
However, previous work shows that Reinforcement Learning (RL) often exploits shortcuts to attain high rewards and overlooks challenging samples.
This focus on quick reward ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* Established the RLHF pipeline—supervised fine-tuning, reward modeling, and PPO-based policy optimization—that this paper seeks to make group-invariant and robust across domains.

**Invariant Risk Minimization** (2020)
- *Authors:* Martin Arjovsky et al.
- *Direct Connection:* Formulates learning predictors invariant across environments, providing the invariance principle motivating a policy whose preference-consistent behavior holds across inferred groups.

**Fairness Without Demographics in Repeated Loss Minimization** (2018)
- *Authors:* Tatsunori B. Hashimoto et al.
- *Direct Connection:* Shows how to improve worst-case subgroup performance without demographic labels via distributionally robust optimization, motivating group-agnostic robustness in alignment without group annotations.

### 💡 Inspiration

**Environment Inference for Invariant Learning** (2021)
- *Authors:* Elliot Creager et al.
- *Direct Connection:* Proposes inferring latent environments by adversarially splitting data to maximize invariance violations, inspiring this paper’s automatic grouping step that maximizes performance variance before group-robust optimization.

### 🔍 Gap Identification

**Learning to summarize with human feedback** (2020)
- *Authors:* Nisan Stiennon et al.
- *Direct Connection:* Documents that optimizing against learned reward models can induce shortcut exploitation and misaligned behavior, motivating robustness mechanisms that prevent RL from ignoring hard examples.

### 📊 Baseline

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Rafailov et al.
- *Direct Connection:* Provides the direct preference optimization objective that the authors adapt into a group-aware, worst-group–focused training scheme to improve alignment generalization.

### 🔧 Extension

**Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization** (2020)
- *Authors:* Shiori Sagawa et al.
- *Direct Connection:* Introduces worst-group (Group DRO) training, whose min–max principle is directly adapted to preference/RL objectives to prioritize challenging groups during policy learning.

---

## Synthesis: How Prior Work Led to This Paper

Instruction-tuned RLHF systems were crystallized by work showing that supervised fine-tuning, reward modeling, and PPO can steer large language models toward human-preferred behavior. Direct Preference Optimization reframed alignment as a supervised objective on pairwise preferences, avoiding explicit reward models while preserving the core preference-optimization setup. In parallel, robustness research developed worst-group optimization, demonstrating that ERM overfits majority patterns and that Group DRO’s min–max objective elevates performance on hard or minority groups. Invariant Risk Minimization formalized the aim of predictors whose conditional relationships remain stable across environments, while Environment Inference for Invariant Learning showed that, when group labels are absent, one can adversarially partition data to expose invariance violations. Fairness Without Demographics established that worst-case performance can be improved without group annotations via distributionally robust optimization, laying groundwork for group-agnostic robustness. Empirically, RLHF work on summarization revealed that directly optimizing learned rewards invites shortcut exploitation and degraded generalization.
Together, these strands reveal a gap: preference-optimized RLHF methods optimize average reward and can exploit spurious shortcuts, yet group labels needed for robust training are unavailable. The natural next step is to infer groups that accentuate performance disparities, then couple preference/RL objectives with a worst-group or invariance-guided criterion. This paper synthesizes DPO/RLHF training with EIIL-style group discovery and Group DRO/IRM principles, yielding a policy that focuses learning on challenging groups to generalize alignment consistently across domains.

---

*Analysis generated on: 2026-01-06T06:17:12.802353*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment

**Conference:** ICLR 2025 (spotlight)

**Authors:** Chenliang Li, Siliang Zeng, Zeyi Liao, Jiaxiang Li, Dongyeop Kang, Alfredo Garcia, Mingyi Hong

**Keywords:** Alignment, Inverse Reinforcement Learning, Reinforment Learning from Human Feedback

**Abstract:** 
> Aligning to human preferences and/or intentions is an important requirement for contemporary foundation models. To ensure alignment, popular approaches such as reinforcement learning with human feedback (RLHF) break down the task into three stages: (i) a model is computed with supervised fine-tuning (SFT) based upon large demonstrations data, (ii) a reward model (RM) is estimated based upon human feedback data, and (iii) reinforcement learning (RL) is used to further refine the SFT model by opti...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Direct Connection:* We adopt the Bradley–Terry preference likelihood introduced here for modeling human comparisons and generalize the reward estimation to also condition on demonstrations within our joint optimization.

**Fine-Tuning Language Models from Human Preferences** (2019)
- *Authors:* Daniel M. Ziegler et al.
- *Direct Connection:* This work established KL-regularized RLHF for language models, whose KL-constrained policy optimization we embed inside our joint objective that couples reward learning with policy updates.

### 💡 Inspiration

**Learning Robust Rewards with Adversarial Inverse Reinforcement Learning** (2018)
- *Authors:* Justin Fu et al.
- *Direct Connection:* AIRL jointly trains reward and policy via adversarial learning; we borrow the joint-estimation principle but replace the adversarial setup with a tractable likelihood-based formulation tailored to human feedback and demonstrations.

### 🔍 Gap Identification

**Direct Preference Optimization: Your Language Model Is Secretly a Reward Model** (2023)
- *Authors:* Avi Singh Rafailov et al.
- *Direct Connection:* DPO derives a preference-odds objective that bypasses explicit reward learning and cannot exploit demonstrations, a limitation we address by learning an explicit reward from both demonstrations and preferences while optimizing the policy.

### 📊 Baseline

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* The three-stage RLHF pipeline (SFT → reward model from human preferences → KL-regularized PPO) from this work is the primary baseline our method replaces with a single joint reward–policy objective that also incorporates demonstration likelihood.

### 🔧 Extension

**Reward learning from human preferences and demonstrations in Atari** (2018)
- *Authors:* Daniel Ibarz et al.
- *Direct Connection:* They showed reward learning improves by combining demonstrations with preferences; we extend this idea to LLM alignment and make it tractable by jointly fitting the reward with the policy using both data sources.

---

## Synthesis: How Prior Work Led to This Paper

Pairwise preference modeling for reward learning was formalized by Christiano et al., who introduced the Bradley–Terry likelihood connecting human comparisons to reward differences. In language settings, Ziegler et al. extended this paradigm into a KL-regularized RLHF framework where a policy is optimized against a learned preference reward while constrained to a reference model. Ouyang et al. then popularized the three-stage RLHF pipeline—SFT from demonstrations, reward modeling from human preferences, and KL-regularized PPO—which became the de facto baseline but trained the reward solely on preference data. Ibarz et al. provided a crucial insight: reward estimation improves when demonstrations are combined with human preferences, showing better policy performance in Atari by leveraging both data sources. Independently, AIRL demonstrated that reward and policy can be learned jointly, using an adversarial objective to alternate reward inference and policy updates. More recently, DPO showed that policy optimization can be derived directly from preference odds without an explicit reward model, tightening the link between reward and policy but discarding the ability to ingest demonstrations into reward learning.

Taken together, these works expose a gap: modern LLM alignment either learns rewards from preferences alone or bypasses rewards entirely, neglecting the complementary information in demonstrations and the benefits of joint estimation. The present work synthesizes these threads by unifying Bradley–Terry preference modeling with a demonstration-informed likelihood under a KL-regularized policy update, yielding a tractable joint reward–policy learning objective that leverages both demonstrations and human feedback to improve alignment.

---

*Analysis generated on: 2026-01-06T06:45:49.988277*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

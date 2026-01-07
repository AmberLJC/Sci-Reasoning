# Prior Work Analysis Report

## Target Paper

**Title:** Query-Policy Misalignment in Preference-Based Reinforcement Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Xiao Hu, Jianxiong Li, Xianyuan Zhan, Qing-Shan Jia, Ya-Qin Zhang

**Keywords:** preference-based reinforcement learning, human feedback efficiency, query-policy misalignment

**Abstract:** 
> Preference-based reinforcement learning (PbRL) provides a natural way to align RL agents’ behavior with human desired outcomes, but is often restrained by costly human feedback. To improve feedback efficiency, most existing PbRL methods focus on selecting queries to maximally improve the overall quality of the reward model, but counter-intuitively, we find that this may not necessarily lead to improved performance. To unravel this mystery, we identify a long-neglected issue in the query selectio...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Paul F. Christiano et al.
- *Direct Connection:* The paper adopts Christiano et al.’s PbRL formulation—learning a reward model from pairwise trajectory-segment preferences and optimizing a policy against it—and directly questions the common uncertainty-driven query heuristic used within this loop.

**Active Preference-Based Learning of Reward Functions** (2017)
- *Authors:* Dorsa Sadigh et al.
- *Direct Connection:* This work established information-gain–based query selection for preference learning, which the current paper shows can be misaligned with policy improvement and therefore motivates a policy-aligned query objective.

### 💡 Inspiration

**A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger)** (2011)
- *Authors:* Stéphane Ross et al.
- *Direct Connection:* DAgger’s insight that supervision should be collected on the learner’s own state distribution directly inspires aligning query selection with the current policy’s occupancy to avoid covariate shift.

**Value-Aware Model Learning** (2017)
- *Authors:* Amir-massoud Farahmand et al.
- *Direct Connection:* The value-aware principle—optimizing models for downstream control rather than pure predictive accuracy—provides the conceptual basis for replacing reward-model–centric query objectives with policy-aligned ones.

### 🔍 Gap Identification

**Batch Active Preference-Based Learning of Reward Functions** (2019)
- *Authors:* Emre Bıyık et al.
- *Direct Connection:* Bıyık et al.’s batch active preference selection focuses on globally improving reward-model fidelity, a strategy the present paper identifies as prone to query–policy misalignment that yields little policy benefit.

### 📊 Baseline

**PEBBLE: Feedback-Efficient Reinforcement Learning via Bootstrapped Labeling** (2021)
- *Authors:* H. Lee et al.
- *Direct Connection:* PEBBLE’s ensemble-disagreement query selection and replay-based training are taken as a leading feedback-efficient PbRL baseline that the new method modifies via policy-aligned querying and hybrid experience replay to convert labels into larger policy gains.

---

## Synthesis: How Prior Work Led to This Paper

Pairwise-preference–based reward modeling for policy optimization was crystallized by Christiano et al., who trained a reward model from trajectory comparisons and optimized an RL agent against it; they also popularized ensemble uncertainty as a practical signal for choosing which comparisons to label. In parallel, Sadigh et al. formalized active preference-based learning by selecting queries that maximize expected information gain about the reward, thereby centering query design on improving global reward-model fidelity. Bıyık et al. extended this line to batch active preference learning, operationalizing uncertainty- and information-centric selection in scalable settings while keeping the objective squarely on reward estimation quality. Building on these ideas, PEBBLE introduced a feedback-efficient PbRL system that samples trajectory pairs from replay and uses ensemble disagreement to pick informative comparisons, becoming a de facto baseline for label efficiency. Outside preference learning, DAgger demonstrated that supervision must be gathered on the learner’s own state distribution to avoid covariate shift, while value-aware model learning argued that learning signals should be aligned with downstream control performance rather than pure predictive accuracy. Together, these works exposed a gap: uncertainty- or information-driven queries can improve the reward model yet offer limited policy benefit because they are not aligned with the agent’s evolving occupancy. The present paper synthesizes these insights by diagnosing query–policy misalignment and introducing policy-aligned query selection plus hybrid experience replay, ensuring that labeled comparisons are both informative and situated where they most impact the current policy’s learning dynamics.

---

*Analysis generated on: 2026-01-06T13:30:52.860154*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

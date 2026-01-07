# Prior Work Analysis Report

## Target Paper

**Title:** Learning from negative feedback, or positive feedback or both

**Conference:** ICLR 2025 (spotlight)

**Authors:** Abbas Abdolmaleki, Bilal Piot, Bobak Shahriari, Jost Tobias Springenberg, Tim Hertweck, Michael Bloesch, Rishabh Joshi, Thomas Lampe, Junhyuk Oh, Nicolas Heess, Jonas Buchli, Martin Riedmiller

**Keywords:** Preference Optimization, Policy Optimization, Negative Feedback, Positive feedback, Reinforcement Learning, Probabilistic Inference

**Abstract:** 
> Existing preference optimization methods often assume scenarios where paired preference feedback (preferred/positive vs. dis-preferred/negative examples) is available. This requirement limits their applicability in scenarios where only unpaired feedback—for example, either positive or negative— is available. To address this, we introduce a novel approach that decouples learning from positive and negative feedback. This decoupling enables control over the influence of each feedback type and, impo...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Using Expectation-Maximization for Reinforcement Learning** (1997)
- *Authors:* Dayan et al.
- *Direct Connection:* This work provides the probabilistic EM formulation for control—optimizing the probability of successful outcomes—that the current paper adopts and extends to decouple positive and negative feedback channels.

**Deep Reinforcement Learning from Human Preferences** (2017)
- *Authors:* Christiano et al.
- *Direct Connection:* This work established the paired-preference formulation (via Bradley–Terry comparisons) that modern preference optimization builds on, whose paired-data requirement is explicitly relaxed by the proposed decoupled approach.

### 🔍 Gap Identification

**Reinforcement Learning by Reward-Weighted Regression** (2007)
- *Authors:* Peters et al.
- *Direct Connection:* Reward-Weighted Regression instantiates the EM idea with strictly positive weights tied to returns, which inherently prevents learning from negative-only feedback and directly motivates the paper’s decoupled positive/negative weighting scheme.

**Kahneman–Tversky Optimization: Supervised Fine-Tuning for Human Preferences** (2024)
- *Authors:* Ethayarajh et al.
- *Direct Connection:* KTO proposes training with unpaired positive/negative labels but relies on heuristic prospect-theory weights; the present work replaces this with a principled EM probabilistic framework and achieves stable learning from negative-only signals.

### 📊 Baseline

**Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023)
- *Authors:* Rafailov et al.
- *Direct Connection:* DPO’s pairwise log-odds objective is a main baseline the paper generalizes beyond by enabling learning from unpaired and negative-only feedback through an EM-based decoupled likelihood objective.

### 🔧 Extension

**Maximum a Posteriori Policy Optimization** (2018)
- *Authors:* Abdolmaleki et al.
- *Direct Connection:* The paper extends MPO’s KL-regularized EM updates by replacing reward-based weightings with separate positive/negative likelihood factors, yielding stable policy updates even from negative-only data.

---

## Synthesis: How Prior Work Led to This Paper

Dayan and Hinton introduced an EM-based view of reinforcement learning that treats control as probabilistic inference over successful outcomes, optimizing the likelihood of positive events rather than expected return. Peters and Schaal instantiated this idea with Reward-Weighted Regression, where policy updates are driven by strictly positive weights proportional to returns, providing an efficient M-step but implicitly precluding learning purely from negative evidence. Abdolmaleki and colleagues advanced this EM lineage with Maximum a Posteriori Policy Optimization, combining an E-step weighting with a KL-regularized M-step that stabilizes policy updates under off-policy data and noisy estimates. In human preference learning, Christiano et al. formalized pairwise preference supervision via Bradley–Terry models, anchoring modern preference optimization on paired comparisons. Building on that, Rafailov et al. proposed Direct Preference Optimization, a direct log-odds objective that still fundamentally requires paired samples. Ethayarajh et al. later explored unpaired binary feedback via Kahneman–Tversky-inspired losses, suggesting a practical route to positive- or negative-only labels but relying on heuristic weighting that can be unstable, especially for negative-only training. Together these works outline a principled EM toolkit for control, effective KL-regularized policy updates, and preference-learning practices still constrained by paired data or heuristic losses. The present paper unifies these strands by recasting preference optimization within the EM control-as-inference framework and explicitly decoupling positive and negative likelihoods, thereby preserving MPO-style stability while eliminating the paired-data requirement and enabling reliable learning from negative-only feedback—a natural next step given the identified methodological gaps.

---

*Analysis generated on: 2026-01-06T10:57:33.720018*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

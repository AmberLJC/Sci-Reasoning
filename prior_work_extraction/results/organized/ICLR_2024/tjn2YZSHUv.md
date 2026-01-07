# Prior Work Analysis Report

## Target Paper

**Title:** Social Reward: Evaluating and Enhancing Generative AI through Million-User Feedback from an Online Creative Community

**Conference:** ICLR 2024 (spotlight)

**Authors:** Arman Isajanyan, Artur Shatveryan, David Kocharian, Zhangyang Wang, Humphrey Shi

**Keywords:** human feedback, text to image, generative AI, image quality scoring

**Abstract:** 
> Social reward as a form of community recognition provides a strong source of
motivation for users of online platforms to actively engage and contribute with
content to accumulate peers approval. In the realm of text-conditioned image
synthesis, the recent surge in progress has ushered in a collaborative era where
users and AI systems coalesce to refine visual creations. This co-creative pro-
cess in the landscape of online social networks empowers users to craft original
visual artworks seeking ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation** (2023)
- *Authors:* Omer M. Kirstain et al.
- *Direct Connection:* Social Reward adopts the pairwise preference learning formulation established by Pick-a-Pic and replaces explicit user comparisons with implicit large-scale social engagement to supervise the reward model.

### 🔍 Gap Identification

**CLIPScore: A Reference-free Evaluation Metric for Image Captioning** (2021)
- *Authors:* Ari Holtzman Hessel et al.
- *Direct Connection:* The paper targets the known gap that CLIPScore’s text-image similarity does not reliably reflect community preference, motivating a reward learned from social approval rather than alignment alone.

**TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering** (2023)
- *Authors:* Jesse Vig et al.
- *Direct Connection:* By focusing on faithfulness via QA, TIFA highlights that alignment-centric metrics overlook popularity and aesthetic appeal—precisely the aspects Social Reward captures through social engagement signals.

### 📊 Baseline

**Human Preference Score v2 (HPS v2): A Stronger Metric for Text-to-Image Evaluation** (2023)
- *Authors:* Mert Çelik et al.
- *Direct Connection:* HPS v2 serves as the primary human-preference baseline that Social Reward is designed to outperform, explicitly addressing HPS v2’s limitation of relying on limited-size crowdsourced pairwise labels.

### 🔧 Extension

**PickScore: Lifting CLIP to Predict Human Preferences in Text-to-Image Generation** (2023)
- *Authors:* Omer M. Kirstain et al.
- *Direct Connection:* The method extends PickScore’s idea of training a CLIP-based preference predictor by retraining the scorer on organic community feedback and using it for both evaluation and generation steering.

**ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation** (2023)
- *Authors:* Yifan Xu et al.
- *Direct Connection:* Social Reward directly builds on ImageReward’s reward-modeling framework for T2I, but replaces lab-curated pairwise annotations with implicit social signals to attain much larger scale and stronger alignment with in-the-wild preferences.

---

## Synthesis: How Prior Work Led to This Paper

Pick-a-Pic introduced large-scale, prompt-conditioned pairwise preference data and a comparative learning formulation that turns human choices into a learnable ranking signal, establishing how to train preference models for text-to-image outputs. Building on this, PickScore showed that a CLIP-based scorer trained on such pairwise judgments can predict which image people prefer, and can even guide generation by scoring candidates. ImageReward generalized this paradigm into a reward-modeling framework specifically tailored to T2I, demonstrating that a learned reward can both evaluate and steer diffusion models when trained on curated human comparisons. Concurrently, HPS v2 refined human-preference metrics via carefully collected crowdsourced pairs, setting a strong but scale-limited baseline for preference-aligned evaluation. In contrast, alignment-centric measures like CLIPScore optimized similarity to the prompt rather than human appeal, while TIFA used question answering to test faithfulness, emphasizing semantic correctness but not community desirability or aesthetics. Together these works established how to learn preference signals for T2I, revealed the strength and limits of curated pairwise data, and exposed gaps in alignment-only evaluation. The natural next step was to preserve the reward-modeling machinery of Pick-a-Pic/PickScore/ImageReward while replacing scarce, lab-style annotations with abundant, real-world social engagement. By training a reward on implicit feedback from a massive creative community and then using it for both evaluation and generation steering, the current work fuses scalability with ecological validity to align image generation with what communities actually value.

---

*Analysis generated on: 2026-01-06T07:41:53.131514*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

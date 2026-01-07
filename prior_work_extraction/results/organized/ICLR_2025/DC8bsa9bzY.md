# Prior Work Analysis Report

## Target Paper

**Title:** Estimating the Probabilities of Rare Outputs in Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Gabriel Wu, Jacob Hilton

**Keywords:** low probabilities, adversarial training, importance sampling

**Abstract:** 
> We consider the problem of *low probability estimation*: given a machine learning model and a formally-specified input distribution, how can we estimate the probability of a binary property of the model's output, even when that probability is too small to estimate by random sampling? This problem is motivated by the need to improve worst-case performance, which distribution shift can make much more likely. We study low probability estimation in the context of argmax sampling from small transform...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**The Cross-Entropy Method: A Unified Approach to Combinatorial Optimization, Monte-Carlo Simulation, and Machine Learning** (2004)
- *Authors:* Rubinstein and Kroese
- *Direct Connection:* The paper’s importance-sampling estimator and adaptive proposal search directly instantiate the cross-entropy method’s rare-event simulation recipe to concentrate sampling on failure-inducing inputs while maintaining unbiased likelihood-ratio estimates of tiny probabilities.

**Red Teaming Language Models** (2022)
- *Authors:* Perez et al.
- *Direct Connection:* This work established systematic adversarial prompt search to elicit undesirable LM behaviors, which the current paper formalizes as an importance-sampling procedure to quantify the probability of such behaviors under a specified input distribution rather than merely discovering them.

### 💡 Inspiration

**Adaptive Stress Testing: Finding Likely Failure Events with Reinforcement Learning** (2018)
- *Authors:* Lee et al.
- *Direct Connection:* Adaptive Stress Testing’s core idea—searching input space to uncover rare failures and using importance sampling to estimate their probabilities in black-box systems—directly motivates translating the same rare-event estimation paradigm to language models and prompt distributions.

**Towards Open Set Deep Networks (OpenMax) using Extreme Value Theory** (2016)
- *Authors:* Bendale and Boult
- *Direct Connection:* OpenMax’s EVT-based tail modeling of logits motivates the paper’s activation-extrapolation approach of fitting a distribution to model logits and extrapolating to estimate tail probabilities for rare outputs under argmax decoding.

### 🔍 Gap Identification

**Universal and Transferable Adversarial Attacks on Aligned Language Models (Jailbroken)** (2023)
- *Authors:* Zou et al.
- *Direct Connection:* By showing that safety-tuned models can still be reliably jailbroken with synthesized prompts, this work exposes the gap of not quantifying how likely such failures are, which the paper addresses by estimating their probabilities under a formal input distribution.

### 🔗 Related Problem

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Bai et al.
- *Direct Connection:* By demonstrating that adversarially sourced data and feedback reduce harmful outputs, this paper provides the adversarial-training paradigm that the present work generalizes by directly minimizing an estimated rare-event probability instead of training on a fixed adversarial set.

**On Calibration of Modern Neural Networks** (2017)
- *Authors:* Guo et al.
- *Direct Connection:* The finding that simple parametric transforms of logits (e.g., temperature scaling) calibrate predicted probabilities underpins the paper’s idea of modeling logit distributions and extrapolating them to estimate very small probabilities.

---

## Synthesis: How Prior Work Led to This Paper

Rare-event simulation offers a blueprint for quantifying tiny probabilities: the cross-entropy method prescribes adaptively reshaping sampling distributions toward failure regions while correcting with likelihood ratios to retain unbiased estimates, and Adaptive Stress Testing converts this idea into black-box search that locates likely failures and estimates their probabilities. In language models, red teaming introduced systematic adversarial prompt search to elicit undesirable behaviors, and Constitutional AI demonstrated how adversarially sourced data and feedback reduce harmful outputs, establishing adversarial training as a practical mitigation. On the modeling side, OpenMax applied extreme value theory to the tails of logit-like scores, showing that fitted tail distributions can extrapolate rare outcomes, while calibration work demonstrated that simple parametric transformations of logits can accurately reflect probabilities, suggesting that the shape of logit distributions carries usable probabilistic information. Jailbreak studies further revealed that safety-tuned models still succumb to carefully constructed prompts, underscoring the need to quantify—not just find—failures.
Taken together, these strands suggest a natural next step: treat adversarial prompt search as a principled importance-sampling procedure to estimate extremely small failure probabilities under a specified input distribution, and complement it with tail modeling of logits to extrapolate beyond feasible sampling regimes. Building on rare-event IS and stress-testing, the paper adapts search-and-reweight techniques to LM prompts; drawing from EVT and calibration, it fits distributions to logits for activation extrapolation. Finally, by optimizing the estimated probability itself, it generalizes adversarial training from minimizing observed failures on curated sets to directly minimizing the modeled prevalence of undesirable behaviors.

---

*Analysis generated on: 2026-01-06T07:09:22.887290*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Faster Cascades via Speculative Decoding

**Conference:** ICLR 2025 (oral)

**Authors:** Harikrishna Narasimhan, Wittawat Jitkrittum, Ankit Singh Rawat, Seungyeon Kim, Neha Gupta, Aditya Krishna Menon, Sanjiv Kumar

**Keywords:** Cascades, Speculative Decoding, Speculative execution, LLM, Inference, Adaptive Inference

**Abstract:** 
> Cascades and speculative decoding are two common approaches to improving language models' inference efficiency.  Both approaches interleave two models, but via fundamentally distinct mechanisms: deferral rule that invokes the larger model only for “hard” inputs, while  speculative decoding uses speculative execution to primarily invoke the larger model in parallel scoring mode. These mechanisms offer different benefits: empirically, cascades offer compelling cost-quality trade-offs, often even o...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Fast Inference from Transformers via Speculative Decoding** (2023)
- *Authors:* Yael Leviathan et al.
- *Direct Connection:* Introduces the quality-neutral speculative decoding mechanism—drafting with a small model and verifying with a large model in parallel—which this paper repurposes to implement cascade deferral via speculative execution.

**Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer to a Human** (2018)
- *Authors:* Jesse Madras et al.
- *Direct Connection:* Formalizes the learning-to-defer decision rule—invoking a stronger expert when uncertain—which directly underpins the optimal deferral formulation derived for cascading between small and large LMs.

**On Optimum Recognition Error and Reject Tradeoff** (1970)
- *Authors:* C. K. Chow
- *Direct Connection:* Derives the optimal reject (deferral) rule based on posteriors and reject cost, which this paper adapts to characterize the optimal deferral criterion for speculative cascades.

### 💡 Inspiration

**SelectiveNet: A Deep Neural Network with an Integrated Reject Option** (2019)
- *Authors:* Yoav Geifman et al.
- *Direct Connection:* Provides a practical risk–coverage framework and plug-in confidence-based gating for selective prediction, which motivates this paper’s plug-in approximation to the optimal deferral rule.

### 📊 Baseline

**FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance** (2023)
- *Authors:* Jiang et al.
- *Direct Connection:* Establishes LLM cascades that route to stronger models only for hard inputs and demonstrates superior cost–quality trade-offs, providing the primary cascade baseline that this paper accelerates using speculative execution.

### 🔗 Related Problem

**Accelerating Large Language Model Decoding with Speculative Sampling** (2023)
- *Authors:* Chen et al.
- *Direct Connection:* Generalizes speculative decoding to sampling-based generation and highlights that speedups preserve the large model’s distribution, a property this paper leverages while embedding a deferral rule into speculative execution.

**Confident Adaptive Language Modeling** (2022)
- *Authors:* Tal Schuster et al.
- *Direct Connection:* Demonstrates token-level adaptive inference for LMs via confidence thresholds and calibration, informing the design of lightweight, confidence-driven deferral rules in the proposed speculative cascade.

---

## Synthesis: How Prior Work Led to This Paper

Speculative decoding established a quality-neutral path to faster generation by having a lightweight draft model propose tokens that a larger model verifies in parallel, ensuring the final distribution matches the large model. Subsequent speculative sampling broadened this to stochastic decoding while reinforcing that gains come from parallel verification rather than changing the target distribution. In parallel, cascaded decision-making matured through formal learning-to-defer frameworks that trigger a stronger expert when uncertainty is high, and selective prediction methods that operationalize risk–coverage trade-offs using confidence-based, plug-in gates. SelectiveNet showed how to implement practical reject options with calibrated confidence, while classical results on reject-option optimality precisely characterize when deferral minimizes expected cost given error penalties. For language models specifically, confident adaptive inference demonstrated that calibrated confidence thresholds can guide early exits and token-level adaptivity, and FrugalGPT exhibited that model cascades—invoking larger models only for hard inputs—can beat single-model baselines on cost–quality trade-offs. Together, these works reveal a gap: classical cascades provide strong cost–quality gains but lack the quality-neutral speedups of speculative execution, while speculative methods ensure neutrality yet do not exploit deferral-based cost–quality improvements. The current paper synthesizes these threads by implementing the cascade deferral rule through speculative execution, deriving the optimal deferral criterion in the reject-option sense, and using a plug-in approximation to realize it in practice—thereby unifying cascade routing benefits with the parallel, quality-preserving advantages of speculative decoding.

---

*Analysis generated on: 2026-01-06T19:56:13.933896*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

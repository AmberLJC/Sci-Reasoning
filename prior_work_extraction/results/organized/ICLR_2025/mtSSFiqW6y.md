# Prior Work Analysis Report

## Target Paper

**Title:** Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment

**Conference:** ICLR 2025 (oral)

**Authors:** Gregor Bachmann, Sotiris Anagnostidis, Albert Pumarola, Markos Georgopoulos, Artsiom Sanakoyeu, Yuming Du, Edgar Schönfeld, Ali Thabet, Jonas K Kohler

**Keywords:** LLM inference, speculative decoding

**Abstract:** 
> The performance of large language models (LLMs) is closely linked to their underlying size, leading to ever-growing networks and hence slower inference. Speculative decoding has been proposed as a technique to accelerate autoregressive generation, leveraging a fast draft model to propose candidate tokens, which are then verified in parallel based on their likelihood under the target model. While this approach guarantees to reproduce the target output, it incurs a substantial penalty: many high-q...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Speculative Decoding** (2023)
- *Authors:* Chen et al.
- *Direct Connection:* Introduced the draft-and-verify paradigm where a fast draft model proposes multiple future tokens that are verified by the target model’s likelihood to preserve exact sampling, whose verification step Judge Decoding explicitly replaces with a learned judge to increase acceptance.

**Blockwise Parallel Decoding for Autoregressive Models** (2018)
- *Authors:* Stern et al.
- *Direct Connection:* Established the general propose-then-verify template for accepting multiple tokens per target-model evaluation, which Judge Decoding keeps structurally while altering the verification criterion away from strict log-probability agreement.

### 💡 Inspiration

**LLM-as-a-Judge: Assessing Generation Quality with LLM Feedback** (2023)
- *Authors:* Zheng et al.
- *Direct Connection:* Demonstrated that LLMs can reliably evaluate textual quality and preference beyond likelihood, directly inspiring Judge Decoding’s use of a learned judge model to verify proposed tokens based on utility rather than exact alignment.

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Bai et al.
- *Direct Connection:* Showed that AI feedback (a rules- or preference-based judge) can steer generation quality, which Judge Decoding adapts by learning a verifier to certify acceptable continuations and thus raise acceptance rates.

### 📊 Baseline

**Medusa: Simple Framework for High-Throughput LLM Inference** (2024)
- *Authors:* Cai et al.
- *Direct Connection:* Uses multi-head drafts with standard alignment-based verification, whose early-rejection bottleneck Judge Decoding directly addresses by swapping in a utility-aware judge that accepts semantically valid continuations even when target probabilities disagree.

**EAGLE: Efficient Autoregressive Generation via Lookahead** (2024)
- *Authors:* Li et al.
- *Direct Connection:* Implements self-speculative decoding that still verifies tokens by target-model likelihood, providing a primary competitor whose alignment-limited acceptance Judge Decoding overcomes with a judge-driven verifier.

---

## Synthesis: How Prior Work Led to This Paper

Speculative Decoding established the modern draft-and-verify recipe: a small model proposes several tokens that are accepted only if the target model’s likelihood validates every step, ensuring exactness but tightly coupling acceptance to probability alignment. Earlier, Blockwise Parallel Decoding introduced the same structural idea—multi-step proposals followed by verification with the base model—demonstrating how parallelization hinges on the verifier’s acceptance behavior. Medusa advanced throughput by attaching multi-token prediction heads yet retained the same alignment-based acceptance rule, revealing that early rejections dominate when proposals diverge from the target’s local likelihood. EAGLE pursued self-speculation using internal lookahead to reduce target calls, but verification still depended on the target’s next-token probabilities, leaving acceptance constrained by cross-entropy gaps. In parallel, LLM-as-a-Judge showed that models can reliably grade or prefer responses without relying on token likelihoods, pointing to a utility-oriented criterion for evaluating text. Constitutional AI further demonstrated that AI feedback, instantiated as a rule- or preference-based judge, can steer and certify outputs effectively.
Taken together, these works exposed a bottleneck: acceptance in speculative methods is limited by strict probability alignment, even when proposed tokens are high quality. The natural next step is to decouple verification from target likelihood while retaining the efficient draft-and-verify structure. Judge Decoding synthesizes this by replacing alignment-based checks with a learned judge that certifies utility-acceptable continuations, thereby unlocking substantially higher acceptance rates—and speedups—without relying on fragile local probability agreement.

---

*Analysis generated on: 2026-01-06T19:14:18.100600*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Copyright-Protected Language Generation via Adaptive Model Fusion

**Conference:** ICLR 2025 (oral)

**Authors:** Javier Abad, Konstantin Donhauser, Francesco Pinto, Fanny Yang

**Keywords:** language models, copyright, model fusion, memorization, safety, privacy

**Abstract:** 
> The risk of language models reproducing copyrighted material from their training data has led to the development of various protective measures. Among these, inference-time strategies that impose constraints via post-processing have shown promise in addressing the complexities of copyright regulation. However, they often incur prohibitive computational costs or suffer from performance trade-offs. To overcome these limitations, we introduce Copyright-Protecting Model Fusion (CP-Fuse), a novel app...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* This work established concrete protocols and evidence for verbatim regurgitation from LMs, defining the copyright/memorization risk and evaluation targets that CP-Fuse directly aims to mitigate.

### 💡 Inspiration

**GeDi: Generative Discriminator Guided Sequence Generation** (2021)
- *Authors:* Ben Krause et al.
- *Direct Connection:* GeDi’s idea of steering generation by combining model distributions via Bayes-guided signals informs CP-Fuse’s principle of inference-time log-probability aggregation to enforce constraints without retraining.

**Model Soups: Averaging Weights of Multiple Fine-Tuned Models Improves Accuracy Without Training** (2022)
- *Authors:* Mitchell Wortsman et al.
- *Direct Connection:* Model Soups demonstrated that post-hoc fusion of models trained on different data can improve behavior without retraining, a compositional insight CP-Fuse adopts at the output-probability level for copyright-safe generation.

### 🔍 Gap Identification

**On Memorization in Language Models** (2022)
- *Authors:* Nikhil Kandpal et al.
- *Direct Connection:* By showing that scaling and data duplication drive memorization and that training-time fixes (e.g., deduplication) only partially reduce regurgitation, this paper motivates CP-Fuse’s post-hoc, inference-time approach that does not require retraining or data changes.

**Plug and Play Language Models: A Simple Approach to Controlled Text Generation** (2020)
- *Authors:* Siddharth Dathathri et al.
- *Direct Connection:* PPLM’s gradient-based, attribute-guided decoding exemplifies effective but computationally expensive inference-time control, a cost/latency limitation that CP-Fuse explicitly addresses with lightweight probability fusion.

### 📊 Baseline

**DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts** (2021)
- *Authors:* Xiang Lisa Li et al.
- *Direct Connection:* CP-Fuse directly generalizes DExperts’ logit-space combination of multiple LMs by adaptively fusing models trained on disjoint copyrighted subsets and adding a balancing property to prevent any single model’s memorized content from dominating.

---

## Synthesis: How Prior Work Led to This Paper

Evidence that large language models can reproduce training data verbatim crystallized with work showing concrete extraction attacks and benchmarks for regurgitation, framing the safety and copyright stakes of open-ended generation. Subsequent analysis connected memorization to scaling and data duplication, and documented that training-time mitigations like deduplication do not fully prevent reproduction, particularly under adversarial prompts, thereby motivating inference-time safeguards. Early decoding-time control methods such as Plug-and-Play Language Models effectively steered attributes by iteratively adjusting hidden states, but incurred significant compute and latency overhead. GeDi introduced a lighter-weight alternative by steering with Bayes-guided combination using a generative discriminator, illustrating that probability-level composition can enforce constraints without retraining. DExperts advanced this line by combining expert and anti-expert language models directly in logit space during decoding, showing that multi-LM fusion can suppress unwanted content distributions. In parallel, Model Soups showed that post-hoc composition of models trained on different data can improve behavior without additional training, underscoring the promise of model fusion as a general strategy. Together, these threads reveal a gap: the need for a fast, post-hoc, probability-level fusion that targets copyright regurgitation specifically. Building on the insight that combining model distributions can steer outputs, and on the feasibility of post-hoc composition across differently trained models, the current work fuses models trained on disjoint copyrighted subsets and introduces an adaptive balancing mechanism to minimize memorized reproduction while preserving generation quality and efficiency.

---

*Analysis generated on: 2026-01-06T14:39:09.509495*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

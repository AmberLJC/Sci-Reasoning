# Prior Work Analysis Report

## Target Paper

**Title:** Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs

**Conference:** ICLR 2025 (oral)

**Authors:** Nguyen Nhat Minh, Andrew Baker, Clement Neo, Allen G Roush, Andreas Kirsch, Ravid Shwartz-Ziv

**Keywords:** Natural Language Processing, Large Language Models, Text Generation, Sampling Methods, Truncation Sampling, Stochastic Sampling, Min-p Sampling, Top-p Sampling, Nucleus Sampling, Temperature Sampling, Decoding Methods, Deep Learning, Artificial Intelligence

**Abstract:** 
> Large Language Models (LLMs) generate text by sampling the next token from a probability distribution over the vocabulary at each decoding step. Popular sampling methods like top-p (nucleus sampling) often struggle to balance quality and diversity, especially at higher temperatures which lead to incoherent or repetitive outputs. We propose min-p sampling, a dynamic truncation method that adjusts the sampling threshold based on the model's confidence by using the top token's probability as a scal...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Hierarchical Neural Story Generation** (2018)
- *Authors:* Angela Fan et al.
- *Direct Connection:* Min-p departs from the fixed-size truncation introduced via top-k sampling by Fan et al., replacing a constant k with a confidence-scaled cutoff that adapts to the shape of the distribution at each step.

**Language Models (Mostly) Know What They Know** (2022)
- *Authors:* Saurav Kadavath et al.
- *Direct Connection:* Min-p leverages the finding that language models’ token probabilities reflect their confidence by using the top-token probability as the scaling factor for truncation, enabling more exploration when uncertain and restraint when confident.

### 💡 Inspiration

**Mirostat: A Method for Controlling the Perplexity of Text Generation** (2021)
- *Authors:* Trieu H. Trinh et al.
- *Direct Connection:* Min-p builds on Mirostat’s insight of dynamically modulating exploration using model uncertainty, but implements it as a one-shot truncation rule keyed to the top-token probability rather than iterative temperature control.

### 🔍 Gap Identification

**Comparison of Decoding Strategies for Open-Ended Language Generation** (2019)
- *Authors:* Violet Ippolito et al.
- *Direct Connection:* Min-p explicitly targets the quality–diversity breakdown at higher temperatures documented by Ippolito et al., providing a drop-in sampler that maintains coherence while supporting creative outputs.

### 📊 Baseline

**The Curious Case of Neural Text Degeneration** (2020)
- *Authors:* Ari Holtzman et al.
- *Direct Connection:* Min-p modifies nucleus (top-p) sampling by making the truncation threshold a function of step-wise confidence (the top-token probability), directly addressing the high-temperature failure mode of nucleus sampling highlighted by Holtzman et al.

### 🔗 Related Problem

**Typical Decoding for Natural Language Generation** (2022)
- *Authors:* Clara Meister et al.
- *Direct Connection:* Min-p adopts the same core idea of adaptive truncation as typical decoding, but substitutes entropy-based typicality with a simpler per-step signal (top-token probability) to better preserve coherence at high temperatures.

---

## Synthesis: How Prior Work Led to This Paper

Holtzman et al. introduced nucleus (top-p) sampling and showed how fixed decoding strategies induce degeneration, with nucleus truncation mitigating some issues but still vulnerable when the probability mass flattens at higher temperatures. Fan et al. popularized top-k sampling for open-ended generation, establishing the fixed-size truncation paradigm and its sensitivity to the local shape of the predictive distribution. Meister et al. proposed typical decoding, using entropy-based typicality to adaptively select tokens whose information content matches the model’s uncertainty, reducing off-manifold sampling while retaining diversity. Trinh et al. (Mirostat) demonstrated that actively controlling surprise (per-token perplexity) via dynamic temperature adjustment can stabilize quality by aligning generation to a target entropy. Kadavath et al. provided evidence that language models’ probabilities, especially top-token probabilities, encode meaningful confidence about correctness, suggesting a simple, local signal for adaptive control. Ippolito et al. systematically documented how standard sampling degrades coherence and diversity as temperature rises, highlighting the need for robust, high-temperature decoding.
Taken together, these works expose a central opportunity: combine the adaptability of dynamic methods with a minimal, local signal that reflects model confidence at each step. The insight that token probabilities convey confidence (Kadavath) and that adaptive truncation or entropy control improves generation (Meister; Mirostat) naturally leads to a rule that scales truncation by the top-token probability. By directly correcting the high-temperature brittleness of nucleus sampling (Holtzman) and avoiding the rigidity of fixed-k (Fan), the resulting approach enables exploration when the model is uncertain and restraint when it is confident—delivering creative yet coherent outputs at elevated temperatures.

---

*Analysis generated on: 2026-01-06T08:25:32.491300*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

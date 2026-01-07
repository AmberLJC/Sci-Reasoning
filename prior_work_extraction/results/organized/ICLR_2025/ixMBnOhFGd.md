# Prior Work Analysis Report

## Target Paper

**Title:** SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction

**Conference:** ICLR 2025 (spotlight)

**Authors:** Lu Dai, Yijie Xu, Jinhui Ye, Hao Liu, Hui Xiong

**Keywords:** information retrieval, metric

**Abstract:** 
> Large Language Models (LLMs) have demonstrated improved generation performance by incorporating externally retrieved knowledge, a process known as retrieval-augmented generation (RAG). Despite the potential of this approach, existing studies evaluate RAG effectiveness by 1) assessing retrieval and generation components jointly, which obscures retrieval's distinct contribution, or 2) examining retrievers using traditional metrics such as NDCG, which creates a gap in understanding retrieval's true...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** (2020)
- *Authors:* Patrick Lewis et al.
- *Direct Connection:* This work formalized the RAG paradigm and highlighted that evaluation typically conflates retrieval and generation, directly motivating a metric that isolates and quantifies retrieval’s standalone utility.

### 💡 Inspiration

**Retrieval Augmented Language Model Pre-Training** (2020)
- *Authors:* Kelvin Guu et al.
- *Direct Connection:* REALM framed retrieval as latent knowledge that improves language modeling likelihood, inspiring SePer’s core idea of measuring retrieval utility via changes in an LM’s uncertainty/perplexity as an information-gain signal.

**Language Models (Mostly) Know What They Know** (2022)
- *Authors:* Saurabh Kadavath et al.
- *Direct Connection:* This paper showed that LMs’ probabilities can reflect calibrated internal beliefs about correctness, directly informing SePer’s use of the LM’s own belief state to quantify the utility of retrieved information.

### 🔍 Gap Identification

**Leveraging Passage Retrieval with Generative Models for Open-Domain Question Answering** (2021)
- *Authors:* Gautier Izacard et al.
- *Direct Connection:* FiD demonstrated large gains from retrieved evidence but evaluated primarily with end-to-end QA accuracy, underscoring the need for a retrieval-specific metric that doesn’t conflate generator strength with retriever quality.

### 📊 Baseline

**BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models** (2021)
- *Authors:* Nandan Thakur et al.
- *Direct Connection:* BEIR popularized NDCG-based evaluation for retrieval, providing the standard baseline that SePer explicitly challenges by arguing NDCG may not reflect a passage’s true utility to downstream generation.

### 🔧 Extension

**Semantic Entropy: Interpretable and Calibrated Uncertainty for Text Generation** (2023)
- *Authors:* Kuhn et al.
- *Direct Connection:* By introducing semantic-level uncertainty via clustering paraphrastic generations, this work provides the technical blueprint that SePer adapts to define semantic perplexity and measure its reduction after retrieval.

### 🔗 Related Problem

**Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection** (2023)
- *Authors:* Akari Asai et al.
- *Direct Connection:* Self-RAG operationalizes an LM’s internal critique to judge whether retrieved content is helpful, closely informing SePer’s idea of using the model’s own signals to assess retrieval utility, but without requiring training.

---

## Synthesis: How Prior Work Led to This Paper

Retrieval-augmented generation was crystallized by Lewis et al., who showed that feeding retrieved evidence to a generator improves knowledge-intensive tasks but leaves evaluation entangled between retriever and generator. Guu et al. took an information-theoretic stance by treating retrieval as latent knowledge that improves language modeling likelihood, establishing that changes in model uncertainty can indicate knowledge utility. Izacard and Grave demonstrated that stronger generators (e.g., FiD) benefit from more evidence, yet performance was still reported as end-to-end accuracy, masking the retriever’s true contribution. Thakur et al. standardized NDCG-based evaluation across retrieval benchmarks (BEIR), reinforcing relevance-centric metrics that don’t necessarily track what helps generation. Kadavath et al. showed that LMs’ predicted probabilities reflect calibrated internal beliefs about correctness, suggesting that model belief can be an evaluative signal. Complementarily, work on semantic entropy proposed clustering semantically equivalent outputs to capture uncertainty at the meaning level, offering a way to measure uncertainty beyond surface probabilities. Self-RAG leveraged an LM’s self-critique to judge the helpfulness of retrieved content, illustrating that internal model signals can guide retrieval decisions. Together these works revealed a gap: relevance metrics don’t capture generative utility, and end-to-end scores conflate components, while internal LM signals can reflect belief and helpfulness. Seizing this opportunity, the current paper synthesizes semantic-level uncertainty with information-gain reasoning to define semantic perplexity and measure its reduction after retrieval, yielding a retrieval-specific utility metric grounded in the LM’s own belief rather than surface relevance or final-task accuracy.

---

*Analysis generated on: 2026-01-06T16:36:21.591253*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

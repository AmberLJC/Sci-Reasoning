# Prior Work Analysis Report

## Target Paper

**Title:** BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval

**Conference:** ICLR 2025 (spotlight)

**Authors:** Hongjin SU, Howard Yen, Mengzhou Xia, Weijia Shi, Niklas Muennighoff, Han-yu Wang, Liu Haisu, Quan Shi, Zachary S Siegel, Michael Tang, Ruoxi Sun, Jinsung Yoon, Sercan O Arik, Danqi Chen, Tao Yu

**Keywords:** Retrieval benchmark, Reasoning

**Abstract:** 
> Existing retrieval benchmarks primarily consist of information-seeking queries (e.g., aggregated questions from search engines) where keyword or semantic-based retrieval is usually sufficient. However, many complex real-world queries require in-depth reasoning to identify relevant documents that go beyond surface form matching. For example, finding documentation for a coding question requires understanding the logic and syntax of the functions involved. To better benchmark retrieval on such chal...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**MTEB: Massive Text Embedding Benchmark** (2023)
- *Authors:* Niklas Muennighoff et al.
- *Direct Connection:* MTEB provides the embedding-model leaderboard and evaluation protocols that BRIGHT stress-tests, and BRIGHT explicitly measures leading MTEB models on reasoning-centric retrieval queries.

**HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering** (2018)
- *Authors:* Zhilin Yang et al.
- *Direct Connection:* HotpotQA introduced multi-hop questions requiring chaining evidence across documents, providing the key insight that finding relevant support can itself demand reasoning beyond single-hop similarity matching.

**KILT: A Benchmark for Knowledge Intensive Language Tasks** (2021)
- *Authors:* Fabio Petroni et al.
- *Direct Connection:* KILT unified knowledge-intensive tasks under shared retrieval corpora and metrics, a framework BRIGHT adopts conceptually while refocusing strictly on retrieval difficulty driven by reasoning.

### 🔍 Gap Identification

**BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models** (2021)
- *Authors:* Nandan Thakur et al.
- *Direct Connection:* BEIR established the dominant zero-shot IR evaluation suite largely populated by information-seeking queries, whose lack of reasoning-heavy retrieval is the explicit gap BRIGHT targets.

**MS MARCO: A Human Generated Machine Reading Comprehension Dataset** (2016)
- *Authors:* Tri Nguyen et al.
- *Direct Connection:* MS MARCO’s search-log–derived queries epitomize cases where lexical or semantic matching is sufficient, motivating BRIGHT’s focus on queries where identifying relevant documents requires logical and multi-step reasoning.

### 🔗 Related Problem

**Answering Complex Open-Domain Questions with Multi-Hop Dense Retrieval** (2020)
- *Authors:* Wenhan Xiong et al.
- *Direct Connection:* This work operationalized reasoning at the retrieval stage via multi-hop dense retrieval paths, directly highlighting the need for a benchmark that isolates and evaluates reasoning in retrieval itself.

---

## Synthesis: How Prior Work Led to This Paper

Existing IR evaluations have been shaped by datasets like MS MARCO, whose search-log–based queries generally reward lexical or straightforward semantic matching, and by BEIR’s heterogeneous zero-shot suite that aggregates mostly information-seeking tasks. MTEB extended this landscape with standardized evaluation of text embeddings across many retrieval tasks, establishing widely used baselines and leaderboards. In contrast, multi-hop QA efforts such as HotpotQA showed that answering complex questions requires chaining evidence across documents, implying that the act of identifying relevant evidence can demand reasoning. Methodologically, Xiong et al. formalized this idea by modeling multi-hop dense retrieval paths, making retrieval itself an iterative reasoning process. Complementing these trends, KILT unified knowledge-intensive tasks and metrics around a shared retrieval corpus, encouraging careful, comparable evaluation of retrieval components across tasks. Together, these works established strong baselines and evaluation practices while implicitly assuming that most retrieval benchmarks center on information-seeking queries where surface-form or single-hop semantic similarity suffices. Yet the multi-hop QA literature revealed that retrieval can be the reasoning bottleneck, and MTEB’s embedding models—optimized for broad coverage—were never stress-tested on retrieval tasks that truly require logical or procedural inference. This confluence created a clear opportunity: construct a retrieval-only benchmark composed of real-world, cross-domain queries where relevance hinges on multi-step, logic-aware understanding, evaluated with standardized IR protocols but designed to expose the limits of state-of-the-art embedding retrievers.

---

*Analysis generated on: 2026-01-06T08:57:01.063795*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

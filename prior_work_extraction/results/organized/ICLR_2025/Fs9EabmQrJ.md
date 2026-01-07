# Prior Work Analysis Report

## Target Paper

**Title:** EmbedLLM: Learning Compact Representations of Large Language Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Richard Zhuang, Tianhao Wu, Zhaojin Wen, Andrew Li, Jiantao Jiao, Kannan Ramchandran

**Keywords:** Large Language Models, Representation Learning, Model Routing

**Abstract:** 
> With hundreds of thousands of language models available on Huggingface today, efficiently evaluating and utilizing these models across various downstream tasks has become increasingly critical. Many existing methods repeatedly learn task-specific representations of Large Language Models (LLMs), which leads to inefficiencies in both time and computational resources. To address this, we propose EmbedLLM, a framework designed to learn compact vector representations of LLMs that facilitate downstrea...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance** (2023)
- *Authors:* Unknown et al.
- *Direct Connection:* This work formalized the practical model-routing problem across multiple LLMs and established cost–quality tradeoffs, which EmbedLLM targets by supplying reusable model-centric embeddings that drive routing decisions.

### 💡 Inspiration

**Task2Vec: Task Embedding for Meta-Learning** (2019)
- *Authors:* Alessandro Achille et al.
- *Direct Connection:* Task2Vec’s insight that tasks can be embedded via Fisher features directly inspired EmbedLLM’s shift to embedding models themselves to capture capability structure across tasks.

**Neural Architecture Optimization** (2018)
- *Authors:* Renqian Luo et al.
- *Direct Connection:* NAO’s encoder–decoder that maps architectures into a continuous space predictive of accuracy directly motivates EmbedLLM’s encoder–decoder for learning model embeddings predictive of capability profiles.

**Editing Models with Task Arithmetic** (2023)
- *Authors:* Gabriel Ilharco et al.
- *Direct Connection:* Task arithmetic shows that task-specific changes correspond to approximately linear directions, informing EmbedLLM’s design to encode a model’s capability profile in a low-dimensional vector space.

### 🔍 Gap Identification

**LogME: Practical Assessment of Pre-trained Models for Transfer Learning** (2021)
- *Authors:* Lei You et al.
- *Direct Connection:* LogME predicts model transferability but requires per-task data and inference; EmbedLLM addresses this limitation by learning model embeddings that forecast performance across benchmarks without additional inference cost.

### 📊 Baseline

**RouteLLM: Learning to Route LLMs with Preference Feedback** (2024)
- *Authors:* Unknown et al.
- *Direct Connection:* As a primary routing baseline that trains policies to select among LLMs, RouteLLM motivates EmbedLLM’s learning of general-purpose model embeddings that improve routing without retraining task-specific routers.

### 🔗 Related Problem

**Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time** (2022)
- *Authors:* Ilya Wortsman et al.
- *Direct Connection:* By revealing linear structure in weight space that captures model capabilities, Model Soups supports the premise that a compact vector can summarize an LLM’s skills, which EmbedLLM operationalizes as an embedding.

---

## Synthesis: How Prior Work Led to This Paper

Frugal routing methods established the practical need to choose among multiple LLMs to balance quality and cost, with FrugalGPT defining the decision problem and empirical tradeoffs, while RouteLLM learned policies that map inputs to model choices using feedback signals. In parallel, representation learning works suggested how to capture functional properties in low-dimensional vectors: Task2Vec embedded tasks via Fisher features to summarize behavior, LogME predicted transferability of pretrained models to new tasks using a closed-form evidence score, and Neural Architecture Optimization introduced an encoder–decoder that places architectures in a continuous space predictive of accuracy. Complementary findings on weight-space structure—Model Soups’ linear averaging and Task Arithmetic’s capability vectors—demonstrated that model skills admit compact, approximately linear representations.
Together these threads expose a gap: routing frameworks retrain task-specific routers and transferability metrics require per-task inference, yet evidence suggests model capabilities can be summarized once in a vector space predictive of performance. EmbedLLM synthesizes these ideas by learning an encoder–decoder that maps entire LLMs to compact embeddings whose geometry forecasts benchmark performance and drives routing across many models without retraining per task. This is a natural next step: it replaces per-task routing and per-task transferability estimation with a reusable, model-centric representation that encodes capability profiles directly.

---

*Analysis generated on: 2026-01-06T12:23:07.616053*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

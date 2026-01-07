# Prior Work Analysis Report

## Target Paper
**Title:** moyG54Okrj
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Connection:* Established the RAG paradigm that Repoformer builds on, introducing the core idea of conditioning generation on retrieved evidence that Repoformer selectively invokes rather than using invariable retrieval.

**Improving language models by retrieving from trillions of tokens** (2022)
- *Authors:* Sebastian Borgeaud et al.
- *Connection:* RETRO integrated large-scale retrieval directly into LM training/inference and highlighted retrieval’s impact on generation quality, providing the foundational retrieval-conditioning mechanism that Repoformer adapts to the repository-level code setting.

### 💡 Inspiration

**Self-RAG: Learning to Retrieve, Generate, and Critique for Language Models** (2023)
- *Authors:* Akari Asai et al.
- *Connection:* Directly inspired Repoformer’s selective RAG policy by showing that an LM can self-evaluate usefulness of retrieved context and control retrieval; Repoformer operationalizes this with a self-supervised signal tailored to code completion and uses the same LM as both policy and generator.

**Language models (mostly) know what they know** (2022)
- *Authors:* Kshitij Kadavath et al.
- *Connection:* Showed LMs can self-assess their answer correctness, motivating Repoformer’s self-supervised training for a code LM to predict when retrieval will improve completion quality (i.e., learn when it needs external context).

### 🔍 Gap Identification

**Lost in the Middle: How Language Models Use Long Context** (2023)
- *Authors:* Nelson F. Liu et al.
- *Connection:* Demonstrated that adding long or poorly placed context can hurt LM performance, motivating Repoformer’s core decision to avoid retrieval when unhelpful and to be selective about incorporating repository context.

### 🔗 Related Problem

**REPLUG: Retrieval-Augmented Black-Box Language Models** (2023)
- *Authors:* Wenhao Shi et al.
- *Connection:* Showed that retrieval quality/noise critically affects RAG and trained retrievers with LM feedback; Repoformer addresses this noise sensitivity on repositories by training the LM to robustly leverage (or skip) potentially noisy retrieved code contexts.

---

## Synthesis

Repoformer’s core innovation is a selective retrieval-augmented generation framework for repository-level code completion in which the same code LM learns, via self-supervision, to predict whether retrieval will help and to robustly use potentially noisy retrieved context. This builds squarely on the RAG lineage established by Lewis et al. (2020) and RETRO (Borgeaud et al., 2022), which codified conditioning generation on retrieved evidence but typically assumed retrieval is always beneficial. Two lines of prior work directly shaped Repoformer’s selectivity and robustness. First, Self-RAG (Asai et al., 2023) demonstrated that an LM can self-critique and control retrieval, providing the template for learning a retrieval policy; Repoformer adapts this idea to code, training the generator itself to decide if repository retrieval will improve completion. Second, REPLUG (Shi et al., 2023) showed that retrieval noise and relevance are pivotal and can be optimized with LM feedback; Repoformer addresses this by teaching the LM to ignore or downweight unhelpful repository snippets and even skip retrieval. The motivation for selectivity is reinforced by Lost in the Middle (Liu et al., 2023), which revealed that extraneous long context can degrade performance, a risk magnified in repositories. Finally, Kadavath et al. (2022) provided the evidence that LMs can self-assess their knowledge, underpinning Repoformer’s self-supervised signal for predicting retrieval helpfulness. Together, these works lead directly to Repoformer’s selective, self-evaluative RAG for repository-level code completion.

---
*Generated: 2026-01-06T23:09:26.429833*

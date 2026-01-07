# Prior Work Analysis Report

## Target Paper

**Title:** To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yukun Huang, Sanxing Chen, Hongyi Cai, Bhuwan Dhingra

**Keywords:** Large Language Model, Knowledge Conflict, Retrieval Augmented Generation, Confidence Estimation, Reasoning

**Abstract:** 
> Large Language Models (LLMs) are often augmented with external contexts, such as those used in retrieval-augmented generation (RAG). However, these contexts can be inaccurate or intentionally misleading, leading to conflicts with the model’s internal knowledge. We argue that robust LLMs should demonstrate situated faithfulness, dynamically calibrating their trust in external information based on their confidence in the internal knowledge and the external context to resolve knowledge conflicts. T...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Self-Ask with Search: Improving Multistep Reasoning by Decomposing Questions** (2022)
- *Authors:* Press et al.
- *Direct Connection:* Self-Ask established the formulation where an LM introspects on what it knows and selectively consults external information, providing the foundational paradigm of balancing internal knowledge and external retrieval that this paper formalizes as situated faithfulness.

**Selective Question Answering under Domain Shift** (2020)
- *Authors:* Kamath et al.
- *Direct Connection:* By formalizing answer-or-abstain decisions using calibrated confidence, this work provides the selective prediction framework that is extended here to selective trust—choosing between internal knowledge and external context based on confidence.

### 💡 Inspiration

**Self-RAG: Learning to Retrieve, Generate, and Critique for Better Language Modeling** (2023)
- *Authors:* Asai et al.
- *Direct Connection:* Self-RAG’s explicit model-internal judgments of the helpfulness/correctness of retrieved passages directly inspire the paper’s Self-Guided Confidence Reasoning, which similarly elicits and uses model-written confidence assessments to decide whether to trust external context.

**SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models** (2023)
- *Authors:* Manakul et al.
- *Direct Connection:* SelfCheckGPT showed that self-evaluation via consistency checks yields practical confidence signals about factuality, which this paper adapts into structured confidence reasoning to quantify internal-knowledge confidence and context reliability.

### 🔍 Gap Identification

**Prompt Injection Attacks against Retrieval-Augmented Language Models** (2023)
- *Authors:* Greshake et al.
- *Direct Connection:* This paper identified that RAG systems over-trust malicious or misleading retrieved text, directly motivating the need for mechanisms that detect and downweight untrustworthy contexts as proposed here.

### 🔗 Related Problem

**FLARE: Active Retrieval Augmented Generation** (2023)
- *Authors:* Jiang et al.
- *Direct Connection:* FLARE triggers retrieval based on model uncertainty, and this work extends that uncertainty-as-signal idea to compute internal and external confidence scores that gate whether retrieved context should be trusted or overridden.

---

## Synthesis: How Prior Work Led to This Paper

Self-RAG introduced a retrieval–generation loop in which the model explicitly critiques the helpfulness and correctness of retrieved passages, showing that model-written meta-judgments can steer evidence use. Self-Ask with Search established an agentic prompting paradigm where a model introspects on what it knows, decomposes questions, and selectively queries external tools when its internal knowledge is insufficient. FLARE operationalized model uncertainty as a control signal for evidence acquisition, triggering retrieval only when the model exhibits low confidence during generation. SelfCheckGPT demonstrated that self-consistency and internal critique produce usable confidence signals for hallucination detection without external supervision. Selective Question Answering formalized the answer-or-abstain setting using calibrated confidence, framing selective prediction as a principled decision based on uncertainty. Prompt Injection Attacks against RAG exposed that systems frequently over-trust retrieved or injected content, highlighting a concrete and prevalent failure mode in which externally provided context is misleading or adversarial.
Together, these works revealed both the promise and the pitfall of retrieval: models can self-assess evidence utility, but they lack calibrated mechanisms to arbitrate conflicts between internal knowledge and external context. The natural next step is to fuse agentic self-assessment (Self-RAG, Self-Ask), uncertainty-driven control (FLARE), and selective prediction principles (Selective QA) into a unified decision process that explicitly estimates confidence in both sources. By casting evidence use as confidence reasoning and targeting the over-trust failure mode identified by prompt-injection studies, the paper synthesizes these ideas into situated faithfulness: dynamically trusting, disputing, or rejecting context based on structured self-guided confidence in internal knowledge and external evidence.

---

*Analysis generated on: 2026-01-06T12:51:22.988600*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

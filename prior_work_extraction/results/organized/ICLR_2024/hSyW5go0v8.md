# Prior Work Analysis Report

## Target Paper

**Title:** Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**Conference:** ICLR 2024 (oral)

**Authors:** Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi

**Keywords:** Retrieval-augmented Generation, Language Models, Retrieval-augmented LMs, Factuality

**Abstract:** 
> Despite their remarkable capabilities, large language models (LLMs) often produce responses containing factual inaccuracies due to their sole reliance on the parametric knowledge they encapsulate. Retrieval-Augmented Generation (RAG), an ad hoc approach that augments LMs with retrieval of relevant knowledge, decreases such issues. However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, di...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** (2020)
- *Authors:* Patrick Lewis et al.
- *Direct Connection:* Established the RAG paradigm of concatenating a fixed top-k set of retrieved passages to the LM context, whose fixed-k and indiscriminate incorporation is the precise limitation Self-RAG replaces with learned, token-level decisions about whether and what to retrieve.

### 💡 Inspiration

**Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions (IRCoT)** (2022)
- *Authors:* Harsh Trivedi et al.
- *Direct Connection:* Demonstrated that interleaving retrieval with generated reasoning steps boosts factual reasoning, an idea Self-RAG operationalizes by learning an explicit, in-model policy (via reflection tokens) for when to retrieve.

**Self-Ask: Measuring and Narrowing the Compositionality Gap in Language Models** (2022)
- *Authors:* Ofir Press et al.
- *Direct Connection:* Showed that LMs can self-decompose questions and invoke external search only when needed through special prompting, which Self-RAG generalizes into supervised, learnable retrieve/no-retrieve control tokens.

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* Coupled explicit thoughts with tool-use actions and fed observations back into reasoning, a thought–action–observation loop that Self-RAG instantiates as trainable reflection and critique tokens around retrieval.

**Toolformer: Language Models Can Teach Themselves to Use Tools** (2023)
- *Authors:* Timo Schick et al.
- *Direct Connection:* Introduced training LMs to insert explicit API-call tokens via self-supervision, directly inspiring Self-RAG’s use of special tokens to trigger on-demand retrieval and to structure self-reflection.

**Self-Refine: Iterative Refinement with Self-Feedback** (2023)
- *Authors:* Aman Madaan et al.
- *Direct Connection:* Proposed generating self-critique and revising outputs to improve quality, which Self-RAG embeds as reflection tokens that assess passage usefulness and answer factuality before producing the final response.

### 📊 Baseline

**Leveraging Passage Retrieval with Generative Models for Open-Domain Question Answering (FiD)** (2021)
- *Authors:* Gautier Izacard and Edouard Grave
- *Direct Connection:* Provides the dominant RAG architecture that fuses a fixed number of passages in the decoder, serving as the main baseline that Self-RAG improves upon by gating retrieval and passage usage via reflection tokens.

---

## Synthesis: How Prior Work Led to This Paper

Retrieval-Augmented Generation established that grounding generation in external documents improves factuality but did so by concatenating a fixed top-k set of passages, creating a rigidity where retrieval is used even when unnecessary. Fusion-in-Decoder became the canonical instantiation of this practice, maximizing utility from many passages but still assuming a fixed retrieval budget and indiscriminate fusion. Subsequent work showed that retrieval need not be monolithic: interleaving retrieval with chain-of-thought demonstrated gains when queries are issued only at the reasoning steps that need evidence, and self-ask revealed that models can decompose problems and call search selectively using special prompting conventions. ReAct further unified explicit thoughts, tool-use actions, and observations into a loop, making the timing and effects of retrieval transparent within the reasoning trace. In parallel, Toolformer showed that models can be trained to insert explicit tool-use tokens, turning decisions like calling a retriever into a learned, tokenized behavior. Complementarily, Self-Refine introduced self-generated critiques to improve outputs through introspection before finalizing answers. Together, these works highlighted a gap: RAG needed a way to unify on-demand retrieval decisions and self-critique within a single LM, rather than always fusing a fixed set of documents. The current work synthesizes these insights by training an LM to emit explicit reflection tokens that (i) decide whether to retrieve, (ii) assess and select retrieved passages, and (iii) critique drafts for factuality, yielding an adaptive, interpretable, and end-to-end learnable retrieval-and-critique policy.

---

*Analysis generated on: 2026-01-06T10:26:49.436394*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

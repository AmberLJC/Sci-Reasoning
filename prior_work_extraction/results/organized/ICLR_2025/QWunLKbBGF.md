# Prior Work Analysis Report

## Target Paper

**Title:** Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs

**Conference:** ICLR 2025 (oral)

**Authors:** Siyan Zhao, Mingyi Hong, Yang Liu, Devamanyu Hazarika, Kaixiang Lin

**Keywords:** personalization, benchmark, Large language models, conversational llm, chatbots

**Abstract:** 
> Large Language Models (LLMs) are increasingly deployed as chatbots, yet their ability to personalize responses to user preferences remains limited. We introduce PrefEval, a benchmark for evaluating LLMs' ability to infer, memorize and adhere to user preferences in long-context conversational setting.
PrefEval comprises 3,000 manually curated user preference and query pairs spanning 20 topics. PrefEval contains user personalization or preference information in both explicit and implicit preferenc...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Personalizing Dialogue Agents: I have a dog, do you have pets?** (2018)
- *Authors:* Saizheng Zhang et al.
- *Direct Connection:* This paper established the persona/profile–conditioned dialogue formulation and evaluation setup that is directly generalized here to test both explicit and implicit user preferences over multi-session, long-context conversations.

**A Persona-Based Neural Conversation Model** (2016)
- *Authors:* Jiwei Li et al.
- *Direct Connection:* It introduced conditioning conversational responses on user traits and evaluating consistency, providing the core problem framing of preference-following that is assessed in both generation and classification tasks.

**LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding** (2023)
- *Authors:* Bai et al.
- *Direct Connection:* LongBench’s methodology for stress-testing long-context abilities and scaling context lengths informs the benchmark design that evaluates preference inference and retention in conversations up to 100k tokens.

### 🔍 Gap Identification

**Lost in the Middle: How Language Models Use Long Context** (2023)
- *Authors:* Nelson F. Liu et al.
- *Direct Connection:* Its finding that models fail to retrieve salient information from long inputs motivates positioning user preferences at varying places in history to diagnose when preference cues are forgotten during dialogue.

### 📊 Baseline

**MemPrompt: Memory-Augmented Prompting for On-the-Fly Personalization** (2023)
- *Authors:* Xu et al.
- *Direct Connection:* MemPrompt’s mechanism of storing user feedback and facts as a memory that can be retrieved in subsequent turns is a concrete baseline technique stress-tested under the benchmark’s personalization tasks.

**Self-Refine: Iterative Refinement with Self-Feedback** (2023)
- *Authors:* Prithviraj Madaan et al.
- *Direct Connection:* Its iterative feedback loop for improving adherence motivates including iterative self-/user-feedback protocols as a key comparison axis when measuring preference following.

### 🔗 Related Problem

**MemGPT: Towards LLMs as Operating Systems** (2023)
- *Authors:* Shi et al.
- *Direct Connection:* By proposing an external, retrievable memory for multi-session agents to persist user-specific facts, it directly informs the retrieval-augmented baselines evaluated for personalized preference adherence.

---

## Synthesis: How Prior Work Led to This Paper

Early persona-based dialogue work showed how to condition a conversational model on user profiles and evaluate whether responses respect those profiles. One strand introduced persona embeddings and consistency metrics, formalizing the notion that responses should reflect a user’s stated preferences. Complementary efforts built a widely used dataset and protocol where agents must tailor replies to explicit persona descriptions, establishing the canonical evaluation of personalized dialogue. In parallel, long-context benchmarks developed methodology to scale inputs to tens of thousands of tokens, with tasks and metrics probing information retention across extended inputs. Crucially, empirical analyses of long-context processing revealed that models often fail to retrieve salient details placed away from the ends of a long sequence, highlighting a specific failure mode for any task requiring persistent memory. To mitigate such issues in practice, memory-augmented prompting and external-memory agent designs emerged to persist user-specific facts across sessions, while iterative self-feedback methods demonstrated that structured correction loops can improve adherence to requirements. Together, these threads exposed an unmet need: no standard evaluation combined persona-style preference following with explicit and implicit cues, tested over multi-session, very long contexts, and systematically compared prompting, memory/retrieval, and iterative feedback strategies. Building on persona conditioning as the core task, adopting long-context benchmarking methodology, and directly stress-testing memory and feedback-based personalization methods, the present work unifies these elements into a focused benchmark that diagnoses whether LLMs can infer, remember, and follow user preferences over extended conversations.

---

*Analysis generated on: 2026-01-06T13:11:16.410311*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

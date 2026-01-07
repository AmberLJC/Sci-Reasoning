# Prior Work Analysis Report

## Target Paper

**Title:** WildChat: 1M ChatGPT Interaction Logs in the Wild

**Conference:** ICLR 2024 (spotlight)

**Authors:** Wenting Zhao, Xiang Ren, Jack Hessel, Claire Cardie, Yejin Choi, Yuntian Deng

**Keywords:** dataset, dialogues, chatbot, ChatGPT, instruction tuning, toxicity, AI safety

**Abstract:** 
> Chatbots such as GPT-4 and ChatGPT are now serving millions of users. Despite their widespread use, there remains a lack of public datasets showcasing how these tools are used by a population of users in practice. To bridge this gap, we offered free access to ChatGPT for online users in exchange for their affirmative, consensual opt-in to anonymously collect their chat transcripts and request headers. From this, we compiled WildChat, a corpus of 1 million user-ChatGPT conversations, which consis...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models** (2020)
- *Authors:* Samuel Gehman et al.
- *Direct Connection:* RealToxicityPrompts established prompt-based toxicity analysis and measurement protocols that WildChat extends by supplying broader, real-user prompt distributions and metadata for nuanced safety research.

### 💡 Inspiration

**Judging LLM-as-a-judge with MT-Bench and Chatbot Arena** (2023)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* Chatbot Arena demonstrated the value of logging genuine user prompts at scale for evaluation, inspiring WildChat’s design to capture large-scale, naturalistic ChatGPT interactions rather than solely curated datasets.

### 🔍 Gap Identification

**ShareGPT: Community-contributed ChatGPT Conversation Dataset** (2023)
- *Authors:* LMSYS Organization
- *Direct Connection:* ShareGPT popularized using real ChatGPT conversations but is self-selected, small, and lacks consented metadata, directly motivating WildChat’s consented, large-scale collection with rich request headers and demographics.

**OpenAssistant Conversations – Democratizing Large Language Model Alignment** (2023)
- *Authors:* Andreas Köpf et al.
- *Direct Connection:* OpenAssistant’s crowdsourced assistant-style chats established open multi-turn dialogue data but are task-driven and not in-the-wild, highlighting the need WildChat addresses for organic, real-user logs with timestamps and geodemographic context.

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Self-Instruct’s synthetic instruction generation exposed a distributional gap between curated prompts and real user behavior, which WildChat closes by capturing authentic, naturally occurring prompts across languages and topics.

**UltraChat: A Large-Scale Automatically Constructed Multi-turn Chat Dataset** (2023)
- *Authors:* Ning Ding et al.
- *Direct Connection:* UltraChat showed scale via model-generated multi-turn dialogues, but its synthetic nature and lack of real-user context directly motivated WildChat’s focus on human-initiated conversations with request-level metadata.

---

## Synthesis: How Prior Work Led to This Paper

Community-sourced ChatGPT logs like ShareGPT revealed that conversational data from actual users can be leveraged for training and analysis, but the collections were small, self-selected, and lacked systematic metadata. OpenAssistant showed that open, multi-turn assistant-style dialogues could be collected at scale with crowd workers, yet its task-driven, platform-mediated setting diverged from organic, in-the-wild usage and provided limited request-level context. Synthetic pipelines such as Self-Instruct demonstrated that models can bootstrap instruction data, while simultaneously underscoring the mismatch between curated synthetic prompts and authentic user needs. UltraChat pushed multi-turn scale through model-generated conversations, but inevitably missed genuine human behavior signals and request headers. In parallel, Chatbot Arena proved that capturing real user prompts through an open interface unlocks robust evaluation and preference modeling, emphasizing the importance of naturalistic data. RealToxicityPrompts established how to analyze toxicity from prompts and generations, offering a protocol to study safety that benefits from more diverse, real-world inputs.

Together, these works exposed a clear opportunity: the field lacked a consented, large-scale corpus of true in-the-wild human–LLM interactions enriched with temporal, geographic, and header-level context to study usage, multilinguality, and safety at deployment scale. WildChat synthesizes these insights by building an open access pipeline that logs authentic ChatGPT sessions at unprecedented scale and diversity, augments them with anonymized demographics and request headers, and enables toxicity and safety analyses grounded in real user behavior—precisely the natural next step after synthetic and crowdsourced datasets and prompt-only logging.

---

*Analysis generated on: 2026-01-06T09:36:35.185538*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

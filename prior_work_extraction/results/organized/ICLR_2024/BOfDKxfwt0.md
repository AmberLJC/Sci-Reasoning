# Prior Work Analysis Report

## Target Paper

**Title:** LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset

**Conference:** ICLR 2024 (spotlight)

**Authors:** Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Tianle Li, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zhuohan Li, Zi Lin, Eric Xing, Joseph E. Gonzalez, Ion Stoica, Hao Zhang

**Keywords:** large language models, dataset, conversation, safety, benchmark

**Abstract:** 
> Studying how people interact with large language models (LLMs) in real-world scenarios is increasingly important due to their widespread use in various applications. In this paper, we introduce LMSYS-Chat-1M, a large-scale dataset containing one million real-world conversations with 25 state-of-the-art LLMs. This dataset is collected from 210K unique IP addresses in the wild on our Vicuna demo and Chatbot Arena website. We offer an overview of the dataset's content, including its curation proces...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Judging LLM-as-a-judge with MT-Bench and Chatbot Arena** (2023)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* This work launched the Chatbot Arena platform and logging pipeline that directly produced the cross-model, real-user conversation traces that LMSYS-Chat-1M aggregates and releases.

**Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality** (2023)
- *Authors:* Lianmin Zheng et al.
- *Direct Connection:* The Vicuna public demo was a primary data source for the new dataset and earlier showed the value of training on real chat transcripts, motivating a larger, cleaner, in-the-wild conversation corpus.

**Training language models to follow instructions with human feedback** (2022)
- *Authors:* Long Ouyang et al.
- *Direct Connection:* By framing instruction-following as a data-driven alignment problem that hinges on real user prompts and responses, this work created the demand that a large-scale, real-world conversational dataset directly fulfills.

### 💡 Inspiration

**DynaBench: Rethinking Benchmarking in NLP** (2021)
- *Authors:* Douwe Kiela et al.
- *Direct Connection:* DynaBench showed that human-in-the-loop, model-facing interactions yield harder, more revealing evaluation data, directly inspiring the use of real user prompts here to derive challenging benchmarks from live deployments.

### 🔍 Gap Identification

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* Self-Instruct’s synthetic, largely single-turn instructions highlighted the lack of authentic multi-turn, organically distributed dialogues, a gap the new dataset addresses by releasing in-the-wild conversations at scale.

### 📊 Baseline

**OpenAssistant Conversations: Democratizing Large Language Model Alignment** (2023)
- *Authors:* Andreas Köpf et al.
- *Direct Connection:* As an open, crowdsourced multi-turn assistant dataset, OASST1 serves as the main prior dataset baseline that this work extends by covering organic usage across many deployed models rather than curated volunteer interactions.

---

## Synthesis: How Prior Work Led to This Paper

A line of work established both the infrastructure and the data-centric motivation for harvesting real-world LLM conversations. MT-Bench and Chatbot Arena introduced a public platform where users interact with many LLMs and provide pairwise judgments, producing high-volume, standardized multi-model chat logs. The Vicuna project exposed a model via a widely used demo and demonstrated that training on real chat transcripts can yield strong instruction-following behavior, signaling the practical value of authentic conversational data. InstructGPT formalized instruction following as an alignment problem dependent on real prompts and human preferences, underscoring the centrality of high-quality human–model interaction data. In contrast, Self-Instruct generated synthetic instructions that improved alignment but lacked the organic, multi-turn distributions seen in the wild. OpenAssistant Conversations offered open, human-authored multi-turn dialogues but collected them via crowdsourcing rather than live deployment, limiting ecological validity across domains and models. DynaBench argued that evaluation should come from human-in-the-loop interactions that probe model weaknesses, motivating the capture of naturally occurring hard prompts during real usage.
Given this backdrop, a natural opportunity emerged: systematically collect and release large-scale, in-the-wild, multi-model conversations from public demos and Arena battles, thereby meeting the data needs highlighted by InstructGPT, overcoming the synthetic and curated limitations of Self-Instruct and OASST1, and operationalizing DynaBench’s “hard data from real users” insight. By leveraging the Arena/Vicuna deployment infrastructure, the new dataset unifies authentic prompts, multi-turn context, and diverse model outputs, enabling safety moderation training, instruction tuning comparable to Vicuna, and the construction of challenging benchmarks directly from real usage.

---

*Analysis generated on: 2026-01-06T16:29:31.679523*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

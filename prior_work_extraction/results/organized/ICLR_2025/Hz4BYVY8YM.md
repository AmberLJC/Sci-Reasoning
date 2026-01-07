# Prior Work Analysis Report

## Target Paper

**Title:** SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zhenyu Yang, Yuhang Hu, Zemin Du, Dizhan Xue, Shengsheng Qian, Jiahong Wu, Fan Yang, Weiming Dong, Changsheng Xu

**Keywords:** Multimodal large language model, Streaming video analysis, Video understanding

**Abstract:** 
> Despite the significant advancements of Large Vision-Language Models (LVLMs) on established benchmarks, there remains a notable gap in suitable evaluation regarding their applicability in the emerging domain of long-context streaming video understanding. Current benchmarks for video understanding typically emphasize isolated single-instance text inputs and fail to evaluate the capacity to sustain temporal reasoning throughout the entire duration of video streams. To address these limitations, we...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Audio Visual Scene-aware Dialog (AVSD): A Dataset for Multi-turn Video-grounded Dialogue** (2019)
- *Authors:* Chiori Hori et al.
- *Direct Connection:* AVSD established the multi-turn dialog formulation grounded in videos, which SVBench directly adopts and extends by enforcing temporally linked QA chains along a streaming timeline.

**TVQA: Localized, Compositional Video Question Answering** (2018)
- *Authors:* Jie Lei et al.
- *Direct Connection:* TVQA introduced temporally localized QA over video segments, and SVBench builds on this idea by organizing questions into consecutive multi-turn chains that maintain temporal coherence across the full stream.

**TGIF-QA: Toward Spatio-Temporal Reasoning in Visual Question Answering** (2017)
- *Authors:* Yunseok Jang et al.
- *Direct Connection:* TGIF-QA framed video QA tasks that probe temporal skills (e.g., repetition, state transition), whose limitations to short, single-turn clips SVBench explicitly addresses with sustained multi-turn temporal reasoning over long streams.

**MovieQA: Understanding Stories in Movies through Question-Answering** (2016)
- *Authors:* Makarand Tapaswi et al.
- *Direct Connection:* MovieQA highlighted narrative-level, long-range reasoning needs in videos, motivating SVBench’s design to evaluate persistent reasoning across entire streaming narratives rather than isolated moments.

### 💡 Inspiration

**Video-ChatGPT: Towards Detailed Video Understanding via Large Vision-Language Models** (2023)
- *Authors:* Hassan Abbas Maaz et al.
- *Direct Connection:* Video-ChatGPT demonstrated LLM-driven, semi-automated generation of video-grounded instruction/QA data and multi-turn interactions, which SVBench adapts and systematizes into a scalable pipeline that enforces temporal linkage across turns.

### 🔍 Gap Identification

**Video-MME: A Comprehensive Evaluation Benchmark for Multimodal LLMs on Video Understanding** (2024)
- *Authors:* Yue Fu et al.
- *Direct Connection:* Video-MME exposed limitations of current LVLMs under predominantly short, single-turn evaluations, a gap SVBench fills by evaluating long-context, temporally chained multi-turn dialogues over streaming videos.

### 🔗 Related Problem

**Ego4D: Around the World in 3,000 Hours of Egocentric Video** (2022)
- *Authors:* Kristen Grauman et al.
- *Direct Connection:* Ego4D foregrounded continuous, long-duration video tasks requiring memory across time, directly inspiring SVBench’s streaming evaluation setup that tests temporal persistence in LVLMs.

---

## Synthesis: How Prior Work Led to This Paper

Audio Visual Scene-aware Dialog (AVSD) crystallized the notion that video understanding could be evaluated via multi-turn, dialog-style question answering, grounding each turn in visual and audio content. TVQA contributed a complementary insight by requiring temporal localization for each question, pushing models to link questions to specific segments rather than entire clips. TGIF-QA went further in probing temporal skills like counting and state transitions but did so on short, single-turn interactions. MovieQA underscored the importance of narrative-scale reasoning in feature-length videos, showing that long-range dependencies and story structure matter. Ego4D reframed video understanding as continuous, streaming perception, where persistence and memory across long durations are central. Video-ChatGPT demonstrated that large language models can generate high-quality, multi-turn, video-grounded instructions and QAs semi-automatically, offering a practical recipe to scale dialog-style supervision. Finally, Video-MME highlighted that many contemporary LVLM evaluations remain short and single-turn, revealing a systematic mismatch with real-world, long-context video use cases.

Collectively, these works point to a missing evaluation target: sustained, temporally coherent, multi-turn reasoning over entire video streams, produced at scale. SVBench emerges as a natural synthesis—marrying AVSD’s dialog format with TVQA’s temporal grounding, extending TGIF-QA’s temporal probes to long narratives emphasized by MovieQA and Ego4D, and operationalizing Video-ChatGPT’s semi-automated data creation to build temporally linked QA chains. By addressing the gap surfaced by Video-MME, SVBench formalizes a rigorous benchmark for streaming video understanding that stresses persistence, temporal linkage across turns, and dialogue continuity.

---

*Analysis generated on: 2026-01-06T15:20:16.508291*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper

**Title:** Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse

**Conference:** ICLR 2025 (oral)

**Authors:** Maojia Song, Shang Hong Sim, Rishabh Bhardwaj, Hai Leong Chieu, Navonil Majumder, Soujanya Poria

**Keywords:** Large Language Models, Trustworthiness, Hallucinations, Retrieval Augmented Generation

**Abstract:** 
> LLMs are an integral component of retrieval-augmented generation (RAG) systems. While many studies focus on evaluating the overall quality of end-to-end RAG systems, there is a gap in understanding the appropriateness of LLMs for the RAG task. To address this, we introduce Trust-Score, a holistic metric that evaluates the trustworthiness of LLMs within the RAG framework. Our results show that various prompting methods, such as in-context learning, fail to effectively adapt LLMs to the RAG task a...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**FActScore: Fine-grained Evaluation of Factual Consistency in Text Generation** (2023)
- *Authors:* Philippe Laban et al.
- *Direct Connection:* FActScore’s claim-level decomposition and evidence verification paradigm underpins the paper’s grounded-attribution component within the Trust-Score metric.

**Attributable to Identified Sources? Measuring Source Attribution in Language Modeling** (2021)
- *Authors:* Hannah Rashkin et al.
- *Direct Connection:* This work formalizes the notion of source attribution, directly informing the paper’s definition and measurement of citation quality and grounding in RAG outputs.

**ASQA: Factoid Answers for Ambiguous Questions** (2020)
- *Authors:* Sewon Min et al.
- *Direct Connection:* ASQA’s ambiguous long-form QA setting motivates evaluating both grounded multi-facet answers and appropriate abstention, which the paper targets with Trust-Score and Trust-Align.

**QAMPARI: A Benchmark for Open-domain Questions with Many Answers** (2022)
- *Authors:* Mor Geva et al.
- *Direct Connection:* QAMPARI’s many-answer formulation stresses coverage with supported evidence, shaping the metric’s emphasis on attribution quality and refusal when coverage is inadequate.

**ELI5: Long Form Question Answering** (2019)
- *Authors:* Angela Fan et al.
- *Direct Connection:* ELI5’s long-form QA emphasizes justification and verifiability, directly motivating the metric’s groundedness and the alignment objective to produce citations or refuse.

### 💡 Inspiration

**Self-RAG: Learning to Retrieve, Generate, and Critique for Reliable Question Answering** (2023)
- *Authors:* Akari Asai et al.
- *Direct Connection:* Self-RAG’s use of critique/control tokens to assess evidence and regulate generation directly inspires the paper’s learning-to-refuse and grounded-attribution alignment for RAG.

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* Constitutional AI establishes refusal as an explicit alignment target, which is adapted here to evidence-grounded refusals when retrieved support is insufficient.

---

## Synthesis: How Prior Work Led to This Paper

Self-RAG introduced control and critique signals that let a model reflect on retrieved evidence and regulate generation, offering a concrete mechanism for reliability-by-design in open-domain QA. Constitutional AI showed that refusals can be trained as an explicit alignment target, providing a general template for shaping when models should decline to answer. FActScore advanced claim-level evaluation by decomposing outputs into atomic facts and verifying them against evidence, spotlighting the need for granular, evidence-aware scoring of long-form outputs. Work on source attribution by Rashkin et al. formalized what it means for generated content to be attributable to identified sources, laying conceptual groundwork for measuring citation quality and grounding. ASQA posed ambiguous questions requiring multi-faceted, consolidated answers with supporting evidence, while QAMPARI stressed many-answer coverage with support, and ELI5 emphasized long-form, verifiable justifications—collectively defining challenging evaluation regimes where hallucination, poor attribution, and overconfident answering are prevalent. Together, these strands revealed a gap: reliable RAG demands a holistic metric that jointly assesses grounded attribution and correct abstention, and a training paradigm that aligns models to those behaviors. Building on critique/reflection and refusal as alignment targets, and on claim-level and attribution-aware evaluation, the paper synthesizes these insights into Trust-Score for measuring trustworthiness and Trust-Align for evidence-grounded refusal and citation, making a natural next step beyond prior RAG prompting and tuning approaches.

---

*Analysis generated on: 2026-01-06T06:25:20.317083*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

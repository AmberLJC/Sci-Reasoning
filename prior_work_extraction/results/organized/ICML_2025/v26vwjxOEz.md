# Prior Work Analysis Report

## Target Paper
**Title:** v26vwjxOEz
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Are You Smarter Than A Sixth Grader? Textbook Question Answering for Multimodal Machine Comprehension** (2017)
- *Authors:* Kembhavi et al.
- *Connection:* Introduced the canonical multimodal science QA setup that jointly uses diagrams and accompanying text, establishing the problem formulation EMMA generalizes and systematizes across STEM with stronger cross-modal interdependence.

**GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering** (2019)
- *Authors:* Hudson et al.
- *Connection:* Defined compositional visual reasoning evaluation and highlighted shortcut issues, providing the reasoning-centric evaluation philosophy that EMMA extends to tightly coupled image–text reasoning requiring multi-step cross-modal composition.

### 💡 Inspiration

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Wei et al.
- *Connection:* Established CoT as a standard reasoning protocol; EMMA explicitly tests whether CoT-style prompting carries over to genuinely multimodal, cross-modal reasoning and reveals its limitations in that setting.

### 🔍 Gap Identification

**ScienceQA: A Large Dataset for Multimodal Science Question Answering** (2022)
- *Authors:* Lu et al.
- *Connection:* Demonstrated multimodal science QA with images and text but many items are solvable via language-only cues; EMMA is designed explicitly to close this gap by constructing tasks that cannot be solved within either modality alone.

**MMMU: A Massive Multi-discipline Multimodal Understanding Benchmark for Foundation Models** (2024)
- *Authors:* Yue et al.
- *Connection:* Provided a broad, multi-discipline MLLM benchmark but many questions are text-dominant or rely on shallow visual cues; EMMA directly targets this limitation with tasks requiring indispensable, multi-step image–text reasoning.

### 🔗 Related Problem

**ChartQA: A Benchmark for Question Answering on Charts with Visual and Logical Reasoning** (2022)
- *Authors:* Masry et al.
- *Connection:* Showed that numerical reasoning over visual artifacts (charts) requires integrating perception with symbolic reasoning, informing EMMA’s inclusion of quantitative, visually grounded reasoning beyond text-only math word problems.

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2023)
- *Authors:* Wang et al.
- *Connection:* Popularized test-time compute scaling via sampling and voting; EMMA evaluates this strategy in multimodal reasoning tasks and shows that such scaling underperforms when deep cross-modal integration is required.

---

## Synthesis

EMMA’s design emerges from a clear lineage of multimodal evaluation that progressively sharpened the need for true cross-modal reasoning. Early work like TextbookQA formalized multimodal science comprehension by pairing diagrams with textual context, while GQA crystallized the goal of compositional visual reasoning and exposed shortcut vulnerabilities in benchmarks. Building on these foundations, ScienceQA scaled multimodal science QA but revealed a critical gap: many items remain solvable via language-only artifacts or shallow visual cues. Parallel efforts such as ChartQA underscored that robust reasoning demands fusing perception with symbolic and numerical operations, motivating EMMA’s insistence that neither the image nor the text alone suffices. At the same time, reasoning protocols from the LLM literature—Chain-of-Thought prompting and its self-consistency–based test-time scaling—became the de facto yardsticks for assessing “reasoning.” EMMA explicitly probes whether these techniques transfer to genuinely multimodal reasoning, finding that they often fall short when visual and textual information must be integrated over multiple steps. Finally, broad benchmarks like MMMU highlighted evaluation breadth across disciplines but continued to suffer from text dominance and shallow visual reliance. EMMA synthesizes these insights into a benchmark purpose-built to test organic, indispensable, multi-step image–text reasoning across mathematics, physics, chemistry, and coding, directly addressing prior benchmarks’ limitations and stress-testing prevailing reasoning protocols.

---
*Generated: 2026-01-06T23:07:19.624250*

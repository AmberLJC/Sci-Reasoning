# Prior Work Analysis Report

## Target Paper

**Title:** MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts

**Conference:** ICLR 2024 (oral)

**Authors:** Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, Jianfeng Gao

**Keywords:** large language models, large multimodal models, mathematical reasoning, vision-language reasoning, foundation models and their evaluations

**Abstract:** 
> Large Language Models (LLMs) and Large Multimodal Models (LMMs) exhibit impressive problem-solving skills in many tasks and domains, but their ability in mathematical reasoning in visual contexts has not been systematically studied. To bridge this gap, we present MathVista, a benchmark designed to combine challenges from diverse mathematical and visual tasks. It consists of 6,141 examples, derived from 28 existing multimodal datasets involving mathematics and 3 newly created datasets (i.e., IQTe...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**DVQA: Understanding Data Visualizations via Question Answering** (2018)
- *Authors:* Kushal Kafle et al.
- *Direct Connection:* DVQA introduced chart question answering with numeric, textual, and structural reasoning over plots, providing one of the core task formulations and data sources that MathVista aggregates and systematically evaluates within a unified math-in-vision benchmark.

**RAVEN: A Dataset for Relational and Analogical Visual Reasoning** (2019)
- *Authors:* Chi Zhang et al.
- *Direct Connection:* RAVEN formalized abstract IQ-style matrix reasoning with visual patterns, directly informing MathVista’s IQTest subset design to probe analogical and relational visual reasoning with mathematical structures.

**DocVQA: A Dataset for Document Visual Question Answering** (2021)
- *Authors:* Minesh Mathew et al.
- *Direct Connection:* DocVQA established document-centric VQA where understanding text, tables, and layout is essential, a formulation MathVista adapts in its PaperQA subset to evaluate mathematical reasoning over figures and scientific documents.

### 💡 Inspiration

**IconQA: A New Benchmark for Abstract Diagram Understanding and Reasoning** (2022)
- *Authors:* Pan Lu et al.
- *Direct Connection:* IconQA demonstrated that LMMs struggle with abstract diagrammatic reasoning (including math-like patterns), inspiring MathVista to broaden and standardize such visual-math challenges and include analogous IQ-style items.

### 🔍 Gap Identification

**ScienceQA: A Large Dataset of Multi-Modal Science Questions and Answers with Explanations** (2022)
- *Authors:* Pan Lu et al.
- *Direct Connection:* ScienceQA showed the value of multi-modal reasoning and explanations across science topics but lacked a focused, rigorous math-in-vision evaluation, a gap MathVista explicitly targets with specialized tasks and diagnostics.

**Measuring Mathematical Problem Solving With the MATH Dataset** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* The MATH dataset catalyzed text-only mathematical reasoning evaluation, and its omission of visual contexts directly motivated MathVista’s formulation to assess math reasoning that requires fine-grained visual understanding.

### 🔧 Extension

**ChartQA: A Benchmark for Question Answering on Charts** (2022)
- *Authors:* Mohamed Masry et al.
- *Direct Connection:* ChartQA extended chart QA toward semantic and logical operations on real charts, and MathVista directly incorporates this style of chart reasoning to test compositional mathematical inference over visualizations at scale.

---

## Synthesis: How Prior Work Led to This Paper

Early chart understanding benchmarks like DVQA established question answering over data visualizations, requiring numeric, textual, and structural reasoning from plots. ChartQA advanced this direction by emphasizing logical and compositional queries on real-world charts, pushing beyond synthetic setups toward realistic chart semantics. Abstract reasoning datasets such as RAVEN defined matrix-style analogical reasoning over visual patterns, crystallizing IQ-like relational structures vital for probing generalization. IconQA brought abstract diagram understanding into a QA setting, revealing persistent weaknesses of multimodal systems on symbol- and pattern-centric reasoning akin to mathematical thinking. In document understanding, DocVQA formalized question answering over visually rich documents—text, tables, and layout—highlighting the need for models that integrate OCR, structure parsing, and reasoning. ScienceQA broadened multi-modal QA across science domains with explanations, demonstrating the promise of cross-modal reasoning but without a dedicated, rigorous focus on mathematical competence. Meanwhile, the MATH dataset sharpened evaluation for text-only mathematical problem solving, setting expectations for reasoning depth while leaving visual perception unaddressed.
Together, these works exposed a clear opportunity: despite strong progress in chart/diagram QA, document understanding, and text-only math benchmarks, there was no unified, systematic assessment of mathematical reasoning that inherently depends on visual inputs. MathVista synthesizes chart, abstract diagram, and document-centric formulations into a comprehensive benchmark, introduces new subsets tailored to mathematical visual reasoning (IQTest, FunctionQA, PaperQA), and standardizes evaluation across state-of-the-art LMMs to diagnose fine-grained visual and compositional math skills.

---

*Analysis generated on: 2026-01-06T09:26:44.836295*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

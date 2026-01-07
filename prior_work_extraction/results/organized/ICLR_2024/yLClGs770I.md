# Prior Work Analysis Report

## Target Paper

**Title:** MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, Wenhu Chen

**Keywords:** Math Reasoning, Instruction Tuning, Large Language Model

**Abstract:** 
> We introduce MAmmoTH, a series of open-source large language models (LLMs) specifically tailored for general math problem-solving. The MAmmoTH models are trained on MathInstruct, our meticulously curated instruction tuning dataset. MathInstruct is compiled from 13 math datasets with intermediate rationales, six of which have rationales newly curated by us. It presents a unique hybrid of chain-of-thought (CoT) and program-of-thought (PoT) rationales, and also ensures extensive coverage of diverse...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* This work established CoT rationales as effective supervision signals for mathematical reasoning, which MathInstruct explicitly adopts as one half of its hybrid (CoT) annotation strategy.

**Training Verifiers to Solve Math Word Problems (GSM8K)** (2021)
- *Authors:* Karl Cobbe et al.
- *Direct Connection:* GSM8K provided high-quality, step-by-step solution rationales for grade-school math that serve as a core source format and content for MathInstruct’s CoT component.

**Measuring Mathematical Problem Solving With the MATH Dataset** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* MATH defined a competition-level, topic-diverse benchmark and solution style that shaped MathInstruct’s coverage goals and the evaluation target for the MAmmoTH series.

### 💡 Inspiration

**Program of Thoughts Prompting: Disentangle Reasoning from Language Models via Program Execution** (2023)
- *Authors:* Chen et al.
- *Direct Connection:* It introduced PoT supervision—having models produce executable code for reasoning—directly motivating MAmmoTH’s inclusion of PoT traces as the complementary half of its hybrid rationale design.

### 🔍 Gap Identification

**MetaMath: Bootstrap LLMs for Math with Self-Improvement** (2023)
- *Authors:* Yu et al.
- *Direct Connection:* MetaMath’s self-improvement pipeline yields scale but primarily CoT-centric supervision with limited curated executable traces, highlighting the need for MathInstruct’s PoT-integrated, broad-coverage instruction data.

### 📊 Baseline

**WizardMath: Empowering Large Language Models to Solve Math via Evol-Instruct** (2023)
- *Authors:* Luo et al.
- *Direct Connection:* As the main math-instruction baseline built from synthetic Evol-Instruct data (largely CoT-only), WizardMath’s limitations in tool-use/programmatic reasoning directly motivated MAmmoTH’s hybrid CoT+PoT instruction tuning and is the primary system MAmmoTH surpasses.

### 🔗 Related Problem

**PAL: Program-Aided Language Models** (2023)
- *Authors:* Luyu Gao et al.
- *Direct Connection:* PAL showed that delegating arithmetic/logic to a Python interpreter via model-generated code boosts math performance, informing MAmmoTH’s decision to curate PoT rationales that enable tool execution during inference.

---

## Synthesis: How Prior Work Led to This Paper

Chain-of-thought prompting established that supervising models with step-by-step natural language solutions substantially improves mathematical reasoning, leading to widespread use of CoT-style training data. In parallel, program-based reasoning demonstrated that generating executable code can offload arithmetic and algorithmic steps to a Python interpreter; both Program-of-Thoughts prompting and PAL provided concrete recipes showing how code-as-rationale and execution materially improve math performance. Foundational datasets reinforced these supervision formats: GSM8K offered carefully curated word problems with explicit rationales that fit the CoT paradigm, while the MATH dataset defined a competition-level, topic-diverse target distribution and solution style that emphasized breadth and rigor. On the modeling side, WizardMath introduced math-specific instruction tuning via Evol-Instruct, but largely centered on CoT-only synthetic data; MetaMath scaled math ability via self-improvement loops yet similarly relied on CoT-centric supervision with limited executable traces or systematic domain coverage. Together, these works revealed that CoT supervision is powerful but incomplete for tasks benefitting from tool use, that program execution can close this gap, and that existing math instruction corpora are either narrow or code-sparse. The natural next step was to unify these strands by constructing an instruction-tuning corpus that deliberately mixes CoT and executable PoT rationales across diverse mathematical subfields, enabling models to flexibly choose natural language reasoning or program generation and thereby become generalist math solvers that outperform CoT-only instruction-tuned baselines.

---

*Analysis generated on: 2026-01-06T23:09:06.583274*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

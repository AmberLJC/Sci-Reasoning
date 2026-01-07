# Prior Work Analysis Report

## Target Paper

**Title:** MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models

**Conference:** ICLR 2024 (spotlight)

**Authors:** Longhui Yu, Weisen Jiang, Han Shi, Jincheng YU, Zhengying Liu, Yu Zhang, James Kwok, Zhenguo Li, Adrian Weller, Weiyang Liu

**Keywords:** Large Language Model; Mathematical Reasoning

**Abstract:** 
> Large language models (LLMs) have pushed the limits of natural language understanding and exhibited excellent problem-solving ability. Despite the great success, most existing open-source LLMs (\eg, LLaMA-2) are still far away from satisfactory for solving mathematical problems due to the complex reasoning procedures. To bridge this gap, we propose \emph{MetaMath}, a finetuned language model that specializes in mathematical reasoning. Specifically, we start by bootstrapping mathematical question...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Training Verifiers to Solve Math Word Problems (GSM8K)** (2021)
- *Authors:* Dan Cobbe et al.
- *Direct Connection:* GSM8K provides the grade-school math problem formulation and step-by-step solution style that MetaMathQA follows for seeding and evaluation, directly shaping the supervision format.

**Measuring Mathematical Problem Solving With the MATH Dataset** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* MATH defines the competition-level problem distribution and rationale format that guide MetaMathQA’s coverage and the paper’s core evaluation targets.

### 💡 Inspiration

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2023)
- *Authors:* Yizhong Wang et al.
- *Direct Connection:* MetaMath adopts the self-instruction paradigm—using a strong teacher to synthesize supervision—and adapts it to math by prompting multiple answer-preserving rewrites of seed problems to expand instruction coverage while maintaining label correctness.

**STaR: Bootstrapping Reasoning With Reasoning** (2022)
- *Authors:* Hattie Zelikman et al.
- *Direct Connection:* MetaMath borrows STaR’s core insight that verified model-generated content can bootstrap reasoning by filtering rewritten math problems and rationales with correctness checks before fine-tuning.

### 📊 Baseline

**WizardMath: Empowering Large Language Models to Solve Math Problems** (2023)
- *Authors:* Luo et al.
- *Direct Connection:* As the main math-specialized instruction-tuning baseline, WizardMath’s reliance on unconstrained evolved problems (often with incorrect or noisy answers) motivates MetaMath’s answer-preserving multi-perspective rewrites and serves as the primary system MetaMath improves upon.

### 🔧 Extension

**WizardLM: Empowering Large Language Models to Follow Complex Instructions** (2023)
- *Authors:* Xu et al.
- *Direct Connection:* MetaMath extends Evol-Instruct’s transformation-based data expansion by constraining the evolution to solution-invariant, mathematics-specific paraphrases, avoiding the validity drift that unconstrained evolution can introduce.

---

## Synthesis: How Prior Work Led to This Paper

Self-Instruct showed that a strong model can bootstrap high-quality supervision by generating new instructions from a small seed set, establishing a practical recipe for scaling instruction-tuning via synthetic data. WizardLM operationalized this idea at scale with Evol-Instruct, proposing transformation operators that systematically evolve instructions to increase diversity and difficulty, but with limited guarantees on label preservation. WizardMath specialized this evolution paradigm to mathematics, demonstrating strong gains from math-focused synthetic data while also revealing a key pain point: unconstrained evolution frequently yields invalid or mislabeled math problems that degrade downstream training. STaR introduced a complementary principle for reasoning—leveraging model-generated rationales, but only after verifying correctness—to ensure that bootstrapped data reliably improves reasoning quality. Concurrently, GSM8K and MATH defined the dominant math reasoning formulations, with step-by-step rationales and rigorous answer formats that enable automatic checking and consistent supervision.
Building on these strands, the current work synthesizes a label-stable evolution strategy tailored to math: instead of unconstrained generation, it rewrites each seed problem from multiple perspectives while preserving the original solution, then filters with correctness checks inspired by verification-centric bootstrapping. This design combines Self-Instruct’s scalable data synthesis, Evol-Instruct’s transformation mindset, and STaR’s verification principle, using GSM8K/MATH formats to ensure structure and evaluability. The result is a high-diversity, solution-invariant math dataset that directly addresses WizardMath-style noise, enabling substantially stronger math-specialized instruction tuning.

---

*Analysis generated on: 2026-01-06T13:28:50.488772*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

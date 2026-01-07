# Prior Work Analysis Report

## Target Paper

**Title:** SWE-bench: Can Language Models Resolve Real-world Github Issues?

**Conference:** ICLR 2024 (oral)

**Authors:** Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik R Narasimhan

**Keywords:** Language models, Natural language processing, Software engineering

**Abstract:** 
> Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popul...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Defects4J: A Database of Existing Faults to Enable Controlled Testing Studies for Java Programs** (2014)
- *Authors:* René Just et al.
- *Direct Connection:* SWE-bench extends Defects4J’s core idea of validating real-bug fixes via project test suites to Python repositories, pairing buggy/fixed commits with their associated GitHub issues to supply natural-language problem statements.

**ManyBugs: A Database of Real-World Software Bugs for Benchmarking Automated Program Repair** (2015)
- *Authors:* Claire Le Goues et al.
- *Direct Connection:* SWE-bench follows ManyBugs’ emphasis on reproducible environments around historical buggy/fixed commits and test-based oracle validation, but adapts this setup to modern Python ecosystems and LLM-driven patch generation.

### 💡 Inspiration

**Bears: An Extensible Java Bug Benchmark for Automatic Program Repair Studies** (2019)
- *Authors:* Francisco Madeiral et al.
- *Direct Connection:* SWE-bench generalizes Bears’ approach of mining PR-linked, test-reproducible bugs across many projects, shifting to Python and exposing the original GitHub issue text as the model’s input for repository-level patching.

### 🔍 Gap Identification

**Evaluating Large Language Models Trained on Code (HumanEval)** (2021)
- *Authors:* Mark Chen et al.
- *Direct Connection:* SWE-bench borrows HumanEval’s pass/fail, unit-test-based evaluation paradigm but directly addresses its single-function, synthetic prompts by framing tasks as repository-level issue resolution grounded in real projects.

**Program Synthesis with Large Language Models (MBPP)** (2021)
- *Authors:* Jacob Austin et al.
- *Direct Connection:* SWE-bench was motivated by MBPP’s short-context, single-file Python problems and replaces them with real GitHub issue reports tied to multi-file code changes validated by existing project tests.

**Measuring Coding Challenge Competence With APPS** (2021)
- *Authors:* Dan Hendrycks et al.
- *Direct Connection:* SWE-bench targets APPS’ limitation of competition-style, isolated problems by grounding evaluation in real repositories where fixes must integrate with mature codebases and pass project test suites.

---

## Synthesis: How Prior Work Led to This Paper

HumanEval established a simple and influential execution-based evaluation, where code is judged by whether generated functions pass unit tests, but its tasks are synthetic and confined to single functions. MBPP similarly uses concise natural-language prompts for small Python functions, favoring short contexts and self-contained snippets. APPS raises problem difficulty with competition-style programming challenges, yet remains largely single-file and detached from the complexities of mature codebases. In parallel, the automated program repair community built realistic, test-driven benchmarks: Defects4J curated real Java bugs with paired buggy/fixed versions and validated fixes against project test suites, demonstrating a rigorous oracle grounded in real software. ManyBugs extended this paradigm for C programs, prioritizing reproducible environments around historical bugs so that candidate patches could be reliably assessed. Bears mined test-reproducible bugs directly from pull requests across many Java projects, linking real development workflows to a benchmarkable corpus of fixes vetted by CI and project tests. Together these works showed two complementary strengths: unit-test-based, execution-grounded evaluation that is easy to score at scale, and real-bug corpora that preserve the integration constraints of production code. What remained was a bridge between them: a sustainable, repository-level benchmark that uses real-world issue descriptions as the natural-language task specification and validates multi-file patches with existing test suites. SWE-bench synthesizes these strands by pairing GitHub issues with their resolving PRs in Python repositories, packaging reproducible environments, and defining an execution-based oracle that scales to complex, long-context software engineering tasks.

---

*Analysis generated on: 2026-01-06T10:06:36.584477*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

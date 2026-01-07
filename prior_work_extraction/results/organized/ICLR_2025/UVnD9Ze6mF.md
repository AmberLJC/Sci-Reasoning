# Prior Work Analysis Report

## Target Paper

**Title:** AIR-BENCH 2024: A Safety Benchmark based on Regulation and Policies Specified Risk Categories

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yi Zeng, Yu Yang, Andy Zhou, Jeffrey Ziwei Tan, Yuheng Tu, Yifan Mai, Kevin Klyman, Minzhou Pan, Ruoxi Jia, Dawn Song, Percy Liang, Bo Li

**Keywords:** AI Safety, Regulation, Policy, Safety Alignment, Foundation Models

**Abstract:** 
> Foundation models (FMs) provide societal benefits but also amplify risks. Governments, companies, and researchers have proposed regulatory frameworks, acceptable use policies, and safety benchmarks in response. However, existing public benchmarks often define safety categories based on previous literature, intuitions, or common sense, leading to disjointed sets of categories for risks specified in recent regulations and policies, which makes it challenging to evaluate and compare FMs across thes...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**AI Risks (AIR) 2024: A Regulation- and Policy-Grounded Taxonomy of AI Risks** (2024)
- *Authors:* Yi Zeng et al.
- *Direct Connection:* AIR 2024 provides the four-tier, regulation- and policy-derived safety taxonomy that AIR-BENCH 2024 directly adopts as its categorical backbone and organizing principle.

### 🔍 Gap Identification

**Holistic Evaluation of Language Models** (2022)
- *Authors:* Percy Liang et al.
- *Direct Connection:* HELM’s influential but literature- and intuition-driven safety dimensions exposed the lack of regulation-aligned categories, a shortcoming AIR-BENCH 2024 explicitly remedies by mapping evaluation to policy-grounded risk classes.

**Ethical and social risks of harm from language models** (2021)
- *Authors:* Laura Weidinger et al.
- *Direct Connection:* This work crystallized a literature-based harms taxonomy that many benchmarks inherit, and AIR-BENCH 2024 directly addresses its policy-misalignment by replacing it with a taxonomy decomposed from concrete regulations and company policies.

**RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models** (2020)
- *Authors:* Samuel Gehman et al.
- *Direct Connection:* As a single-axis toxicity benchmark widely used to proxy ‘safety,’ it exemplifies fragmented, category-specific evaluation that AIR-BENCH 2024 unifies under a comprehensive, regulation-derived risk taxonomy.

### 🔗 Related Problem

**Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* By popularizing ‘harmlessness’ with a set of broad prohibited content types, this work highlighted how de facto safety categories emerge from practice rather than policy, motivating AIR-BENCH 2024’s shift to regulation-specified risk categories.

**Universal and Transferable Adversarial Attacks on Aligned Language Models** (2023)
- *Authors:* Andy Zou et al.
- *Direct Connection:* This jailbreak work operationalized harmful-intent categories for stress-testing alignment, a scope AIR-BENCH 2024 retains but systematically re-anchors to explicit regulatory and policy risk classes for consistent coverage and comparison.

---

## Synthesis: How Prior Work Led to This Paper

A regulation- and policy-grounded view of AI risks was crystallized in AIR 2024, which decomposed governmental regulations and company policies into a four-tier taxonomy of granular risk categories. HELM codified a holistic but largely literature- and intuition-driven set of safety dimensions to evaluate language models across, establishing influential practices for benchmarking that nevertheless lacked explicit ties to regulatory risk formulations. Weidinger and colleagues cataloged ethical and social harms for language models in a taxonomy that many subsequent evaluations implicitly inherited, further entrenching literature-based categories. Bai et al. operationalized ‘harmlessness’ through RLHF, popularizing broad prohibited-content types that shaped practical safety evaluation without grounding them in policy. RealToxicityPrompts offered a focused toxicity axis—useful but emblematic of fragmented, single-harm benchmarks. Zou et al. showed how adversarial prompts expose unsafe behaviors, organizing harmful intents for stress tests but again outside any regulatory taxonomy. Together, these works established how to evaluate safety, what harms to look for, and how models can fail—but they diverged in category systems and were not anchored to laws or corporate acceptable-use policies. The natural next step was to retain the evaluation rigor and harmful-intent stress testing while remapping categories to a policy-derived taxonomy. Building on AIR 2024’s decomposition of regulations and policies, the current work synthesizes this lineage into a benchmark whose prompts and labels directly reflect regulation-specified risks, enabling consistent, comparable safety evaluation across diverse harm types.

---

*Analysis generated on: 2026-01-06T12:59:35.369532*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

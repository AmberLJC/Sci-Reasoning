# Prior Work Analysis Report

## Target Paper

**Title:** Revisiting text-to-image evaluation with Gecko: on metrics, prompts, and human rating

**Conference:** ICLR 2025 (spotlight)

**Authors:** Olivia Wiles, Chuhan Zhang, Isabela Albuquerque, Ivana Kajic, Su Wang, Emanuele Bugliarello, Yasumasa Onoe, Pinelopi Papalampidi, Ira Ktena, Christopher Knutsen, Cyrus Rashtchian, Anant Nawalgaria, Jordi Pont-Tuset, Aida Nematzadeh

**Keywords:** text-to-image evaluation; text-to-image alignment; human evaluation;

**Abstract:** 
> While text-to-image (T2I) generative models have become ubiquitous, they do not necessarily generate images that align with a given prompt. 
While many metrics and benchmarks have been proposed to evaluate T2I models and alignment metrics, the impact of the evaluation components (prompt sets, human annotations, evaluation task) has not been systematically measured.
We find that looking at only *one slice of data*, i.e. one set of capabilities or human annotations, is not enough to obtain stable ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Photorealistic Text-to-Image Diffusion Models with Imagen** (2022)
- *Authors:* Chitwan Saharia et al.
- *Direct Connection:* Gecko’s curated prompt set explicitly builds on the idea of diagnostic, capability-focused prompt suites popularized by DrawBench in Imagen, while addressing its coverage and single-template limitations.

**Rank Analysis of Incomplete Block Designs I: The Method of Paired Comparisons** (1952)
- *Authors:* Ralph Allan Bradley and Milton E. Terry
- *Direct Connection:* Gecko’s statistically grounded model comparison builds on Bradley–Terry style paired-comparison inference to aggregate human preferences into robust cross-model rankings across multiple slices.

### 🔍 Gap Identification

**Parti: Scaling Autoregressive Models for Content-Rich Image Generation** (2022)
- *Authors:* Yu et al.
- *Direct Connection:* Parti’s PartiPrompts established broad, hand-crafted prompts for stress-testing T2I models, and Gecko directly targets the gap that such single-slice prompt collections can yield unstable conclusions across different prompt categories and annotation styles.

### 📊 Baseline

**CLIPScore: A Reference-free Evaluation Metric for Image Captioning** (2021)
- *Authors:* Jack Hessel et al.
- *Direct Connection:* Gecko evaluates and contextualizes CLIP-based alignment metrics like CLIPScore, showing how conclusions about model alignment can change across prompt slices and human-annotation templates.

**Pick-a-Pic: An Open Dataset of Human Preferences for Text-to-Image Generation** (2023)
- *Authors:* Kirstain et al.
- *Direct Connection:* Gecko directly compares against preference-trained scoring functions (e.g., PickScore) derived from Pick-a-Pic’s pairwise human annotations and shows how relying on a single annotation template or slice can mislead conclusions.

**ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation** (2023)
- *Authors:* Xu et al.
- *Direct Connection:* Gecko benchmarks reward-model-based evaluators like ImageReward and demonstrates that their perceived reliability depends strongly on the prompt distribution and the human rating protocol used.

### 🔗 Related Problem

**TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering** (2023)
- *Authors:* Hu et al.
- *Direct Connection:* TIFA’s QA-based faithfulness evaluation exemplifies an alternative alignment assessment, and Gecko systematically situates such metric-based judgments within a broader, multi-template human evaluation to reveal cross-slice instability.

---

## Synthesis: How Prior Work Led to This Paper

DrawBench introduced a focused, human-curated prompt suite within Imagen to probe specific capabilities, establishing the practice of using diagnostic prompts for model comparison. Parti extended this idea with PartiPrompts, broadening the scope of capabilities and compositions stress-tested by text-to-image systems. In parallel, CLIPScore became a dominant reference-free alignment metric, operationalizing CLIP similarity as a proxy for text-image faithfulness. Preference-driven evaluators emerged with Pick-a-Pic, which collected large-scale pairwise human judgments and led to learned scoring functions (e.g., PickScore) that rank images by user preference. ImageReward likewise trained a reward model directly on human preferences to score alignment and quality, offering a learned evaluator alternative to fixed CLIP-based metrics. TIFA proposed a complementary approach—converting prompts into visual question answering checks to measure grounded faithfulness—highlighting that different evaluation formulations capture distinct facets of “alignment.” Underpinning many human preference studies, Bradley–Terry modeling provides a principled way to infer system rankings from pairwise comparisons. Together, these works revealed powerful but siloed evaluation practices: curated prompt sets, CLIP-based similarity, learned preference metrics, and QA-based faithfulness. However, each typically relied on a single prompt slice or annotation template, obscuring generalization. Gecko synthesizes these strands by curating a capability-diverse prompt set, unifying multiple human annotation templates, and applying a Bradley–Terry-style statistical comparison to aggregate across slices. This integration exposes when metric conclusions fail to transfer and yields more stable, generalizable rankings of text-to-image models and evaluators.

---

*Analysis generated on: 2026-01-06T17:09:05.459508*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

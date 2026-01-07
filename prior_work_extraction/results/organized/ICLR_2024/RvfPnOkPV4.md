# Prior Work Analysis Report

## Target Paper

**Title:** What's In My Big Data?

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yanai Elazar, Akshita Bhagia, Ian Helgi Magnusson, Abhilasha Ravichander, Dustin Schwenk, Alane Suhr, Evan Pete Walsh, Dirk Groeneveld, Luca Soldaini, Sameer Singh, Hannaneh Hajishirzi, Noah A. Smith, Jesse Dodge

**Keywords:** nlp, dataset, analaysis, data-statistics, data-quality, PII

**Abstract:** 
> Large text corpora are the backbone of language models.
However, we have a limited understanding of the content of these corpora, including general statistics, quality, social factors, and inclusion of evaluation data (contamination).
In this work, we propose What's In My Big Data? (WIMBD), a platform and a set of sixteen analyses that allow us to reveal and compare the contents of large text corpora. WIMBD builds on two basic capabilities---count and search---*at scale*, which allows us to anal...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer** (2020)
- *Authors:* Colin Raffel et al.
- *Direct Connection:* By introducing the C4 corpus and detailing large-scale Common Crawl cleaning/dedup heuristics, this work established the concrete pretraining data formulation that WIMBD audits and systematically analyzes for duplication, PII, toxicity, and contamination.

**The Pile: An 800GB Dataset of Diverse Text for Language Modeling** (2021)
- *Authors:* Leo Gao et al.
- *Direct Connection:* This paper defined a widely used, composite pretraining corpus and documented source-level filtering/dedup, directly providing one of the principal datasets WIMBD interrogates and compares with uniform count-and-search analyses.

**CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data** (2020)
- *Authors:* Guillaume Wenzek et al.
- *Direct Connection:* CCNet’s perplexity-based filtering, language-ID, and dedup pipeline underpin many web corpora (including C4), and WIMBD revisits these outputs with scalable search/count to reveal residual low-quality and duplicate content.

**Dolma: an Open Corpus of Training Data for Large Language Models** (2023)
- *Authors:* Luca Soldaini et al.
- *Direct Connection:* Dolma proposed an openly documented, filter-heavy large corpus (including PII and safety filtering), and WIMBD generalizes and standardizes such checks across multiple corpora to assess their prevalence and effectiveness at scale.

### 💡 Inspiration

**Datasheets for Datasets** (2021)
- *Authors:* Timnit Gebru et al.
- *Direct Connection:* By proposing structured, standardized documentation of dataset contents and provenance, this work inspired WIMBD’s operationalization of automated, scalable ‘what’s-in-the-corpus’ reporting via count-and-search primitives.

### 🔍 Gap Identification

**Extracting Training Data from Large Language Models** (2021)
- *Authors:* Nicholas Carlini et al.
- *Direct Connection:* By demonstrating memorization and leakage of sensitive strings such as PII from pretrained LMs, this work motivated WIMBD’s explicit large-scale searches for PII and sensitive content directly in pretraining corpora.

**Deduplicating Training Data Makes Language Models Better** (2022)
- *Authors:* Katherine Lee et al.
- *Direct Connection:* This paper showed that document and near-duplicate repetition harms LM training, directly motivating WIMBD’s corpus-wide quantification of duplicates and synthetic repetition via scalable count-and-search.

---

## Synthesis: How Prior Work Led to This Paper

C4 established a concrete, large-scale web-crawl-derived pretraining corpus and publicized practical cleaning and deduplication heuristics that set the template for modern LM data. The Pile expanded this paradigm with a composite, openly documented dataset and source-level dedup/filters, highlighting the diversity and heterogeneity of ingredients used in practice. CCNet contributed the widely adopted perplexity-based filtering and language-ID pipeline for Common Crawl, defining de facto quality control steps and dedup strategies for web text. Dolma advanced open data transparency with explicit PII and safety filtering and thorough provenance reporting, offering a modern, large-scale corpus with stronger stated safeguards. In parallel, Carlini et al. demonstrated that pretrained LMs memorize and can leak sensitive strings, foregrounding the importance of quantifying PII and sensitive content in the training data itself. Lee et al. showed that duplication and near-duplication materially degrade LM performance, emphasizing the need to measure duplicate prevalence rather than assume it is solved. Finally, Datasheets for Datasets articulated the blueprint for systematic, standardized documentation of dataset contents.
Together, these works revealed a gap: despite influential corpora and filtering pipelines, the field lacked a unified, scalable way to directly inspect and compare what is actually inside massive text datasets—duplicates, PII, toxicity, and benchmark contamination—across heterogeneous sources. The natural next step was to operationalize datasheet-like transparency at web scale by building simple, robust primitives—count and search—that can run over tens of terabytes, enabling standardized, cross-corpus audits and stress-testing the efficacy of prevailing filtering and dedup assumptions.

---

*Analysis generated on: 2026-01-06T07:37:29.656984*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

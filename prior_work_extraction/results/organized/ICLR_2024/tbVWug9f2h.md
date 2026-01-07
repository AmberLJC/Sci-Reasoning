# Prior Work Analysis Report

## Target Paper

**Title:** A Benchmark for Learning to Translate a New Language from One Grammar Book

**Conference:** ICLR 2024 (spotlight)

**Authors:** Garrett Tanzer, Mirac Suzgun, Eline Visser, Dan Jurafsky, Luke Melas-Kyriazi

**Keywords:** low-resource languages, indigenous languages, endangered languages, long context, field linguistics, unseen tasks, large language models, machine translation, benchmark

**Abstract:** 
> Large language models (LLMs) can perform impressive feats with in-context learning or lightweight finetuning. It is natural to wonder how well these models adapt to genuinely new tasks, but how does one find tasks that are unseen in internet-scale training sets? We turn to a field that is explicitly motivated and bottlenecked by a scarcity of web data: low-resource languages. In this paper, we introduce MTOB (Machine Translation from One Book), a benchmark for learning to translate between Engli...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**A Grammar of Kalamang** (2018)
- *Authors:* Eline Visser
- *Direct Connection:* This descriptive grammar provides the single human-readable source the benchmark uses as its sole supervision signal, concretely enabling the “translate from one book” task design.

### 💡 Inspiration

**The ODIN Project: On Extracting and Using Low-Resource Language Materials from the Web** (2007)
- *Authors:* Fei Xia and William D. Lewis
- *Direct Connection:* ODIN established that field-linguistic artifacts (e.g., interlinear glossed text) can be harvested and operationalized for NLP, inspiring the core idea of learning translation from human-written linguistic descriptions.

### 🔍 Gap Identification

**The FLORES-200 Evaluation Benchmark for Low-Resource and Multilingual Machine Translation** (2022)
- *Authors:* Naman Goyal et al.
- *Direct Connection:* FLORES-200 established rigorous evaluation practices for low-resource MT but primarily targets web-present languages, directly motivating the benchmark’s focus on a truly unseen language with virtually no internet footprint.

**Unsupervised Machine Translation Using Monolingual Corpora Only** (2018)
- *Authors:* Guillaume Lample et al.
- *Direct Connection:* This work showed how to train MT without parallel data but still assumes sizable monolingual corpora, a key limitation the benchmark addresses by replacing web corpora with a single descriptive grammar as supervision.

### 📊 Baseline

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Direct Connection:* The benchmark adapts RAG-style retrieval over the grammar book as a primary baseline, using retrieved sections to condition the translator on relevant linguistic facts at inference.

### 🔧 Extension

**Leveraging Passage Retrieval with Generative Models for Open-Domain Question Answering (FiD)** (2021)
- *Authors:* Gautier Izacard and Edouard Grave
- *Direct Connection:* The FiD paradigm of fusing multiple retrieved passages is directly extended as a book-reading strategy to aggregate dispersed grammatical evidence for translation decisions.

### 🔗 Related Problem

**No Language Left Behind: Scaling Human-Centered Machine Translation** (2022)
- *Authors:* NLLB Team
- *Direct Connection:* NLLB demonstrated state-of-the-art massively multilingual MT under data-rich mining and supervised regimes, contextualizing the need for a setting where translation must be learned from non-parallel linguistic descriptions rather than web-mined text.

---

## Synthesis: How Prior Work Led to This Paper

Field linguistics has long shown that human-authored linguistic resources can supervise NLP for low-resource languages: ODIN demonstrated how interlinear glossed text and other artifacts could be extracted and operationalized, establishing that descriptive materials themselves can be supervision. Parallelly, FLORES-200 introduced rigorous evaluation methodology for low-resource MT across many languages, while NLLB pushed multilingual translation at scale using mined corpora. Unsupervised MT advanced the idea of translation without bitext (e.g., via back-translation) but still presupposed sizable monolingual data, a requirement often impossible for endangered or minimally documented languages. On the systems side, retrieval-augmented generation (RAG) and Fusion-in-Decoder (FiD) showed that models can read and aggregate information from long, dispersed sources by retrieving relevant passages and conditioning generation on them. Finally, the Kalamang descriptive grammar by Visser provided a comprehensive, human-readable account of a language with almost no web presence, offering a unique, compact supervision source.
Together these works exposed a gap: while low-resource MT benchmarks and systems matured, they largely relied on web-minable corpora, leaving truly unseen languages underserved; yet retrieval methods and linguistic documentation hinted that a single, descriptive source could be leveraged. The current benchmark synthesizes these threads by formulating translation as learning from one grammar book: it operationalizes field-linguistic description as supervision, evaluates under FLORES-style rigor but on an unseen language, and employs RAG/FiD-style book-reading as principled baselines, creating a natural next step for studying genuine adaptation to new languages.

---

*Analysis generated on: 2026-01-06T07:54:27.555553*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

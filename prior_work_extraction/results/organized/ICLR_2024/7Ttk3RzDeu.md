# Prior Work Analysis Report

## Target Paper

**Title:** BooookScore: A systematic exploration of book-length summarization in the era of LLMs

**Conference:** ICLR 2024 (oral)

**Authors:** Yapei Chang, Kyle Lo, Tanya Goyal, Mohit Iyyer

**Keywords:** summarization, evaluation, long context, prompting, LLM

**Abstract:** 
> Summarizing book-length documents ($>$100K tokens)  that exceed the context window size of large language models (LLMs) requires first breaking the input document into smaller chunks and then prompting an LLM to merge, update, and compress chunk-level summaries. Despite the complexity and importance of this task, it has yet to be meaningfully studied due to the challenges of evaluation: existing book-length summarization datasets (e.g., BookSum) are in the pretraining data of most public LLMs, a...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Overview of the TAC 2008 Update Summarization Task** (2008)
- *Authors:* Hoa Trang Dang and Karolina Owczarzak
- *Direct Connection:* The TAC update summarization paradigm directly motivates BooookScore’s second workflow—incrementally updating a running summary as new chunks arrive—adapting the ‘update’ notion to a single long document.

### 🔍 Gap Identification

**BookSum: A Collection of Datasets for Long-form Narrative Summarization** (2022)
- *Authors:* Tanya Goyal et al.
- *Direct Connection:* BookSum established book-length summarization as a task but its presence in common LLM pretraining corpora created contamination concerns that BooookScore explicitly addresses by curating recent books for unbiased evaluation.

**SummEval: Re-evaluating Summarization Evaluation** (2021)
- *Authors:* Alexander Fabbri et al.
- *Direct Connection:* SummEval showed that standard automatic metrics poorly capture human judgments, a limitation BooookScore revisits in the LLM era by demonstrating these metrics’ failure to detect long-range coherence errors in book summaries.

**FRANK: A Benchmark for Factuality Evaluation in Abstractive Summarization** (2021)
- *Authors:* Artidoro Pagnoni et al.
- *Direct Connection:* FRANK’s sentence-level factuality error taxonomy for news highlights evaluation blind spots (e.g., narrative coherence and cross-document entity tracking) that BooookScore fills with a book-scale coherence error taxonomy.

### 📊 Baseline

**Summarizing Books with Human Feedback** (2021)
- *Authors:* Jeff Wu et al.
- *Direct Connection:* This work popularized the recursive chunk-and-merge approach for book-length summarization that BooookScore instantiates as one of its two prompting workflows and evaluates for coherence at book scale.

**SummaC: Re-Visiting NLI-based Models for Factual Consistency Evaluation in Summarization** (2022)
- *Authors:* Philippe Laban et al.
- *Direct Connection:* As a leading NLI-based consistency metric, SummaC serves as an automatic evaluation baseline that BooookScore tests and finds insufficient for detecting multi-chapter coherence failures in LLM-generated book summaries.

---

## Synthesis: How Prior Work Led to This Paper

Recursive, chunk-based summarization emerged as a practical strategy for book-length inputs with Summarizing Books with Human Feedback, which operationalized a hierarchical merge of chunk summaries to handle context limits. In parallel, the TAC 2008 Update Summarization task formalized an incremental ‘update’ paradigm in which a system maintains and revises a running summary as new information arrives, establishing a template for iterative integration of content. BookSum then anchored the community around long-form narrative summarization by providing aligned book/chapter summaries at scale, while SummEval exposed systemic gaps in automatic metrics’ ability to reflect human judgments. FRANK deepened this critique by cataloging factuality errors at the sentence level for news, but it left unaddressed the cross-chapter coherence phenomena central to narratives (e.g., character tracking, temporal consistency). NLI-based metrics like SummaC offered stronger factuality checks than lexical overlap, yet remained local in scope and struggled with long-range dependencies and global coherence in multi-section texts. Together these works revealed a clear opportunity: evaluate book-length summarization in the LLM era using the two dominant decomposition workflows—hierarchical merge and incremental update—on uncontaminated books, and examine coherence beyond sentence-level factuality. BooookScore synthesizes these strands by curating recent books, instantiating both workflows with state-of-the-art LLMs, and constructing a fine-grained, narrative-focused coherence error taxonomy, thereby providing the first systematic study of coherence failures specific to book-scale LLM summarization.

---

*Analysis generated on: 2026-01-06T06:22:34.358487*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

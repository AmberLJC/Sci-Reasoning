# Prior Work Analysis Report

## Target Paper
**Title:** GLGYYqPwjy
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

QuRating sits at the intersection of three lines of work: heuristic web-scale data filtering, preference-based learning from pairwise comparisons, and score-weighted sampling for data curation. Early large-scale corpora such as C4 and OpenWebText, as well as the CCNet pipeline, established that filtering noisy web data with simple heuristics or proxy signals can materially improve language model pretraining. However, these approaches largely rely on static rules (e.g., language ID, perplexity thresholds, toxicity lists) or crude popularity signals, leaving richer human notions of quality—style, expertise, factuality, educational value—under-modeled.

The second thread, inaugurated in NLP by preference-based training such as Learning to Summarize with Human Feedback, showed how pairwise comparisons can train scalar reward models that capture nuanced human judgments. Subsequent evidence from MT-Bench and Chatbot Arena that LLMs can reliably act as judges enabled scaling such comparisons beyond costly human annotation. QuRating directly leverages this: LLM-generated pairwise judgments are converted into scalar ratings (QuRater), providing multi-criterion quality scores for massive corpora.

Finally, classic data selection methods (Moore–Lewis) and dynamic/soft sampling in NMT demonstrated that selecting or sampling examples proportional to relevance scores can improve generalization while preserving diversity. QuRating’s sampling “using quality ratings as logits” operationalizes this principle, balancing high-quality text with breadth. Together, these prior works shaped QuRating’s core innovation: learning rich, LLM-judged quality scores from pairwise comparisons and using them to curate pretraining data in a way that outperforms heuristic filtering while maintaining diversity.

---
*Generated: 2026-01-07T00:02:04.880095*

# Prior Work Analysis Report

## Target Paper

**Title:** Consistency Checks for Language Model Forecasters

**Conference:** ICLR 2025 (oral)

**Authors:** Daniel Paleka, Abhimanyu Pallavi Sudhir, Alejandro Alvarez, Vineeth Bhat, Adam Shen, Evan Wang, Florian Tramèr

**Keywords:** forecasting, markets, trading, LLM, evaluation, eval, consistency, robustness

**Abstract:** 
> Forecasting is a task that is difficult to evaluate: the ground truth can only be known in the future. Recent work showing LLM forecasters rapidly approaching human-level performance begs the question: how can we benchmark and evaluate these forecasters *instantaneously*? Following the consistency check framework, we measure the performance of forecasters in terms of the consistency of their predictions on different logically-related questions. We propose a new, general consistency metric based ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**La prévision: ses lois logiques, ses sources subjectives** (1937)
- *Authors:* Bruno de Finetti
- *Direct Connection:* This work’s Dutch book/coherence principle directly underpins the paper’s arbitrage-based consistency metric by formalizing when a set of probabilities admits a sure-profit bet.

**Combinatorial Information Market Design** (2003)
- *Authors:* Robin Hanson
- *Direct Connection:* Hanson’s cost-function prediction markets operationalize arbitrage-free price constraints across logically related events, which the paper adapts as a general procedure for detecting incoherent forecasts.

### 💡 Inspiration

**SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models** (2023)
- *Authors:* Yao Khai Manakul et al.
- *Direct Connection:* SelfCheckGPT’s idea of using internal consistency among model outputs as a proxy for correctness directly inspires evaluating forecasters via logical-consistency checks rather than resolved outcomes.

**Beyond Accuracy: Behavioral Testing of NLP Models with CheckList** (2020)
- *Authors:* Marco Tulio Ribeiro et al.
- *Direct Connection:* CheckList’s template-driven generation of logically related test cases motivates the paper’s automated system for instantiating consistency checks from base forecasting questions.

### 🔍 Gap Identification

**Strictly Proper Scoring Rules, Prediction, and Estimation** (2007)
- *Authors:* Tilmann Gneiting et al.
- *Direct Connection:* By framing evaluation via proper scoring rules that require realized outcomes, this paper highlights the core limitation the new arbitrage-based metric overcomes—instantaneous assessment without ground truth.

### 🔧 Extension

**Efficient Market Making via Convex Optimization** (2013)
- *Authors:* Jacob Abernethy et al.
- *Direct Connection:* This work’s convex-optimization view of market makers provides the computational lens for quantifying maximum arbitrage (sure-profit) against inconsistent quotes, which the paper repurposes to score LLM forecast consistency.

---

## Synthesis: How Prior Work Led to This Paper

De Finetti established the Dutch book criterion, showing that a set of probability assignments is rational only if it precludes a sure-profit bet; this coherence notion precisely characterizes when forecasts are internally consistent. Hanson translated coherence into market design, using cost-function prediction markets to ensure arbitrage-free prices across logically related outcomes, and thus operationalized practical tests for inconsistencies like complementary events not summing to one. Abernethy and colleagues cast such market makers in a convex-optimization framework, quantifying and computing maximum arbitrage when quotes violate constraints—making inconsistency measurable as exploitable profit. On the evaluation side, Gneiting and Raftery formalized strictly proper scoring rules as the normative way to assess probabilistic forecasts, but these inherently require waiting for outcomes to resolve. In NLP, SelfCheckGPT showed that internal agreement among a model’s own outputs can serve as a proxy for correctness without ground truth. Complementarily, CheckList demonstrated how templated, logically related test suites can be programmatically generated to probe specific behavioral properties. Taken together, these strands revealed a gap: forecasting urgently needs instant, outcome-free evaluation, and there exists a principled notion—arbitrage—that both defines inconsistency and can be computed over logically related questions. The paper synthesizes these insights by auto-generating structured forecasting question sets (à la CheckList), eliciting probabilistic predictions, and scoring them via the maximum arbitrage implied by de Finetti/Hanson-style coherence, computed with the optimization tools inspired by Abernethy et al., thereby offering a ground-truth-free, quantitative consistency benchmark for LLM forecasters.

---

*Analysis generated on: 2026-01-06T06:41:39.394441*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

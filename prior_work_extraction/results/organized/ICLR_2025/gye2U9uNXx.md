# Prior Work Analysis Report

## Target Paper

**Title:** Uncovering Gaps in How Humans and LLMs Interpret Subjective Language

**Conference:** ICLR 2025 (spotlight)

**Authors:** Erik Jones, Arjun Patrawala, Jacob Steinhardt

**Keywords:** safety, alignment, constitutional ai, language model failures, misalignment, automated evaluation, automated red-teaming

**Abstract:** 
> Humans often rely on subjective natural language to direct language models (LLMs); for example, users might instruct the LLM to write an *enthusiastic* blogpost, while developers might train models to be *helpful* and *harmless* using LLM-based edits. The LLM’s *operational semantics* of such subjective phrases---how it adjusts its behavior when each phrase is included in the prompt---thus dictates how aligned it is with human intent. In this work, we uncover instances of *misalignment* between ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* This work operationalized subjective principles like “helpful” and “harmless” via a critique-and-revise loop using natural-language rules, directly motivating TED’s focus on whether models’ operational semantics for such subjective phrases match human intent.

**Training a Helpful and Harmless Assistant with RLHF** (2022)
- *Authors:* Yuntao Bai et al.
- *Direct Connection:* By formalizing the helpful/harmless alignment objective and providing widely used data/protocols, this paper establishes the subjective value targets whose meanings TED checks for alignment with human expectations.

**WordNet: A Lexical Database for English** (1995)
- *Authors:* George A. Miller
- *Direct Connection:* WordNet’s curated synonym/antonym relations provide the human-reference thesaurus that TED explicitly compares against to detect discrepancies in the LLM’s operational semantics.

### 💡 Inspiration

**Discovering Language Model Behaviors with Model-Written Evaluations** (2022)
- *Authors:* Ethan Perez et al.
- *Direct Connection:* Showing that LLMs can generate targeted evaluations to expose unexpected behaviors inspired TED’s use of model-driven structure (an operational thesaurus) to automatically surface surprising misalignments tied to subjective descriptors.

### 🔧 Extension

**Semantically Equivalent Adversarial Rules for Debugging NLP Models** (2018)
- *Authors:* Marco Tulio Ribeiro et al.
- *Direct Connection:* SEAR’s insight—probing models with human-defined semantic equivalences (e.g., synonym substitutions) to reveal failures—is directly extended by TED to the instruction-following setting via a large-scale, LLM-induced synonymy over subjective phrases.

### 🔗 Related Problem

**Red Teaming Language Models with Language Models** (2022)
- *Authors:* Ethan Perez et al.
- *Direct Connection:* This paper introduced automated failure elicitation with LLMs; TED builds on that paradigm by systematically eliciting failures through disagreements between an LLM-derived ‘operational thesaurus’ and a human reference thesaurus.

---

## Synthesis: How Prior Work Led to This Paper

Constitutional AI demonstrated that natural-language principles like “helpful” and “harmless” can guide a critique-and-revise training loop, thereby making subjective descriptors a central mechanism for alignment. In parallel, Anthropic’s helpful/harmless RLHF work concretized these subjective targets and popularized the practice of specifying them in instructions and training, establishing the exact value-laden phrases models are supposed to implement. Red Teaming Language Models with Language Models showed that LLMs can systematically uncover their own failure modes through automated prompt generation, motivating structured, model-driven searches for safety gaps. Model-Written Evaluations extended this idea by using LMs to synthesize targeted tests that reveal surprising, misaligned behaviors, suggesting that model-internal regularities can be exploited to find failures at scale. Earlier, SEAR introduced the principle of diagnosing NLP systems with human-declared semantic invariances (e.g., synonym swaps), revealing brittleness when models diverge from these equivalences. WordNet, as a canonical human-built lexicon of synonymy and antonymy, provides a stable reference of semantic relations for such tests.
Taken together, these works point to a gap: alignment methods heavily rely on subjective language while automated safety discovery lacks a principled way to verify that models implement these descriptors as humans intend. The current paper synthesizes these threads by constructing an LLM-induced “operational thesaurus” over subjective phrases and explicitly comparing it to a human reference (WordNet-like) to target disagreements, then using this structured mismatch to elicit concrete misalignments. Given the prevalence of CAI/RLHF and automated red teaming, codifying descriptor semantics and auditing their fidelity was a natural next step.

---

*Analysis generated on: 2026-01-06T18:08:17.238995*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

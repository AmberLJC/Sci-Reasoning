# Prior Work Analysis Report

## Target Paper

**Title:** LEGO-Prover: Neural Theorem Proving with Growing Libraries

**Conference:** ICLR 2024 (oral)

**Authors:** Haiming Wang, Huajian Xin, Chuanyang Zheng, Zhengying Liu, Qingxing Cao, Yinya Huang, Jing Xiong, Han Shi, Enze Xie, Jian Yin, Zhenguo Li, Xiaodan Liang

**Keywords:** Theorem proving, Large language model, Autoformalization

**Abstract:** 
> Despite the success of large language models (LLMs), the task of theorem proving still remains one of the hardest reasoning tasks that is far from being fully solved. Prior methods using language models have demonstrated promising results, but they still struggle to prove even middle school level theorems. One common limitation of these methods is that they assume a fixed theorem library during the whole theorem proving process. However, as we all know, creating new useful theorems or even new t...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**HOList: Machine Learning for Higher-Order Logic Theorem Proving** (2019)
- *Authors:* Kshitij Bansal et al.
- *Direct Connection:* HOList established the tactic-level learning and premise-selection formulation in interactive theorem proving that LEGO-Prover adopts while upgrading the knowledge source from a fixed corpus to a self-grown lemma library.

### 💡 Inspiration

**MaLARea: a Metasystem for Automated Reasoning in Large Theories** (2007)
- *Authors:* Josef Urban
- *Direct Connection:* MaLARea’s feedback loop—proving theorems, adding them to the knowledge base, and improving premise selection—directly inspires LEGO-Prover’s growing library of verified lemmas to progressively enable harder proofs.

**Voyager: An Open-Ended Embodied Agent with Large Language Models** (2023)
- *Authors:* Guanzhi Wang et al.
- *Direct Connection:* Voyager’s idea of a continually expanding, verified skill library informs LEGO-Prover’s skills-as-lemmas abstraction and its mechanisms to retrieve, create, and evolve reusable capabilities during problem solving.

### 🔍 Gap Identification

**Generative Language Modeling for Automated Theorem Proving (GPT-f)** (2020)
- *Authors:* Fabrice Polu et al.
- *Direct Connection:* GPT-f demonstrated LLM-guided proof search over a fixed Metamath library, and its inability to introduce reusable lemmas directly motivates LEGO-Prover’s growing, persistent library of verified lemma-skills.

### 📊 Baseline

**LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (2023)
- *Authors:* Jiaxuan Yang et al.
- *Direct Connection:* LEGO-Prover builds on LeanDojo’s retrieval-augmented LLM-in-the-loop proving in Lean by extending retrieval to a dynamically expanding set of verified lemmas and reusing them as modular skills across problems.

### 🔗 Related Problem

**TacticToe: Learning to Prove Theorems by Learning Proof Tactics** (2018)
- *Authors:* Thibault Gauthier et al.
- *Direct Connection:* TacticToe’s learning-to-select tactics and premises from a static HOL Light library is generalized in LEGO-Prover by creating, verifying, and reusing new lemmas as first-class skills during search.

---

## Synthesis: How Prior Work Led to This Paper

GPT-f showed that autoregressive language models can guide formal proof search, but it operated over a static collection of axioms and theorems, never introducing new, reusable lemmas. LeanDojo advanced LLM-based proving in Lean by coupling tactic generation with retrieval of relevant facts from an existing library, concretizing retrieval-augmented proof search in a modern interactive prover. HOList encoded interactive proving as tactic-level decision making with premise selection, clarifying how learning can steer search in higher-order logic environments. TacticToe further demonstrated that learning to pick tactics and premises from a fixed corpus can scale across a large library, yet still assumed an immutable base of available lemmas. In automated reasoning over large theories, MaLARea pioneered the feedback loop where newly proved theorems are fed back into learning and premise selection, enabling iterative improvement by expanding the knowledge base. Beyond theorem proving, Voyager established that LLM agents can accumulate a growing library of verified, reusable skills and retrieve them to tackle progressively harder tasks.
Bringing these threads together reveals a gap: LLM-guided, retrieval-augmented tactic search remains bottlenecked by a fixed library, while iterative knowledge accumulation demonstrably boosts capability in both ATP and LLM agents. LEGO-Prover synthesizes these insights by treating verified lemmas as modular skills, retrieving from and continually expanding a persistent library during proof search, and evolving these skills so they can be composed to prove harder results—turning static premise selection into a lifelong, library-growing theorem-proving paradigm.

---

*Analysis generated on: 2026-01-06T16:14:19.149505*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

# Prior Work Analysis Report

## Target Paper
**Title:** DJcEoC9JpQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Bandit Based Monte-Carlo Planning** (2006)
- *Authors:* Levente Kocsis and Csaba Szepesvári
- *Connection:* RCTS’s re-ranking is instantiated with MCTS using UCT to balance exploration and exploitation, relying on the foundational UCT framework introduced in this work.

**OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge** (2019)
- *Authors:* Kenneth Marino et al.
- *Connection:* RCTS targets the knowledge-intensive VQA setting defined by OK-VQA, motivating the need for external retrieval and richer reasoning exemplars to overcome knowledge scarcity.

### 💡 Inspiration

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2022)
- *Authors:* Xuezhi Wang et al.
- *Connection:* RCTS’s self-consistent evaluation mechanism for constructing a reasoning-context knowledge base is inspired by Self-Consistency’s idea of aggregating multiple reasoning paths to obtain reliable signals.

**Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Connection:* RCTS’s MCTS-HR reframes example selection as a tree search over candidate reasoning contexts, directly building on Tree-of-Thoughts’ insight to search over intermediate reasoning states with heuristic evaluations.

**Mastering the game of Go with deep neural networks and tree search** (2016)
- *Authors:* David Silver et al.
- *Connection:* RCTS mirrors AlphaGo’s principle of guiding MCTS with heuristic value/policy signals by using LVLM-derived consistency and relevance scores as heuristic rewards to steer the search over contexts.

### 🔍 Gap Identification

**Self-RAG: Learning to Retrieve, Generate, and Critique for Better Language Modeling** (2023)
- *Authors:* Akari Asai et al.
- *Connection:* Self-RAG highlights instability and noise in retrieved evidence and proposes critique-guided selection; RCTS addresses this gap by extending critique to multimodal reasoning contexts and replacing greedy reranking with MCTS-HR.

### 📊 Baseline

**Retrieval-Augmented Generation for Knowledge-Intensive NLP** (2020)
- *Authors:* Patrick Lewis et al.
- *Connection:* RCTS adopts the RAG pipeline and directly improves the retrieval→context→generation loop by enriching contexts with reasoning patterns and replacing flat relevance scoring with tree-search re-ranking.

---

## Synthesis

RCTS sits at the intersection of retrieval-augmented generation and structured search for reasoning. The problem setting originates from OK-VQA, which establishes that VQA often requires external knowledge beyond the image. The RAG framework by Lewis et al. provides the baseline pipeline—retrieve, condition the model on retrieved context, then generate—yet its performance hinges on the quality of retrieved evidence. Recent advances in reasoning highlight two key ideas RCTS fuses. First, Self-Consistency shows that aggregating multiple reasoning paths yields reliable signals; RCTS adapts this to curate a reasoning-context knowledge base by selecting exemplars with intrinsically consistent reasoning. Second, Tree-of-Thoughts demonstrates that explicitly searching over intermediate reasoning states improves solution quality; RCTS operationalizes this via a Monte Carlo Tree Search scheme. Grounded in the UCT formulation and inspired by AlphaGo’s heuristic-guided tree search, RCTS introduces MCTS with heuristic rewards to explore and prioritize combinations of retrieved reasoning exemplars, balancing exploration and exploitation. Finally, Self-RAG identifies a core gap of RAG—noisy retrieval and unstable use of evidence—and proposes critique-guided retrieval in text; RCTS extends this idea to the multimodal setting and replaces greedy/learned reranking with principled tree search. Together, these works directly shape RCTS’s core contributions: a reasoning-enriched knowledge base and MCTS-driven re-ranking that strengthens LVLM reasoning consistency and accuracy.

---
*Generated: 2026-01-06T23:07:19.608394*

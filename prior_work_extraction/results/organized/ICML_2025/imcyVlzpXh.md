# Prior Work Analysis Report

## Target Paper
**Title:** imcyVlzpXh
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**DARTS: Differentiable Architecture Search** (2019)
- *Authors:* Hanxiao Liu et al.
- *Connection:* MaAS directly borrows the idea of continuous relaxation over discrete architectural choices from DARTS to parameterize an 'agentic supernet' over workflow graphs and enable gradient-based optimization.

### 💡 Inspiration

**Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (2021)
- *Authors:* William Fedus et al.
- *Connection:* MaAS’s goal of allocating LLM/tool calls and token budgets per query echoes Switch Transformer’s conditional computation—routing compute based on input—now lifted from layers to agentic workflow selection.

### 🔍 Gap Identification

**DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines** (2024)
- *Authors:* Omar Khattab et al.
- *Connection:* DSPy automates LLM pipeline design but yields a single, static program; MaAS explicitly addresses this limitation by optimizing a distribution over agentic architectures and sampling query-specific workflows to adapt computation and cost.

### 📊 Baseline

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Connection:* MaAS treats reasoning–acting tool use (as in ReAct) as a core building block of agentic workflows and improves on this static pattern by selecting query-dependent compositions from a learned supernet rather than committing to a fixed loop.

### 🔧 Extension

**Once-for-All: Train One Network and Specialize it for Efficient Deployment** (2020)
- *Authors:* Han Cai et al.
- *Connection:* Analogous to OFA’s supernet that supports on-the-fly subnetwork sampling under constraints, MaAS extends the supernet paradigm to agentic architectures to sample query-conditioned sub-workflows that meet resource budgets.

### 🔗 Related Problem

**Graph of Thoughts: Solving Elaborate Problems with Large Language Models** (2024)
- *Authors:* Jakub Besta et al.
- *Connection:* By framing reasoning as traversals over graph-structured thought processes, GoT motivates MaAS’s view of agentic workflows as graph architectures whose paths can be sampled per-instance from a learned distribution.

---

## Synthesis

MaAS departs from the prevailing practice of designing a single, static multi-step LLM workflow by treating the space of agentic systems as a supernet and sampling query-dependent sub-architectures. This shift is enabled by two key lines of prior work. From the neural architecture search literature, DARTS introduced a continuous relaxation of discrete architectural choices, forming the methodological foundation for MaAS’s differentiable optimization of an agentic supernet. Once-for-All extended this idea to support on-the-fly subnetwork selection under deployment constraints; MaAS adapts this supernet specialization concept to the domain of agentic workflows, sampling sub-graphs conditioned on query difficulty and resource budgets. In parallel, conditional computation research, epitomized by Switch Transformers, demonstrated the utility of routing compute per input; MaAS generalizes this principle from token- or layer-level routing to selecting which agents, tools, and interactions to invoke per query. On the LLM reasoning/agent side, ReAct provided the core reasoning–acting loop that many agentic workflows rely on; MaAS improves over such fixed patterns by learning to assemble (or skip) these components dynamically. Finally, DSPy showed that automated compilation and optimization of LLM pipelines is feasible but typically produces a single program; MaAS directly addresses this gap by optimizing a distribution over workflows, and the graph-structured perspective of Graph of Thoughts further motivates viewing agentic systems as paths sampled from a larger architecture. Together, these works form the direct intellectual lineage to MaAS’s agentic supernet.

---
*Generated: 2026-01-06T23:07:19.634241*

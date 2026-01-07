# Prior Work Analysis Report

## Target Paper
**Title:** NPKZF1WDjZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DeAR sits at the intersection of three influential threads in LLM reasoning research: rationale generation, decomposition, and iterative self-feedback. Chain-of-Thought established that explicit rationales unlock stronger reasoning, while Least-to-Most and Decomposed Prompting showed that decomposing problems into simpler sub-questions can make complex tasks tractable. Tree of Thoughts advanced this further by casting reasoning as a branching tree, enabling deliberative exploration of alternative paths.

DeAR’s core innovation unifies these ideas while addressing their limitations: it adopts a tree-structured, decomposition-first plan like ToT and Least-to-Most, but executes the entire process within a single LLM that iteratively updates a global reasoning state. Instead of ToT’s external search/evaluation or Self-Consistency’s post-hoc voting over independent chains, DeAR’s Analyze and Rethink stages propagate natural-language feedback through the tree, allowing child nodes to correct and refine parent rationales. This draws on the feedback paradigm from Self-Refine and the reflective corrections of Reflexion, but applies them structurally across a hierarchical reasoning plan.

The result is a human-like reasoning cycle—Decompose, Analyze, Rethink—that constructs, evaluates, and revises a reasoning tree holistically. By coupling hierarchical planning with global, feedback-driven updates, DeAR moves beyond linear CoT, modular decomposition without cross-level revision, and sampling-based selection, providing a principled mechanism to build coherent, adaptive rationales for intricate problems.

---
*Generated: 2026-01-06T23:33:36.272013*

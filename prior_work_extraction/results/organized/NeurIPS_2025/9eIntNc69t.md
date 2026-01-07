# Prior Work Analysis Report

## Target Paper
**Title:** 9eIntNc69t
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Memo’s core idea—learning to create and retrieve compact summaries within a Transformer policy to operate over long horizons—emerges at the intersection of memory-augmented RL and long-context Transformers. On the RL side, MERLIN and Neural Map established that agents benefit from writing compressed, queryable memories of past experience, especially in partially observable, embodied settings. These works crystallized the need for explicit mechanisms that distill high-dimensional sensory streams into actionable state abstractions. On the sequence modeling side, Transformer-XL and its RL adaptation GTrXL demonstrated how segment-level recurrence enables long-range dependencies in Transformer policies, but still leaves models vulnerable to context overflow. Compressive Transformer advanced this further by showing that older activations can be learnably compressed without sacrificing access, directly motivating Memo’s emphasis on selective retention rather than full-context reliance. Complementing these, Set Transformer’s inducing-point tokens provided a general blueprint for learnable latent summaries that can stand in for large input sets, a concept Memo recasts temporally as periodic summarization tokens interleaved with sensory inputs. Decision Transformer highlighted the practical limitations of vanilla Transformer policies in RL due to finite context, underscoring the importance of memory efficiency. Synthesizing these threads, Memo embeds learnable summarization tokens into the policy’s training loop, teaching the agent when and what to write and how to retrieve it, thereby achieving memory efficiency and long-horizon competence in embodied RL.

---
*Generated: 2026-01-07T00:21:33.130107*

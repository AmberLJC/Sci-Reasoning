# Prior Work Analysis Report

## Target Paper
**Title:** S3GhJooWIC
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Universal Transformers** (2018)
- *Authors:* Mostafa Dehghani et al.
- *Connection:* This paper adopts the Universal Transformer idea of repeatedly applying a shared block and allowing variable-depth inference, scaling it to a decoder-only LM that unrolls to arbitrary depth to scale test-time compute for reasoning.

**Adaptive Computation Time for Recurrent Neural Networks** (2016)
- *Authors:* Alex Graves
- *Connection:* The model’s per-token adaptive compute and halting behavior directly build on ACT’s paradigm of dynamically iterating a recurrent computation and deciding when to stop based on learned signals.

### 💡 Inspiration

**Deep Equilibrium Models** (2019)
- *Authors:* Shaojie Bai et al.
- *Connection:* DEQ framed depth as recurrent fixed-point iteration where the number of solver steps trades off compute and accuracy; the present work similarly treats depth as iterative latent refinement at test time, while opting for explicit unrolling to fit generative LMs and enable cache sharing.

**Neural GPUs Learn Algorithms** (2015)
- *Authors:* Łukasz Kaiser et al.
- *Connection:* Neural GPU demonstrated that iterating a shared computation cell over many steps enables algorithmic reasoning; this work carries the same iterative latent-computation principle into modern decoder-only transformers for math and code.

### 📊 Baseline

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Connection:* CoT established the dominant approach to test-time compute scaling by emitting long textual rationales; this paper directly targets the same goal but replaces output-token expansion with latent recurrent depth, addressing CoT’s context and data dependencies.

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2022)
- *Authors:* Xuezhi Wang et al.
- *Connection:* Self-Consistency scales test-time compute via multiple sampled CoTs and voting; the current work offers an alternative by increasing latent depth within a single run, avoiding multi-sample decoding while achieving similar or better reasoning gains.

### 🔧 Extension

**Depth-Adaptive Transformer** (2019)
- *Authors:* M. Elbayad et al.
- *Connection:* Depth-Adaptive Transformer introduced token-wise halting to choose the number of transformer steps; this work extends that mechanism to large decoder-only LMs and positions it explicitly as a vehicle for test-time compute scaling on reasoning tasks.

---

## Synthesis

The core innovation—scaling test-time compute by iterating a shared block to arbitrary depth so the model reasons in latent space—stands on the lineage of recurrent-depth and adaptive computation ideas. Universal Transformers provided the key architectural foundation by sharing parameters across layers and enabling variable-depth computation, while Adaptive Computation Time established the learned halting mechanism that underpins per-token adaptive compute. Depth-Adaptive Transformer took these ideas into token-wise dynamic depth, directly foreshadowing the present work’s per-token compute control in a large-scale, decoder-only LM. Deep Equilibrium Models contributed the conceptual framing of depth as iterative refinement, showing that the number of inference iterations can be traded against accuracy—an insight mirrored here with explicit unrolling to suit autoregressive generation and facilitate KV-cache reuse. On the evaluation and motivation side, Chain-of-Thought prompting and Self-Consistency defined the mainstream baselines for test-time scaling by producing more tokens, but they suffer from context-window pressure and reliance on explicit rationales. The present paper addresses these gaps by moving the extra computation into latent space, requiring no specialized CoT data and supporting small contexts. Finally, Neural GPU’s demonstration that many-step iteration of a shared cell yields algorithmic reasoning provides early inspiration for the claim that certain forms of reasoning are better realized via latent iterative computation than via explicit natural-language traces.

---
*Generated: 2026-01-06T23:08:23.946676*

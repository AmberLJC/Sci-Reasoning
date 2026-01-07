# Prior Work Analysis Report

## Target Paper

**Title:** Lean-STaR: Learning to Interleave Thinking and Proving

**Conference:** ICLR 2025 (spotlight)

**Authors:** Haohan Lin, Zhiqing Sun, Sean Welleck, Yiming Yang

**Keywords:** Automated Theorem Proving, Chain-of-Thought, Reinforcement Learning, Reasoning

**Abstract:** 
> Traditional language model-based theorem proving assumes that by training on a sufficient amount of formal proof data, a model will learn to prove theorems. Our key observation is that a wealth of informal information that is not present in formal proofs can be useful for learning to prove theorems. For instance, humans think through steps of a proof, but this thought process is not visible in the resulting code. We present Lean-STaR, a framework for training language models to produce informal ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Thinking Fast and Slow with Deep Learning and Tree Search (Expert Iteration)** (2017)
- *Authors:* Thomas Anthony et al.
- *Direct Connection:* Lean-STaR adopts the expert-iteration paradigm by iteratively training on data produced by a stronger ‘expert’ (verified proofs sampled by the model), mirroring the expert-iteration loop without MCTS.

**LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (2023)
- *Authors:* Michihiro Yasunaga et al.
- *Direct Connection:* LeanDojo’s formulation of step-wise Lean tactic prediction and its access to ground-truth tactic traces enable Lean-STaR’s retrospective generation of step-aligned synthetic thoughts and proof verification.

### 💡 Inspiration

**ReAct: Synergizing Reasoning and Acting in Language Models** (2023)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* ReAct’s explicit interleaving of natural language ‘thoughts’ with actions directly inspired Lean-STaR’s design of generating an informal thought before each Lean tactic during proof construction.

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Jason Wei et al.
- *Direct Connection:* The finding that explicitly generating rationales improves reasoning motivated Lean-STaR’s use of synthetic ‘thoughts’ to guide tactic prediction at every proof step.

### 🔧 Extension

**Self-Taught Reasoner: Bootstrapping Reasoning With Reasoning** (2022)
- *Authors:* Tomer Zelikman et al.
- *Direct Connection:* Lean-STaR directly extends STaR’s self-improvement loop by fine-tuning on proofs the model itself samples and that are verified by a proof assistant, but adapts the target to interleave learned thoughts with formal tactics at each step.

### 🔗 Related Problem

**Generative Language Modeling for Automated Theorem Proving in Metamath (GPT-f)** (2020)
- *Authors:* Stanislas Polu and Ilya Sutskever
- *Direct Connection:* GPT-f’s LM+verifier loop for formal proofs informed Lean-STaR’s verify-and-train scheme, which similarly samples candidate proofs and filters by a proof assistant before updating the model.

---

## Synthesis: How Prior Work Led to This Paper

Self-Taught Reasoner demonstrated that language models can bootstrap their reasoning by generating rationales and then fine-tuning on the model’s own verified correct solutions, establishing a self-improvement loop grounded in correctness. ReAct showed that interleaving natural-language ‘thoughts’ with concrete actions/tool calls helps models plan and execute complex tasks, highlighting the value of coupling internal deliberation with stepwise acting. Chain-of-Thought revealed that explicitly producing intermediate rationales improves performance across reasoning tasks, suggesting that latent reasoning can be externalized and trained. Expert Iteration provided the general recipe of iteratively improving a policy by training on data produced by a stronger expert obtained via search/verification, crystallizing a powerful self-training loop. LeanDojo framed Lean proving as stepwise tactic prediction with verifiable trajectories and accessible ground-truth tactic sequences, making it possible to align supervision precisely to each proof step. GPT-f established that language models can perform formal proof search when paired with a symbolic verifier, validating the practicality of sample-and-verify pipelines in theorem proving. Together, these works exposed a gap: formal proof traces lack the informal reasoning that humans use between steps, yet iterative self-training and verifier feedback can reliably improve models. Lean-STaR synthesizes these insights by retrofitting step-aligned, synthetic thoughts onto ground-truth tactics, training a model to think before each action, and then applying an expert-iteration, verify-and-fine-tune loop to progressively strengthen both its thoughts and its tactic choices—an immediate next step given the evidence that interleaved thought–action and verified self-improvement are synergistic.

---

*Analysis generated on: 2026-01-06T11:55:34.617320*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

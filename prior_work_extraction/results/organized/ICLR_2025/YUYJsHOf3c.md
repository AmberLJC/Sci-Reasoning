# Prior Work Analysis Report

## Target Paper

**Title:** ReGenesis: LLMs can Grow into Reasoning Generalists via Self-Improvement

**Conference:** ICLR 2025 (oral)

**Authors:** XIANGYU PENG, Congying Xia, Xinyi Yang, Caiming Xiong, Chien-Sheng Wu, Chen Xing

**Keywords:** LLM, reasoning, generalization, self-improvement

**Abstract:** 
> Post-training Large Language Models (LLMs) with explicit reasoning trajectories can enhance their reasoning abilities. However, acquiring such high-quality trajectory data typically demands meticulous supervision from humans or superior models, which can be either expensive or license-constrained. In this paper, we explore how far an LLM can improve its reasoning by self-synthesizing reasoning paths as training data without any additional supervision. Existing self-synthesizing methods, such as ...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022)
- *Authors:* Wei et al.
- *Direct Connection:* Established that explicit multi-step reasoning trajectories can supervise and improve LLM reasoning, providing the core supervision signal that ReGenesis self-synthesizes without external teachers.

**Self-Instruct: Aligning Language Models with Self-Generated Instructions** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* Demonstrated that models can bootstrap new training data without humans, a self-supervision principle ReGenesis adapts specifically to generate and learn from its own reasoning trajectories.

### 💡 Inspiration

**Least-to-Most Prompting Enables Complex Reasoning in Large Language Models** (2022)
- *Authors:* Zhou et al.
- *Direct Connection:* Introduced the paradigm of solving by first outlining high-level abstractions and then concretizing subproblems, directly inspiring ReGenesis’s abstract-to-concrete synthesis of reasoning paths.

**Self-Refine: Iterative Refinement with Self-Feedback** (2023)
- *Authors:* Madaan et al.
- *Direct Connection:* Showed that model-generated critiques and high-level feedback can guide improved solutions, motivating ReGenesis’s use of task-agnostic guidance before concretizing task-specific reasoning paths.

**Constitutional AI: Harmlessness from AI Feedback** (2022)
- *Authors:* Bai et al.
- *Direct Connection:* Pioneered using abstract principles to govern self-supervision without humans, an idea mirrored in ReGenesis’s use of general, task-agnostic reasoning guidance to steer self-synthesized trajectories.

### 🔍 Gap Identification

**Self-Taught Reasoner: Bootstrap your own reasoning with chain-of-thought** (2022)
- *Authors:* Zelikman et al.
- *Direct Connection:* Identified and popularized self-synthesizing reasoning trajectories via rationale-augmented self-training, whose task-specific rationales and poor OOD transfer are the explicit limitations ReGenesis targets by introducing task-agnostic, abstract-to-concrete guidance.

### 🔗 Related Problem

**Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2023)
- *Authors:* Yao et al.
- *Direct Connection:* Framed reasoning as structured deliberation with high-level planning and exploration, informing ReGenesis’s emphasis on generalizable, structure-first guidance prior to concrete step generation.

---

## Synthesis: How Prior Work Led to This Paper

Work on chain-of-thought showed that exposing intermediate rationales improves reasoning by making latent steps explicit, establishing rationales as a powerful supervision signal. Building on this, self-training approaches like STaR closed the loop by having models generate their own rationales and fine-tune on them, but the rationales tended to be task-specific and struggled to transfer out of domain. Decomposition methods such as least-to-most prompting introduced a structure-first approach: articulate high-level abstractions before tackling concrete subproblems, suggesting a general template for transferable reasoning. In parallel, Self-Instruct demonstrated that models could self-generate training data without human labels, while Self-Refine showed model-produced critiques can provide general feedback that improves downstream solutions. Constitutional AI extended this idea to training with abstract principles, using task-agnostic guidance to steer self-supervision. Tree of Thoughts further highlighted the value of explicit planning and structured deliberation beyond single linear chains.
Taken together, these works exposed a gap: self-synthesized rationales boost reasoning but lack cross-task generalization, whereas abstract, principle- or structure-driven guidance yields more transferable behavior. The natural next step is to synthesize reasoning data by first deriving task-agnostic, high-level guidance and then concretizing it into task-specific trajectories. ReGenesis operationalizes this abstract-to-concrete self-supervision, addressing STaR’s OOD weakness while retaining the benefits of self-generated reasoning signals.

---

*Analysis generated on: 2026-01-06T13:01:05.743279*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*

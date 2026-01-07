# Prior Work Analysis Report

## Target Paper

**Title:** Prompt Gradient Projection for Continual Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Jingyang Qiao, zhizhong zhang, Xin Tan, Chengwei Chen, Yanyun Qu, Yong Peng, Yuan Xie

**Keywords:** Continual Learning, Prompt Tuning, Gradient Projection, Anti-forgetting

**Abstract:** 
> Prompt-tuning has demonstrated impressive performance in continual learning by querying relevant prompts for each input instance, which can avoid the introduction of task identifier. Its forgetting is therefore reduced as this instance-wise query mechanism enables us to select and update only relevant prompts. In this paper, we further integrate prompt-tuning with gradient projection approach. Our observation is: prompt-tuning releases the necessity of task identifier for gradient projection met...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Visual Prompt Tuning** (2022)
- *Authors:* Jia et al.
- *Direct Connection:* PGP relies on VPT’s mechanism that prompts are injected into ViT self-attention, enabling the derivation that making prompt-gradient updates orthogonal mitigates attention-mediated interference.

**Gradient Episodic Memory for Continual Learning** (2017)
- *Authors:* Lopez-Paz et al.
- *Direct Connection:* PGP adopts GEM’s core idea of projecting current-task gradients so they do not harm past tasks, but applies the projection specifically to prompt gradients and removes task identifiers via instance-wise prompt querying.

### 💡 Inspiration

**Orthogonal Gradient Descent for Continual Learning** (2020)
- *Authors:* Farajtabar et al.
- *Direct Connection:* PGP extends OGD’s orthogonality principle by deriving an explicit orthogonality condition for prompt gradients within ViT self-attention and enforcing it via SVD-based projection.

### 🔍 Gap Identification

**DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning** (2022)
- *Authors:* Zhang et al.
- *Direct Connection:* PGP targets DualPrompt’s residual prompt interference by enforcing theoretically grounded orthogonality on prompt-gradient updates to provide anti-forgetting guarantees.

**Efficient Lifelong Learning with A-GEM** (2019)
- *Authors:* Chaudhry et al.
- *Direct Connection:* PGP addresses A-GEM’s reliance on episodic memory and task delineations by showing that prompt-tuning enables task-agnostic gradient projection with theoretical guarantees at the prompt level.

### 📊 Baseline

**Learning to Prompt for Continual Learning** (2022)
- *Authors:* Wang et al.
- *Direct Connection:* PGP builds directly on L2P’s instance-wise prompt retrieval/tuning to avoid task identifiers and inserts a projection step that regulates those prompt updates to prevent interference with past knowledge.

### 🔗 Related Problem

**OWM: Orthogonal Weight Modification to Protect Previous Knowledge in Neural Networks** (2019)
- *Authors:* Zeng et al.
- *Direct Connection:* PGP leverages OWM’s insight that preserving the subspace spanned by past inputs prevents forgetting, adapting it to construct a projector in the joint input–prompt space for prompt updates.

---

## Synthesis: How Prior Work Led to This Paper

Instance-wise prompting for continual learning was established by Learning to Prompt for Continual Learning, which retrieves and tunes a small prompt set per input to avoid explicit task identifiers; this highlighted that restricting updates to relevant prompts reduces interference. DualPrompt refined this idea with complementary prompt pools, yet still exhibited prompt interference without formal guarantees against forgetting. Visual Prompt Tuning formalized how learnable prompt tokens are injected into Vision Transformer self-attention, clarifying where and how prompt parameters influence representations and gradients. On the anti-forgetting side, Gradient Episodic Memory introduced projecting the current gradient to avoid increasing loss on past tasks, formulating gradient projection as a principled constraint. A-GEM made this projection efficient via averaged memory gradients, though it depended on episodic memories and task delineations. Orthogonal Gradient Descent reframed protection as enforcing orthogonality of new gradients to a subspace capturing prior tasks, while OWM showed that building projectors from input-feature subspaces can preserve previous knowledge. Bringing these threads together, the opportunity emerged to couple instance-wise prompt updates with projection-based guarantees: prompts obviate task identifiers, and projection/orthogonality offers formal anti-forgetting control. PGP synthesizes this by deriving an orthogonality condition specifically for prompt gradients in ViT self-attention and realizing it via SVD in a joint input–prompt space, yielding task-agnostic, theoretically grounded prompt updates that curb forgetting while retaining the flexibility of instance-wise prompt selection.

---

*Analysis generated on: 2026-01-06T23:47:40.594720*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
